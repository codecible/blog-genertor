# 智能文本生成与网页搜索工具

这是一个Python程序，可以根据用户提供的主题生成相关关键词，并基于这些关键词进行智能网页搜索，获取相关的高质量内容。

## 功能特点

1. **关键词生成**
   - 使用Monica API（OpenAI兼容接口）根据主题智能生成关键词
   - 生成5个准确、简洁、不重复的关键词
   - 支持中文输入和输出

2. **智能网页搜索**
   - 使用Exa API进行神经网络搜索
   - 支持多个主流网站（如Wikipedia、知乎、百度等）
   - 智能排序搜索结果
   - 提供相关度评分和内容摘要

## 使用前准备

1. 确保已安装Python 3.7或更高版本

2. 安装项目依赖：   
    ```bash
    pip install -r requirements.txt   
    ```

3. 配置环境变量：   
   创建 `.env` 文件并设置以下环境变量：
   ```text
   # Monica API配置
   MONICA_API_KEY=你的Monica API密钥
   MONICA_MODEL=moonshot-v1-8k  # 可选，默认使用moonshot-v1-8k

   # Exa API配置
   EXA_API_KEY=你的Exa API密钥
   ```

## 使用方法

在命令行中运行以下命令：
```bash
python main.py "你的主题"
```

示例：
```bash
python main.py "人工智能"
```

## 输出说明

程序会输出两部分内容：

1. **生成的关键词**
   - 5个与主题相关的关键词
   - 关键词之间用中文逗号分隔

2. **搜索结果**
   - 标题（title）：网页标题
   - 链接（url）：网页链接
   - 相关度（score）：内容相关度评分
   - 摘要（highlight）：相关内容摘要

## 错误处理

程序会处理以下常见错误：
- API密钥未设置或无效
- API调用失败
- 搜索结果为空
- 网络连接问题

## 技术说明

1. **Monica API配置**
   - 基础URL：https://api.moonshot.cn/v1
   - 默认模型：moonshot-v1-8k
   - 支持自定义模型通过环境变量设置

2. **Exa搜索配置**
   - 支持的网站：wikipedia.org, zhihu.com, baidu.com
   - 每次返回前5个最相关的结果
   - 每个结果包含3句相关内容摘要

## 注意事项

1. 请确保您有足够的API调用额度
2. 建议使用VPN或代理以确保稳定的API访问
3. 搜索结果的质量可能因主题和关键词的具体情况而异

## 维护和更新

如需修改或扩展功能，可以调整以下部分：
1. `openai_handler.py`中的`generate_text`函数：修改关键词生成逻辑
2. `openai_handler.py`中的`web_key_search`函数：调整搜索参数和结果处理
3. `.env`文件：更新API密钥和模型配置