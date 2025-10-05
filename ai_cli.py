
import os
import openai
import click

"""Interactive AI Command Line Interface (CLI) using OpenAI's GPT-4o-mini model.
This script allows users to input a prompt and receive a response from the AI model.
This is a simple command line tool that uses OpenAI's API to interact with the GPT-4o-mini model.
Usage:
    python ai_cli.py "Your prompt here"
Requirements:
pip install openai click

API Key: Create a new API key at https://platform.openai.com/
# Set your OpenAI API key as an environment variable
# Example:
export OPENAI_API_KEY='your_api_key'
"""

openai.api_key = os.getenv("OPENAI_API_KEY")

@click.command()
@click.argument('prompt')
def ask_ai(prompt):
    """Simple AI CLI: Pass a prompt and get a response."""
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500
        )
        answer = response.choices[0].message.content.strip()
        click.echo(answer)
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == "__main__":
    ask_ai()

