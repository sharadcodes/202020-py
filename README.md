# 20-20-20 Rule Reminder with TTS

## Description:

This is a small project designed to remind users to take a break every 20 minutes and follow the 20-20-20 rule. The rule involves taking a 20-second break every 20 minutes and looking at something 20 feet away to help reduce eye strain and fatigue. The code also provides motivational quotes or messages during the break time using Text-To-Speech (TTS) technology.

The code utilizes the Edge TTS API for online TTS and the pyttsx3 library for local TTS. It also retrieves a random quote from the ZenQuotes API for online TTS during break time if there is an internet connection.

## Installation Steps:

- Install Python 3.x if it is not already installed on your system
- Clone this repository or download & unzip the ZIP file
- Run `cd ./202020-py/`
- Install the required libraries by running the command

  Run either

  ```bash
  pip install -r requirements.txt
  ```

  OR

  ```bash
  pip install edge-tts winsound pyttsx3 pydub requests
  ```

  in the command prompt or terminal.

## Usage

To use the script, simply run the main.py file in the command line or terminal using the command

```bash
python 202020.py
```

During the work time, the script will display the time left in minutes and seconds. When the break time starts, it will either speak a random quote or message, depending on whether you have an internet connection. It will then wait for 20 seconds before resetting the timer and starting again.

## Customization Variables:

The code has the following customization variables that can be modified according to your preferences:

- `DEFAULT_NON_NEURAL_VOICE`: Default voice for local TTS. Change the value to an available voice ID in your system.
- `DEFAULT_NEURAL_VOICE`: Default voice for online TTS. Change the value to an available voice from the Edge TTS API.
- `RULE_202020_TIME_IN_MINUTES`: The work time in minutes (default is 20 minutes).
- `BREAK_TIME_IN_SECONDS`: The break time in seconds (default is 20 seconds).
- `LIST_OF_MESSAGES_FOR_BREAK`: List of messages to be spoken during break time if there is no internet connection. Add or remove messages from the list as needed.

## Support & Social Links:

If you face any issues with this code or have any feedback, please feel free to reach out to me. You can create an issue on the GitHub repository.

If you find this code useful, you can show your support by sponsoring the GitHub repository. Your support will motivate me to continue creating useful tools and improving existing ones.

GitHub Sponsor Link: https://github.com/sponsors/sharadcodes
