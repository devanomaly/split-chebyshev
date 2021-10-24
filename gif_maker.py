import os, glob
from PIL import Image

def get_key(fp):
    filename = os.path.splitext(os.path.basename(fp))[0]
    numeric = filename.split("=")[-1]
    return int(numeric)
  
def make_gif(frame_folder, file_name):
    resultados_glob = sorted(glob.glob("*.png"), key=get_key)
    for resultado in resultados_glob:
        print(resultado)
    frames = [Image.open(image) for image in resultados_glob]
    frame_one = frames[0]
    print(len(frames))
    frame_one.save(str(file_name)+".gif", format="GIF", append_images=frames,save_all=True, duration=50, loop=0)

if __name__ == "__main__":
    make_gif("/path/to/images", "babinet?")
