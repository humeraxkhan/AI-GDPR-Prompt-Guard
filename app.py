from fastapi import FastAPI
from pydantic import BaseModel

from pii_detector import (
    detect_pii,
    redact_pii,
    detect_prompt_injection,
    detect_secrets
)

from alerts import send_alert


app = FastAPI(title="AI GDPR Prompt Guard")


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "AI Security Guard Running"}


@app.post("/check_prompt")
def check_prompt(data: PromptRequest):

    prompt = data.prompt

    pii_found = detect_pii(prompt)
    injection_found = detect_prompt_injection(prompt)
    secrets_found = detect_secrets(prompt)

    safe_prompt = redact_pii(prompt)

    risk_detected = bool(pii_found or injection_found or secrets_found)

    if risk_detected:

        alert_message = f"""
AI SECURITY ALERT

Prompt: {prompt}

PII Detected: {pii_found}
Prompt Injection: {injection_found}
Secrets Detected: {secrets_found}
"""

        send_alert(alert_message)

    return {
        "original_prompt": prompt,
        "pii_detected": pii_found,
        "prompt_injection_detected": injection_found,
        "secrets_detected": secrets_found,
        "safe_prompt": safe_prompt
    }
