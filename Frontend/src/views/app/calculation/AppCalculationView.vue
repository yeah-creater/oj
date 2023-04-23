<template>
    <ContentBase>
        <div class="row justify-content-md-center" >
            <div class="col-lg-6 col-md-10 col-sm-12">
                <table align="center">
                <caption><b>🐷不支持负数和小数运算🐷</b> </caption>
                <tr>
                    <td colspan="4"><input type="text" id="result" value=""
                            style="width: 410px;height: 100px;background-color: white;" align-text="center" /></td>
                </tr>
                <tr>
                    <td><input type="button" id="btn" value="+" class="color" @click="ope('+')" /></td>
                    <td><input type="button" id="btn" value="-" class="color" @click="ope('-')" /></td>
                    <td><input type="button" id="btn" value="x" class="color" @click="ope('*')" /></td>
                    <td><input type="button" id="btn" value="/" class="color" @click="ope('/')" /></td>
                </tr>
                <tr>
                    <td><input type="button" id="btn" value="9️" @click="ope('9')" /></td>
                    <td><input type="button" id="btn" value="8️" @click="ope('8')" /></td>
                    <td><input type="button" id="btn" value="7" @click="ope('7')" /></td>
                    <td><input type="button" id="btn" value="🔙" @click="ope('delete')" /></td>
                </tr>
                <tr>
                    <td><input type="button" id="btn" value="6️" @click="ope('6')" /></td>
                    <td><input type="button" id="btn" value="5️" @click="ope('5')" /></td>
                    <td><input type="button" id="btn" value="4️" @click="ope('4')" /></td>
                    <td><input type="button" id="btn" value="🔚" @click="ope('clear')" /></td>
                </tr>
                <tr>
                    <td><input type="button" id="btn" value="3️" @click="ope('3')" /></td>
                    <td><input type="button" id="btn" value="2️" @click="ope('2')" /></td>
                    <td><input type="button" id="btn" value="1️" @click="ope('1')" /></td>
                    <td rowspan="4"><input type="button" id="btn" value="=" @click="calc"
                            style="width: 100px;height: 120px; background-color: white;" /></td>
                </tr>
                <tr>
                    <td><input type="button" id="btn" value="(" class="color" @click="ope('(')" /></td>
                    <td><input type="button" id="btn" value="0️" onclick="ope('0')" /></td>
                    <td><input type="button" id="btn" value=")" class="color" @click="ope(')')" /></td>
                </tr>
            </table>
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '@/components/ContentBase';

export default {
    name: 'AppCalculationView',
    components: {
        ContentBase,
    },
    setup() { 
        let pr = [];
        pr['+'] = 1;
        pr['-'] = 1;
        pr['*'] = 2;
        pr['/'] = 2;

        const ope=(x)=> {
            var ele = document.getElementById('result');
            if (x == 'delete')
                ele.value = ele.value.substring(0, ele.value.length - 1);
            else if (x == 'clear')
                ele.value = "";
            else
                ele.value = ele.value + x;
        }

        const  isdigit=(x)=> {
            return x >= '0' && x <= '9';
        }

        const cal = (num, op)=> {
            var b = num[num.length - 1];
            num.pop();
            var a = num[num.length - 1];
            num.pop();
            var c = op[op.length - 1];
            op.pop();
            if (c == '+') num.push(a + b);
            if (c == '-') num.push(a - b);
            if (c == '*') num.push(a * b);
            if (c == '/') num.push(a / b);
        }


        const calc=()=> {
            let num = [];
            let op = [];
            var ele = document.getElementById('result');
            var text = ele.value;
            text = text.replace(/ +/g, '');
            for (var i = 0; i < text.length; i++) {
                if (isdigit(text[i])) {
                    var j = i;
                    var x = 0;
                    while (j < text.length && isdigit(text[j])) {
                        x = x * 10 + (text[j] - '0');
                        j++;
                    }
                    num.push(x);
                    i = j - 1;
                } else if (text[i] == '(')
                    op.push('(');
                else if (text[i] == ')') {
                    while (op[op.length - 1] != '(' && op.length) cal(num, op);
                    op.pop();
                } else {
                    while (op.length && op[op.length - 1] != '(' && pr[op[op.length - 1]] >= pr[text[i]])
                        cal(num, op);
                    op.push(text[i]);
                }
            }
            while (op.length) cal(num, op);
            ele.value = num[num.length - 1];
            document.getElementById('result').value = text + '=' + ele.value + "\n";
            num.pop();
        }
        return {
            pr,
            ope,
            isdigit,
            cal,
            calc,
        }
    }

}

</script>
<style scoped>

 table {
     width: 400px;
     height: 400px;
     border-color: white;
 }

 #btn {
     width: 100px;
     height: 60px;
     font-size: 35px;
 }

 #result {
     font-size: 25px;
 }

 .color {
     background-color: white;
 }
</style>