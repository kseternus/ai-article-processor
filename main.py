import openai
from openai_api_key import api_key

# Set up the API key with error handling
try:
    openai.api_key = api_key  # For security reasons import API key from another file
    print("API Key set successfully.")
except Exception as e:
    print(f"Error setting API key: {e}")
    raise


def read_file(file_path):
    """Reads text from a specified file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'The file at {file_path} was not found.')
    except IOError as e:
        raise IOError(f'Error reading the file: {str(e)}')


def save_file(file_path, content):
    """Saves the given content to a specified file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except IOError as e:
        raise IOError(f'Error saving the file: {str(e)}')


def create_html_file(article):
    """Create an HTML file based on given text using OpenAI's GPT model."""
    system = 'You are an assistant that converts a text article into HTML.'

    prompt = (
        'Convert the following article into HTML, using appropriate HTML tags to structure your content. Do not include'
        ' <html>, <head>, or <body> tags. Do not use any CSS or JS. The code should be ready to paste between <body>'
        ' and </body> tags in a target HTML file. Find the best places to insert images, marking them with the <img>'
        ' tag and using the placeholder src="image_placeholder.jpg". Add an alt attribute to each image with the exact'
        ' prompt that can be used to generate the image. Place captions under images using the appropriate HTML tags.'
        f'\n\n{article}'
    )

    messages = [
        {'role': 'system', 'content': system},
        {'role': 'user', 'content': prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            max_tokens=3000,
            temperature=0.5
        )
        # Extract the HTML content from the response
        return response['choices'][0]['message']['content'].strip()
    except openai.error.OpenAIError as e:
        raise RuntimeError(f'Error communicating with OpenAI API: {e}')


def main():
    """Main function that reads an article, converts it to HTML, and saves it to a file."""
    print('Generating HTML based on the provided text article. Please wait...')

    article_path = 'article.txt'

    # Read the article from a file
    try:
        article_content = read_file(article_path)
    except Exception as e:
        print(f'Error reading article: {e}')
        return

    # Convert the article text to HTML format
    try:
        html_content = create_html_file(article_content)
    except Exception as e:
        print(f'Error generating HTML: {e}')
        return

    # Save the generated HTML to a file
    try:
        save_file('artykul.html', html_content)
        print('HTML file saved successfully')
    except Exception as e:
        print(f'Error saving HTML file: {e}')


if __name__ == '__main__':
    main()
