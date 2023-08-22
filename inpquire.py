#!/usr/bin/env python3
import openai
import sys
import os
import re

# !!!You need an API key!!!
# https://platform.openai.com/account/api-keys
with open("/users/tim/.api_key.txt") as f:
    openai.api_key = f.read().strip()

def ask_gpt(prompt):
    r = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert in all fields and disciplines. Explain concepts, theories and phenomena in an engaging and accessible way"},
            {"role": "user", "content": prompt}
        ]
    )

    text = r["choices"][0]["message"]["content"]
    if text.startswith('`') and text.endswith('`'):
        text = text[1:-1]
    return text

def stream_gpt(prompt):
    r = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI."},
        {"role": "user", "content": prompt}
    ],
    stream=True
    )
    
    print()
    for chunk in r:
    # if chunk["choices"][0]["delta"]["content"]:
    #token = chunk.get"choices"][0]["delta"]["content"])
        content = chunk.get("choices", [{}])[0].get("delta", {}).get("content")
        if content:
            print(content, end="")
    print("\n")


if len(sys.argv) < 2:
    os.system('clear')
    while True:  # Keep the interaction going in a loop
        prompt = input("How can I help: ")
        if prompt.lower() in ['exit', 'quit']:
            break  # Exit the loop if user types 'exit' or 'quit'
        response = stream_gpt(prompt)
        input("[continue...]")
        os.system('clear')
else:
    prompt = ' ' .join(sys.argv[1:])
    response = ask_gpt(prompt)
    print("\n" + response + "\n")
