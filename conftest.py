import os
import time

import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig
from epeda_method import Connect_epeda
from pywinauto import mouse
from epeda_method import Gui_main
from pywinauto.keyboard import send_keys
from pywinauto.application import Application
from pywinauto import application,mouse,Desktop

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/test_report/"


# 定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    return RunConfig.url


# 设置用例描述表头
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.pop()


# 设置用例描述表格
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            capture_screenshots(case_name)
            img_path = "image/" + case_name.split("/")[-1]
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]
    
    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def capture_screenshots(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    global epeda_driver
    file_name = case_name.split("/")[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
        # RunConfig.driver.save_screenshot(image_dir)
        print("*"*30,"pic")
        # top_window=epeda_driver.get_top_win()
        # top_window.capture_as_image().save(image_dir)

def capture_screenshots_selenium(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
        RunConfig.driver.save_screenshot(image_dir)

# 启动浏览器
@pytest.fixture(scope='session', autouse=False)
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器

        options = webdriver.ChromeOptions()
        # 忽略无用的日志
        options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "edge":
        # 本地firefox浏览器
        driver = webdriver.Edge()
        driver.maximize_window()

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif RunConfig.driver_type == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://localhost:4444/wd/hub',
                        desired_capabilities={
                              "browserName": "chrome",
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver

    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=False)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")



#启动EDA
@pytest.fixture(scope='session',autouse=True)
def epeda():
    global epeda_driver
    # print("*" * 30)
    if RunConfig.epeda_driver_type=='epeda':
        pass
        # print("*"*30)
        process_id=Connect_epeda.get_process_id_epeda(RunConfig.epeda_path)
        # print(process_id)
        epeda_driver=Connect_epeda(processid=process_id)
    else:
        raise NameError("epeda_driver驱动类型定义错误！")

    RunConfig.epeda_driver=epeda_driver
    return epeda_driver

#关闭EDA
@pytest.fixture(scope='session',autouse=False)
def epeda_close_1():
    yield epeda_driver
    win=epeda_driver.get_win('Dialog')
    mouse.double_click(coords=Gui_main().get_close_coor())
    try:
        mouse.double_click(coords=Gui_main.get_save_coor(win))
    except:
        pass
    # send_keys('{ENTER}')

    time.sleep(2)
    print("test end!")

    # win = app.get_top_win()

#关闭EDA
@pytest.fixture(scope='session',autouse=True)
def epeda_close():
    yield epeda_driver
    win = epeda_driver.get_win('Dialog')
    app = Application(backend="win32").connect(path="explorer.exe")
    sys_tray = app.window(class_name="Shell_TrayWnd")
    eda_sys_icon = sys_tray.child_window(title="用户提示通知区域")
    eda_sys_icon.click_input()
    eda_sys_icon.right_click_input()
    app = Desktop(backend='uia')
    eda_right_menu = app.window(class_name='Qt5QWindowPopupDropShadowSaveBits')
    eda_exit = eda_right_menu.child_window(title='退出')
    eda_exit.click_input()

    try:
        eda_exit_confirm = epeda_driver.get_win('Dialog')
        eda_exit_confirm_save = eda_exit_confirm.child_window(title='保存')
        eda_exit_confirm_save.click_input()
    except:
        pass

    time.sleep(2)
    print("test end!")

    # win = app.get_top_win()


if __name__ == "__main__":
    capture_screenshots("test_dir/test_baidu_search.test_search_python.png")
