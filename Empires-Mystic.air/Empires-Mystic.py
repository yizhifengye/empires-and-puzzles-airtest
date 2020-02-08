# -*- encoding=utf8 -*-
__author__ = "chenry"

from airtest.core.api import *

auto_setup(__file__)

ST.OPDELAY = 0.2
period = 30

start_app("com.smallgiantgames.empires")

wait(Template(r"tpl1581100157818.png", record_pos=(0.044, -0.156), resolution=(1080, 2248)),999)

touch(Template(r"tpl1581100157818.png", record_pos=(0.044, -0.156), resolution=(1080, 2248)))

sum = 0
if True:
    # 失败重来
    if exists(Template(r"tpl1581100188273.png", record_pos=(-0.007, 0.343), resolution=(1080, 2248))):  
        touch(Template(r"tpl1581100188273.png", record_pos=(-0.007, 0.343), resolution=(1080, 2248)))
    sleep(30)
    keyevent("KEYCODE_BACK") 