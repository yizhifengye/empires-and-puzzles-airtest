# -*- encoding=utf8 -*-
__author__ = "chenry"

from airtest.core.api import *
ST.OPDELAY = 2
stage_icon=Template(r"tpl1572350844594.png", record_pos=(-0.312, -0.116), resolution=(1080, 2248))
# stage_2_icon=Template(r"tpl1575626585502.png", record_pos=(-0.023, 0.119), resolution=(1080, 2248))

fight_icon=Template(r"tpl1571990525813.png", record_pos=(0.265, 0.944), resolution=(1080, 2248))
auto_icon=Template(r"tpl1572836301720.png", record_pos=(0.32, -0.893), resolution=(1080, 2248))
next_icon=Template(r"tpl1571997796779.png", record_pos=(0.018, 0.841), resolution=(1080, 2248))

def try_touch(s):
    if exists(s):
        touch(s)
        return True
    return False
        
def must_touch(s):
    assert_exists(s)
    touch(s)

def enter_dungeon():
    try_touch(stage_icon)

def fight():
    must_touch(fight_icon)
    sleep(5)
    must_touch(auto_icon)
    sleep(100)
    while(not exists(next_icon)):
        sleep(100)
    must_touch(next_icon)
    
    
# 进入章节
# enter_chapter()
# 循环战斗
for i in range(3):
    enter_dungeon()
    fight()
    sleep(2)