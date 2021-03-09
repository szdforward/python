#!/usr/bin/env python
import sys
import subprocess
def monitor_process(key_word, cmd):
    p1 = subprocess.Popen(['ps','-ef'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', key_word],stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(['grep','-v', 'grep'], stdin=p2.stdout, stdout=subprocess.PIPE)
    lines = p3.stdout.readlines()
    if len(lines) > 0:
       return
    sys.stderr.write('process[%s] is lost, run [%s]\n' % (key_word,cmd))
    subprocess.call(cmd, shell=True)

# szd分析
# 这个脚本是分析subprocess的使用的，主要的目的是判断test.sh这个任务是否还在运行，如果不在运行了，就启动他，如果还在运行中，就返回空
monitor_process("test.sh","/home/hadoop/test.sh")