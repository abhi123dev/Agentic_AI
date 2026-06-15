import os
# print(os.getenv("ANTHROPIC_API_KEY")) 
from anthropic import Anthropic

# Get API key from environment variable
api_key = os.getenv("ANTHROPIC_API_KEY")

# Check if API key exists
if not api_key:
    print("Error: ANTHROPIC_API_KEY is not set.")
    exit()

# Create Anthropic client
client = Anthropic(api_key=api_key)

# Get topic from user
topic = input("Enter a topic to study: ").strip()

# Input validation
if topic == "":
    print("Error: Topic cannot be empty.")
    exit()

# Send request to Claude
response = client.messages.create(
    max_tokens=150,
    messages=[
        {
            "role": "user",
            "content": f"Explain the topic \"{topic}\" in simple terms in under 100 words, as if you were a study buddy helping a friend understand it.`"
        }
    ],
    model="claude-sonnet-4-5"
)

# Print response
print("\nStudy Buddy Explanation:\n")
print(response.content[0].text)