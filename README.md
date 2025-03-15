# Chat Assistant Backend

This is the backend service for the Chat Assistant application, which helps users analyze chat conversations and provides response suggestions.

## Features

- Convert chat screenshots to structured text format
- Process manually entered chat text
- Generate analysis and response suggestions based solely on the conversation content
- RESTful API for frontend integration

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Running the Application

Start the development server:

```
python app.py
```

The server will start on http://localhost:4998 by default.

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

## License

[MIT License](LICENSE) 