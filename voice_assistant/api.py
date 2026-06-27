from fastapi import FastAPI
from recorder import record_audio
from transcriber import transcribe

app = FastAPI()


@app.post("/listen")
def listen():
    audio_path = record_audio()
    text = transcribe(audio_path)

    return {
        "transcript": text
    }