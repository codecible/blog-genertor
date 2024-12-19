import os
from openai import OpenAI
from dotenv import load_dotenv

def generate_text(theme: str) -> str:
    """
    根据给定主题生成搜索关键词
    
    Args:
        theme (str): 用户提供的主题
    
    Returns:
        str: 生成的文本内容
    
    Raises:
        Exception: 当API调用失败时抛出异常
    """
    # 加载.env文件中的环境变量
    load_dotenv()
    
    # 从环境变量获取Monica API密钥
    api_key = os.getenv('MONICA_API_KEY')
    if not api_key:
        raise Exception("请设置MONICA_API_KEY环境变量")
    
    # 初始化OpenAI客户端，但使用Monica的API地址
    client = OpenAI(
        api_key=api_key,
        base_url="https://openapi.monica.im/v1"  # Monica API的基础URL
    )
    
    try:
        # 调用Monica API (与OpenAI兼容的接口)
        model = os.getenv('MONICA_MODEL', 'gpt-4o-mini')  # 使用环境变量或默认值
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是一个专业的内容创作者，请根据用户提供的主题生成相关内容。"},
                {"role": "user", "content": f"主题：{theme}\n"
                 "请为以上主题生成5个关键词,这些关键词应当:\n"
                 "准确反映主题的核心内容\n"
                 "简洁且具有代表性\n" 
                 "相互之间不重复\n"
                 "用中文逗号分隔\n"
                 "直接输出关键词,无需其他说明文字\n"
                 "请按照以下格式输出:\n"
                 "关键词1，关键词2，关键词3，关键词4，关键词5"}
            ],
            temperature=os.getenv('TEMPERATURE', 0.7),
            max_tokens=os.getenv('MAX_TOKENS', 1000)
        )
        
        # 返回生成的文本
        return response.choices[0].message.content
    
    except Exception as e:
        raise Exception(f"调用Monica API时发生错误: {str(e)}") 