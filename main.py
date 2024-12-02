from write_script import write_content,get_content,get_title
from voice_gen import voice_main, split_words,create_folder_if_not_exists
from image_gen import image_main
from video_creation import video_main
from pathlib import Path
import sys 
import time 

my_file = Path("font.ttf")
if not my_file.is_file():
    print("font.ttf is missing. Please add it to the same directory (any font named as font.ttf)")
    print("QUITTING in 5 Seconds")
    time.sleep(5)
    sys.exit()
create_folder_if_not_exists('./outputs')


print("*"*25+" CONTENT GENERATION " + "*"*25)
write_content(get_content(get_title()))
print("Check your content in text.txt")
print("Some Tips: \n 1. Space your Abbreviations eg: AI -> A I. So that TTS models dont get confused. \n 2. Add initial hook or thanks at end")

print("*"*25+" TTS " + "*"*25)
print("Make sure the TTS model is online at http://127.0.0.1:7860/")
tts = input("Need to do TTS? (y/n)")
print("Proceeding to next step!")
if tts == "y":
    voice_main()
    print("Check voices folder and line_by_line.txt to check if everything is fine.")
else:
    split_words()
    print("Check line_by_line.txt")
    print("Enter each line in any TTS model and save the audio from part0 to partn")
c2 = input("Enter any to move on to next one")

print("*"*25+" Image Generation " + "*"*25)
image_main()
print("Check images folder")
c3 = input("Enter any key to proceed to next")

print("*"*25+" Video Creation " + "*"*25)
video_main()
print("Your video is saved in youtube_short.mp4")