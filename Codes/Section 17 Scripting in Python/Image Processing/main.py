from PIL import Image, ImageFilter

img = Image.open('./Images/bulbasaur.jpg')

# tells image format
print(img.format)

print(img.size)

print(img.mode)

print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", 'png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png", 'png')

filtered_img = img.convert('L')
filtered_img.save("blackwhite.png", 'png')

#filtered_img.show()
# rotate image
filtered_img = img.rotate(90)
filtered_img.save("rotated.png", 'png')

resized_img = img.resize((200,200))
resized_img.save("resizedimg.png", "png")

# Cropping an Image
box = (100, 100, 200, 200)
region = img.crop(box)
region.show()

# Downsample image
img = Image.open('./Images/astro.jpg')
print(img.size)
img.thumbnail((400,200))
img.save("thumbnail.jpg")
# thumbnail keeps the aspect ratio
