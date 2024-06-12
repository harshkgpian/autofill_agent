from PyPDF2 import PdfReader
from groq import Groq
import ast
# from fill import fill
# Initialize the Groq client with your API key
client = Groq(api_key="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")
model = "llama3-8b-8192"

def extract_function_values(pdf_content):
    # Define the tool for extracting values
    extract_values_tool = {
        "type": "function",
        "function": {
            "name": "Extract Function Values",
            "description": "Extract specific values from a formula description",
            "parameters": {
                "type": "object",
                "properties": {
                    "First Name": {
                        "type": "string",
                        "description": "First Name"
                    },
                    "Middle Name": {
                        "type": "string",
                        "description": "Middle Name"
                    },
                    "Last Name": {
                        "type": "string",
                        "description": "Last Name"
                    },
                    "Street Address": {
                        "type": "string",
                        "description": "Street Address"
                    },
                    "Street Address Line 2": {
                        "type": "string",
                        "description": "Street Address Line 2"
                    },
                    "City": {
                        "type": "string",
                        "description": "City"
                    },
                    "State / Province": {
                        "type": "string",
                        "description": "State / Province"
                    },
                    "Email Address": {
                        "type": "string",
                        "description": "Email Address"
                    },
                    "Phone Number": {
                        "type": "string",
                        "description": "Phone Number"
                    },
                    "LinkedIn": {
                        "type": "string",
                        "description": "LinkedIn"
                    },
                    "Write something interesting about AI Agents/ LLMs": {
                        "type": "string",
                        "description": "Write something interesting about AI Agents/ LLMs"
                    },
                    "Write something interesting about Web Automation": {
                        "type": "string",
                        "description": "Write something interesting about Web Automation"
                    },
                    "Reverse a LinkedList": {
                        "type": "string",
                        "description": "Reverse a LinkedList"
                    },
                    "Upload Your Resume": {
                        "type": "string",
                        "description": "Upload Your Resume"
                    },
                    "Cover Letter": {
                        "type": "string",
                        "description": "Cover Letter"
                    }
                },
                "required": ["First Name", "Middle Name", "Last Name", "Street Address", "Street Address Line 2", "City", "State / Province", "Email Address", "Phone Number", "LinkedIn", "Write something interesting about AI Agents/ LLMs", "Write something interesting about Web Automation", "Reverse a LinkedList", "Upload Your Resume", "Cover Letter"]
            },
        },
    }

    # Prior message from the system providing context
    system_message = {
        "role": "system",
        "content": (
            "You are an AI model designed to extract specific values from a given PDF."
        )
    }

    # Instruction for extracting values from the PDF
    instruction = {
        "role": "user",
        "content": (
            "You are tasked with extracting the following required fields from the provided PDF:\n\n"
            "Full Name, First Name, Middle Name, Current Address, Street Address, Street Address Line 2, City, State / Province, Email Address, Phone Number, LinkedIn, Write something interesting about AI Agents/ LLMs, Write something interesting about Web Automation, Reverse a LinkedList, Upload Your Resume, Cover Letter\n\n"
            "Your goal is to extract the required information from the PDF.\n\n"
            f"Use the provided PDF content to extract the required information:\n\n{pdf_content}\n\n"
        )
    }

    try:
        # Create the chat completion
        chat_completion = client.chat.completions.create(
            messages=[
                system_message,
                instruction,
            ],
            model=model,
            tools=[extract_values_tool]
        )

        # Extract the values from the tool call arguments
        values = ast.literal_eval(chat_completion.choices[0].message.tool_calls[0].function.arguments)
        print(values)
        return values

    except Exception as e:
        print(f"Error processing PDF content. Error: {e}")

# Example usage
file_path = r"C:\Users\harsh\Desktop\GEN AI\Intern/CV.pdf"

with open(file_path, "rb") as file:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

data = extract_function_values(text)
