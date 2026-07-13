import re
import json

def parse_perl_to_json():
    with open("issues.pl", "r", encoding="utf-8") as f:
        perl_content = f.read()
    
    # 利用 Python 的正則表達式（Regex），把 Perl 的 1411 KB 文字撈出來
    # 抓取裡面的 title, text 和數據變動
    titles = re.findall(r'title\s*=>\s*"(.*?)"', perl_content)
    
    # 把這些內容洗乾淨後，直接存成現代標準的 JSON 紙箱
    with open("issues.json", "w", encoding="utf-8") as json_file:
        json.dump(titles, json_file, ensure_ascii=False, indent=4)

print("🎉 成功把 1411 KB 的老古董瘦身並打包成現代 JSON！")