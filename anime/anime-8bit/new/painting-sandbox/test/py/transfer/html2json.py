import re
import json
import os

def parse_html_inside_perl():
    current_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
    input_path = os.path.join(current_dir, "issues.pl")
    output_path = os.path.join(current_dir, "issues.json")
    
    if not os.path.exists(input_path):
        print("❌ 找不到 issues.pl")
        return

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    print("🚀 偵測到 HTML 結構，正在啟動網頁標籤字串清理引擎...")

    # 1. 🎯 策略 A：抓取所有 <h1> 或 <h2> 標題標籤裡面的文字
    # 2002 年的網頁很喜歡用 <h1>當作法案名稱
    headings = re.findall(r'<h[12]>(.*?)</h[12]>', content, re.IGNORECASE)

    # 2. 🎯 策略 B：如果沒有 h1，改抓所有 <p> 段落（這通常是法案的故事內容）
    paragraphs = re.findall(r'<p>(.*?)</p>', content, re.IGNORECASE)

    # 清洗資料：去掉文字兩端的空格，移除殘留的 HTML 碼
    clean_headings = [re.sub(r'<[^>]+>', '', h).strip() for h in headings if h.strip()]
    clean_paragraphs = [re.sub(r'<[^>]+>', '', p).strip() for p in paragraphs if p.strip()]

    # 3. 組合包：把抓到的東西整理成漂亮的結構
    game_data = {
        "detected_titles_count": len(clean_headings),
        "detected_stories_count": len(clean_paragraphs),
        "extracted_titles": clean_headings[:100], # 先拿前 100 個出來看
        "extracted_paragraphs": clean_paragraphs[:50]
    }

    # 4. 真正寫入 JSON 檔案
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(game_data, json_file, ensure_ascii=False, indent=4)

    print(f"🎉 成功！這次成功抓到了 {len(clean_headings)} 個標題與 {len(clean_paragraphs)} 段故事文字！")
    print(f"💾 請檢查這個新生成的檔案：{output_path}")

parse_html_inside_perl()