# -*- encoding=utf8 -*-
__author__ = "chenry"

import logging
from airtest.core.api import *

logging.getLogger("airtest").setLevel(logging.INFO)
connect_device("Android:///192.168.1.5:5269?cap_method=javacap")
start_app("com.smallgiantgames.empires")
    
ST.OPDELAY = 0.2
period = 30

wait(Template(r"tpl1575164852793.png", record_pos=(-0.003, 0.839), resolution=(1080, 2248)),999)

touch(Template(r"tpl1575164852793.png", record_pos=(-0.003, 0.839), resolution=(1080, 2248)))

sum = 0
while True:
    # 失败重来
    if exists(Template(r"tpl1571990961780.png", record_pos=(-0.194, 0.751), resolution=(1080, 2248))):  
        touch(Template(r"tpl1571990961780.png", record_pos=(-0.194, 0.751), resolution=(1080, 2248)))

    # 战斗
    print ("The Stage you' ve pass: " , sum)
    if exists(Template(r"tpl1573022154510.png", record_pos=(0.218, 0.936), resolution=(1080, 2248))):
        touch(Template(r"tpl1573022154510.png", record_pos=(0.218, 0.936), resolution=(1080, 2248)))
        if not exists(Template(r"tpl1573630257647.png", record_pos=(0.313, -0.893), resolution=(1080, 2248))):
            touch(Template(r"tpl1573022154510.png", record_pos=(0.218, 0.936), resolution=(1080, 2248)))
        touch(Template(r"tpl1573630257647.png", record_pos=(0.313, -0.893), resolution=(1080, 2248)))
        sum = sum + 1
        sleep(period)
    wait(Template(r"tpl1571990961780.png", record_pos=(-0.194, 0.751), resolution=(1080, 2248)), 999)
        