import os, glob
from PIL import Image

def get_key(fp):
    filename = os.path.splitext(os.path.basename(fp))[0]
    numeric = filename.split("=")[-1]
    return int(numeric)
  
def make_gif(file_name):
    resultados_glob = sorted(glob.glob("*.png"), key=get_key)
    for resultado in resultados_glob:
        print(resultado)
    frames = [Image.open(image) for image in resultados_glob]
    frame_one = frames[0]
    print(len(frames))
    frame_one.save(str(file_name)+".gif", format="GIF", append_images=frames,save_all=True, duration=50, loop=0)
