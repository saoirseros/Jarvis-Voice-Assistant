# Jarvis Voice Assistant: Python System Control and API Integration

This project is a **Python-powered voice assistant** capable of performing **system operations**, **web navigation**, and **real-time data retrieval** using speech recognition and external APIs.  
It demonstrates strong fundamentals in **programming, speech processing, and system integration**.


## Key Features

- **Speech-to-Text (STT) & Text-to-Speech (TTS):** Enables natural two-way voice interaction using industry-standard libraries.  
- **System Automation:** Executes system commands such as opening web apps or performing general computer operations.  
- **Real-time Data Retrieval:** Integrates APIs like OpenWeatherMap, Wikipedia, and Google Speech for instant, contextual information.  
- **Cross-Platform Compatibility:** Works seamlessly across different operating systems using Python-based libraries.


## Technology Stack

| Category | Technologies Used |
|-----------|-------------------|
| **Primary Language** | Python |
| **Speech Processing** | `speech_recognition`, `pyttsx3` |
| **API Integration** | OpenWeatherMap API (`requests`), Google Web Speech API, Wikipedia API |
| **UI/Display** | Tkinter (for weather output window) |


## Getting Started

### Prerequisites
- **Python 3.x** installed  
- **Working Microphone**  
- **Valid OpenWeatherMap API Key** (for weather feature)  
- **PyAudio** installed (required for microphone input)  


### Setup Instructions:

**1️. Clone the Repository**
git clone https://github.com/saoirseros/Jarvis-Voice-Assistant

cd Jarvis-Voice-Assistant


**2️. Create and Activate Virtual Environment**

python -m venv venv

.\venv\Scripts\activate

**3️. Install Dependencies**

pip install SpeechRecognition pyttsx3 PyAudio pyjokes wikipedia requests

 # API Key Setup

Open the main file

Replace the placeholder OpenWeatherMap API Key with your actual key.

▶️ Running the Application

## Start Jarvis:

python main.py

Once started, Jarvis will announce that it’s listening — you can then speak any supported voice command.

# Supported Voice Commands

| **Command Phrase** | **Action Performed** |
|--------------------|----------------------|
| “What is your name?” | Jarvis introduces itself |
| “What time is it?” | Retrieves and speaks the current time |
| “What is the date?” | Announces today’s date |
| “Open Google / YouTube / Netflix” | Opens the requested website in the default browser |
| “Tell me a joke” | Fetches a random joke |
| “Search Wikipedia for [topic]” | Reads a short summary for the topic using the Wikipedia API |
| “Weather” | Opens a Tkinter window to display live weather data |
| “Exit” | Stops the Jarvis assistant |
