# -*- encoding=utf8 -*-
__author__ = "chenry"

from airtest.core.api import *
ST.OPDELAY = 2

stage_icon=Template(r"tpl1573638593682.png", record_pos=(0.006, -0.21), resolution=(1080, 2248))
fight_icon=Template(r"tpl1573022154510.png", record_pos=(0.218, 0.936), resolution=(1080, 2248))
auto_icon=Template(r"tpl1573630257647.png", record_pos=(0.313, -0.893), resolution=(1080, 2248))
next_icon=Template(r"tpl1573639275282.png", record_pos=(0.192, 0.752), resolution=(1080, 2248))

def try_touch(s):
    if exists(s):
        touch(s)
        return True
    return False

def must_touch(s):
    assert_exists(s)
    touch(s)

def fight():
    try_touch(stage_icon)
    must_touch(fight_icon)
    must_touch(auto_icon)
    sleep(60)
    while(not exists(next_icon)):
        sleep(5)
    must_touch(next_icon)
    

# 循环战斗
for i in range(10):
    fight()