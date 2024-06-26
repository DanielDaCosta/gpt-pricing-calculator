import tiktoken
from dotenv import load_dotenv
import typing
import os
import json
import argparse
load_dotenv();

def count_num_tokens_message(messages: list[dict], model_name: str) -> int:
    """Return number of tokens per message
    """
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        print("Warning: Model Name not found")
        raise Exception
    

    if model_name in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
    }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model_name == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model_name:
        print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return count_num_tokens_message(messages, model_name="gpt-3.5-turbo-0613")
    # elif "gpt-4o" in model_name:
    #     print("Warning: gpt-4o may update over time. Returning num tokens assuming gpt-4o-2024-05-13")
    #     return count_num_tokens_message(messages, model="gpt-4o-2024-05-13")
    elif "gpt-4" in model_name:
        print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return count_num_tokens_message(messages, model_name="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model_name}."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens

    
def read_messages_from_file(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data


if __name__ == '__main__':
    # MODEL NAME and FILE NAME are required parameters
    parser = argparse.ArgumentParser(description='Read and print JSON data from a file.')
    parser.add_argument('model_name', type=str, help='The GPT model used for computation.')
    parser.add_argument('file_name', type=str, help='The name of the JSON file to read.')
    
    args = parser.parse_args()

    # Read Input file
    messages = read_messages_from_file(args.file_name)

    # Compute the number of tokens
    num_tokens = count_num_tokens_message(messages, args.model_name)

    print(f"{num_tokens} prompt tokens counted by count_num_tokens_message().")

