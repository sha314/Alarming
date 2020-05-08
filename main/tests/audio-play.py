import os

from pydub import AudioSegment
from pydub.playback import play


# name of the audio filenames
AUDIO_LISTS={
    "alarm":"",
    "timer":"",
}

def playsound():
    filename = "./resources/sound/"
    filename += "sonicscrewdriver.mp3"
    # os.system("aplay {}".format(filename)) # using Linux's aplay
    os.system("ffplay {}".format(filename))  # using Linux's aplay


def playsound2():
    filename = "./resources/sound/"
    filename += "sonicscrewdriver.mp3"
    song = AudioSegment.from_mp3(filename)
    play(song)



if __name__ == '__main__':
    playsound2()