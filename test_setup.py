import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found.")
    print("Make sure your .env file contains:")
    print("GEMINI_API_KEY=your_api_key")
    raise SystemExit(1)

print("✓ API key found")

try:
    client = genai.Client(api_key=api_key)

    models = list(client.models.list())

    print("✓ Gemini API connection successful")
    print(f"✓ Available models found: {len(models)}")

    print("\nSetup looks good!")

except Exception as e:
    print("❌ Gemini API connection failed.")
    print(f"Error: {e}")
    raise SystemExit(1)