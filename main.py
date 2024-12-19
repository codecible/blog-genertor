import sys
from openai_handler import generate_text

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
        generated_text = generate_text(theme)
        
        # 打印生成的内容
        print("\n=== 生成的内容 ===")
        print(generated_text)
        
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main() 