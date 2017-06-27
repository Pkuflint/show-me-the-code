#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 任务是将一个图片右上角添加上一个红色数字4
from PIL import Image, ImageDraw, ImageFont

im = Image.open('images.jpg')

draw = ImageDraw.Draw(im)

# 通过 ls -R /Library/Fonts | grep ttf 获取系统字体
font = ImageFont.truetype('Times New Roman Bold.ttf', 30)

# 数字的位置设置在右上角，即宽度4/5位置和高度1/5位置
draw.text((im.width * 4 / 5, im.height * 1 /5), '4', font = font, fill = 'red')

im.save('new_photo.jpg', 'JPEG')