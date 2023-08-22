#!/usr/bin/env python3
import openai
import sys
import os
import platform

openai.api_key = os.environ.get('OPENAI_API_KEY')

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def choose_prompt(prompts):
    print("Would you like to use one of the default prompts, or enter your own?")
    choice = input("Enter 'd' for default, 'c' for custom: ").lower()
    if choice == 'c':
        return input("Enter your custom prompt: ")
    elif choice == 'd':
        return display_system_prompts(prompts)
    else:
        print("Invalid choice, defaulting to first system prompt.")
        return prompts[0]

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
            {"role": "system", "content": prompt},
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
            {"role": "system", "content": prompt},
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

system_prompts = [
    "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.",
    "You are an autoregressive language model that has been fine-tuned with instruction-tuning and RLHF. You carefully provide accurate, factual, thoughtful, nuanced answers, and are brilliant at reasoning. If you think there might not be a correct answer, you say so.",
]

if len(sys.argv) < 2:
    clear_screen()
    selected_prompt = choose_prompt(system_prompts)
    while True:  # Keep the interaction going in a loop
        prompt = input("\033[32mHow can I help:\033[0m ")
        if prompt.lower() in ['exit', 'quit']:
            break
        if prompt.lower() == 'np':
            selected_prompt = choose_prompt(system_prompts)
            clear_screen()
            continue
        response = stream_gpt(prompt)  # or use selected_prompt if needed
        input("[continue...]")
        clear_screen()
else:
    prompt = ' '.join(sys.argv[1:])
    response = ask_gpt(prompt)
    print("\n" + response + "\n")