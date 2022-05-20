import sys
import json,time
from time import sleep
import numpy as np
import pytest
from os.path import dirname, abspath
from config import RunConfig
from pywinauto import mouse
from pywinauto.keyboard import send_keys
from epeda_method import Gui_main
import os
import cv2


base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.baidu_page import BaiduPage
from page.epsemicon_page import EpsemiconPage

# @pytest.mark.gui_main
class TestGuiMain:
    pytestmark = [pytest.mark.gui_main]

    @pytest.mark.person
    def test_person(self):
        app = RunConfig.epeda_driver
        win = app.get_win('Dialog')

        # image_dir = os.path.join(RunConfig.NEW_REPORT, "image", 'file_name')
        # RunConfig.driver.save_screenshot(image_dir)
        print("*" * 30, "pic")
        top_window = app.get_top_win()
        gui_main_jpg=top_window.capture_as_image()
        gui_main_jpg.save(r'temp\gui_main.jpg')
        img = cv2.imread(r'temp\gui_main.jpg')
        img_cut = img[1:100, 1:300]
        cv2.imwrite(r"temp\person.jpg", img_cut)
        cv2.waitKey(0)
        # time.sleep(1)

        # print(os.getcwd())
        # print(os.path.abspath('__file__'))
        # print(os.path.join(os.getcwd(),r'temp\gui_main.jpg'))
        img_standard = cv2.imread(os.path.join(os.getcwd(),r'test_dir\data\test_gui_main\person.jpg'))
        img_current = cv2.imread(os.path.join(os.getcwd(),r'temp\person.jpg'))

        if img_standard.shape == img_current.shape:
            print("shape一样")
        else:
            print("shape not equal")

        difference = cv2.subtract(img_standard, img_current)
        print(difference)
        result = not np.any(difference)

        if result is True:
            print("两张图一样")
        else:
            cv2.imwrite(r"temp\result.jpg", difference)
            print("两张图不一样")





    @pytest.mark.tool
    def test_group_box(self):
        app=RunConfig.epeda_driver
        win=app.get_win('Dialog')
        assert Gui_main.get_GroupBox_title(win) == ['工具', '数据', '向导', '制造端']

    @pytest.mark.top
    def test_top_module(self):
        app=RunConfig.epeda_driver
        win=app.get_win('Dialog')
        # print(top_module_drzl.print_control_identifiers())

        # 导入资料
        win['Custom9'].click_input()
        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点
        # print(win['Custom17'].print_control_identifiers())
        assert Gui_main.get_top_module(win['Custom9']) == ['导入资料', '支持gerber、odb++、ipc2581、eps等多种格式资料导入']

        # EP-CAM
        win['Custom10'].click_input()
        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点
        assert Gui_main.get_top_module(win['Custom10']) == ['EP-CAM', '快速进入EP-CAM基础软件']

        # 前处理
        win['Custom11'].click_input()
        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点
        assert Gui_main.get_top_module(win['Custom11']) == ['前处理', '图形资料报价和优化前的资料处理模块']

        # CAM自动化
        win['Custom12'].click_input()
        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点
        assert Gui_main.get_top_module(win['Custom12']) == ['CAM自动化', '实现优化功能自动化，包含一键优化和分步骤优化模块']

        # 资料分析 DFM
        win['Custom13'].click_input()
        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点
        assert Gui_main.get_top_module(win['Custom13']) == ['资料分析 DFM', '多层面解析资料，完整给出PCB相关参数或cam服务报价结果模块']

        # 自动移孔功能
        win['Custom14'].click_input()
        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点
        assert Gui_main.get_top_module(win['Custom14']) == ['自动移孔功能', 'ep-cam附带全部高级功能，可实现自动移孔，保证间距模块']

        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点

    @pytest.mark.pre_check
    def test_input_pre_check(self):
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

        # 导入与预审下的前处理
        win['Custom18'].click_input()
        win.child_window(title="陈成").click_input()  # 释放一下，加到主界面焦点
        assert Gui_main.get_top_module(win['Custom18']) == ['前处理', '图形资料报价和优化前的资料处理模块']
