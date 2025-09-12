import pandas as pd

df = pd.read_excel("D:\新建文件夹\OneDrive\桌面\python file\git_project\git_python\城市编码表\AMap_adcode_citycode.xlsx")


def main_one():
    data_dic = df.to_dict()
    print("方法一 - 整个DataFrame转换为字典:")
    print(data_dic)


def main_two():
    data_dic = df.to_dict("records")
    print("方法二 - 按行转换为字典列表:")
    print(data_dic)


def main_three():
    index_dict = df.to_dict("index")
    print("方法三-按索引转换为字典")
    print(index_dict)


def main_four():
    df.set_index("中文名", inplace=True)
    index_dict = df.to_dict("index")
    print("方法四-按指定列为索引转换为字典")
    print(index_dict)


def main_five():
    specific_dict = dict(zip(df['中文名'], df['adcode']))
    print("\n方法五 - 特定列转换为字典:")
    print(specific_dict)
    print(specific_dict.get('北京市', None))


if __name__ == '__main__':
    # main_one()
    # main_two()
    # main_three()
    # main_four()
    main_five()
