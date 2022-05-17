import sys,re
class TextArea(object):
    def __init__(self):
        self.buffer=[]
    def write(self,*args,**kwargs):
        self.buffer.append(args)

class Method_improve_pywinauto(object):
    def get_print_control_identifiers_text(object_print_control_identifiers):
        #获取程序File坐标
        stdout=sys.stdout
        sys.stdout=TextArea()
        object_print_control_identifiers.print_control_identifiers()
        text_area,sys.stdout=sys.stdout,stdout
        return text_area.buffer

    def get_coor_of_object(text_wanted,text_from):
        for tup in text_from:
            i=tup[0].find(text_wanted)
            if i>0:
                pattern=re.compile(r"(\(L\d+, T\d+, R\d+, B\d+\))")
                result=pattern.findall(tup[0])
                tup_coor=result[0]
        coor_file_w = int(tup_coor.split(",")[0][2:]) + 1
        coor_file_h = int(tup_coor.split(",")[1][2:]) + 1
        return (coor_file_w,coor_file_h)

    def get_coor_of_object_id(text_wanted,text_from,id):
        date_item_list=[]
        tup_coor_id=""
        for tup in text_from:
            i=tup[0].find(text_wanted)
            if i>0:
                pattern = re.compile(r"(\(L\d+, T\d+, R\d+, B\d+\))")
                result = pattern.findall(tup[0])
                tup_coor_id = result[0]
                coor_file_w = int(tup_coor_id.split(",")[0][2:]) + 1
                coor_file_h = int(tup_coor_id.split(",")[1][2:]) + 1
                date_item_list.append(coor_file_w,coor_file_h)
        return (date_item_list[id])

    def get_coor_of_object2(text_wanted, text_from):
        tup_coor_cc=()
        for tup in text_from:
            i = tup[0].find(text_wanted)
            if i > 0:
                pattern = re.compile(r"(\(L\d+, T\d+, R\d+, B\d+\))")
                result = pattern.findall(tup[0])
                tup_coor_cc = result[0]
        coor_file_w = int(tup_coor_cc.split(",")[0][2:]) + 1
        coor_file_h = int(tup_coor_cc.split(",")[1][2:]) + 1
        return (coor_file_w, coor_file_h)

    def get_coor_of_object_r(text_wanted, text_from):

        for tup in text_from:
            i = tup[0].find(text_wanted)
            if i > 0:
                pattern = re.compile(r"(\(L\d+, T\d+, R\d+, B\d+\))")
                result = pattern.findall(tup[0])
                tup_coor = result[0]
        coor_file_w = int(tup_coor.split(",")[2][2:]) - 1
        coor_file_h = int(tup_coor.split(",")[3][2:].replace(")","")) - 1
        return (coor_file_w, coor_file_h)

    def get_title_of_object(text1_wanted,text2_wanted,text_from):
        result_list=[]
        for tup in text_from:
            i=tup[0].find(text1_wanted)
            j=tup[0].find(text2_wanted)
            if i>0  and j>0:
                # print("i>0 and j>0")
                # print(tup[0])
                pattern=re.compile(r'''child_window\(title="(.+)",''')
                result=pattern.findall(tup[0])
                tup_coor=result[0]
                # print("*"*30,tup_coor)
                result_list.append(tup_coor)
        # coor_file_w = int(tup_coor.split(",")[0][2:]) + 1
        return (result_list)

