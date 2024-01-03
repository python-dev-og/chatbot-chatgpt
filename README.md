![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-%5E6.2-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-blue)
![Chatbot](https://img.shields.io/badge/Chatbot-Enabled-brightgreen)
![API](https://img.shields.io/badge/API-RESTful-orange)
![ChatGPT](https://img.shields.io/badge/ChatGPT-OpenAI-blue)

# Chatbot Application

## Introduction
This repository contains the source code for a simple chatbot application. The application is built using Python with PyQt6 for the graphical user interface (GUI) and includes a backend module that handles chatbot interactions. It's designed to provide a basic example of how to integrate a chatbot in a GUI application.

## Features
- GUI application using PyQt6.
- Input field for user queries.
- Display area for conversation history.
- Separate thread for handling chatbot responses to maintain UI responsiveness.

## Requirements
- Python 3.x
- PyQt6
- A custom `backend` module with a `Chatbot` class.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install PyQt6 using pip:
   ```bash
   pip install PyQt6
   ```
3. Clone this repository or download the source code.

## Usage
To run the application, navigate to the directory containing the source code and execute the main Python script:
```bash
python main.py
```
Replace `main.py` with the actual name of the script if different.

## Code Structure
- `ChatbotWindow`: The main window class for the application, derived from `QMainWindow`.
  - Initializes the chatbot instance.
  - Sets up the GUI layout with a chat area, input field, and send button.
  - Handles the sending of messages and display of chatbot responses.

- `send_message`: Method connected to the input field and button to handle sending messages.

- `get_bot_response`: Method that runs in a separate thread to fetch responses from the chatbot.

## Backend Module
The application requires a `backend` module that contains the `Chatbot` class. This class must have a `get_response` method that accepts a user query and returns the chatbot's response.

## Customization
- Modify the `backend` module to integrate your chatbot logic.
- Update the GUI layout and styles in the `ChatbotWindow` class as needed.

## Contribution
Contributions to enhance this application are welcome. Please follow standard coding practices and provide documentation for any significant changes.

## License
This project is licensed under the MIT License. See the LICENSE file in this repository for more information.

## Final Look 

![start.png](images%2Fstart.png)

![result.png](images%2Fresult.png)

