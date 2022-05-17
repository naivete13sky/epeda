from pywinauto import application,mouse,Desktop
from pywinauto.keyboard import send_keys
import time
from config import RunConfig
from method_improve_pywinauto import Method_improve_pywinauto
import re

class Connect_epeda(object):
    def __init__(self,processid):
        self.app = application.Application(backend='uia').connect(process=processid)
        # self.app = application.Application(backend='win32').connect(process=processid)

    def get_win(self,title):
        self.win=self.app[title]
        return self.win

    def get_top_win(self):
        self.top_win=self.app.top_window()
        return self.top_win

    def connect_by_processid_title(processid,title):
        app=application.Application(backend='uia').connect(process=processid)
        return app[title]

    #通过单击程序实现启动
    def get_process_id_epeda(epeda_dir):
        start_directory=epeda_dir
        app_open=application.Application().start("explorer.exe %s" % start_directory)
        app_open=Desktop()
        win_open=app_open[start_directory.split("\\")[-1]]
        time.sleep(1)
        mouse.double_click(coords=(2200, 215))
        time.sleep(10)#登录时间较长
        win = app_open['Dialog']
        print(win.print_control_identifiers())
        # print(win.process_id())
        app_open2 = application.Application(backend='win32').connect(process=win.process_id())
        win2=app_open2['Dialog']
        print(win2.print_control_identifiers())
        return win.process_id()



class Gui_main(object):
    def get_File_coor(win_text):
        win_text_2=Method_improve_pywinauto.get_print_control_identifiers_text(win_text)
        coor_ok=Method_improve_pywinauto.get_coor_of_object('File(F) Alt+F',win_text_2)
