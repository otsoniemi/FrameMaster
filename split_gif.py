from PIL import Image
import os

def split_gif(gif_path, output_folder):
    if os.path.isfile(gif_path):
        gif = Image.open(gif_path)
        try:
            while True:
                gif.seek(gif.tell()+1)
                frame = gif.copy()
                frame.save(os.path.join(output_folder, f"frame{gif.tell()}.png"))
        except EOFError:
            pass
    else:
        print(f"File {gif_path} doesn't exist.")