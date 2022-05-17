import sys
import json,time
from time import sleep
import pytest
from os.path import dirname, abspath
from config import RunConfig
from pywinauto import mouse
from pywinauto.keyboard import send_keys
from epeda_method import Gui_main

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.baidu_page import BaiduPage
from page.epsemicon_page import EpsemiconPage

def get_data(file_path):
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(tuple(i.values()))
    return data

@pytest.mark.parametrize("name, search_key",get_data(base_path + "/test_dir/data/data_file.json"))
def atest_baidu_search(name, search_key, browser, base_url):
    page = BaiduPage(browser)
    page.open(base_url)
    page.search_input = search_key
    page.search_button.click()
    sleep(2)
    assert browser.title == search_key + "_百度搜索"


def atest_index(browser, base_url):
    pass
    page=EpsemiconPage(browser)
    # page.get(base_url)
    page.open(base_url)
    sleep(2)

    #标题="epsemicon"
    assert browser.title == "epsemicon"
    #主菜单第1个="首页"
    assert page.index_main_menu_result_1.text=="首页"
    # 主菜单第2个="动态资讯"
    assert page.index_main_menu_result_2.text == "动态资讯"
    # 主菜单第3个="产品与解决方案"
    assert page.index_main_menu_result_3.text == "产品与解决方案"
    # 主菜单第4个="我们的优势"
    assert page.index_main_menu_result_4.text == "我们的优势"
    # 主菜单第5个="下载专区"
    assert page.index_main_menu_result_5.text == "下载专区"
    # 主菜单第6个="诚邀加盟商/代理商"
    assert page.index_main_menu_result_6.text == "诚邀加盟商/代理商"
    # 主菜单第7个="加入我们"
    assert page.index_main_menu_result_7.text == "加入我们"

def atest_one():
    app=RunConfig.epeda_driver
    win=app.get_win('Dialog')
    # print(win.print_control_identifiers())
    time.sleep(5)

    # mouse.double_click(coords=Gui_main().get_close_coor())
    # win = app.get_top_win()
    # # print(win.print_control_identifiers())
    #
    # cc=Gui_main.get_save_coor(win)
    # print("*"*30,cc)
    # mouse.double_click(coords=Gui_main.get_save_coor(win))
    assert 1==1

def test_two():
    app=RunConfig.epeda_driver
    win=app.get_win('Dialog')
    # print(win.print_control_identifiers())
    # time.sleep(12)
    cc=Gui_main.get_GroupBox_coor(win)
    print("*"*30,cc)

    cc2=Gui_main.get_GroupBox_title(win)
    print("*"*30,cc2)


    assert 1==1


