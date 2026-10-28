person = {}
def add_person(name,number):
    if len(person) < 100:
        person[name] = number
        print("==添加成功==")
    else:
        print("通讯录已满，无法添加...")
def del_person(name):
    if name in person:
        person.pop(name)
        print("==删除成功==")
    else:
        print("未找到该联系人")
def mdf_person(name,number):
    if name in person:
        person[name] = number
        print("==修改成功==")
    else:
        print("未找到该联系人")
def search_person(name):
    flag = 0
    for i in person:
        if i == name:
            print(f"该联系人的联系方式为:{person[i]}")
            flag = 1
    if flag == 0:
        print("未查找到该联系人")
def show_person():
    for i in person:
        print(f"{i}:{person[i]}")
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
        add_person(name,number)
    elif num == 2:
        print("-----  删除联系人  -----")
        name = input("请输入你想要删除联系人的姓名：")
        del_person(name)
    elif num == 3:
        print("-----  修改联系人  -----")
        name = input("请输入你想修改联系人的姓名：")
        number = input("请输入电话：")
        mdf_person(name,number)
    elif num == 4:
        print("----- 查询联系人 -----")
        name = input("请输入你想查询联系人的姓名：")
        search_person(name)
    elif num == 5:
        print("-----  显示全部联系人  -----")
        show_person()
    else:
        print("请输入正确功能编号")


