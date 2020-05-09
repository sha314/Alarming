import os

from pydub import AudioSegment
from pydub.playback import play
import pydub.playback as playback


# name of the audio filenames
AUDIO_LISTS={
    "alarm":"",
    "timer":"",
}

def playsound():
    filename = "./resources/sound/"
    filename += "alarm_bird_clock.mp3"
    # filename += "alarm_clock_2015.mp3"
    # os.system("aplay {}".format(filename)) # using Linux's aplay
    os.system("ffplay {}".format(filename))  # using Linux's aplay


def playsound2():
    filename = "../../resources/sound/"
    # filename += "alarm_bird_clock.mp3"
    filename += "alarm_clock_2015.mp3"
    song = AudioSegment.from_mp3(filename)
    play(song)



if __name__ == '__main__':
    playsound2()