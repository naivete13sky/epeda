from pywinauto.application import Application
from pywinauto import application,mouse,Desktop
import time
app = Application(backend="win32").connect(path="explorer.exe")
sys_tray = app.window(class_name="Shell_TrayWnd")
# sys_tray.child_window(title='“系统音量状态”按钮 扬声器 (Realtek(R) Audio): 已静音').click()
# print(sys_tray.print_control_identifiers())
eda_sys_icon=sys_tray.child_window(title="用户提示通知区域")
# print(eda_sys_icon.print_control_identifiers())
eda_sys_icon.click_input()
eda_sys_icon.right_click_input()
app=Desktop(backend='uia')
eda_right_menu=app.window(class_name='Qt5QWindowPopupDropShadowSaveBits')
# print(eda_right_menu.print_control_identifiers())
eda_exit=eda_right_menu.child_window(title='退出')
# print(eda_exit.print_control_identifiers())
eda_exit.click_input()

try:
    from epeda_method import Connect_epeda
    epeda_driver=Connect_epeda(processid=12032)
    eda_exit_confirm=epeda_driver.get_win('Dialog')
    # print(eda_exit_confirm.print_control_identifiers())
    eda_exit_confirm_save=eda_exit_confirm.child_window(title='保存')
    eda_exit_confirm_save.click_input()
except:
    pass


