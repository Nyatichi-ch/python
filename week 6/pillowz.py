from PIL import Image, ImageFilter, ImageDraw, ImageFont

#open an image file
img = Image.open('example.jpg')
print(img.format, img.size, img.mode)

#image resize
img_resized = img.resize((200, 200))
print(img_resized.size)
img_resized.save('resized_example.jpg')
#display the resized image
img_resized.show()

#image rotate
img_rotated = img.rotate(45)
img_rotated.save('rotated_example.jpg')
img_rotated.show()

#apply filter
img_filtered = img.filter(ImageFilter.BLUR)
img_filtered.save('blurred_example.jpg')
img_filtered.show()