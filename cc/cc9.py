from pywinauto.application import Application
from pywinauto import application,mouse,Desktop
from epeda_method import Connect_epeda
from pywinauto.win32functions import SetFocus



epeda_driver=Connect_epeda(processid=14420)
# eda_exit_confirm=epeda_driver.get_win('Dialog')
# # print(eda_exit_confirm.print_control_identifiers())
# eda_exit_confirm_save=eda_exit_confirm.child_window(title='保存')
# eda_exit_confirm_save.click_input()
gui_main=epeda_driver.get_win('Dialog')
# print(gui_main.print_control_identifiers())
drzl=gui_main.child_window(title="导入资料")
# print(drzl.print_control_identifiers())
drzl.click_input()
drzl.set_focus()