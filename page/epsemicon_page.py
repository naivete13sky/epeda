from poium import Page,Element,Elements
class EpsemiconPage(Page):
    search_input = Element(id_="kw", describe="搜索框")
    search_button = Element(id_="su", describe="搜索按钮")
    settings = Element(link_text="设置", describe="设置下拉框")
    # settings = NewPageElement(id_='s-usersetting-top',describe="设置下拉框")#此行有效，可测试通过；如果想看测试不通过的结果，用上面那个语句。
    search_setting = Element(css=".setpref", describe="搜索设置选项")#下面这行的方法也可以。
    # search_setting = NewPageElement(link_text='搜索设置', describe="搜索设置选项")
    save_setting = Element(css=".prefpanelgo", describe="保存设置")
    # 定位一组元素
    search_result = Elements(xpath="//div/h3/a", describe="搜索结果")

    # 定位所有主菜单
    index_main_menu_result = Elements(xpath="/html/body/div[1]/nav/div/ul", describe="所有主菜单")
    #定位主菜单-首页
    index_main_menu_result_1 = Element(xpath="/html/body/div[1]/nav/div/ul/li[1]/a", describe="首页")
    # 定位主菜单-动态资讯
    index_main_menu_result_2 = Element(xpath="/html/body/div[1]/nav/div/ul/li[3]/a", describe="动态资讯")
    # 定位主菜单-产品与解决方案
    index_main_menu_result_3 = Element(xpath="/html/body/div[1]/nav/div/ul/li[5]/a", describe="产品与解决方案")
    # 定位主菜单-我们的优势
    index_main_menu_result_4 = Element(xpath="/html/body/div[1]/nav/div/ul/li[7]/a", describe="我们的优势")
    # 定位主菜单-会员中心
    index_main_menu_result_5 = Element(xpath="/html/body/div[1]/nav/div/ul/li[9]/a", describe="下载专区")
    # 定位主菜单-诚邀加盟商/代理商
    index_main_menu_result_6 = Element(xpath="/html/body/div[1]/nav/div/ul/li[10]/a", describe="诚邀加盟商/代理商")
    # 定位主菜单-加入我们
    index_main_menu_result_7 = Element(xpath="/html/body/div[1]/nav/div/ul/li[11]/a", describe="加入我们")
    # # 定位主菜单-加入我们
    # index_main_menu_result_8 = Element(xpath="/html/body/div[1]/nav/div/ul/li[12]/a", describe="加入我们")
