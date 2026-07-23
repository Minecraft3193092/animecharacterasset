// 在 gemini.google.com 的 Console 中執行此檢測腳本
const checkSearchGrounding = () => {
    // 檢查頁面中是否含有外部來源連結或 Grounding 標籤元件
    const sourceLinks = document.querySelectorAll('a[href^="http"]:not([href*="google.com"])');
    const groundingElements = document.querySelectorAll('.fact-check-container, [data-test-id="source-attribution"], .sources-container');

    if (sourceLinks.length > 0 || groundingElements.length > 0) {
        console.log("🔍 [檢測結果]: 本次回應有呼叫 Google 搜尋 (Search Grounding)！");
        console.log("偵測到的外部來源:", Array.from(sourceLinks).map(a => a.href));
    } else {
        console.log("⚡ [檢測結果]: 本次回應完全由 Gemini 內部權重生成（未偵測到搜尋）。");
    }
};

// 執行檢測
checkSearchGrounding();