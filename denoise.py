from PIL import Image, ImageEnhance, ImageFilter
from config import *


def normalProcess(x) :
    ret = x
    ret = ImageEnhance.Contrast(ret).enhance(10)
    ret = ImageEnhance.Sharpness(ret).enhance(10)
    ret = ret.filter(ImageFilter.EDGE_ENHANCE)
    return ret

def gray(image) :
    img = image
    img = img.convert("L")
    return img

def polar(image) :
    img = image
    img = gray(img)
    height, width = img.size
    for x in range(0, height) :
        for y in range(0, width) :
            if img.getpixel((x, y)) < 128 :
                img.putpixel((x, y), 0)
            else :
                img.putpixel((x, y), 255)
    return img

def denoise(image) :
    img = image
    img = polar(img)
    height, width = img.size
    
    for times in range(0, TIMES_DENOISE) :
        data = img.getdata()
        for x in range(0, height) :
            for y in range(0, width) :
                if data[y * height + x] != 0 :
                    continue
                count = 0
                for direction in range(0, 8) :
                    _x = x + DX[direction]
                    _y = y + DY[direction]
                    if _x < 0 or _x >= height or _y < 0 or _y >= width :
                        count += 1
                        continue
                    if data[_y * height + _x] == 0 :
                        count += 1
                if count < 3 :
                    img.putpixel((x, y), 255)
    
    for times in range(0, TIMES_DENOISE) :
        data = img.getdata()
        for x in range(0, height) :
            for y in range(0, width) :
                if data[y * height + x] != 255 :
                    continue
                count = 0
                for direction in range(0, 8) :
                    _x = x + DX[direction]
                    _y = y + DY[direction]
                    if _x < 0 or _x >= height or _y < 0 or _y >= width :
                        count += 1
                        continue
                    if data[_y * height + _x] == 255 :
                        count += 1
                if count < 3 :
                    img.putpixel((x, y), 0)
    return img

if __name__ == '__main__' :
    x = Image.open('checkcode.jpg')
    x.load()
    x = denoise(x)
    x.save('c.jpg')
