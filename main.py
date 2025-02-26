import os
from google import genai

def main():
    # This uses the API key from environment variable GOOGLE_API_KEY
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp", contents="How does RLHF work?"
    )
    print(response.text)

if __name__ == "__main__":
    main()
