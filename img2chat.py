"""
Function to convert an image of chat to structured text using OpenAI's GPT-4o model.

This module provides a function to process chat screenshots and convert them
into structured text format using OpenAI's vision capabilities.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def img2chat(image_url):
    """
    Convert a chat screenshot to structured text using OpenAI's GPT-4o model.

    This function takes an image URL of a chat screenshot and uses OpenAI's
    GPT-4o model to extract the conversation in a structured format.

    Args:
        image_url (str): URL or base64 encoded image of the chat screenshot

    Returns:
        dict: The response from OpenAI containing the structured chat text
    """
    # Initialize OpenAI client with API key from environment variable
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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


# https://hackmd.io/_uploads/SJpzusfnkl.png
if __name__ == "__main__":
    print(img2chat("https://hackmd.io/_uploads/SJpzusfnkl.png"))