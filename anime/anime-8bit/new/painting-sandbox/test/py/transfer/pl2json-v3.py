import re
import json

def parse_perl_to_json():
    # 確保讀取的是你本地的那台 1411 KB 檔案
    with open("issues.pl", "r", encoding="utf-8") as f:
        perl_content = f.read()
    
    # 抓取所有 title => "..." 裡面的文字
    titles = re.findall(r'title\s*=>\s*"(.*?)"', perl_content)
    
    # 寫入 JSON 檔案
    with open("issues.json", "w", encoding="utf-8") as json_file:
        json.dump(titles, json_file, ensure_ascii=False, indent=4)

# 💡 關鍵：必須在這裡真正呼叫它，程式才會動手寫檔案！
parse_perl_to_json()

print("🎉 成功把 1411 KB 的老古董瘦身並打包成現代 JSON！")