// 本地端的翻譯字典
const myTranslationMap = {
  "我的相簿": "My Album",
  "留言板": "Guestbook",
  "加入好友": "Add Friend"
};

// 寫一個遞迴函數，物理性地掃描網頁上所有的「純文字節點」
function translateDOM(node) {
  if (node.nodeType === Node.TEXT_NODE) {
    const trimmedText = node.nodeValue.trim();
    if (myTranslationMap[trimmedText]) {
      // 找到匹配的中文，直接在瀏覽器記憶體中物理替換成英文/日文
      node.nodeValue = myTranslationMap[trimmedText];
    }
  } else {
    // 如果不是文字節點，就繼續往子節點物理深挖（如 <div> 裡的 <span>）
    node.childNodes.forEach(translateDOM);
  }
}

// 開始在本地端執行全網頁物理替換
translateDOM(document.body);