#! /usr/bin/env python3

import glob
import sys
sys.path.insert(0, glob.glob('../../')[0])

from judge_server.judge_service import Judge

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from threading import Thread
from time import sleep
import os
import json
from judger import judge
import subprocess
# from queue import Queue

# queue = Queue()  # 消息队列

# 定义一个Task类
class Task:
    def __init__(self,user_id,problem_content_id,record_id,problem_content_language,problem_content_code,code_judge_type,debug_code_input):
        self.user_id = user_id
        self.problem_content_id = problem_content_id
        self.record_id = record_id
        self.problem_content_language = problem_content_language
        self.problem_content_code = problem_content_code
        self.code_judge_type = code_judge_type
        self.debug_code_input = debug_code_input

# def get_task_from_queue():
#     try:
#         return queue.get_nowait()
#     except:
#         return None
class JudgeMachine():
    def deal(self,task):
        if task.code_judge_type == 'debug':
            return self.deal_debug_code(task)
        elif task.code_judge_type == 'submit':
            return self.deal_submit_code(task)
        return ""
    def deal_debug_code(self,task):
        path = '../debug_record/'+str(task.record_id)+'/'
        os.makedirs(path)
        code = task.problem_content_code
        back={}
        # 将代码输出到main.cpp 并将debug_input写入1.in
        if code != None:
            f = open(path+'main.cpp','w')
            f.write(code)
            if task.debug_code_input == None:
                task.debug_code_input = " "
            f = open(path+'1.in','w')
            f.write(task.debug_code_input)
            f.close()
        if os.system("g++ "+path+"main.cpp"+" -O2 -Wall -lm --static -DONLINE_JUDGE -o "+path+"main"):
            result = subprocess.getoutput("g++ "+path+"main.cpp"+" -O2 -Wall -lm --static -DONLINE_JUDGE -o "+path+"main")
            back['status'] = 'Compile Error'
            back['result'] = result 
            return json.dumps(back)
        # result return value
        # WRONG_ANSWER (judger module will never return this value, it's used for awswer checker)
        # SUCCESS = 0 (this only means the process exited normally)
        # CPU_TIME_LIMIT_EXCEEDED = 1
        # REAL_TIME_LIMIT_EXCEEDED = 2
        # MEMORY_LIMIT_EXCEEDED = 3
        # RUNTIME_ERROR = 4
        # SYSTEM_ERROR = 5
        value = judge(task, {
            'exe_path':path+'main',
            'input_path':path+'1.in',
            'output_path':path+'1.out',
            'error_path':path+'1.out',
        })
        print(value)
        back['real_time'] = value.get('real_time')
        value = value.get('result')
        back['status'] = 'Finished'
       
        back['result'] = ''
        if value == 0: 
            f = open(path+'1.out','r')
            result = f.read()
            f.close()
            back['result'] = result
        elif value == 1 or value == 2:
            back['status'] = "Time Limit Exceeded"
        elif value == 3:
            back['status'] = "Memory Limit Exceeded"
        elif value == 4:
            back['status'] = "Runtime Error"
        return json.dumps(back)
    def deal_submit_code(self,task):
        path = '../submit_record/'+str(task.record_id)+'/'
        os.makedirs(path)
        code = task.problem_content_code
        back={}
        back['status']='Accepted'
        # # 将代码输出到main.cpp 
        if code != None:
            f = open(path+'main.cpp','w')
            f.write(code)
            f.close()
        if os.system("g++ "+path+"main.cpp"+" -o2 -o "+path+"main"):
            result = subprocess.getoutput("g++ "+path+"main.cpp"+" -o2 -o "+path+"main")
            back['status'] = 'Compile Error'
            return json.dumps(back)
        input_path='../test_case/' + str(task.problem_content_id) + '/in/'
        answer_path='../test_case/' + str(task.problem_content_id) + '/out/'
        # 测试代码
        # 获取 测试数据的数量
        sz = len(os.listdir(input_path))
        for i in range(1,sz + 1):
            value = judge(task, {
            'exe_path':path + 'main',
            'input_path':input_path + str(i) + '.in',
            'output_path':path + str(i) + '.out',
            'error_path':path + 'error.out',
            }).get('result')
            if value == 0: 
                user_f = open(path + str(i) + '.out','r')
                answer_f = open(answer_path + str(i) + '.out','r')
                user_output = user_f.read().rstrip()
                answer_output = answer_f.read().rstrip()
                user_f.close()
                answer_f.close()
                if user_output != answer_output:
                    back['status'] = 'Wrong Answer'
                    return json.dumps(back)
            elif value == 1 or value == 2:
                back['status'] = "Time Limit Exceeded"
                return json.dumps(back)
            elif value == 3:
                back['status'] = "Memory Limit Exceeded"
                return json.dumps(back)
            elif value == 4:
                back['status'] = "Runtime Error"
                return json.dumps(back)
        return json.dumps(back)
machine = JudgeMachine()
class JudgeHandler:
   def judge_code(self, info, other):
        info = json.loads(info)
        record_id = json.loads(other).get('record_id')
        task = Task(info.get('user_id'),
                    info.get('problem_content_id'),
                    record_id,
                    info.get('problem_content_language'),
                    info.get('problem_content_code'),
                    info.get('code_judge_type'),
                    info.get('debug_code_input'))
        return machine.deal(task)
        
        
# 消费者
# def worker():
#     judge_machine=JudgeMachine()
#     while True:
#         task = get_task_from_queue()
#         if task:
#             judge_machine.deal(task)
#         else:
#             sleep(1)


if __name__ == '__main__':
    handler = JudgeHandler()
    processor = Judge.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # 无限制多线程
    server = TServer.TThreadedServer(
        processor, transport, tfactory, pfactory)
    # # 开启消费者进程
    # Thread(target=worker, daemon=True).start()

    print('Starting the server...')
    server.serve()
    print('done.')
