import requests


def main():
    city_name = input("请输入地点：")
    req = requests.get(f"https://restapi.amap.com/v3/geocode/geo?address={city_name}&output=JSON&key=ef96e661e28431337d3840b195e2aa77")
    req_data = req.json()
    print(req_data)
    # print(type(req_data))
    data = req_data["geocodes"][0]
    print(data)
    data_ad = data["adcode"]
    print(data_ad)
    '''
    判断status/info/infocode是否为1/ok/10000=>是否可以得到地点信息
    判断count是否为0=>无此地点
                为1=>为唯一正选地点
                为1以上=>列出每一项结果的formatted_address/以逗号隔开country,province,city,district,输入地点/利用字符串切片形成以逗号隔开的形式
    供用户进行选择正确地点
    获取正确地点的adcode
    进行其他操作=>地点定位/天气预报等
    '''



if __name__ == '__main__':
    main()
