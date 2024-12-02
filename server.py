import os
from fastapi import FastAPI, Request, HTTPException
from groq import Groq
from pydantic import BaseModel

# Load the GROQ API key from environment variable
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# FastAPI app
app = FastAPI()

# List of unwanted keywords
unwanted_keywords = ["ass", "bitch", "fuck", "generate", "Java", "Python", "Javascript", "code"]

# Define a function to check for unwanted keywords
def contains_unwanted_keywords(text: str) -> bool:
    return any(keyword in text.lower() for keyword in unwanted_keywords)

class WebhookRequest(BaseModel):
    queryResult: dict

@app.post("/dialogflow-webhook")
async def dialogflow_webhook(request: WebhookRequest):
    user_message = request.queryResult.get("queryText", "")

    # Check if the message contains any unwanted keywords
    if contains_unwanted_keywords(user_message):
        return {
            "fulfillmentText": "I am a legal assistant. I can't provide information about that."
        }
    
    # If no unwanted keywords, send the message to Groq API
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_message}
        ],
        model="llama3-8b-8192"
    )

    # Respond with Groq API's output
    return {
        "fulfillmentText": chat_completion.choices[0].message.content
    }
