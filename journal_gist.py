"""This module will summarize a research paper"""

# Imports
import logging
from dotenv import load_dotenv
from openai import OpenAI

logging.basicConfig(level=logging.DEBUG, filename='journal_gist_output.log')

LOAD_ENV_SUCCESS =  load_dotenv()
if not LOAD_ENV_SUCCESS:
    # logic to pull env from github
    logging.error("Error: No Environment Variable Set")

def query_openai(messages: list) -> list:
    """This function is used to query the OpenAI API.

    Args:
        messages (list): This is the list of messages to send to the API.

    Returns:
        list: This is the response to the message queries.
    """
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )

    return completion

if __name__ == "__main__":
    message = [
            {"role": "system", "content":"You are a helpful assistant."},
            {"role":"user", "content":"Hello!"}
        ]

    response = query_openai(message)
    logging.debug(response)
