// 1. 物理定位：抓取特定 Class 的 Canvas 元素
const canvas = document.querySelector(".video-overlay-canvas");

if (canvas) {
  // 2. 取得 2D 渲染上下文（這是操作畫布的物理畫筆）
  const ctx = canvas.getContext("2d");
  
  // 3. 物理擦除：將整張畫布（或特定區域）的像素全部清空
  // clearRect(x, y, width, height)
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // 4. 設定新文字的物理樣式（必須手動指定字型、大小與顏色）
  ctx.font = "bold 32px Arial";     // 字體大小與字型
  ctx.fillStyle = "#FF0000";        // 顏色（例如紅色）
  ctx.textAlign = "center";         // 水平對齊
  ctx.textBaseline = "middle";      // 垂直對齊
  
  // 5. 重新繪製：在畫布的物理中心點印上新文字
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  ctx.fillText("阿根廷", centerX, centerY);
  
  console.log("Canvas 物理重繪完成！文字已替換為『阿根廷』！");
} else {
  console.log("找不到該 Class 的 Canvas 元素");
}