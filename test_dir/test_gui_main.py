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

def atest_group_box():
    app=RunConfig.epeda_driver
    win=app.get_win('Dialog')
    assert Gui_main.get_GroupBox_title(win) == ['工具', '数据', '向导', '制造端']

def test_top_module():
    app=RunConfig.epeda_driver
    win=app.get_win('Dialog')
    # print(top_module_drzl.print_control_identifiers())
    # 导入资料
    assert Gui_main.get_top_module(win['Custom9']) == ['导入资料', '支持gerber、odb++、ipc2581、eps等多种格式资料导入']
    # EP-CAM
    assert Gui_main.get_top_module(win['Custom10']) == ['EP-CAM', '快速进入EP-CAM基础软件']
    # 前处理
    assert Gui_main.get_top_module(win['Custom11']) == ['前处理', '图形资料报价和优化前的资料处理模块']
    # CAM自动化
    assert Gui_main.get_top_module(win['Custom12']) == ['CAM自动化', '实现优化功能自动化，包含一键优化和分步骤优化模块']
    # 资料分析 DFM
    assert Gui_main.get_top_module(win['Custom13']) == ['资料分析 DFM', '多层面解析资料，完整给出PCB相关参数或cam服务报价结果模块']
    # 自动移孔功能
    assert Gui_main.get_top_module(win['Custom14']) == ['自动移孔功能', 'ep-cam附带全部高级功能，可实现自动移孔，保证间距模块']

    win.child_window(title="导入资料").click_input()
    win.child_window(title="EP-CAM").click_input()
    win.child_window(title="前处理").click_input()
    win.child_window(title="CAM自动化").click_input()
    win.child_window(title="资料分析 DFM").click_input()
    win.child_window(title="自动移孔功能").click_input()


def atest_input_pre_check():
    app=RunConfig.epeda_driver
    win=app.get_win('Dialog')
    # print(top_module_drzl.print_control_identifiers())
    # win.child_window(title="导入与预审").click_input()

    # win.child_window(title="导入资料").click_input()
    # win.child_window(title="EP-CAM").click_input()
    # win.child_window(title="前处理").click_input()
    # win.child_window(title="CAM自动化").click_input()
    # win.child_window(title="资料分析 DFM").click_input()
    # win.child_window(title="自动移孔功能").click_input()
