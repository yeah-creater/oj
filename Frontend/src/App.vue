<template>
  <div>
    <NavBar />
    <router-view :key="$route.fullPath" />
  </div>
</template>
<script>
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";
import NavBar from "./components/NavBar.vue";
import { useStore } from "vuex";
export default {
  name: "APP",
  components: {
    NavBar,
  },
  setup() {
    const store = useStore();
    store.dispatch("getInfo");
  },
};
</script>
<style>
body {
  background-image: url("https://cdn.acwing.com/static/web/img/background.png");
}
.card {
  background: #fafafa;
}

.codehilite {
  background: rgba(0, 10, 32, 0.05);
  border: 1px solid #f0f0f0;
  border-radius: 5px;
  margin-top: 10px;
}
.codehilite .hll {
  background-color: #ffffcc;
}
.codehilite .c {
  color: #408080;
  font-style: italic;
}

/* Comment */
.codehilite .err {
  border: 1px solid #ff0000;
}

/* Error */
.codehilite .k {
  color: #008000;
  font-weight: bold;
}

/* Keyword */
.codehilite .o {
  color: #666666;
}

/* Operator */
.codehilite .ch {
  color: #408080;
  font-style: italic;
}

/* Comment.Hashbang */
.codehilite .cm {
  color: #408080;
  font-style: italic;
}

/* Comment.Multiline */
.codehilite .cp {
  color: #bc7a00;
}

/* Comment.Preproc */
.codehilite .cpf {
  color: #408080;
  font-style: italic;
}

/* Comment.PreprocFile */
.codehilite .c1 {
  color: #408080;
  font-style: italic;
}

/* Comment.Single */
.codehilite .cs {
  color: #408080;
  font-style: italic;
}

/* Comment.Special */
.codehilite .gd {
  color: #a00000;
}

/* Generic.Deleted */
.codehilite .ge {
  font-style: italic;
}

/* Generic.Emph */
.codehilite .gr {
  color: #ff0000;
}

/* Generic.Error */
.codehilite .gh {
  color: #000080;
  font-weight: bold;
}

/* Generic.Heading */
.codehilite .gi {
  color: #00a000;
}

/* Generic.Inserted */
.codehilite .go {
  color: #888888;
}

/* Generic.Output */
.codehilite .gp {
  color: #000080;
  font-weight: bold;
}

/* Generic.Prompt */
.codehilite .gs {
  font-weight: bold;
}

/* Generic.Strong */
.codehilite .gu {
  color: #800080;
  font-weight: bold;
}

/* Generic.Subheading */
.codehilite .gt {
  color: #0044dd;
}

/* Generic.Traceback */
.codehilite .kc {
  color: #008000;
  font-weight: bold;
}

/* Keyword.Constant */
.codehilite .kd {
  color: #008000;
  font-weight: bold;
}

/* Keyword.Declaration */
.codehilite .kn {
  color: #008000;
  font-weight: bold;
}

/* Keyword.Namespace */
.codehilite .kp {
  color: #008000;
}

/* Keyword.Pseudo */
.codehilite .kr {
  color: #008000;
  font-weight: bold;
}

/* Keyword.Reserved */
.codehilite .kt {
  color: #b00040;
}

/* Keyword.Type */
.codehilite .m {
  color: #666666;
}

/* Literal.Number */
.codehilite .s {
  color: #ba2121;
}

/* Literal.String */
.codehilite .na {
  color: #7d9029;
}

/* Name.Attribute */
.codehilite .nb {
  color: #008000;
}

/* Name.Builtin */
.codehilite .nc {
  color: #0000ff;
  font-weight: bold;
}

/* Name.Class */
.codehilite .no {
  color: #880000;
}

/* Name.Constant */
.codehilite .nd {
  color: #aa22ff;
}

/* Name.Decorator */
.codehilite .ni {
  color: #999999;
  font-weight: bold;
}

/* Name.Entity */
.codehilite .ne {
  color: #d2413a;
  font-weight: bold;
}

/* Name.Exception */
.codehilite .nf {
  color: #0000ff;
}

/* Name.Function */
.codehilite .nl {
  color: #a0a000;
}

/* Name.Label */
.codehilite .nn {
  color: #0000ff;
  font-weight: bold;
}

/* Name.Namespace */
.codehilite .nt {
  color: #008000;
  font-weight: bold;
}

