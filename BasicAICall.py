#import google.generativeai as genai
from google import genai
from pydantic import BaseModel


# Configure Gemini with your API key
client = genai.Client()
#genai.configure(api_key="AIzaSyClq0Mg9l5aApSnxAcQ6xHOrb6thQLJ9W4", transport="rest")  # Or use os.getenv("GEMINI_API_KEY")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)
print(response.text)
