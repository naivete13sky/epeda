from pywinauto.application import Application
from pywinauto import application,mouse,Desktop
import time
app_open=application.Application().connect(path=r'C:\Windows\explorer.exe')
# app_open=application.Application().connect(process=12936)
print(app_open)
print(app_open.process)
win=app_open.window(title="通知 V 形")
# print(win)
# print(win.print_control_identifiers())


from pywinauto import taskbar
taskbar.TaskBar.Button.click_input()
popup_dlg = taskbar.explorer_app.window(class_name='NotifyIconOverflowWindow')
popup_toolbar = popup_dlg.Overflow_Notification_Area
print(popup_toolbar.texts())
# print(popup_toolbar.texts()[1:])
# popup_toolbar.button('your program name').click_input(double=True)