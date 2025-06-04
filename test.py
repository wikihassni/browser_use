import asyncio
import os
from langchain_openai import AzureChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import argparse 

load_dotenv()

async def main(task_override: str | None = None):       # {{ edit_2 }}
    # Explicitly get the environment variables
    azure_endpoint = "https://ai-wikihassni9653ai233209954268.cognitiveservices.azure.com/"
    azure_api_key = os.getenv("AZURE_OPENAI_KEY") or "21q4Qes3uWAIyBXa2r291MFvsxxXH0McuCiMiAB9rRnu15SEZLxIJQQJ99BDACfhMk5XJ3w3AAAAACOGeJNq"

    # use the override if provided, otherwise fall back to your original task
    task_str = task_override or (                      # {{ edit_3 }}
        "Visit the official YC website and compile all enterprise "
        "information under the W25 B2B tag into a clear, well-structured table. "
        "Be sure to find all of it"
    )

    agent = Agent(
        task=task_str,
        llm=AzureChatOpenAI(
            azure_deployment="gpt-4.1-mini",
            model="gpt-4.1-mini",
            azure_endpoint=azure_endpoint,
            api_key=azure_api_key,
            api_version="2024-12-01-preview",
        ),
    )
    await agent.run()
    print("Task completed successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(                 # {{ edit_4 }}
        description="Override the natural-language task for browser-use"
    )
    parser.add_argument(
        "--task",
        type=str,
        help="Natural‑language task to send to the agent",
        required=False,
    )                                                  # {{ edit_5 }}
    args = parser.parse_args()                         # {{ edit_6 }}
    asyncio.run(main(task_override=args.task))  