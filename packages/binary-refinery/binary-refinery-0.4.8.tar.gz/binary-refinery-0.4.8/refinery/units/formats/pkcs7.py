#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from contextlib import suppress
from datetime import datetime

from refinery.units import Unit
from refinery.lib.json import BytesAsArrayEncoder


class ParsedASN1ToJSON(BytesAsArrayEncoder):

    @classmethod
    def _is_keyval(cls, obj):
        return (
            isinstance(obj, dict)
            and set(obj.keys()) == {'type', 'values'}
            and len(obj['values']) == 1
        )

    @classmethod
    def handled(cls, obj) -> bool:
        return (
            BytesAsArrayEncoder.handled(obj)
            or cls._is_keyval(obj)
        )

    def default(self, obj):
        if self._is_keyval(obj):
            return dict(type=obj['type'], value=obj['values'][0])
        with suppress(TypeError):
            return super().default(obj)
        if isinstance(obj, (set, tuple)):
            return list(obj)
        if isinstance(obj, datetime):
            return str(obj)
        dictionary_result = {}
        if isinstance(obj, pkcs7._asn1crypto.x509.Certificate):
            dictionary_result.update(fingerprint=obj.sha1.hex())
        with suppress(Exception):
            keys = list(obj)
            if all(isinstance(k, str) for k in keys):
                dictionary_result.update((key, obj[key]) for key in keys)
        if dictionary_result:
            return dictionary_result
        with suppress(Exception):
            return list(obj)
        if isinstance(obj, pkcs7._asn1crypto.cms.CertificateChoices):
            return pkcs7._asn1crypto.x509.Certificate.load(obj.dump())
        with suppress(AttributeError, ValueError):
            return obj.native
        if isinstance(obj, pkcs7._asn1crypto.core.Any):
            return obj.dump()
        if isinstance(obj, pkcs7._asn1crypto.core.Asn1Value):
            return obj.dump()
        raise ValueError(F'Unable to determine JSON encoding of {obj.__class__.__name__} object.')


class pkcs7(Unit):
    """
    Converts PKCS7 encoded data to a JSON representation.
    """
    @Unit.Requires('asn1crypto', optional=False)
    def _asn1crypto():
        import asn1crypto
        import asn1crypto.cms
        import asn1crypto.core
        import asn1crypto.x509
        return asn1crypto

    def process(self, data: bytes):
        signature = self._asn1crypto.cms.ContentInfo.load(data)
        with ParsedASN1ToJSON as encoder:
            return encoder.dumps(signature).encode(self.codec)
