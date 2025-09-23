import pyttsx3


def text_to_speech(text):
    """使用pyttsx3将文本转为语音并播放"""
    # 1. 初始化语音引擎
    engine = pyttsx3.init()

    # 2. 设置参数（可选）
    # 设置语速（默认200，范围可调整）
    engine.setProperty('rate', 180)
    # 设置音量（0.0-1.0，默认1.0）
    engine.setProperty('volume', 0.9)

    # 3. 获取可用 voices（可查看支持的语言和音色）
    voices = engine.getProperty('voices')
    # 选择第一个 voice（默认英文，中文需特殊处理，见注意事项）
    engine.setProperty('voice', voices[0].id)

    # 4. 文本转语音并播放
    engine.say(text)
    engine.runAndWait()  # 等待播放完成


# 示例：将大模型输出转为语音
if __name__ == "__main__":
    # 假设这是大模型的输出内容
    model_output = "这是大模型生成的文本，现在将通过语音朗读播放出来。"
    text_to_speech(model_output)