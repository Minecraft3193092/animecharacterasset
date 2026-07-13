import re
import json
import os

def parse_perl_to_json():
    # 1. 自動定位路徑，確保在 Windows 下不會迷路
    current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
    input_path = os.path.join(current_dir, "issues.pl")
    output_path = os.path.join(current_dir, "issues.json")
    
    # 檢查檔案是否存在
    if not os.path.exists(input_path):
        print(f"❌ 找不到輸入檔案！請確保 'issues.pl' 放在這個資料夾：\n   {current_dir}")
        return

    print("📖 正在讀取 1411 KB 的 issues.pl 檔案...")
    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        perl_content = f.read()
    
    print(f"原始檔案大小: {len(perl_content) / 1024:.2f} KB")

    # 2. 🚀 升級版 Regex：
    # title\s*=>\s* -> 匹配 title => 
    # (['"])          -> 匹配開頭是單引號或雙引號 (暫存為群組 1)
    # (.*?)           -> 抓取裡面的故事標題 (我們要的資料)
    # \1              -> 確保結尾的引號跟開頭的一模一樣
    pattern = r'title\s*=>\s*([\'"])(.*?)\1'
    titles_with_quotes = re.findall(pattern, perl_content)
    
    # 因為 re.findall 帶有兩個群組，會抓出 [('"', '標題'), ("'", '標題2')]
    # 我們只需要後面的標題文字，所以用列表推導式洗乾淨：
    titles = [item[1] for item in titles_with_quotes]

    # 3. 🔍 檢查是否有抓到東西
    print(f"🔍 掃描完畢！共抓取到 {len(titles)} 個法案標題。")
    
    if len(titles) == 0:
        print("⚠️ 警告：Regex 沒有匹配到任何 title 欄位！")
        print("請檢查 issues.pl 檔案裡，標題那一行是不是寫成 'title' => ... 或是其它寫法？")
        # 印出前 500 個字元供你肉眼觀察語法
        print("\n=== 檔案前 500 字元預覽 ===")
        print(perl_content[:500])
        print("===========================\n")

    # 4. 寫入 JSON 檔案
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(titles, json_file, ensure_ascii=False, indent=4)
        
    print(f"💾 檔案已寫入：{output_path}")

# 执行執行
parse_perl_to_json()