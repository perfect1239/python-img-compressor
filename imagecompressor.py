from tkinter.filedialog import askopenfilename

import PIL
from PIL import Image

file_path = askopenfilename()
img = PIL.Image.open(file_path)

myWidth, myHeight = img.size

img = img.resize((myWidth, myHeight), PIL.Image.LANCZOS)

save_path = askopenfilename()


img.save(save_path + "_compressed.jpg")
