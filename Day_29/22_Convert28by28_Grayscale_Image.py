from PIL import Image # Image module is used to handle (read,etc) the images such as File I/O

img = Image.open("digit.png")
img = img.convert("L")      # grayscale
img = img.resize((28,28))

img.save("digit_28x28.png")

print(img.size)