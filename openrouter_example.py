"""Minimal example of calling an OpenRouter model.

OpenRouter is OpenAI-compatible, so we use the official `openai` SDK and just
point it at OpenRouter's base URL. Set your API key in the environment first:

    export OPENROUTER_API_KEY=sk-or-v1-...

Then run:

    pip install openai
    python openrouter_example.py
"""

import os

from openai import OpenAI

# The model id, taken from https://openrouter.ai/poolside/laguna-xs-2.1:free
MODEL = "poolside/laguna-xs-2.1:free"


def main() -> None:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit(
            "Set the OPENROUTER_API_KEY environment variable "
            "(get a key at https://openrouter.ai/keys)."
        )

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Write a one-line haiku about blackjack."}
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
