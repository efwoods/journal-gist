"""This module will summarize a research paper"""

# Imports
from dotenv import load_dotenv
from openai import OpenAI

load_env_success =  load_dotenv()
if load_env_success == False:
    # logic to pull env from github
    pass

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5",
    messages=[
        {"role": "system", "content":"You are a helpful assistant."},
        {"role":"user", "content":"Hello!"}
    ]
)

