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

@pytest.mark.input
class TestInput:
    def test_input_gerber274d(self):
        app=RunConfig.epeda_driver
        win=app.get_win('Dialog')
        # print(top_module_drzl.print_control_identifiers())
        win.child_window(title="导入与预审").click_input()
        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点
        # print(win.print_control_identifiers())

        # 导入与预审下的导入资料
        win['Custom17'].click_input()
        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点
        # print(win['Custom17'].print_control_identifiers())
        assert Gui_main.get_top_module(win['Custom17']) == ['导入资料', '支持gerber、odb++、ipc2581、eps等多种格式资料导入']
