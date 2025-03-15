# For GirlGPT Developers

## API Documentation

See [api_documentation.md](api_documentation.md) for detailed API documentation.

## Project Structure

- `app.py` - Main Flask application with API endpoints
- `img2chat.py` - Module for converting chat screenshots to text
- `uploads/` - Directory for temporary storage of uploaded images
- `requirements.txt` - Python dependencies
- `api_documentation.md` - API documentation for frontend developers

## Development

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