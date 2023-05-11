// let isMathjaxConfig = false; //用于标识是否配置

// const initMathjaxConfig = () => {
//     if (!window.MathJax) {
//         return;
//     }
//     window.MathJax.Hub.Config({
//         isMathjaxConfig: true,
//         extensions: ["tex2jax.js"],
//         showProcessingMessages: false, //关闭js加载过程信息
//         messageStyle: "none", //不显示信息
//         jax: ["input/TeX", "output/HTML-CSS"],
//         tex2jax: {
//             inlineMath: [
//                 ["$", "$"],
//                 ["\\(", "\\)"]
//             ], //行内公式选择符
//             displayMath: [
//                 ["$$", "$$"],
//                 ["\\[", "\\]"]
//             ], //段内公式选择符
//             skipTags: ["script", "noscript", "style", "textarea", "pre", "code", "a"] //避开某些标签
//         },
//         "HTML-CSS": {
//             availableFonts: ["STIX", "TeX"], //可选字体
//             showMathMenu: true //关闭右击菜单显示
//         },
//     });
//     isMathjaxConfig = true;

// };

// const MathQueue = function() {
//     if (!window.MathJax) {
//         return;
//     }
//     console.log("aaaaaaa======0");
//     window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]); //整个dom下渲染
//     // window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, document.getElementById(elementId)]); //固定id元素渲染，
// }


// export default {
//     isMathjaxConfig,
//     initMathjaxConfig,
//     MathQueue
// }