from PIL import Image
import numpy as np
from moviepy.editor import ImageSequenceClip
import os

def combine_frames(input_folder, output_folder, output_format, fps_amount):
    png_files = [f for f in os.listdir(input_folder) if f.endswith(".png")]
    png_files.sort(key=lambda x: int(x.split(".")[0].split("frame")[1]))
    frames = []
    for file_name in png_files:
        frame = Image.open(os.path.join(input_folder, file_name))
        frame = np.array(frame)
        frames.append(frame)
    if output_format == "gif":
        output_path = os.path.join(output_folder,'output.gif')
        clip = ImageSequenceClip(frames, fps=fps_amount)
        clip.write_gif(output_path)
    elif output_format == "mp4":
        output_path = os.path.join(output_folder,'output.mp4')
        clip = ImageSequenceClip(frames, fps=fps_amount)
        clip.write_videofile(output_path)
    else:
        print("Invalid output format")

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"
    output_format = "gif"
    fps_amount = "24"
    combine_frames(input_folder, output_folder, output_format)
