// 強制改為 2000 年
const RealDate = window.Date;
window.Date = function(...args) {
  if (args.length === 0) {
    const d = new RealDate();
    d.setFullYear(2000); // 強制改為 2000 年
    return d;
  }
  return new RealDate(...args);
};
window.Date.prototype = RealDate.prototype;
window.Date.now = () => new window.Date().getTime();

// 強制改為 2000 年 0101
const RealDate = window.Date;
window.Date = function(...args) {
  if (args.length === 0) {
    const d = new RealDate();
    d.setFullYear(2000, 12, 1); // 強制改為 2000 年
    return d;
  }
  return new RealDate(...args);
};
window.Date.prototype = RealDate.prototype;
window.Date.now = () => new window.Date().getTime();