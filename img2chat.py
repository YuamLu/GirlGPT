"""
Function to convert an image of chat to structured text using OpenAI's GPT-4o model.

This module provides a function to process chat screenshots and convert them
into structured text format using OpenAI's vision capabilities.
"""
import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def encode_image(image_path):
    """
    Encode an image file to base64.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Base64 encoded image string
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def img2chat(image_input):
    """
    Convert a chat screenshot to structured text using OpenAI's GPT-4o model.

    This function takes either an image path or a base64 encoded image string
    and uses OpenAI's GPT-4o model to extract the conversation in a structured format.

    Args:
        image_input (str): Either a file path to an image, a URL, or a base64 encoded image

    Returns:
        str: The structured chat text extracted from the image
    """
    # Initialize OpenAI client with API key from environment variable
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Determine if the input is a file path, URL, or base64 string
    if os.path.isfile(image_input):
        # It's a file path, encode it to base64
        base64_image = encode_image(image_input)
        image_url = f"data:image/jpeg;base64,{base64_image}"
    elif image_input.startswith("data:image"):
        # It's already a base64 data URL
        image_url = image_input
    elif image_input.startswith("http"):
        # It's a URL
        image_url = image_input
    else:
        # Assume it's a raw base64 string
        image_url = f"data:image/jpeg;base64,{image_input}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "你是一位善於將對話的聊天紀錄的截圖，還原成文本結構的聊天資訊的專家。"
                           "對於收到的每一張截圖，請仔細閱讀他們的聊天紀錄，左側的訊息表示其他人傳的訊息、"
                           "右邊則是用戶傳的訊息，將聊天紀錄的截圖轉換成文本格式的聊天。"
                           "請依照訊息的時間順序，由舊到新的順序，使用XML的格式來輸出聊天紀錄，"
                           "<usr>表示使用者的聊天對象的訊息、<self>表示使用者傳的訊息，"
                           "最多只能有chat、usr這種二級結構，"
                           "例如<chat><usr>你好你好</usr><usr>哈囉哈囉</usr></chat>\n\n"
                           "務必要確保忠時的還原使用者的對話紀錄，並且忽略聊天室中像是圖片、音訊等非文字的資訊。"
                           "並使用<chat></chat>為標記，包裹整段的聊天資訊。如果你解析不出任何訊息，輸出<chat></chat>就好。"
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "請分析這張聊天截圖並轉換成文本格式:"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        }
                    }
                ]
            }
        ],
        max_tokens=913,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    # Example usage with a file path
    print("\nExample with file path:")
    print(img2chat("tst_img/tst1.png"))