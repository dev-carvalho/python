# Author: Marcos Antônio de Carvaho
# Description: API para solicitar script Python ao ChatGPT
#
# Referências
#   Python Automation with ChatGPT  https://www.youtube.com/watch?v=w-X_EQ2Xva4
#
# Created: 01.april.2023 - Londrina/Paraná

# import openai
# import os
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="the prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save Python script")

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"
args = parser.parse_args()

request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": f"Write python script to {args.prompt}. Provide only code, no text",
    "max_tokens": 1000,
    "temperature": 0.5
}

response = requests.post(
    api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    # print(response.json()["choices"][0]["text"])
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")
