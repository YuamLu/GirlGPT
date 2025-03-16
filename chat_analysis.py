"""
Chat analysis module for generating response suggestions.

This module provides functionality to generate response suggestions
using OpenAI's GPT models.
"""

from openai import OpenAI


def get_suggestion(user_input):
    """
    Generate a response suggestion based on user input.
    
    This function uses OpenAI's GPT model to generate a response suggestion
    for a given user input. The response is formatted in XML with suggestion
    and example tags.
    
    Args:
        user_input (str): The user's input message
        
    Returns:
        str: The generated response suggestion
    """
    client = OpenAI()
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system", 
                "content": "你是一個可以提供尊重對方且讓提問者開心的回覆的助手，"
                           "使用者將會輸入對方的問題，回覆時請撇除預設立場且一定要給出回復不要轉移話題，"
                           "可以偏愛提問者，要強調出他特殊的魅力。請使用XML格式，"
                           "生成針對使用者的應對建議，以及實際舉例來回覆使用者訊息，"
                           "使用<suggestion>和<example>標記來格式化你的回覆，<example>不超過30字"
            },
            {"role": "user", "content": user_input}
        ]
    )
    
    return completion.choices[0].message.content


if __name__ == "__main__":
    # Example usage
    dialogue = "你喜歡過除了我以外的異性嗎"
    response = get_suggestion(dialogue)
    print(response)
