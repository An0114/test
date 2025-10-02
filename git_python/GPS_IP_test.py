import requests


def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        print(data)

        if 'loc' in data:
            latitude, longitude = data['loc'].split(',')
            city = data.get('city', '未知')
            region = data.get('region', '未知')
            country = data.get('country', '未知')
            print(f"位置: {city}, {region}, {country}")
            print(f"纬度: {latitude}")
            print(f"经度: {longitude}")
        else:
            print("无法获取位置信息")
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误{e}")


if __name__ == '__main__':
    get_location_by_ip()