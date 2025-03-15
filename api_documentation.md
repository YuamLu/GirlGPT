# Chat Assistant API Documentation

This document describes the API endpoints available for the Chat Assistant backend service.

## Base URL

All endpoints are relative to the base URL of the deployed service:

```
http://localhost:4998
```

When deployed to production, this will be replaced with the actual production URL.

## Endpoints

### Health Check

Check if the API is running.

- **URL**: `/api/health`
- **Method**: `GET`
- **Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
      "status": "ok"
    }
    ```

### Process Image

Upload a chat screenshot and get analysis and response suggestions.

- **URL**: `/api/process-image`
- **Method**: `POST`
- **Content-Type**: `multipart/form-data` or `application/json`

#### Option 1: File Upload

- **Parameters**:
  - `file`: The image file (PNG, JPG, JPEG, GIF)

- **Example Request**:
  ```
  POST /api/process-image
  Content-Type: multipart/form-data
  
  file: [binary data]
  ```

#### Option 2: Base64 Image

- **Parameters**:
  - `image_data`: Base64 encoded image string or image URL

- **Example Request**:
  ```json
  POST /api/process-image
  Content-Type: application/json
  
  {
    "image_data": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD..."
  }
  ```

- **Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
      "chat_text": "<chat><usr>Hello, how are you?</usr><self>I'm good, thanks!</self></chat>",
      "analysis": "This is a friendly conversation with simple greetings.",
      "suggestions": [
        "You could ask them about their day.",
        "You might want to share something interesting that happened to you.",
        "You could continue the conversation by asking a question."
      ]
    }
    ```

- **Error Responses**:
  - **Code**: 400
    - No image provided
    - File type not allowed
    - No selected file
  - **Code**: 500
    - Internal server error

### Process Text

Process manually entered chat text and get analysis and response suggestions.

- **URL**: `/api/process-text`
- **Method**: `POST`
- **Content-Type**: `application/json`

- **Parameters**:
  - `chat_text`: The chat text in XML format (required)

- **Example Request**:
  ```json
  {
    "chat_text": "<chat><usr>Can we meet tomorrow?</usr><self>I'm not sure yet.</self></chat>"
  }
  ```

- **Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
      "analysis": "This conversation is about scheduling a meeting. The user seems uncertain about their availability.",
      "suggestions": [
        "You could suggest an alternative time: 'How about next week instead?'",
        "You might want to explain why you're uncertain: 'I need to check my schedule first.'",
        "You could ask for more details: 'What time were you thinking?'"
      ]
    }
    ```

- **Error Responses**:
  - **Code**: 400
    - No chat text provided
  - **Code**: 500
    - Internal server error

## Chat Text Format

The chat text is formatted in XML with the following structure:

```xml
<chat>
  <usr>Message from the other person</usr>
  <self>Message from the user</self>
  <usr>Another message from the other person</usr>
  ...
</chat>
```

- `<usr>` tags contain messages from the user's chat partner
- `<self>` tags contain messages from the user themselves
- Messages should be in chronological order 