import hashlib
from typing import Self

data = {
    "value": "3435435dee-ofefr4ds",
    "rules": {
        "case_type": "lower",
        "affix": "prefix",
        "clear_empty_space": True,
    }
}


class SANITIZATION_RULES:
    AFFIX_TYPE_PREFIX = "prefix"
    CASE_TYPE = "lower"


class Sanitizer:
    def __init__(self: Self, data: dict) -> None:
        self._value = data.get("value")
        self._is_trim = data.get("rules").get("clear_empty_space", False)
        self._text_case_type = data.get("rules").get("case_type")
        self._affix_type = data.get("rules").get("affix")

    @property
    def value(self: Self) -> str:
        return self._value

    @property
    def should_strip(self: Self) -> bool:
        return self._is_trim

    @property
    def case_type(self: Self) -> str:
        return self._text_case_type

    @property
    def affix_type(self: Self) -> str:
        return self._affix_type


class Anonymiser:
    @staticmethod
    def anonymise(property_value: str, data: dict) -> str:
        sanitized_value = Anonymiser.sanitize(
            property_value=property_value, salt_data=data
        )
        hashed_value = hashlib.md5(sanitized_value.encode("utf-8"))
        return hashed_value.hexdigest()

    @staticmethod
    def sanitize(property_value: str, salt_data: dict) -> str:
        sanitizer = Sanitizer(salt_data)
        sanitized_value = property_value

        if sanitizer.should_strip:
            sanitized_value = property_value.strip()

        if Anonymiser._is_case_type_lower(sanitizer=sanitizer):
            sanitized_value = sanitized_value.lower()

        if Anonymiser._is_affix_type_prefix(sanitizer=sanitizer):
            sanitized_value = sanitizer.value + sanitized_value
        return sanitized_value

    @staticmethod
    def _is_affix_type_prefix(sanitizer: Sanitizer) -> bool:
        return sanitizer.affix_type == SANITIZATION_RULES.AFFIX_TYPE_PREFIX

    @staticmethod
    def _is_case_type_lower(sanitizer: Sanitizer) -> bool:
        return sanitizer.case_type == SANITIZATION_RULES.CASE_TYPE

print(Anonymiser.anonymise(" someone", data=data))
