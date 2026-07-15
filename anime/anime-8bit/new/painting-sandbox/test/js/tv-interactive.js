// 1. 監聽整個網頁的鍵盤事件
window.addEventListener('keydown', function(event) {
  // 阻止瀏覽器的預設行為（例如防止按空白鍵時網頁往下捲動）
  event.preventDefault();

  console.log(`[Debug] 偵測到按鍵輸入! Key: ${event.key} | Code: ${event.keyCode}`);

  // 2. 模擬遙控器紅、綠、黃、藍四色按鍵
  switch(event.key) {
    case "Red":
    case "r": // 電腦鍵盤按 R
      triggerEbcWeatherUI(); // 執行「東森氣象查詢」Debug
      break;
    case "Blue":
    case "b": // 電腦鍵盤按 B
      triggerEbcLotteryUI(); // 執行「抽獎活動」Debug
      break;
    case "Enter": // 按 確認 鍵
      console.log("[Debug] 執行選單確認操作");
      break;
  }
});

// 模擬東森氣象介面彈出
function triggerEbcWeatherUI() {
  console.log("%c[EBC 互動渲染] 🔴 紅色鍵觸發成功：正在加載氣象數據...", "color: red; font-weight: bold;");
  // 在畫面上渲染出一個測試用的氣象 UI 框
  let ui = document.getElementById('debug-weather-box');
  if(!ui) {
    ui = document.createElement('div');
    ui.id = 'debug-weather-box';
    ui.style.cssText = "position: absolute; top: 10%; left: 10%; width: 300px; height: 200px; background: rgba(0,0,0,0.8); color: white; border: 2px solid red; z-index: 10000; padding: 20px;";
    ui.innerHTML = "<h3>🌦️ 東森氣象 Debug 視窗</h3><p>地區：新北市五股區</p><p>溫度：28°C</p><p>按 'Esc' 鍵關閉</p>";
    document.body.appendChild(ui);
  }
}