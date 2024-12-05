# README

## Overview

This Python script provides a simple command-line interface for interacting with the OpenAI API. It allows users to ask questions and receive responses from a language model, while maintaining a history of the conversation. The script validates the API key and base URL before allowing interaction.

## Features

- Validates the provided API key and base URL.
- Maintains a conversation history.
- Allows users to ask questions and receive answers.
- Supports commands to clear history and view conversation history.
- Exits the program gracefully.

## Requirements

- Python 3.x
- OpenAI Python client library (install via pip)

## Installation

1. Clone this repository or download the script.
2. Install the OpenAI Python client library if you haven't already:

   ```bash
   pip install openai
   ```

3. Set your API key and base URL in the script:

   ```python
   api_key = 'your_api_key_here'
   base_url = 'your_base_url_here'
   ```

## Usage

1. Run the script:

   ```bash
   python your_script_name.py
   ```

2. If the API key and base URL are valid, you will see a welcome message. You can then start asking questions.

3. Commands:
   - Type your question and press Enter to receive a response.
   - Type `quit` or `exit` to end the session.
   - Type `clear` to clear the conversation history.
   - Type `history` to view the conversation history.

## Example Interaction

```
Welcome!

<Question>
What is the capital of France?

<Answer>
The capital of France is Paris.

<Question>
history

<History>
[{'role': 'system', 'content': 'U r a helpful assistant.'}, {'role': 'user', 'content': 'What is the capital of France?'}, {'role': 'assistant', 'content': 'The capital of France is Paris.'}]

<Question>
clear

History Cleared

<Question>
quit

----------------------- Thank you for your use -----------------------
```

## Error Handling

If the API key or base URL is invalid, the script will display an error message and terminate.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## Contact

For any questions or feedback, please contact [wangchutian1@foxmail.com].
