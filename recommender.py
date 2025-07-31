import openai
import streamlit as st

def recommend_program(sr_index: float, ar_index: float) -> str:
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    prompt = (
        f"A student has an SR index of {sr_index} and an AR index of {ar_index}. "
        "Based on these values, recommend an English video program suitable for their level. "
        "Include the program title and a short explanation (about 2 sentences). "
        "Respond in Korean."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful education assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )

    return response.choices[0].message["content"]
