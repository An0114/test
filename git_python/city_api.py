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



if __name__ == '__main__':
    main()
