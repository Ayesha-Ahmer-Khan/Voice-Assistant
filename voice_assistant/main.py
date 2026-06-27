import keyboard
from recorder import record_audio_until_release
from transcriber import transcribe
from config import HOTKEY
from brain import generate_response
from tts import speak


def main():
    print(f"Hold {HOTKEY} to talk.")

    while True:
        keyboard.wait(HOTKEY)

        audio = record_audio_until_release()

        if audio:
            user_text = transcribe(audio)

            print()
            print("You said:", user_text)
            print()

            response = generate_response(user_text)

            speak(response)


if __name__ == "__main__":
    main()