# For GirlGPT Developers

## API Documentation

See [api_documentation.md](api_documentation.md) for detailed API documentation.

## Project Structure

- `app.py` - Main Flask application with API endpoints
- `img2chat.py` - Module for converting chat screenshots to text
- `test_img2chat.py` - Test script demonstrating how to use img2chat.py
- `uploads/` - Directory for temporary storage of uploaded images
- `requirements.txt` - Python dependencies
- `api_documentation.md` - API documentation for frontend developers
- `tst_img/` - Directory containing test images

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

See `test_img2chat.py` for more detailed examples.

### Adding the Response Generation Function

The response generation function is currently a placeholder. When the actual implementation is ready, replace the `generate_response` function in `app.py` with the real implementation. The function should extract all necessary context from the provided chat text without requiring additional context information.

### Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key
- `PORT` (optional) - Port to run the server on (default: 4998)

## Deployment

For production deployment, consider using Gunicorn:

```
gunicorn -w 4 -b 0.0.0.0:4998 app:app
```