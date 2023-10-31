import os
import azure.functions as func
import openai
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get your OpenAI API key from environment variables
    openai.api_key = os.environ["OPENAI_API_KEY"]
    openai.api_type = "azure"
    openai.api_version = "2023-07-01-preview" 
    openai.api_base = os.environ("OPENAI_API_BASE")  # Your Azure OpenAI resource's endpoint value.

    # Retrieve the prompt from the request payload
    try:
        req_body = req.get_json()
        prompt = req_body.get("prompt")
    except ValueError:
        return func.HttpResponse("Invalid request payload", status_code=400)

    # Generate text from the GPT-4 engine
    response = openai.Completion.create(
        engine="lumiq-rnd-openai-gpt4", # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )

    generated_text = response.choices[0].text

    return func.HttpResponse(generated_text, mimetype="text/plain")