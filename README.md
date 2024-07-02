# GPT Pricing Calculator
Pricing calculator for OpenAI GPT API

**tiktoken library**
```
pip install tiktoken
```
## Usage

**Example input**

```json

example_message = [
    {
        "role": "system",
        "content": "You are a helpful, pattern-following assistant that translates corporate jargon into plain English.",
    },
    {
        "role": "system",
        "name": "example_user",
        "content": "New synergies will help drive top-line growth.",
    },
    {
        "role": "system",
        "name": "example_assistant",
        "content": "Things working well together will increase revenue.",
    },
    {
        "role": "system",
        "name": "example_user",
        "content": "Let's circle back when we have more bandwidth to touch base on opportunities for increased leverage.",
    },
    {
        "role": "system",
        "name": "example_assistant",
        "content": "Let's talk later when we're less busy about how to do better.",
    },
    {
        "role": "user",
        "content": "This late pivot means we don't have time to boil the ocean for the client deliverable.",
    },
]
```

**Command**

Input Params:
- `--model_name`: `gpt-4`, `gpt-3.5`...
- `--file_path`: JSON

```python
python pricing-calculator.py gpt-4 messages_example.json
```

**Output**
```python
Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.
129 prompt tokens counted by count_num_tokens_message().
```
