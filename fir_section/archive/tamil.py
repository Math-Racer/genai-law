import requests
from langdetect import detect
import urllib.parse  # For URL encoding

translation = False  # Declare globally

def translate_to_english(text):
    """Translates Tamil text to English using Google Translate."""

    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=ta&tl=en&dt=t&q=" + urllib.parse.quote(text)  # Proper URL encoding

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    translated_text = data[0][0][0]
    return translated_text

def check_and_translate(prompt):
    """Checks if the prompt is in Tamil and translates it to English if needed."""

    global translation  # Declare global inside the function to update it
    detected_language = detect(prompt)

    if detected_language == "ta":
        translation = True
        translated_text = translate_to_english(prompt)
        return translated_text
    else:
        translation = False  # Ensure translation is False if not Tamil
        return prompt

def tamil(prompt):
    # Translates the prompt if needed
    translated_prompt = check_and_translate(prompt)
    return translated_prompt, translation
