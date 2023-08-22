#!/usr/bin/env python3
import openai
import sys
import os
import re

# !!! You need an API key !!!
openai.api_key = os.environ.get('OPENAI_API_KEY')

# taken from https://github.com/mustvlad/ChatGPT-System-Prompts/
system_prompts = [
    "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.",
    "You are a language learning coach who helps users learn and practice new languages. Offer grammar explanations, vocabulary building exercises, and pronunciation tips. Engage users in conversations to help them improve their listening and speaking skills and gain confidence in using the language.",
    "You are an expert in world history, knowledgeable about different eras, civilizations, and significant events. Provide detailed historical context and explanations when answering questions. Be as informative as possible, while keeping your responses engaging and accessible"
]

def display_system_prompts(prompts):
    print("Select a system prompt:")
    for idx, prompt in enumerate(prompts, 1):
        print(f"{idx}. {prompt}")
    choice = int(input("\nEnter your choice (number): "))
    return prompts[choice - 1]


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
        content = chunk.get("choices", [{}])[0].get("delta", {}).get("content")
        if content:
            print(content, end="")
    print("\n")

selected_prompt = system_prompts[0]

if len(sys.argv) < 2:
    os.system('clear')
    while True:  # Keep the interaction going in a loop
        prompt = input("How can I help: ")
        if prompt.lower() in ['exit', 'quit']:
            break  # Exit the loop if user types 'exit' or 'quit'
        if prompt.lower() == 'np':
            selected_prompt = display_system_prompts(system_prompts)
            os.system('clear')
            continue
        response = stream_gpt(prompt)
        input("[continue...]")
        os.system('clear')
else:
    prompt = ' ' .join(sys.argv[1:])
    response = ask_gpt(prompt)
    print("\n" + response + "\n")
