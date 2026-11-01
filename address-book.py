import json
import os
FILE_NAME = "address_book.json"
# 读取文件
def load_file():
    if not os.path.exists(FILE_NAME):  # 如果该路径下的文件不存在，返回空字典
        return {}
    try:
        with open(FILE_NAME,"r",encoding='UTF-8') as f:
            # 将读取到的json文件转为python字典
            return json.load(f)
    except Exception as e:
        # 文件出现其他错误（空文件，格式不符合json规范等）
        print(e)
        # 说明当前文件不可用，返回空字典
        return {}
# 写入文件
def save_file(data):
    with open(FILE_NAME, "w", encoding='UTF-8') as f:
        # 把字典转化成json存进文件（每次调用该函数都会清空原有内容）
        json.dump(data,f,ensure_ascii=False,indent=4)  # 存的内容-存到哪个文件-是否把中文转成ascii码-不同层级之间进行缩进
# 查找
def search_person(name):
    # 得到通讯录字典
    data = load_file()
    # 如果姓名在字典的键中出现
    if name in data:
        # 通过[键名]取该键的值（一个列表，第一个元素是电话，第二个元素是地址）
        print(f"该联系人的联系方式为：{data[name][0]},地址为：{data[name][1]}")
    else:
        print("未找到该联系人...")
# 添加联系人
def add_person(name,number,addr):
    # json转成字典
    data = load_file()
    # 在原有字典上通过{键:值}追加元素到当前字典
    data[name] = [number,addr]
    # 连同新追加的元素重新覆盖通讯录
    save_file(data)
    print("==添加成功==")
# 删除联系人
def del_person(name):
    # 得到字典
    data = load_file()
    # 如果姓名不在data字典键中
    if name not in data:
        print("未找到该联系人...")
        return
    # 调用字典的pop方法弹出该元素
    data.pop(name)
    # 重新写入得到的新字典
    save_file(data)
    print("删除成功")
# 修改联系人
def mdf_person(name,number,addr):
    data = load_file()
    if name not in data:
        print("未找到该联系人...")
        return
    # 相同键会进行值的覆盖
    data[name] = [number,addr]
    save_file(data)
    print("==修改成功==")
# 查看所有联系人
def show_person():
    # 得到字典
    data = load_file()
    # 取出字典中所有键
    data_key = data.keys()
    # 依次取出键元素
    for key in data_key:
        # 取出该键的值（列表），通过下标拿到列表元素
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


