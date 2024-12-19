import sys
import openai_handler

def main():
    # 检查是否提供了主题参数
    if len(sys.argv) < 2:
        print("请提供一个主题作为参数")
        print("使用方式: python main.py '你的主题'")
        sys.exit(1)
    
    # 获取命令行参数中的主题
    theme = sys.argv[1]
    
    try:
        # 调用OpenAI API生成文本
        generated_text = openai_handler.generate_text(theme)
        
        # 打印生成的内容
        print("\n=== 生成的关键词 ===")
        print(generated_text)
        
        # 使用关键词搜索并显示结果
        search_results = openai_handler.web_key_search(generated_text)
        # 打印生成的内容
        print("\n=== 使用关键词搜索并显示结果 ===")
        print(search_results)
        
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main() 