"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
exports.__esModule = true;
var raw = '/static';
var faceList = ["".concat(raw, "/emoji/smile.webp"), "".concat(raw, "/emoji/tv/tv.webp")];
var emojiList = [
    {
        '[口罩]': "".concat(raw, "/emoji/kouzhao.webp"),
        '[狗头]': "".concat(raw, "/emoji/goutou.webp"),
        '[微笑]': "".concat(raw, "/emoji/smile.webp"),
        '[OK]': "".concat(raw, "/emoji/ok.webp"),
        '[星星眼]': "".concat(raw, "/emoji/star.webp"),
        '[辣眼睛]': "".concat(raw, "/emoji/layanjing.webp"),
        '[吃瓜]': "".concat(raw, "/emoji/chigua.webp"),
        '[滑稽]': "".concat(raw, "/emoji/huaji.webp"),
        '[呲牙]': "".concat(raw, "/emoji/teeth.webp"),
        '[打call]': "".concat(raw, "/emoji/dacall.webp"),
        '[喝酒]': "".concat(raw, "/emoji/hejiu.webp"),
        '[乖]': "".concat(raw, "/emoji/guai.webp"),
        '[吐舌]': "".concat(raw, "/emoji/tushe.webp"),
        '[汗]': "".concat(raw, "/emoji/han.webp"),
        '[大哭2]': "".concat(raw, "/emoji/daku.webp"),
        '[超赞]': "".concat(raw, "/emoji/chaozan.webp"),
        '[超开心]': "".concat(raw, "/emoji/chaokaixin.webp"),
        '[委屈]': "".concat(raw, "/emoji/weiqu.webp"),
        '[困狗]': "".concat(raw, "/emoji/kungou.webp"),
        '[藏狐]': "".concat(raw, "/emoji/zanghu.webp"),
        '[脸红]': "".concat(raw, "/emoji/lianhong.webp"),
        '[脱单doge]': "".concat(raw, "/emoji/doge.webp"),
        '[给心心]': "".concat(raw, "/emoji/heart.webp"),
        '[笑]': "".concat(raw, "/emoji/dx.webp"),
        '[哦呼]': "".concat(raw, "/emoji/oh.webp"),
        '[嫌弃]': "".concat(raw, "/emoji/xq.webp"),
        '[喜欢]': "".concat(raw, "/emoji/like.webp"),
        '[酸了]': "".concat(raw, "/emoji/sl.webp"),
        '[大哭]': "".concat(raw, "/emoji/dq.webp"),
        '[害羞]': "".concat(raw, "/emoji/hx.webp"),
        '[无语]': "".concat(raw, "/emoji/wy.webp"),
        '[疑惑]': "".concat(raw, "/emoji/yh.webp"),
        '[调皮]': "".concat(raw, "/emoji/tiaopi.webp"),
        '[笑哭]': "".concat(raw, "/emoji/xiaoku.webp"),
        '[奸笑]': "".concat(raw, "/emoji/jianxiao.webp"),
        '[偷笑]': "".concat(raw, "/emoji/touxiao.webp"),
        '[大笑]': "".concat(raw, "/emoji/daxiao.webp"),
        '[阴险]': "".concat(raw, "/emoji/yinxian.webp"),
        '[捂脸]': "".concat(raw, "/emoji/wulian.webp"),
        '[惊喜]': "".concat(raw, "/emoji/jingxi.webp"),
        '[惊讶]': "".concat(raw, "/emoji/jingya.webp"),
        '[捂脸哭]': "".concat(raw, "/emoji/wulianku.webp"),
        '[妙啊]': "".concat(raw, "/emoji/miaoa.webp"),
        '[鼓掌]': "".concat(raw, "/emoji/guzhang.webp"),
        '[尴尬]': "".concat(raw, "/emoji/ganga.webp"),
        '[冷]': "".concat(raw, "/emoji/cold.webp"),
        '[灵魂出窍]': "".concat(raw, "/emoji/linghunchuqiao.webp"),
        '[傲娇]': "".concat(raw, "/emoji/aojiao.webp"),
        '[疼]': "".concat(raw, "/emoji/teng.webp"),
        '[吓]': "".concat(raw, "/emoji/xia.webp"),
        '[生病]': "".concat(raw, "/emoji/shengbing.webp"),
        '[吐]': "".concat(raw, "/emoji/tu.webp"),
        '[嘘声]': "".concat(raw, "/emoji/xusheng.webp"),
        '[捂眼]': "".concat(raw, "/emoji/wuyan.webp"),
        '[思考]': "".concat(raw, "/emoji/sikao.webp"),
        '[再见]': "".concat(raw, "/emoji/zaijian.webp"),
        '[翻白眼]': "".concat(raw, "/emoji/fanbaiyan.webp"),
        '[哈欠]': "".concat(raw, "/emoji/haqian.webp"),
        '[奋斗]': "".concat(raw, "/emoji/fengdou.webp"),
        '[墨镜]': "".concat(raw, "/emoji/mojing.webp"),
        '[撇嘴]': "".concat(raw, "/emoji/piezui.webp"),
        '[难过]': "".concat(raw, "/emoji/nanguo.webp"),
        '[抓狂]': "".concat(raw, "/emoji/zhuakuang.webp"),
        '[生气]': "".concat(raw, "/emoji/shengqi.webp"),
        '[爱心]': "".concat(raw, "/emoji/aixin.webp"),
        '[胜利]': "".concat(raw, "/emoji/shengli.webp"),
        '[抱拳]': "".concat(raw, "/emoji/baoquan.webp"),
        '[保佑]': "".concat(raw, "/emoji/baoyou.webp"),
        '[支持]': "".concat(raw, "/emoji/zhichi.webp")
    },
    {
        '[tv_doge]': "".concat(raw, "/emoji/tv/doge.webp"),
        '[tv_坏笑]': "".concat(raw, "/emoji/tv/huaixiao.webp"),
        '[tv_难过]': "".concat(raw, "/emoji/tv/nanguo.webp"),
        '[tv_生气]': "".concat(raw, "/emoji/tv/shengqi.webp"),
        '[tv_委屈]': "".concat(raw, "/emoji/tv/weiqu.webp"),
        '[tv_斜眼笑]': "".concat(raw, "/emoji/tv/xieyanxiao.webp"),
        '[tv_呆]': "".concat(raw, "/emoji/tv/dai.webp"),
        '[tv_发怒]': "".concat(raw, "/emoji/tv/fanu.webp"),
        '[tv_惊吓]': "".concat(raw, "/emoji/tv/jingxia.webp"),
        '[tv_呕吐]': "".concat(raw, "/emoji/tv/outu.webp"),
        '[tv_思考]': "".concat(raw, "/emoji/tv/sikao.webp"),
        '[tv_微笑]': "".concat(raw, "/emoji/tv/weixiao.webp"),
        '[tv_疑问]': "".concat(raw, "/emoji/tv/yiwen.webp"),
        '[tv_大哭]': "".concat(raw, "/emoji/tv/daku.webp"),
        '[tv_鼓掌]': "".concat(raw, "/emoji/tv/guzhang.webp"),
        '[tv_抠鼻]': "".concat(raw, "/emoji/tv/koubi.webp"),
        '[tv_亲亲]': "".concat(raw, "/emoji/tv/qinqin.webp"),
        '[tv_调皮]': "".concat(raw, "/emoji/tv/tiaopi.webp"),
        '[tv_笑哭]': "".concat(raw, "/emoji/tv/xiaoku.webp"),
        '[tv_晕]': "".concat(raw, "/emoji/tv/yun.webp"),
        '[tv_点赞]': "".concat(raw, "/emoji/tv/dianzan.webp"),
        '[tv_害羞]': "".concat(raw, "/emoji/tv/haixiu.webp"),
        '[tv_睡着]': "".concat(raw, "/emoji/tv/shuizhe.webp"),
        '[tv_色]': "".concat(raw, "/emoji/tv/se.webp"),
        '[tv_吐血]': "".concat(raw, "/emoji/tv/tuxue.webp"),
        '[tv_无奈]': "".concat(raw, "/emoji/tv/wunai.webp"),
        '[tv_再见]': "".concat(raw, "/emoji/tv/zaijian.webp"),
        '[tv_流汗]': "".concat(raw, "/emoji/tv/liuhan.webp"),
        '[tv_偷笑]': "".concat(raw, "/emoji/tv/touxiao.webp"),
        '[tv_抓狂]': "".concat(raw, "/emoji/tv/zhuakuang.webp"),
        '[tv_黑人问号]': "".concat(raw, "/emoji/tv/wenhao.webp"),
        '[tv_困]': "".concat(raw, "/emoji/tv/kun.webp"),
        '[tv_打脸]': "".concat(raw, "/emoji/tv/dalian.webp"),
        '[tv_闭嘴]': "".concat(raw, "/emoji/tv/bizui.webp"),
        '[tv_鄙视]': "".concat(raw, "/emoji/tv/bishi.webp"),
        '[tv_腼腆]': "".concat(raw, "/emoji/tv/miantian.webp"),
        '[tv_馋]': "".concat(raw, "/emoji/tv/chan.webp"),
        '[tv_可爱]': "".concat(raw, "/emoji/tv/keai.webp"),
        '[tv_发财]': "".concat(raw, "/emoji/tv/facai.webp"),
        '[tv_生病]': "".concat(raw, "/emoji/tv/shengbing.webp"),
        '[tv_流鼻血]': "".concat(raw, "/emoji/tv/liubixue.webp"),
        '[tv_尴尬]': "".concat(raw, "/emoji/tv/ganga.webp"),
        '[tv_大佬]': "".concat(raw, "/emoji/tv/dalao.webp"),
        '[tv_流泪]': "".concat(raw, "/emoji/tv/liulei.webp"),
        '[tv_冷漠]': "".concat(raw, "/emoji/tv/lenmo.webp"),
        '[tv_皱眉]': "".concat(raw, "/emoji/tv/zhoumei.webp"),
        '[tv_鬼脸]': "".concat(raw, "/emoji/tv/guilian.webp"),
        '[tv_调侃]': "".concat(raw, "/emoji/tv/tiaokan.webp"),
        '[tv_目瞪口呆]': "".concat(raw, "/emoji/tv/mudengkoudai.webp")
    }
];
//把emojiList数组中的每一个对象，放到emojiMap中方便取用
function allEmoji() {
    var emojiMap = {};
    emojiList.map(function (emojis) { return (emojiMap = __assign(__assign({}, emojiMap), emojis)); });
    return emojiMap;
}
exports["default"] = {
    faceList: faceList,
    emojiList: emojiList,
    allEmoji: allEmoji()
};
