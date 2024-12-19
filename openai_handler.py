import os
import requests
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
    
    t = os.getenv('TEMPERATURE', 0.7)
    # print(t)

    # return "hhh"
    try:
        # 调用Monica API (与OpenAI兼容的接口)
        model = os.getenv('MONICA_MODEL', 'gpt-4o-mini')  # 使用环境变量或默认值
        # 发送请求参数值参考文档：https://platform.openai.com/docs/api-reference/chat/create
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
        )
        
        # 返回生成的文本
        return response.choices[0].message.content
    
    except Exception as e:
        raise Exception(f"调用Monica API时发生错误: {str(e)}") 
    

def web_key_search(keywords: str) -> list:
    """
    使用Exa API搜索关键词相关的网页内容
    
    Args:
        keywords (str): 以中文逗号分隔的关键词字符串
    
    Returns:
        list: 包含搜索结果的列表，每个结果是一个字典，包含标题、URL、相关度和摘要
    """
    # 加载环境变量
    load_dotenv()
    
    # 获取API密钥
    exa_api_key = os.getenv('EXA_API_KEY')
    if not exa_api_key:
        raise Exception("请设置EXA_API_KEY环境变量")
    
    # 准备请求
    headers = {
        "x-api-key": exa_api_key,
        "Content-Type": "application/json"
    }
    
    # 构建搜索请求
    data = {
        "query": keywords.replace("，", " "),  # 将中文逗号替换为空格
        "type": "neural",  # 使用神经搜索
        "numResults": 10,  # 返回的搜索结果数量。默认 10。
        "includeDomains": ["wikipedia.org", "zhihu.com", "baidu.com"],
        # "excludeDomains": ["twitter.com", "facebook.com"],
        "contents": {
            # 内容高亮，相当于相关网页摘录。
            "highlights": {
                # 内容高亮句子数
                "numSentences": 3,
                # 每页返回的片段数量。默认为 1
                "highlightsPerUrl": 1
            }
        }
    }
    
    try:
        # 发送请求
        response = requests.post(
            "https://api.exa.ai/search",
            headers=headers,
            json=data
        )
        # 检查响应状态码
        response.raise_for_status()
        
        # 解析JSON响应
        response_data = response.json()
        
        # 验证响应数据格式
        if not isinstance(response_data, dict):
            raise Exception("API返回的数据格式无效")
            
        # 获取搜索结果
        results = response_data.get("results")
        if not results:
            return []  # 如果没有结果返回空列表
        
        # 验证results是否为列表类型
        if not isinstance(results, list):
            raise Exception("API返回的results不是列表格式")
        
        # 按score排序并获取前5个结果
        sorted_results = sorted(results, key=lambda x: x.get("score", 0), reverse=True)[:5]
        
        # 整理搜索结果
        formatted_results = []
        for result in sorted_results:
            formatted_results.append({
                "title": result["title"],
                "url": result["url"],
                "score": result.get("score", "N/A"),
                "highlight": result.get("highlights", [""])[0] if result.get("highlights") else ""
            })
            
        return formatted_results
            
    except Exception as e:
        raise Exception(f"根据关键词在线搜索过程中发生错误: {str(e)}")