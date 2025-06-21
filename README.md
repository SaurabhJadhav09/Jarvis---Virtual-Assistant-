# 🗣️ Jarvis - Voice Assistant (Python)

“I am Jarvis, your personal assistant.” 🧠

Jarvis is a basic voice assistant built in Python. It listens for a wake word ("Jarvis") and can perform tasks such as opening websites, playing songs, reading news, and answering general questions using OpenAI's GPT API.

---

## 🛠 Features

- Wake word detection: "Jarvis"
- Open websites (Google, YouTube, LinkedIn, Facebook)
- Play songs from a custom `musicLibrary`
- Fetch news headlines (via NewsAPI)
- Respond to custom queries using OpenAI GPT
- Text-to-speech with `gTTS` and `pyttsx3`

---

###For better voice recognition:

```bash

- **pip install pocketsphinx

## 📦 Dependencies

Install required packages using:

```bash
pip install speechrecognition pyttsx3 gTTS pygame requests openai


## 🔐 API Keys Required

- **OpenAI API Key** (for GPT responses)
- **NewsAPI Key** (for fetching news)

🔒 Replace the `#` placeholders in the script with your actual API keys.

---

## 📁 Notes

Create a file named `musicLibrary.py` with a dictionary of songs like:

```python
music = {
    "believer": "https://example.com/believer.mp3",
    "shapeofyou": "https://example.com/shapeofyou.mp3"
}

##🔧 How to Run
```bash
- ** python jarvis.py
- ** Make sure your microphone is working. Say "Jarvis" to activate the assistant.