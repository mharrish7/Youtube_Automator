# Todo: Add Frontend web preferrably. To add more customization such as resolution, etc.. 
from moviepy import *

target_width = 540
target_height = 960

# Background
baseLayer = ColorClip((1080,1920), color=(0,0,0))

font = "font.ttf"

# Create text clips
def create_text(text,duration):
    words = text.split(' ')
    cur = 0
    cur_line = ""
    for i in words:
        cur_line += i + " "
        cur += 1 
        if cur > 3:
            cur_line += "\n"
            cur = 0
    text1 = TextClip(font=font, text= cur_line, font_size=60, color='white',stroke_color="black",stroke_width = 2)
    text1 = text1.with_duration(duration)
    text1 = text1.with_position(('center', 1200)).with_effects(
        [vfx.CrossFadeIn(0.2), vfx.CrossFadeOut(0.2), vfx.Resize(zoom_in)])
    return text1

def create_image_clip(image,duration):
    imageLayer = ImageClip(image).resized(width=1280).with_duration(duration + 0.5).with_position(("center","center"))
    imageLayer = imageLayer.with_effects([vfx.Resize(zoom_in_image)])
    return imageLayer


prev_t = 0
def zoom_in(t):
    global prev_t
    if t < 0.5:
        prev_t = t + 0.4
        return t + 0.4
    else:
        return prev_t

def zoom_in_image(t):
    return 1.5 + t*0.1


def video_main():
    global baseLayer
    line_by_line = open("./outputs/line_by_line.txt")
    videos = []
    content = line_by_line.read().split("\n")
    part = 0
    for text in content:
        if text == "":
            break
        fname = f'./outputs/audio/part{part}.wav'
        audioclip = AudioFileClip(fname)
        image_path = f"./outputs/images/part{part}.jpg"
        imageLayer = create_image_clip(image_path, audioclip.duration)
        text1 = create_text(text,audioclip.duration)
        baseLayer = baseLayer.with_duration(audioclip.duration)
        video1 = CompositeVideoClip([baseLayer, imageLayer, text1]).with_audio(audioclip)
        videos.append(video1)
        part += 1

    final_clip = concatenate_videoclips(videos)
    final_clip.write_videofile("./outputs/youtube_short.mp4", fps=30, audio=True)


if __name__ == "__main__":
    video_main()