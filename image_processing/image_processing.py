from PIL import Image

img = Image.open('../static_resources/image_1.jpg')

# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))

# filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
# resized_img = filtered_img.rotate(180)
resized_img = filtered_img.resize((240, 240))

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('../static_resources/image_1_blurred.jpg')
# filtered_img.save('../static_resources/image_1_blurred.png', 'png')

# grayscale_img = img.convert('L')
# grayscale_img.save('../static_resources/image_1_grayscale.png', 'png')
