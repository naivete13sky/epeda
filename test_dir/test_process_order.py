import sys
import json,time
from time import sleep
import pytest
from os.path import dirname, abspath
from config import RunConfig
from pywinauto import mouse,Desktop
from pywinauto.keyboard import send_keys
from epeda_method import Gui_main

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.baidu_page import BaiduPage
from page.epsemicon_page import EpsemiconPage

@pytest.mark.process_order
class TestProcessOrder:
    def test_one(self):
        app=RunConfig.epeda_driver
        win=app.get_win('Dialog')
        # print(top_module_drzl.print_control_identifiers())
        win.child_window(title="抢单").click_input()
        # app=Desktop(backend="win32")
        # win=app.get_win('标准流程创建订单')
        app = Desktop(backend='uia')
        buy_order_right_menu = app.window(class_name='Qt5QWindowPopupDropShadowSaveBits')
        buy_order_right_menu_standard = buy_order_right_menu.child_window(title='抢单池')
        buy_order_right_menu_standard.click_input()

        qdc = app.window(class_name='Qt5QWindowIcon')
        print(qdc.print_control_identifiers())

        win.child_window(title="查看资料").click_input()

