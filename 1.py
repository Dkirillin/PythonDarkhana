import speech_recognition as sr
import pyttsx3
import datetime

# Инициализация распознавателя речи и синтезатора
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='ru-RU')
            print(f"Вы сказали: {command}")
            return command
        except sr.UnknownValueError:
            print("Не распознала, попробуйте еще раз.")
            return None
        except sr.RequestError:
            print("Ошибка соединения, проверьте интернет.")
            return None


def main():
    speak("Привет! Я ваш персональный помощник.")

    while True:
        command = listen()

        if command:
            command = command.lower()

            if "привет" in command:
                speak("Привет! Как я могу помочь?")
            elif "текущее время" in command:
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M")
                speak(f"Текущее время: {current_time}")
            elif "дата" in command:
                today = datetime.date.today()
                speak(f"Сегодня: {today}")
            elif "выход" in command:
                speak("До свидания!")
                break
            else:
                speak("Извините, я не понимаю.")


if __name__ == "__main__":
    main()