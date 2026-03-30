# Assistant.ai (Ultron)

A simple, voice-activated desktop assistant built with Python. Ultron listens to your voice commands and can perform various basic tasks to help streamline your workflow.

## Features

- **Voice Recognition**: Listens to commands using the `speech_recognition` library.
- **Text-to-Speech**: Responds back using the `pyttsx3` library.
- **Current Time**: Can tell you the current time.
- **Web Navigation**: Opens popular websites like YouTube and Google.
- **Media Playback**: Can play a predefined song on YouTube.
- **System Applications**: Can launch desktop applications like Notepad and Calculator.

## Prerequisites

To run this project, you need to have Python installed on your system. You also need to install the following dependencies:

- `SpeechRecognition`
- `pyttsx3`
- `PyAudio` (required by `SpeechRecognition` for microphone input)

You can install these dependencies using `pip`:

```bash
pip install SpeechRecognition pyttsx3 PyAudio
```

## How to Run

1. Clone or download the repository to your local machine.
2. Activate the virtual environment if you have one set up (e.g., `venv\Scripts\activate` on Windows).
3. Run the script:
   ```bash
   python ultron.py
   ```

## Available Commands

Once the assistant is running and says "Listening...", you can try giving the following commands:

- **"hello"**: Receives a greeting.
- **"time"**: Tells the current system time.
- **"youtube"**: Opens YouTube in your default web browser.
- **"google"**: Opens Google in your default web browser.
- **"song"** or **"play song"**: Plays a specific song on YouTube.
- **"notepad"**: Opens the Windows Notepad application.
- **"calculator"**: Opens the Windows Calculator application.
- **"exit"** or **"quit"**: Shuts down the assistant.

## Customization

You can easily add more commands by modifying the `ultron.py` file. Just add another `elif` block in the `main` loop and define the action!
