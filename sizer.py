from PIL import Image, ImageOps

aspect_ratio = 4/8

img_path = "test.png"
img = Image.open(img_path)

if aspect_ratio < 1:
    aspect_ratio = (1 / aspect_ratio)

if (int(img.width * aspect_ratio) - img.height) < (int(img.height * aspect_ratio) - img.width):
    img_with_border = ImageOps.expand(img,border=(0, int(((img.width * aspect_ratio) - img.height) / 2)),fill='#ffffff')
else:
    img_with_border = ImageOps.expand(img,border=(int(((img.height * aspect_ratio) - img.width) / 2), 0),fill='#ffffff')


img_with_border.save('image-with-border.png')