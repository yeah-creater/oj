import _judger
import os

def judge(task,path):
    ret = _judger.run(max_cpu_time=1000,
                    max_real_time=1000,
                    max_memory=64 * 1024 * 1024,
                    max_process_number=200,
                    max_output_size=128*1024,
                    max_stack=32 * 1024 * 1024,
                    # five args above can be _judger.UNLIMITED
                    exe_path=path['exe_path'],
                    input_path=path['input_path'],
                    output_path=path['output_path'],
                    error_path=path['output_path'],
                    args=[],
                    # can be empty list
                    env=[],
                    log_path="../log/judger.log",
                    # can be None
                    seccomp_rule_name = 'c_cpp',
                    uid=0,
                    gid=0)
    return ret

