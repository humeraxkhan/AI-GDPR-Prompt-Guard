import re

# -----------------------------
# PII Patterns (GDPR protection)
# -----------------------------

PII_PATTERNS = {
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "phone": r"\b\d{10}\b",
    "credit_card": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
    "iban": r"\b[A-Z]{2}[0-9]{2}[A-Z0-9]{1,30}\b"
}


def detect_pii(text):
    findings = []

    for name, pattern in PII_PATTERNS.items():
        if re.search(pattern, text):
            findings.append(name)

    return findings


def redact_pii(text):

    text = re.sub(PII_PATTERNS["email"], "[EMAIL_REDACTED]", text)
    text = re.sub(PII_PATTERNS["phone"], "[PHONE_REDACTED]", text)
    text = re.sub(PII_PATTERNS["credit_card"], "[CARD_REDACTED]", text)
    text = re.sub(PII_PATTERNS["iban"], "[IBAN_REDACTED]", text)

    return text


# -----------------------------
# Prompt Injection Detection
# -----------------------------

PROMPT_INJECTION_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "bypass safety",
    "act as system",
    "developer mode",
    "jailbreak",
]


def detect_prompt_injection(text):

    text = text.lower()
    found = []

    for pattern in PROMPT_INJECTION_PATTERNS:
        if pattern in text:
            found.append(pattern)

    return found


# -----------------------------
# Secret / API Key Detection
# -----------------------------

SECRET_PATTERNS = {
    "openai_key": r"sk-[A-Za-z0-9]{20,}",
    "aws_access_key": r"AKIA[0-9A-Z]{16}",
    "generic_api_key": r"api[_-]?key\s*=\s*[A-Za-z0-9]{16,}"
}


def detect_secrets(text):

    findings = []

    for name, pattern in SECRET_PATTERNS.items():
        if re.search(pattern, text):
            findings.append(name)

    return findings