/* Name.Tag */
.codehilite .nv {
  color: #19177c;
}

/* Name.Variable */
.codehilite .ow {
  color: #aa22ff;
  font-weight: bold;
}

/* Operator.Word */
.codehilite .w {
  color: #bbbbbb;
}

/* Text.Whitespace */
.codehilite .mb {
  color: #666666;
}

/* Literal.Number.Bin */
.codehilite .mf {
  color: #666666;
}

/* Literal.Number.Float */
.codehilite .mh {
  color: #666666;
}

/* Literal.Number.Hex */
.codehilite .mi {
  color: #666666;
}

/* Literal.Number.Integer */
.codehilite .mo {
  color: #666666;
}

/* Literal.Number.Oct */
.codehilite .sa {
  color: #ba2121;
}

/* Literal.String.Affix */
.codehilite .sb {
  color: #ba2121;
}

/* Literal.String.Backtick */
.codehilite .sc {
  color: #ba2121;
}

/* Literal.String.Char */
.codehilite .dl {
  color: #ba2121;
}

/* Literal.String.Delimiter */
.codehilite .sd {
  color: #ba2121;
  font-style: italic;
}

/* Literal.String.Doc */
.codehilite .s2 {
  color: #ba2121;
}

/* Literal.String.Double */
.codehilite .se {
  color: #bb6622;
  font-weight: bold;
}

/* Literal.String.Escape */
.codehilite .sh {
  color: #ba2121;
}

/* Literal.String.Heredoc */
.codehilite .si {
  color: #bb6688;
  font-weight: bold;
}

/* Literal.String.Interpol */
.codehilite .sx {
  color: #008000;
}

/* Literal.String.Other */
.codehilite .sr {
  color: #bb6688;
}

/* Literal.String.Regex */
.codehilite .s1 {
  color: #ba2121;
}

/* Literal.String.Single */
.codehilite .ss {
  color: #19177c;
}

/* Literal.String.Symbol */
.codehilite .bp {
  color: #008000;
}

/* Name.Builtin.Pseudo */
.codehilite .fm {
  color: #0000ff;
}

/* Name.Function.Magic */
.codehilite .vc {
  color: #19177c;
}

/* Name.Variable.Class */
.codehilite .vg {
  color: #19177c;
}

/* Name.Variable.Global */
.codehilite .vi {
  color: #19177c;
}

/* Name.Variable.Instance */
.codehilite .vm {
  color: #19177c;
}

/* Name.Variable.Magic */
.codehilite .il {
  color: #666666;
}
code {
  margin: 0 2px;
  padding: 0 5px;
  border: 1px solid #eaeaea;
  background-color: #f8f8f8;
  border-radius: 3px;
}

pre {
  margin-bottom: 0;
  padding: 0.3em 0.5em;
  border: 1px #ddd solid;
  border-left: 3px solid #67c23a;
  background-color: #f8f8f8;
  border-radius: 3px;
  position: relative;
}
pre .btn-pre-copy {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  -khtml-user-select: none;
  user-select: none;
  position: absolute;
  top: 10px;
  right: 12px;
  font-size: 12px;
  line-height: 1;
  cursor: pointer;
  color: hsla(0, 0%, 54.9%, 0.8);
  transition: color 0.1s;
}
.btn-pre-copy:hover {
  color: #67c23a;
}
blockquote {
  margin: 0 0 20px;
  padding: 12px 15px;
  border-left: 3px solid #49b1f5;
  background-color: rgba(73, 177, 245, 0.1);
  color: #6a737d;
}
blockquote > :last-child {
  margin-bottom: 0 !important;
}
li::marker {
  color: #ff8886;
  font-weight: 600;
  font-size: 1.05em;
}
.article img {
  display: block;
  margin: 0 auto 20px;
  max-width: 100%;
  transition: filter 375ms ease-in 0.2s;
}
.article table thead,
.article table tr {
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: #a8bfde;
}
.article table {
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: #a8bfde;
  margin: auto;
  min-width: 80%;
}

/* Padding and font style */
.article table td,
.article table th {
  padding: 5px 10px;
  font-size: 12px;
  font-family: Verdana;
  color: #5b7da3;
}

/* Alternating background colors */
.article table tr:nth-child(even) {
  background: #d3dfed;
}
.article table tr:nth-child(odd) {
  background: #fff;
}
</style>
