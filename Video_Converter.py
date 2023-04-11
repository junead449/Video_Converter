import moviepy.editor
from tkinter.filedialog import *

vid=askopenfilename()
# Place File direct Path at vid as Optional
video=moviepy.editor.VideoFileClip(vid)

aud=video.audio
aud.write_audiofile("Chaudhary_Converted_File.mp3")

print("----Your File is converted---- Completely ")
