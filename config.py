

class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = "./test_dir/"

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"
    # driver_type = "edge"

    epeda_driver_type='epeda'
    # epeda_path=r'C:\EPSemicon\EDA_TEST'
    epeda_path=r'C:\EPSemicon\EDA_TEST'
    epeda_driver=None

    # 配置运行的 URL
    url = "http://www.epsemicon.com/"

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None
