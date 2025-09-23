import pyttsx3

def tts_with_voice(text, voice_id = None):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    print("可用音色列表：")
    for i, voice in enumerate(voices):
        print(f"{i}. ID: {voice.id}, Name: {voice.name}, language: {voice.languages}")

    if voice_id is not None:
        engine.setProperty('voice', voice_id)
    else:
        engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

tts_with_voice("这是默认音色的语音")
