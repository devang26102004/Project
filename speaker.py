import pyttsx3

if __name__ == "__main__":
    x = input("Enter the string you want to speak: ")
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
