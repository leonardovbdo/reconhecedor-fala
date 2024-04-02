import speech_recognition as speech

def capture_speech():
    isCaptured, text = False, None

    recognizer = speech.Recognizer()

    try:
        with speech.Microphone() as audio_source:
            recognizer.adjust_for_ambient_noise(audio_source)

            print("Say something...")
            listener = recognizer.listen(audio_source, timeout=4, phrase_time_limit=4)

            text = recognizer.recognize_google(listener, language="pt-BR")

            isCaptured = True
    except Exception as e:
        print(f"Error on speech capture: {str(e)}")

    return isCaptured, text

def print_text(text):
    print(f"Captured text: {text}")

if __name__ == "__main__":
    isCaptured, text = capture_speech()

    if isCaptured:
        print_text(text)