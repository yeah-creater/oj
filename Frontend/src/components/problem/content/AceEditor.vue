<template>
  <div class="code-editor">
    <div class="code-tools">
      <form>
        <div class="editor-header">
          <label>语言:</label>
          <select
            v-model="language"
            class="form-select code-editor-option"
            @change="changeLanguage"
          >
            <option value="C++" selected>C++</option>
            <!-- <option value="Python3">Python3</option> -->
            <option value="C">C</option>
            <!-- <option value="Java">Java</option>
            <option value="Go">Go</option> -->
          </select>
          <label>主题:</label>
          <select
            v-model="theme"
            class="form-select code-editor-option"
            @change="changeTheme"
          >
            <option value="ace/theme/textmate">textmate</option>
            <option value="ace/theme/monokai">monokai</option>
            <option value="ace/theme/terminal">terminal</option>
          </select>
          <label>编辑类型:</label>
          <select
            v-model="keyboard"
            class="form-select code-editor-option"
            @change="changeKeyboard"
          >
            <option value="ace/keyboard/vscode" selected>VScode</option>
            <option value="ace/keyboard/vim">Vim</option>
            <option value="ace/keyboard/emacs">Emacs</option>
          </select>
          <label>字体大小:</label>
          <select
            v-model="fontSize"
            class="form-select code-editor-option"
            @change="changeFontSize"
          >
            <option value="16px">16</option>
            <option value="18px">18</option>
            <option value="20px" selected>20</option>
            <option value="22px">22</option>
            <option value="24px">24</option>
          </select>
        </div>
      </form>
    </div>
    <VAceEditor
      id="editor"
      @init="editorInit"
      lang="c_cpp"
      theme="textmate"
      style="height: 300px"
    />

    <div>
      <button
        ref="submit_code"
        @click="submitCode"
        class="btn btn-outline-success"
        style="float: right; border-radius: 20px; margin: 20px 0 0 20px"
      >
        提交代码
      </button>
      <button
        ref="debug_code"
        @click="debugCode"
        class="btn btn-light"
        style="float: right; border-radius: 20px; margin: 20px 0 0 0"
      >
        调试代码
      </button>
    </div>
    <div
      id="judge-code-status-block"
      class="panel panel-default"
      style="
        margin-top: 75px;
        border: 1px solid;
        border-color: #ddd;
        border-radius: 5px;
        padding: 10px;
      "
    >
      <div class="panel-heading">
        <span class="judge-code-status-label"
          >代码运行状态：<span
            :style="{ color: judge_code_status_label_color }"
            >{{ code_status_value }}</span
          ></span
        >
        <div
          v-show="judge_code_status_loading"
          class="spinner-border"
          role="status"
        >
          <span class="visually-hidden">Loading...</span>
        </div>
        <span
          @click="
            show_judge_code_result == true
              ? (show_judge_code_result = false)
              : (show_judge_code_result = true)
          "
          style="cursor: pointer; float: right"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-caret-down-fill"
            viewBox="0 0 16 16"
          >
            <path
              d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"
            ></path>
          </svg>
        </span>
      </div>
      <div
        v-show="show_judge_code_result"
        class="panel-body"
        style="padding: 25px"
      >
        <label
          for="debug-code-stdin"
          style="font-weight: normal; font-size: 15px"
          >输入</label
        >
        <textarea
          v-model="debug_code_stdin"
          id="debug-code-stdin"
          class="form-control autofit"
          maxlength="2000"
          rows="1"
          style="
            background-color: rgb(248, 248, 248);
            border-radius: 5px;
            resize: none;
            font-family: monospace;
            height: 200px;
            min-height: 20px;
          "
        ></textarea>
        <br />
        <span style="font-weight: normal; font-size: 15px">输出</span>
        <pre
          ref="debug_code_stdout"
          id="deubg-code-stdout"
          style="
            background-color: #f8f8f8;
            border-radius: 5px;
            margin-top: 5px;
            min-height: 40px;
            padding: 8px;
          "
          class="hljs"
        ></pre>
        <span
          ref="debug_code_real_time"
          style="font-weight: normal; font-size: 15px"
        ></span>
      </div>
    </div>
  </div>
  <div class="mobile-tips"><h3>请使用PC端打开编辑代码</h3></div>
</template>
<script>
import { VAceEditor } from "vue3-ace-editor";
import ace from "ace-builds";
import "ace-builds/src-noconflict/ext-language_tools";
import { ref } from "vue";

