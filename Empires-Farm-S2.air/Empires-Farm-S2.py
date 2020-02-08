# -*- encoding=utf8 -*-
__author__ = "chenry"

from airtest.core.api import *

auto_setup(__file__)# -*- encoding=utf8 -*-
__author__ = "chenry"

from airtest.core.api import *
ST.OPDELAY = 2

castle_icon=Template(r"tpl1572183887459.png", record_pos=(-0.021, 0.198), resolution=(1080, 2248))
food_icon=Template(r"tpl1572183982836.png", record_pos=(-0.229, 0.016), resolution=(1080, 2248))
iron_icon=Template(r"tpl1572184001438.png", record_pos=(-0.359, 0.246), resolution=(1080, 2248))
hero_icon=Template(r"tpl1572184009699.png", record_pos=(0.082, 0.57), resolution=(1080, 2248))
ok_icon=Template(r"tpl1572184019820.png", record_pos=(-0.002, 0.708), resolution=(1080, 2248))
claim_icon=Template(r"tpl1572184039263.png", record_pos=(0.001, 0.59), resolution=(1080, 2248))
currency_icon=Template(r"tpl1572184056046.png", record_pos=(-0.088, -0.17), resolution=(1080, 2248))

map_icon = Template(r"tpl1572005107575.png", record_pos=(-0.411, 0.869), resolution=(1080, 2248))
province_icon = Template(r"tpl1572184716756.png", record_pos=(-0.083, -0.243), resolution=(1080, 2248))
stage_icon=Template(r"tpl1573563815115.png", record_pos=(0.076, 0.491), resolution=(1080, 2248))
next_icon=Template(r"tpl1571997796779.png", record_pos=(0.018, 0.841), resolution=(1080, 2248))
fight_icon=Template(r"tpl1573022154510.png", record_pos=(0.218, 0.936), resolution=(1080, 2248))
auto_icon=Template(r"tpl1573630257647.png", record_pos=(0.313, -0.893), resolution=(1080, 2248))
replay_icon=Template(r"tpl1571990961780.png", record_pos=(-0.194, 0.751), resolution=(1080, 2248))

def try_touch(s):
    if exists(s):
        touch(s)
        return True
    return False

def must_touch(s):
    assert_exists(s)
    touch(s)

    
def collect_resources():
    if exists(castle_icon):
        swipe(castle_icon, vector=[0.3895, -0.243])
    while(try_touch(food_icon)):
        continue
    while(try_touch(iron_icon)):
        continue
    while(try_touch(hero_icon)):
        must_touch(ok_icon)
        must_touch(claim_icon)
    
def enter_chapter():
    if exists(Template(r"tpl1572184308723.png", record_pos=(-0.415, 0.595), resolution=(1080, 2248))):  
        try_touch(map_icon)
#     try_touch(season_icon)
    try_touch(province_icon)
    
def enter_dungeon():
    try_touch(stage_icon)    
    try_touch(next_icon)

def fight():
    try_touch(fight_icon)
    sleep(5)
    must_touch(auto_icon)
    sleep(120)
    i = 3
    while(not exists(replay_icon) and i > 0):
        sleep(30)
        i -= 1
    must_touch(replay_icon)
    
    
# 收集资源
# collect_resources()
# 进入章节
# enter_chapter()
# 进入关卡
enter_dungeon()
# 循环战斗
for i in range(10):
    fight()