import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import VueMarkdownEditor from '@kangc/v-md-editor';
// import VueMarkdownEditor from '@kangc/v-md-editor/lib/codemirror-editor';
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
import createKatexPlugin from '@kangc/v-md-editor/lib/plugins/katex/cdn';


VueMarkdownEditor.use(githubTheme, {
    Hljs: hljs,
});
VueMarkdownEditor.use(createKatexPlugin());



createApp(App)
    .use(store)
    .use(router)
    .use(VueMarkdownEditor)
    .use(ElementPlus)
    .use(UndrawUi)
    .use(vue3videoPlay)
    .mount('#app')