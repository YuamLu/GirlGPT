"""
Flask backend for the chat assistance website.

This application provides API endpoints for processing chat screenshots,
manual text input, and generating response suggestions.
"""
import os
import base64
import json
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from img2chat import img2chat

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure upload folder for images
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_response(chat_text):
    """
    Generate response suggestions based on chat text.
    
    This is a placeholder function that will be replaced with the actual
    implementation once it's developed.
    
    Args:
        chat_text (str): The chat text to analyze
        
    Returns:
        dict: Analysis and response suggestions
    """
    # Placeholder implementation
    return {
        "analysis": "This is a placeholder analysis of the conversation.",
        "suggestion": "Here's a suggested response based on the conversation."
    }

@app.route('/', methods=['GET'])
def index():
    """Serve the main HTML page"""
    return send_file('index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok"})

@app.route('/api/process-image', methods=['POST'])
def process_image():
    """
    Process a chat screenshot and return analysis and suggestions.
    
    Accepts an image file or a base64 encoded image string.
    """
    try:
        # Check if the post request has the file part
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                return jsonify({"error": "No selected file"}), 400
                
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Convert file to base64 for processing
                with open(filepath, "rb") as image_file:
                    base64_image = base64.b64encode(image_file.read()).decode('utf-8')
                image_url = f"data:image/{filepath.split('.')[-1]};base64,{base64_image}"
                
                # Process the image
                chat_text = img2chat(image_url)
                
                # Generate response suggestions
                response_data = generate_response(chat_text)
                
                # Return the results
                return jsonify({
                    "chat_text": chat_text,
                    "analysis": response_data["analysis"],
                    "suggestion": response_data["suggestion"]
                })
            else:
                return jsonify({"error": "File type not allowed"}), 400
                
        # Check if base64 image was provided
        elif 'image_data' in request.json:
            image_data = request.json['image_data']
            
            # Process the image
            chat_text = img2chat(image_data)
            
            # Generate response suggestions
            response_data = generate_response(chat_text)
            
            # Return the results
            return jsonify({
                "chat_text": chat_text,
                "analysis": response_data["analysis"],
                "suggestion": response_data["suggestion"]
            })
            
        else:
            return jsonify({"error": "No image provided"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/process-text', methods=['POST'])
def process_text():
    """
    Process manually entered chat text and return analysis and suggestions.
    """
    try:
        data = request.json
        
        if not data or 'chat_text' not in data:
            return jsonify({"error": "No chat text provided"}), 400
            
        chat_text = data['chat_text']
        
        # Generate response suggestions
        response_data = generate_response(chat_text)
        
        # Return the results
        return jsonify({
            "analysis": response_data["analysis"],
            "suggestion": response_data["suggestion"]
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4998))
    app.run(host='0.0.0.0', port=port, debug=True) 