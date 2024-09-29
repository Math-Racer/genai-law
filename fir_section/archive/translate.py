import requests
def translate_to_tamil(text):
    """Translates Tamil text to English using Google Translate."""

    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ta&dt=t&q=" + text

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    translated_text = data[0][0][0]
    return translated_text

