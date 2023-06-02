from PIL import Image, ImageOps
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.colorchooser import askcolor


def expand_img(img, aspect_ratio, colour_hex):
    if (int(img.width * aspect_ratio) - img.height) < (int(img.height * aspect_ratio) - img.width):
        if (int(img.width * aspect_ratio) - img.height) < 0:
            return ImageOps.expand(img,border=(int(((img.height / aspect_ratio) - img.width) / 2), 0), fill=colour_hex)
        else:
            return ImageOps.expand(img,border=(0, int(((img.width * aspect_ratio) - img.height) / 2)), fill=colour_hex)
    else:
        if  (int(img.height * aspect_ratio) - img.width) < 0:
            return ImageOps.expand(img,border=(0, int(((img.width / aspect_ratio) - img.height) / 2)), fill=colour_hex)
        else:
            return ImageOps.expand(img,border=(int(((img.height * aspect_ratio) - img.width) / 2), 0), fill=colour_hex)

class BtnStore:
    def __init__(self):
        self.colour = "#000000"
        self.imgs_lst = ()
        self.output_dir = ""
        self.ratio_var = tk.StringVar()

        self.aspect_label = tk.Label(root, text = 'Aspect Ratio:')
        self.ratio_entry = tk.Entry(root,textvariable = self.ratio_var)
        self.img_sel_btn = tk.Button(root, text="Select Images", command=self.select_imgs)
        self.colour_btn = tk.Button(root, text="Set Border Colour", command=self.select_colour)
        self.colour_dsp = tk.Button(root, bg="#000000", state="disabled")
        self.dir_sel_btn = tk.Button(root, text="Select Output Directory", command=self.select_dir)
        self.run_btn = tk.Button(root, text="Convert Images", command=self.convert_imgs)

        self.ratio_entry.grid(row=0, column=1)
        self.aspect_label.grid(row=0, column=0)
        self.colour_btn.grid(row=1, column=1)
        self.colour_dsp.grid(row=1, column=2, padx=5)
        self.img_sel_btn.grid(row=2, column=1)
        self.dir_sel_btn.grid(row=3, column=1)
        self.run_btn.grid(row=4, column=1)

    def select_imgs(self):
        self.imgs_lst = fd.askopenfilenames(parent=root, title="Select images", multiple=True)

    def select_dir(self):
        self.output_dir = fd.askdirectory(parent=root, title="Select output directory")

    def select_colour(self):
        self.colour = askcolor(title="Select Colour")[1]
        self.colour_dsp.configure(bg=self.colour)
    
    def convert_imgs(self):
        for image in self.imgs_lst:
            img = Image.open(image)
            if image.split(".")[-1].lower() == "jpg":
                img = img.convert("RGB")
            expand_img(img, float(self.ratio_var.get()), self.colour).save(self.output_dir + "/" + image.split("/")[-1])
            print("Saved as: " + self.output_dir + "/" + image.split("/")[-1])


root = tk.Tk()
root.title('Image Sizer')
root.geometry('300x150')
root["bg"] = "#ffffff"

btnStore = BtnStore()

root.mainloop()