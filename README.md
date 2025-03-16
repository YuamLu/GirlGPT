# For GirlGPT Developers

## API Documentation

See [api_documentation.md](api_documentation.md) for detailed API documentation.

## Project Structure

- `app.py` - Main Flask application with API endpoints
- `img2chat.py` - Module for converting chat screenshots to text
- `chat_analysis.py` - Module for generating response suggestions
- `uploads/` - Directory for temporary storage of uploaded images
- `requirements.txt` - Python dependencies
- `api_documentation.md` - API documentation for frontend developers
- `tst_img/` - Directory containing test images
- `index.html` - Frontend interface for the application

## Development

### Using the img2chat Module

The `img2chat.py` module provides a function to convert chat screenshots to structured text using OpenAI's GPT-4o model. The function supports three types of inputs:

1. **File path**: Path to an image file on the local filesystem
2. **Base64 encoded image**: A base64 encoded string of an image
3. **URL**: A URL pointing to an image

Example usage:

```python
from img2chat import img2chat

# Using a file path
result = img2chat("path/to/image.jpg")

# Using a base64 encoded image
with open("path/to/image.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")
result = img2chat(base64_image)

# Using a URL
result = img2chat("https://example.com/image.jpg")
```

### Using the chat_analysis Module

The `chat_analysis.py` module provides a function to generate response suggestions based on chat text using OpenAI's GPT-4o model. The function takes a chat text as input and returns a response suggestion in XML format.

Example usage:

```python
from chat_analysis import get_suggestion

# Using a chat text
chat_text = "<chat><usr>你喜歡過除了我以外的異性嗎</usr></chat>"
result = get_suggestion(chat_text)
```

The response is formatted in XML with `<suggestion>` and `<example>` tags:

```
<suggestion>建議內容</suggestion><example>範例回覆</example>
```

### Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key
- `PORT` (optional) - Port to run the server on (default: 8080)

## Running the Application

To run the application locally:

```
python app.py
```

The application will be available at http://localhost:8080

## Frontend Interface

The application provides a simple web interface for users to:

1. Upload a chat screenshot for analysis
2. Manually enter chat text for analysis
3. Receive response suggestions based on the chat content

## Deployment

For production deployment, consider using Gunicorn:

```
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```