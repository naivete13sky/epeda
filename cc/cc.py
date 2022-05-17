from pywinauto.application import Application
from pywinauto import application,mouse,Desktop
import time
from pywinauto.keyboard import send_keys
# app = Application(backend='uia').start("notepad.exe")
# app = Application(backend='uia').start(r"C:\EPSemicon\EDA_TEST\EPEDA.exe2")
start_directory=r'C:\EPSemicon\EDA_TEST\cc'
app_open=Application().start("explorer.exe %s" % start_directory)
# app_open=Application(backend='win32').start("explorer.exe %s" % start_directory)
app_open=Desktop()
win_open=app_open[start_directory.split("\\")[-1]]
# print(win_open.print_control_identifiers())
time.sleep(1)
#双击打开快捷方式
mouse.double_click(coords=(2200,215))
time.sleep(10)
win=app_open['Dialog']
print(win.print_control_identifiers())