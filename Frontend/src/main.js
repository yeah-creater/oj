import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import VueMarkdownEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import ElementPlus from 'element-plus'
import hljs from 'highlight.js';
import 'element-plus/dist/index.css'
import UndrawUi from 'undraw-ui'
import 'undraw-ui/dist/style.css'
import vue3videoPlay from 'vue3-video-play' // 引入组件
import 'vue3-video-play/dist/style.css' // 引入css
// import BaiduCalendar from "vue-baidu-calendar"
VueMarkdownEditor.use(githubTheme, {
    Hljs: hljs,
});


createApp(App).use(store)
    .use(router)
    .use(VueMarkdownEditor)
    .use(ElementPlus)
    .use(UndrawUi)
    .use(vue3videoPlay)
    // .use(BaiduCalendar)
    .mount('#app')