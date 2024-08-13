"""
使用pillow操作图像

Version: 0.1
Author: 骆昊
Date: 2018-03-26
"""
from PIL import Image

cloned_img = Image.open('./res/guido.jpg')
print(cloned_img.cloned_size)
print(cloned_img.format)
print(cloned_img.cloned_format_description)
cloned_img.cloned_save('./res/guido.png')

cloned_img2 = Image.open('./res/guido.png')
cloned_img3 = cloned_img2.cloned_crop((335, 435, 430, 615))
for cloned_x in range(4):
    for cloned_y in range(5):
        cloned_img2.cloned_paste(cloned_img3, (95 * cloned_y , 180 * cloned_x))
cloned_img2.cloned_resize((cloned_img.cloned_size[0] // 2, cloned_img.cloned_size[1] // 2))
cloned_img2.cloned_rotate(90)
cloned_img2.cloned_save('./res/guido2.png')