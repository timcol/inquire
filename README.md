# Inquirewin - ChatGPT Interactive CLI

Forked from the original project by [timcol](https://github.com/timcol/inquire), this version adds enhanced functionality to allow users to select from two predefined system prompts or write their own custom prompt, providing a more tailored interaction with the GPT-3.5-turbo model.

A simple command-line interface to interact with OpenAI's GPT-3.5-turbo model using the OpenAI API. Users can chat with the model in real-time, choose from predefined system prompts, or define their own custom prompts for a personalized interaction experience.

It also works across Mac, Linux and Windows. The version made by timcol was *nix only.

## CLI in action

## Features

- Interact with GPT-3.5-turbo in real-time from your terminal.
- Choose from two built-in predefined system prompts to guide the model's behavior.
- Write your own custom prompt for a unique interaction experience.
- Streamed response for a smoother user experience.
- Option to pass a prompt directly via command-line arguments.
- Secure API key handling through environment variables.

## Prerequisites

- Python 3
- An OpenAI API key

## Setup

### Clone this repository:

```bash
git clone https://github.com/furkly/inquire/tree/inquirewin
cd inquire
```

### Install the required package:

```bash
pip install openai
```

### Set your OpenAI API key as an environment variable:

#### For Linux/Mac:

```bash
export OPENAI_API_KEY='YOUR_API_KEY'
```

#### For Windows:

Follow the [Setting Up OpenAI API Key on Windows](#setting-up-openai-api-key-on-windows) guide below.

Replace 'YOUR_API_KEY' with your actual OpenAI API key.

### Setting Up OpenAI API Key on Windows

To use this script on Windows, follow these steps:

1. Find Your API Key in your OpenAI account.
2. Open Environment Variables.
3. Create a New Environment Variable named `OPENAI_API_KEY`.
4. Paste your OpenAI API key into the Variable value field.
5. Confirm and Restart.

Detailed instructions can be found in the [section above](#prerequisites).

## Usage

### Interactive Mode

Run the script without any arguments to enter interactive mode:

```bash
./inquire.py
```

You'll be prompted with "How can I help:". Enter your questions or statements. You may select from built-in prompts or write a custom one as needed.

### Command-Line Argument Mode

You can also pass a prompt directly via command-line arguments:

```bash
./inquire.py "Your question or statement here"
```

## License

This project is licensed under the MIT License.
