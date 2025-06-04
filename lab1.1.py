from PIL import Image
img = Image.open("laptop.jpg") 


width, height = img.size

print("Image Format :", img.format)
print("Image Width  :", width)
print("Image Height :", height)
print("Image Mode   :", img.mode)  


img.show()
