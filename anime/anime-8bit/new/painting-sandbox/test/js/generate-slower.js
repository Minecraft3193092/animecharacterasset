const fullText = "這裡有長達數萬字的程式碼資產...（省略）";
const responseBox = document.getElementById('response-box');
let currentIndex = 0;
const charsPerFrame = 2; // ⚡ 每幀（約16.6毫秒）注入2個字，可自由調整速度大帳簿

function renderFrame() {
    if (currentIndex < fullText.length) {
        // ✂️ 從緩衝區切出一小塊字
        const chunk = fullText.substr(currentIndex, charsPerFrame);
        
        // 物理增量注入，0% 重複排版前面已畫好的字
        responseBox.insertAdjacentText('beforeend', chunk);
        
        currentIndex += charsPerFrame;
        
        // 📡 配合螢幕刷新率，下一幀繼續餵食 DOM
        requestAnimationFrame(renderFrame);
    }
}

// 啟動高效能渲染
requestAnimationFrame(renderFrame);