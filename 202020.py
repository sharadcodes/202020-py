import random
import time
import os
import socket
import requests
import asyncio
import edge_tts
import winsound
import pyttsx3
from pydub import AudioSegment

# Initialize the TTS engine for local TTS
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Change it according to your preference
DEFAULT_NON_NEURAL_VOICE = voices[1].id
# Set the voice and the rate of the TTS engine
engine.setProperty('voice', DEFAULT_NON_NEURAL_VOICE)
engine.setProperty('rate', 160)


# Set the time for the 20-20-20 rule in seconds
# 20 x 60 = 1200 seconds = 20 minutes work time
RULE_202020_TIME_IN_MINUTES = 20 * 60
BREAK_TIME_IN_SECONDS = 20  # 20 seconds break
# Set the timer to the work time
timer = RULE_202020_TIME_IN_MINUTES  # Set the timer to the work time

# Set the default voice for online TTS using Edge TTS
DEFAULT_NEURAL_VOICE = "en-US-AriaNeural"


def is_connected():
    """
    Check if there is internet connection
    args: None
    returns: True if there is internet connection, False otherwise
    """
    try:
        # Connect to the host (can be any host, but google works well)
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


# List of messages to speak & show when there is no internet connection
LIST_OF_MESSAGES_FOR_BREAK = [
    "Take a break, go grab some coffee and come back stronger!",
    "Your eyes are important, give them a break and take a walk",
    "Stand up, shake it off, and take a few deep breaths!",
    "20 seconds of eyes closed = 20 minutes of fresh eyes",
    "It's time to rest and recharge for the next session",
    "Stretch your legs, your neck and your brain!",
    "Step away from the screen, go grab a snack and come back refreshed",
    "Take a break, it's a marathon not a sprint"
]


async def tts(text):
    """
    Use the Edge TTS API to speak the text
    args: text to speak
    returns: None
    """
    if is_connected():
        voice = DEFAULT_NEURAL_VOICE
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save("tts.mp3")
        song = AudioSegment.from_mp3("tts.mp3")
        song.export('tts.wav', format='wav')
        winsound.PlaySound("tts.wav", winsound.SND_FILENAME)
    else:
        engine.say(text)
        engine.runAndWait()


async def get_random_quote():
    """
    Retrieve a random quote from the ZenQuotes API
    args: None
    returns: a tuple containing the quote text and author
    """
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"]
    return quote, author


async def main():
    """
    Main function
    args: None
    returns: None
    """
    global timer
    while True:
        if timer == 0:
            # Clear the screen
            os.system("cls")
            if is_connected():
                # Get a random quote from the ZenQuotes API
                quote, author = await get_random_quote()
                print("It's time for a break. Here is a quote for you:\n")
                await tts("It's time for a break. Here is a quote for you:")
                print(f"{author} ....... once said & I quote ........\n\n{quote}")
                await tts(f"{author} once said and I quote. {quote}")
            else:
                # Get a random message from the list
                message = random.choice(LIST_OF_MESSAGES_FOR_BREAK)
                print(message)
                await tts(message)

            # Wait for the break time to finish
            time.sleep(BREAK_TIME_IN_SECONDS)
            # Reset the timer
            timer = RULE_202020_TIME_IN_MINUTES
            # Clear the screen
            os.system("cls")
            print("Your break is over, let's get back to work!")
            await tts("Your break is over, let's get back to work!")
        else:
            # Clear the screen
            os.system("cls")
            # Show the time left in minutes and seconds
            print(f"Time left: {timer // 60} minutes and {timer % 60} seconds")
            timer -= 1
            time.sleep(1)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
