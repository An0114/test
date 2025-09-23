import speech_recognition as sr

def mic_input_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("请开始说话（说完会自动识别）...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    try:
        print("正在识别...")
        text = recognizer.recognize_google(audio, language='zh_CN')
        print(f"识别结果:{text}")
        return text

    except sr.WaitTimeoutError:
        print("错误：等待语音超时（5秒内未检测到声音）")
        return None
    except sr.UnknownValueError:
        print("错误：无法识别语音（可能声音模糊或无有效语音）")
        return None
    except sr.RequestError as e:
        print(f"错误：语音识别服务请求失败（{e}）")
        return None

mic_text = mic_input_to_text()
if mic_text:
    print(f"程序接收的麦克风输入：{mic_text}")