export default {
  name: "AceEditor",
  components: {
    VAceEditor,
  },

  setup(props, context) {
    ace.config.set(
      "basePath",
      "https://cdn.jsdelivr.net/npm/ace-builds@" +
        require("ace-builds").version +
        "/src-noconflict/"
    );
    let theme = ref("ace/theme/textmate");
    let language = ref("C++");
    let keyboard = ref("ace/keyboard/vscode");
    let fontSize = ref("20px");
    let editor = null,
      debug_code = ref(),
      submit_code = ref(),
      debug_code_stdin = ref(),
      debug_code_stdout = ref(),
      code_status_value = ref("");
    let judge_code_status_loading = ref(false),
      show_judge_code_result = ref(false);
    let judge_code_status_label_color = ref("black"),
      debug_code_real_time = ref("");
    const editorInit = () => {
      //初始化
      editor = ace.edit("editor");
      editor.setFontSize(fontSize.value);
      editor.renderer.setOptions({
        minLines: 13,
        maxLines: 10000,
      });
      editor.setOptions({
        enableSnippets: true,
        enableLiveAutocompletion: true,
      });
    };
    const debugCode = () => {
      show_judge_code_result.value = true;
      code_status_value.value = "";
      debug_code_stdout.value.innerHTML = "";
      debug_code_real_time.value.innerHTML = "";
      debug_code.value.disabled = true;
      judge_code_status_loading.value = true;
      context.emit(
        "judgeCode",
        editor.getValue(),
        language.value,
        "debug",
        debug_code_stdin.value
      );
    };
    const submitCode = () => {
      show_judge_code_result.value = false;
      code_status_value.value = "";
      debug_code_stdout.value.innerHTML = "";
      debug_code_real_time.value.innerHTML = "";
      submit_code.value.disabled = true;
      judge_code_status_loading.value = true;
      context.emit(
        "judgeCode",
        editor.getValue(),
        language.value,
        "submit",
        ""
      );
    };
    const changeTheme = () => {
      editor.setTheme(theme.value);
    };
    const changeLanguage = () => {
      let dict = {
        cpp: "c_cpp",
        c: "c_cpp",
        java: "java",
        py: "python",
        go: "golang",
      };
      editor.session.setMode("ace/mode/" + dict[language.value]);
    };
    const changeKeyboard = () => {
      editor.setKeyboardHandler(keyboard.value);
    };
    const changeFontSize = () => {
      editor.setFontSize(fontSize.value);
    };
    const changeSubmitOutput = (status) => {
      code_status_value.value = status;
      judge_code_status_loading.value = false;
      if (status === "Accepted")
        judge_code_status_label_color.value = "rgb(68, 157, 68)";
      else judge_code_status_label_color.value = "rgb(208, 84, 81)";
      setTimeout(function () {
        submit_code.value.disabled = false;
      }, 1000);
    };
    const changeDebugOutput = (status, output, real_time) => {
      code_status_value.value = status;
      debug_code_stdout.value.innerHTML = output;
      judge_code_status_loading.value = false;

      if (status === "Finished") {
        debug_code_real_time.value.innerHTML = "运行时间: " + real_time + "ms";
        judge_code_status_label_color.value = "rgb(68, 157, 68)";
      } else judge_code_status_label_color.value = "rgb(208, 84, 81)";
      setTimeout(function () {
        debug_code.value.disabled = false;
      }, 1000);
    };
    return {
      editorInit,
      language,
      theme,
      keyboard,
      fontSize,
      changeTheme,
      changeLanguage,
      changeKeyboard,
      changeFontSize,
      changeDebugOutput,
      changeSubmitOutput,
      submitCode,
      debugCode,
      debug_code,
      submit_code,
      debug_code_stdin,
      debug_code_stdout,
      debug_code_real_time,
      code_status_value,
      judge_code_status_loading,
      show_judge_code_result,
      judge_code_status_label_color,
    };
  },
};
</script>

<style scoped>
label {
  color: gray;
}
.code-tools {
  height: 60px;
  width: 100%;
  background: #f8f9fa;
  border: 1px solid #c2c7d0;
  margin-bottom: 0;
  text-align: center;
}
.code-editor-option {
  width: 15%;
  border-radius: 4px;
  margin: 10px;
  display: inline-block;
}
@media screen and (max-width: 768px) {
  .code-editor {
    display: none;
  }
  .mobile-tips {
    display: inline;
  }
}
@media screen and (min-width: 768px) {
  .mobile-tips {
    display: none;
  }
}
</style>
