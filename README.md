# Voice Actuator Assistant

A Python-based voice-controlled actuator assistant that listens for spoken commands, transcribes them using Whisper, parses structured actuator instructions, and sends commands to actuator control logic.

---

## Project Overview

The assistant follows this pipeline:

```text
Speech Input
    ↓
Audio Recording
    ↓
Speech-to-Text (Whisper)
    ↓
Command Parsing
    ↓
Actuator Controller
    ↓
Physical Actuator Movement
```

Example voice command:

```text
25 30 1 4 1 second up
```

Parsed output:

```python
{
    "actuators": [25, 30, 1, 4],
    "duration": 1,
    "direction": "up"
}
```

---

# Libraries Used

| Library | Purpose | Install Command |
|---------|---------|----------------|
| keyboard | Detect hotkey press/release | `pip install keyboard` |
| sounddevice | Record microphone audio | `pip install sounddevice` |
| soundfile | Save audio as WAV | `pip install soundfile` |
| numpy | Handle audio buffers | `pip install numpy` |
| faster-whisper | Speech-to-text transcription | `pip install faster-whisper` |
| re | Command parsing via regex | Built into Python |
| tkinter | GUI frontend | Built into Python |

---

## Optional Libraries

| Library | Purpose |
|---------|---------|
| pyttsx3 | Text-to-Speech |
| requests | API communication / LLM integration |

---

# Installation

Install required packages:

```bash
pip install keyboard sounddevice soundfile numpy faster-whisper
```

---

# Project Structure

```text
voice_assistant/
│
├── config.py
├── recorder.py
├── transcriber.py
├── command_parser.py
├── actuator_controller.py
├── main.py
└── gui.py
```

---

# File Descriptions

---

## 1. `config.py`

Stores global configuration.

Example:

```python
SAMPLE_RATE = 16000
CHANNELS = 1
HOTKEY = "space"
MODEL_SIZE = "tiny"
TEMP_AUDIO_PATH = "input.wav"
```

Responsibilities:

- Audio settings
- Whisper model size
- Hotkey configuration
- Temporary file path

---

## 2. `recorder.py`

Handles microphone recording.

Responsibilities:

- Start recording when hotkey is pressed
- Stop recording when released
- Save audio as WAV

Libraries used:

- `sounddevice`
- `soundfile`
- `numpy`
- `keyboard`

Flow:

```text
Press Space
    ↓
Start Recording
    ↓
Release Space
    ↓
Save input.wav
```

---

## 3. `transcriber.py`

Handles speech-to-text.

Responsibilities:

- Load Whisper model
- Transcribe audio
- Return clean text

Library:

- `faster-whisper`

Example:

```text
input.wav
    ↓
Whisper
    ↓
"25 30 1 4 1 second up"
```

---

## 4. `command_parser.py`

Converts transcript into structured commands.

Example input:

```text
25 30 1 4 1 second up
```

Output:

```python
{
    "actuators": [25, 30, 1, 4],
    "duration": 1,
    "direction": "up"
}
```

Responsibilities:

- Clean punctuation
- Detect actuator IDs
- Detect duration
- Detect direction
- Handle special commands:
  - `all stop`
  - `all move`

Direction options:

- `up`
- `down`
- `all stop`
- `all move`

---

## 5. `actuator_controller.py`

Controls physical actuators.

Current version:

```python
print("Moving actuators...")
```

Future integration:

- Arduino
- Serial COM
- Motor driver board
- PLC
- Hardware API

Example:

```python
execute_command(command)
```

Input:

```python
{
    "actuators": [25, 30],
    "duration": 1,
    "direction": "up"
}
```

Output:

Physical movement of actuators.

---

## 6. `main.py`

Main backend orchestrator.

Pipeline:

```text
Hotkey
  ↓
Recorder
  ↓
Transcriber
  ↓
Parser
  ↓
Actuator Controller
```

Responsibilities:

- Run main loop
- Coordinate modules

Pseudo code:

```python
audio = record_audio()
text = transcribe(audio)
command = parse_command(text)
execute_command(command)
```

---

## 7. `gui.py`

Tkinter-based frontend.

Responsibilities:

- Display system status
- Show transcript
- Show parsed command
- Provide control buttons
- Emergency stop

Example UI:

```text
┌─────────────────────────┐
│ Voice Actuator Control  │
├─────────────────────────┤
│ Status: Idle            │
│ Transcript: ...         │
│ Parsed Command: ...     │
│                         │
│ [Listen]   [All Stop]   │
└─────────────────────────┘
```

Library:

- `tkinter`

---

# Module Dependency Graph

```text
config.py
   ↑
   │
recorder.py
transcriber.py
   │
   ↓
main.py / gui.py
   │
   ↓
command_parser.py
   │
   ↓
actuator_controller.py
```

---

# Command Format

Supported command structure:

```text
[Actuator IDs...] [Duration] [Direction]
```

Examples:

### Single actuator

```text
12 3 sec up
```

Parsed:

```python
{
    "actuators": [12],
    "duration": 3,
    "direction": "up"
}
```

---

### Multiple actuators

```text
11 23 56 1 sec down
```

Parsed:

```python
{
    "actuators": [11, 23, 56],
    "duration": 1,
    "direction": "down"
}
```

---

### Special commands

```text
all stop
```

```text
all move
```

---

# Future Improvements

- Improve number recognition
- Reduce Whisper latency
- Add actuator state feedback
- Add GUI control panel
- Add emergency stop override
- Replace Whisper with grammar-based STT for better numeric accuracy
