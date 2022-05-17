import re
text_from='''Pane - 'Dialog'    (L1634, T0, R1920, B716)
['Dialog', 'DialogPane', 'Pane', 'Pane0', 'Pane1']
child_window(title="Dialog", control_type="Pane")
   |
   | Static - ''    (L1634, T0, R1920, B151)
   | ['Static', '具，推荐立享200元优惠券，后续功能将陆续上线，敬请试用。Static', 'Static0', 'Static1']
   |
   | GroupBox - ''    (L1634, T155, R1920, B205)
   | ['GroupBox', '具，推荐立享200元优惠券，后续功能将陆续上线，敬请试用。GroupBox']
   |    |
   |    | RadioButton - '工具'    (L1635, T156, R1729, B203)
   |    | ['工具RadioButton', 'RadioButton', '工具', 'RadioButton0', 'RadioButton1']
   |    | child_window(title="工具", control_type="RadioButton")
   |    |
   |    | RadioButton - '数据'    (L1729, T156, R1823, B203)
   |    | ['数据', 'RadioButton2', '数据RadioButton']
   |    | child_window(title="数据", control_type="RadioButton")
   |    |
   |    | RadioButton - '向导'    (L1823, T156, R1918, B203)
   |    | ['向导RadioButton', '向导', 'RadioButton3']
   |    | child_window(title="向导", control_type="RadioButton")   |
   '''
text_wanted='title'
for tup in text_from.splitlines():
    # print(tup)
    i = tup.find(text_wanted)
    if i > 0:
        # print("i>0")
        # print(tup)
        pattern = re.compile(r'''child_window\(title="(.+)",''')
        result = pattern.findall(tup)[0]
        print("*" * 30, result)
        # tup_coor = result[0]
        # print("*" * 30, tup_coor)