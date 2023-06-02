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
        self.imgs_txt = tk.StringVar()
        self.imgs_txt.set("0 Selected")
        self.output_dir = tk.StringVar()
        self.output_dir.set("None Selected")
        self.status = tk.StringVar()
        self.status.set("Status: Ready")
        self.ratio_var = tk.StringVar()

        self.aspect_label = tk.Label(root, text = 'Aspect Ratio:')
        self.ratio_entry = tk.Entry(root,textvariable = self.ratio_var)
        self.img_sel_btn = tk.Button(root, text="Select Images", command=self.select_imgs)
        self.imgs_label = tk.Label(root, textvariable = self.imgs_txt)
        self.colour_btn = tk.Button(root, text="Set Border Colour", command=self.select_colour)
        self.colour_dsp = tk.Button(root, bg="#000000", state="disabled")
        self.dir_sel_btn = tk.Button(root, text="Select Output Directory", command=self.select_dir)
        self.dir_label = tk.Label(root, textvariable = self.output_dir)
        self.run_btn = tk.Button(root, text="Convert Images", command=self.convert_imgs)
        self.status_label = tk.Label(root, textvariable=self.status)

        self.ratio_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")
        self.aspect_label.grid(row=0, column=0, padx=5, pady=2)
        self.colour_btn.grid(row=1, column=0, padx=5, pady=2)
        self.colour_dsp.grid(row=1, column=1, padx=5, pady=2, sticky="nesw")
        self.img_sel_btn.grid(row=2, column=0, padx=5, pady=2)
        self.imgs_label.grid(row=2, column=1, padx=5, pady=2)
        self.dir_sel_btn.grid(row=3, column=0, padx=5, pady=2)
        self.dir_label.grid(row=3, column=1, padx=5, pady=2)
        self.run_btn.grid(row=4, column=0, padx=5, pady=10)
        self.status_label.grid(row=5, column=0, padx=5, pady=2)

    def select_imgs(self):
        self.imgs_lst = fd.askopenfilenames(parent=root, title="Select images", multiple=True)
        self.imgs_txt.set(f"{len(self.imgs_lst)} Selected")

    def select_dir(self):
        self.output_dir.set(fd.askdirectory(parent=root, title="Select output directory"))

    def select_colour(self):
        self.colour = askcolor(title="Select Colour")[1]
        self.colour_dsp.configure(bg=self.colour)
    
    def convert_imgs(self):
        self.status.set("Status: Processing")
        for image in self.imgs_lst:
            img = Image.open(image)
            if image.split(".")[-1].lower() == "jpg":
                img = img.convert("RGB")
            expand_img(img, float(self.ratio_var.get()), self.colour).save(self.output_dir.get() + "/" + image.split("/")[-1])

        self.status.set("Status: Completed!")


root = tk.Tk()
root.title('Image Sizer')

btnStore = BtnStore()

for row in range(5):
    root.grid_rowconfigure(row, weight=1)
for col in range(2):
    root.grid_columnconfigure(col, weight=1)

root.mainloop()