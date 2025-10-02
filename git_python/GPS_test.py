import serial
import pynmea2


def read_gps_data():
    ser = serial.Serial(port='COM3', baudrate=9600, timeout=5, parity=serial.PARITY_NONE, rtscts=0)
    print(ser.readline())

    while True:
        try:
            data = ser.readline().decode('utf-8', errors='replace')
            print(data)
            if data.startswith('$GPGGA'):
                msg = pynmea2.parse(data)
                print(msg)

                latitude = msg.latitude
                longitude = msg.longitude
                altitude = msg.altitude
                print(latitude, longitude, altitude)

                lat_dir = 'N' if msg.lat_dir == 'N' else 'E'
                lon_dir = 'E' if msg.lon_dir == 'E' else 'w'
                print(lat_dir, lon_dir)

                print(f"纬度: {latitude}° {lat_dir}")
                print(f"经度: {longitude}° {lon_dir}")
                print(f"海拔: {altitude}米")
                break

        except serial.SerialException as e:
            print(f"串口错误{e}")
        except pynmea2.ParseError as e:
            print(f"解析错误{e}")
            continue


if __name__ == '__main__':
    read_gps_data()