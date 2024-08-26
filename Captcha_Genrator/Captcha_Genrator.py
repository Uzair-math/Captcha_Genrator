from io import BytesIO
from tkinter import *
from random import *
from tkinter import messagebox
from captcha.image import ImageCaptcha
import string
from PIL import ImageFont

# Simplified font paths
fonts = [
    r'E:\python\Mini-Project\Captcha_Genrator\fonts\ChelseaMarketsr.ttf', 
    r'E:\python\Mini-Project\Captcha_Genrator\fonts\DejaVuSanssr.ttf'
]

# Verify font loading
try:
    for font_path in fonts:
        ImageFont.truetype(font_path, size=40)
    print("Fonts loaded successfully")
except OSError as e:
    print(f"Failed to load font: {e}")
    exit(1)

# Generate initial captcha
image = ImageCaptcha(fonts=fonts)
random = str(randint(100000, 999999))
data = image.generate(random)
assert isinstance(data, BytesIO)
image.write(random, 'out.png')

def verify():
    global random
    x = t1.get("0.0", END)
    if int(x.strip()) == int(random):
        messagebox.showinfo("success", "verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

def refresh():
    global random, captcha_image
    random = str(randint(100000, 999999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random, 'out.png')
    
    # Update captcha image
    captcha_image = PhotoImage(file='out.png')
    l1.config(image=captcha_image, height=100, width=200)
    l1.update()

root = Tk()
captcha_image = PhotoImage(file="out.png")

l1 = Label(root, image=captcha_image, height=100, width=200)
t1 = Text(root, height=5, width=50)
b1 = Button(root, text="submit", command=verify)
b2 = Button(root, text="refresh", command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()
