# Inquire - ChatGPT Interactive CLI

A simple command-line interface to interact with OpenAI's GPT-3.5-turbo model using the OpenAI API. Users can chat with the model in real-time, choose from a variety of system prompts, or pass a prompt directly via command-line arguments.

## Features

- Interact with GPT-3.5-turbo in real-time from your terminal.
- Choose from a variety of predefined system prompts to guide the model's behavior.
- Streamed response for a smoother user experience.
- Option to pass a prompt directly via command-line arguments.
- Secure API key handling through environment variables.

## Prerequisites

- Python 3
- An OpenAI API key

## Setup

1. Clone this repository:

```
git clone https://github.com/timcol/inquire 
cd inquire
```


2. Install the required package:

```
pip install openai
```

3. Set your OpenAI API key as an environment variable:

```
export OPENAI_API_KEY='YOUR_API_KEY'
```

Replace `'YOUR_API_KEY'` with your actual OpenAI API key.

## Usage

### Interactive Mode

Run the script without any arguments to enter interactive mode:

```
./inquire.py
```

You'll be prompted with `How can I help:`. Enter your questions or statements. 

To change the system prompt, type `np`. To exit, type `exit` or `quit`.

### Command-Line Argument Mode

You can also pass a prompt directly via command-line arguments:

```
./inquire.py "Your question or statement here"
```

## License

This project is licensed under the MIT License.
