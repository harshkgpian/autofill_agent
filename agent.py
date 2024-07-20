from groq import Groq
import ast

client = Groq(api_key=YOUR_KEY)
model = "llama3-8b-8192"

def extract_input_fields(scraped_content):
    fill_form_tool = {
        "type": "function",
        "function": {
            "name": "Fill Form Details",
            "description": "Form filling from input fields Labels.",
            "parameters": {
                "type": "object",
                "properties": {
                    "fields": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "List of input fields Label Names."
                    }
                },
                "required": ["fields"]
            }
        }
    }

    # Prior message from the system providing context
    system_message = {
        "role": "system",
        "content": (
            "You are an AI model tasked with extracting input field labels from the following scraped form content:\n\n"
        )
    }

    # Instruction for extracting input field labels
    instruction = {
        "role": "user",
        "content": (
            "You are tasked with extracting input field labels from the following scraped form content:\n\n"
            f"{scraped_content}\n\n"
            "Your goal is to provide a list of input field labels.\n\n"
            "Step 1: Analyze the provided form details to identify all input fields.\n"
            "Step 2: Extract the label of each input field.\n\n"
            "Use the provided form details to generate the list of input field labels."
        )
    }

    # Create the chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            system_message,
            instruction,
        ],
        model=model,
        tools=[fill_form_tool]
    )
    names = ast.literal_eval(chat_completion.choices[0].message.tool_calls[0].function.arguments)["fields"]
    return names

