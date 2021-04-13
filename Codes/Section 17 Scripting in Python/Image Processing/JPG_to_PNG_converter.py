from PIL import Image
import sys
import os

# Grab the first and second arguement
existing_folder = sys.argv[1]
new_folder = sys.argv[2]

print(existing_folder)
print(new_folder)

# Check if new folder exist or not. If not, create one
if not(os.path.isdir(new_folder)):
    os.mkdir(new_folder)

print(os.path.isdir(new_folder))

# Loop through input folder, and convert images to png and save them to new folder
l = os.listdir(existing_folder)
for file in l:
    img = Image.open(f'{existing_folder}{file}')
    if(img.format != 'png'):
        split_string = file.split(".", 1)[0]
        img.save(f'{new_folder}{split_string}.png', 'png')

print(l)