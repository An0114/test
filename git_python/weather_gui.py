from tkinter import *
import WeatherGui as wg
import requests
import json
import pandas as pd

base_url = "https://restapi.amap.com/v3/weather/weatherInfo"
df = pd.read_excel("D:\新建文件夹\OneDrive\桌面\python file\git_project\git_python\城市编码表\AMap_adcode_citycode.xlsx")


def get_location_id(city_name):
    # 这里是一个简单的城市adcode映射字典，实际使用时建议使用完整的城市编码表
    city_adcode_map = dict(zip(df['中文名'], df['adcode']))

    return city_adcode_map.get(city_name, None)

def get_weather_data(location_id):

    if location_id is None:
        return None

    params = {
        "key": "ef96e661e28431337d3840b195e2aa77",
        "city":location_id,
        "extensions":"base",
        "output":"JSON"
    }

    try:
        response = requests.get(base_url, params=params)
        # return response.status_code test网络链接
        response.raise_for_status()

        data = response.json()

        if data["status"] == "1" and data["infocode"] == "10000":
            return data.get('lives', [{}])[0]
        else:
            return {"error": f"API错误{data.get('infocode','未知错误')}"}


    except requests.exceptions.RequestException as e:
        return {"error": f"网络请求异常：{str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"解析错误{str(e)}"}

def get_weather():
    city_name = weather_app.get_entry()

    if not city_name:
        print("Please enter a city name")
        return

    location_id = get_location_id(city_name)
    if not location_id:
        print("无法获取城市")
        return

    weather_data = get_weather_data(location_id)
    if not weather_data:
        print("无法获取该地区天气")
        return

    raw_weather_text = f"""
    当前城市：{weather_data.get('live','')} {weather_data.get('city','')}
    天气: {weather_data.get('weather', '')}
    温度: {weather_data.get('temperature', '')}°C
    风向: {weather_data.get('winddirection', '')}风
    风力: {weather_data.get('windpower', '')}级
    湿度: {weather_data.get('humidity', '')}%
    报告时间: {weather_data.get('reporttime', '')}
    """

    weather_app.print_weather(raw_weather_text)

def main():
    weather_app.btn['command'] = get_weather

if __name__ == '__main__':
    root = Tk()
    weather_app = wg.WeatherGui(root)
    main()
    weather_app.run()