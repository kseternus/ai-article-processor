
# AI Article to HTML Converter

This script takes a plain text article and converts it into a structured HTML file using OpenAI's GPT model. The generated HTML file contains properly formatted text, `<img>` tags for image placeholders, and captions. The script is designed to be simple and easy to use, with error handling for file reading/writing and API communication.

## Features

- Converts plain text articles into HTML using OpenAI's GPT-3.5 model.
- Automatically adds image placeholders (`<img src="image_placeholder.jpg" alt="prompt">`).
- Structures the article content with appropriate HTML tags.
- Saves the generated HTML to a file (`artykul.html`).

## Requirements

- Python 3.x
- OpenAI API key
- OpenAI Python library

## Installation

To install the project locally, clone the repository using Git:

```
git clone https://github.com/kseternus/ai-article-processor.git
cd ai-article-processor
```
Then, install the required dependencies:
```
pip install -r requirements.txt
```

## How to Use

1. Place your article text in a file called `article.txt` in the same directory as the script.
2. Run the script:
    ```bash
    python main.py
    ```

3. The script will:
    - Read the text from `article.txt`.
    - Send the text to the OpenAI API for conversion to HTML.
    - Save the generated HTML content in a file named `artykul.html`.

4. After running the script, you will find the `artykul.html` file in the same directory, ready for use.

## Error Handling

- The script includes error handling for file reading and writing. If the file `article.txt` is not found or cannot be read, you will get an appropriate error message.
- If there are issues with the OpenAI API communication, an error message will be displayed and the script will terminate gracefully.

## Script Breakdown

1. **Reading the Article**: 
   The script reads the article from a file (`article.txt`) using the `read_file()` function.

2. **Converting to HTML**:
   The `create_html_file()` function sends the article content to OpenAI's GPT model, asking it to convert the article into HTML. The prompt instructs the model to format the text with HTML tags and add image placeholders.

3. **Saving the HTML File**: 
   The generated HTML content is saved to a file (`artykul.html`) using the `save_file()` function.

4. **Main Function**: 
   The `main()` function orchestrates the reading, processing, and saving of the article.

## Troubleshooting

- **API Key Errors**: Make sure that you have correctly set up your OpenAI API key in the `openai_api_key.py` file. If the key is missing or invalid, you will get an authentication error.
- **File Not Found**: Ensure that `article.txt` exists in the same directory as the script. If the file is missing, the script will not work.
- **API Communication Errors**: If there is an issue with OpenAI's API (e.g., rate limiting or network issues), the script will print an error message and terminate.
