# Designed by Marcos Antonio de Carvalho
# Description: API para solicitar script Python ao ChatGPT
#
# Referências
#   Python Automation with ChatGPT  https://www.youtube.com/watch?v=w-X_EQ2Xva4
#
# Created: 01.april.2023 - Londrina/Paraná (Dia da Mentira kkk)

# import openai

import requests
import argparse
#import os 
#api_key = os.getenv("Variavel")

# Criar uma chave de acesso para api da OpenAI 
# em https://platform.openai.com/account/api-keys 
# e configurar o arquivo key.py
from key import api_key # carregar a api_key do arquivo key.py

api_endpoint = "https://api.openai.com/v1/completions"

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="the prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save Python script")

print("Python Automation with ChatGPT - Version 0.0.1")
print("Designed by Marcos Antonio de Carvalho\n")

args = parser.parse_args()

print(f'API Endpoint..: {api_endpoint}')
print(f'API Access Key: {api_key}')

request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
    "model": "text-davinci-003",
    # 1 Token por minuto 
    #
    "prompt": f"Write python script to {args.prompt}. Provide only code, no text",
    "max_tokens": 4097, # https://platform.openai.com/docs/models/gpt-3-5
    "temperature": 0.8 # 0.5 0.2 # define o nível ousadia da resposta (mais alto mais criativo)
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    #print(response.json()["choices"][0]["text"])
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
    print(f'Generated code: {args.file_name}')
else:
    print(f"Request failed with status code: {str(response.status_code)}")
