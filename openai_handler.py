import os
from openai import OpenAI
from dotenv import load_dotenv

def generate_text(theme: str) -> str:
    """
    根据给定主题生成文本内容
    
    Args:
        theme (str): 用户提供的主题
    
    Returns:
        str: 生成的文本内容
    
    Raises:
        Exception: 当API调用失败时抛出异常
    """
    # 加载.env文件中的环境变量
    load_dotenv()
    
    # 从环境变量获取API密钥
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise Exception("请设置OPENAI_API_KEY环境变量")
    
    # 初始化OpenAI客户端
    client = OpenAI(api_key=api_key)
    
    try:
        # 调用OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个专业的内容创作者，请根据用户提供的主题生成相关内容。"},
                {"role": "user", "content": f"请围绕主题'{theme}'生成内容"}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        # 返回生成的文本
        return response.choices[0].message.content
    
    except Exception as e:
        raise Exception(f"调用OpenAI API时发生错误: {str(e)}") 