import streamlit as st

from pii_detector import (
    detect_pii,
    redact_pii,
    detect_prompt_injection,
    detect_secrets
)

st.title("AI GDPR Prompt Guard")

prompt = st.text_area("Enter Prompt")

if st.button("Check Prompt Security"):

    pii = detect_pii(prompt)
    injection = detect_prompt_injection(prompt)
    secrets = detect_secrets(prompt)

    cleaned = redact_pii(prompt)

    st.subheader("Detected Risks")

    st.write("PII:", pii)
    st.write("Prompt Injection:", injection)
    st.write("Secrets:", secrets)

    st.subheader("Safe Prompt")

    st.write(cleaned)