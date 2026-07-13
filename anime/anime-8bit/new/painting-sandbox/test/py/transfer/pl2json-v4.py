import re
import json
import os

def parse_perl_to_json():
    # 🎯 自動獲取當前 Python 檔案所在的資料夾絕對路徑
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 拼湊出絕對路徑，徹底解決 Windows 工作目錄迷路的問題
    input_path = os.path.join(current_dir, "issues.pl")
    output_path = os.path.join(current_dir, "issues.json")
    
    with open(input_path, "r", encoding="utf-8") as f:
        perl_content = f.read()
    
    titles = re.findall(r'title\s*=>\s*"(.*?)"', perl_content)
    
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(titles, json_file, ensure_ascii=False, indent=4)

# 執行函式
parse_perl_to_json()
print("🎉 成功把 1411 KB 的老古董瘦身並打包成現代 JSON！")