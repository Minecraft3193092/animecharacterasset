// 1. Select the specific element
const element = document.querySelector(".content-box");

// 1.1 Select all the elements
const elements = document.querySelectorAll(".content-box");

// 2. Perform a case-sensitive replacement of the first match
element.innerHTML = element.innerHTML.replace("oldWord", "newWord");

// 3. Perform a global, case-insensitive replacement using Regular Expressions (Regex)
element.innerHTML = element.innerHTML.replace(/oldWord/gi, "newWord");

// 3.1 Perform a global, case-insensitive replacement using Regular Expressions (Regex)
elements.forEach(el => {
  el.innerHTML = el.innerHTML.replace(/西班牙/g, "阿根廷");
});

// 1. 抓到最外層的播放器影子宿主
const host = document.querySelector('video-player-tag-name'); 

if (host && host.shadowRoot) {
  // 2. 穿透影子邊界，尋找裡面的內容盒子
  const element = host.shadowRoot.querySelector('.content-box');
  if (element) {
    element.innerHTML = element.innerHTML.replace("西班牙", "阿根廷");
  }
}