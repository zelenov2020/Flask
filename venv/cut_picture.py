from PIL import Image

img = Image.open('image.png')
r0, g0, b0 = img.getpixel((0, 0))
x1 = 0
y1 = 0
x, y = img.size
x0 = x
y0 = y
for i in range(x):
    for j in range(y):
        r, g, b = img.getpixel((i, j))
        if r != r0 or g != g0 or b != b0:
            if i > x1:
                x1 = i
            if i < x0:
                x0 = i
            if j > y1:
                y1 = j
            if j < y0:
                y0 = j
img2 = img.crop((x0, y0, x1 + 1, y1 + 1))
img2.save('res.png')

