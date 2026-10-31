import json
import os
FILE_NAME = "address_book.json"
# 读取文件
def load_file():
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME,"r",encoding='UTF-8') as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return {}
# 写入文件
def save_file(data):
    with open(FILE_NAME, "w", encoding='UTF-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

def search_person(name):
    data = load_file()
    if name in data:
        print(f"该联系人的联系方式为：{data[name][0]},地址为：{data[name][1]}")
    else:
        print("未找到该联系人...")
def add_person(name,number,addr):
    data = load_file()
    data[name] = [number,addr]
    save_file(data)
    print("==添加成功==")
def del_person(name):
    data = load_file()
    if name not in data:
        print("未找到该联系人...")
        return
    data.pop(name)
    save_file(data)
    print("删除成功")
def mdf_person(name,number,addr):
    data = load_file()
    if name not in data:
        print("未找到该联系人...")
        return
    data[name] = [number,addr]
    save_file(data)
    print("==修改成功==")
def show_person():
    data = load_file()
    data_key = data.keys()
    for key in data_key:
        print(f"{key}:{data[key][0]},{data[key][1]}")
while True:
    print("====通讯录系统====")
    print("添加联系人   --1")
    print("删除联系人   --2")
    print("修改联系人   --3")
    print("查询联系人   --4")
    print("显示全部联系人--5")
    print("退出        --0")
    num = int(input("请输入你想要查询的数字编号："))
    if num == 0:
        print("正在退出...")
        break
    elif num == 1:
        print("-----  添加联系人  -----")
        name = input("请输入你想要添加联系人的姓名：")
        number = input("请输入联系电话：")
        addr = input("请输入地址：")
        add_person(name,number,addr)
    elif num == 2:
        print("-----  删除联系人  -----")
        name = input("请输入你想要删除联系人的姓名：")
        del_person(name)
    elif num == 3:
        print("-----  修改联系人  -----")
        name = input("请输入你想修改联系人的姓名：")
        number = input("请输入电话：")
        addr = input("请输入地址：")
        mdf_person(name,number,addr)
    elif num == 4:
        print("----- 查询联系人 -----")
        name = input("请输入你想查询联系人的姓名：")
        search_person(name)
    elif num == 5:
        print("-----  显示全部联系人  -----")
        show_person()
    else:
        print("请输入正确功能编号")

