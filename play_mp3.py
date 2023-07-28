"""
CircuitPython I2S MP3 playback example.
Plays a single MP3 once.
"""
import board
import audiomp3
import audiobusio
import digitalio
import time

audio = audiobusio.I2SOut(board.GP0, board.GP1, board.GP2)

button1 = digitalio.DigitalInOut(board.GP15)
button1.switch_to_input(pull=digitalio.Pull.UP)

button2 = digitalio.DigitalInOut(board.GP14)
button2.switch_to_input(pull=digitalio.Pull.UP)

mp3 = audiomp3.MP3Decoder(open("felicita.mp3", "rb"))

while True:
    if not button1.value:
        audio.play(mp3)
        while audio.playing:
            time.sleep(0.2)
            if not button2.value:
                audio.pause()
                while True:
                    time.sleep(0.2)
                    if not button2.value:
                        audio.resume()
                        break

print("Done playing!")
