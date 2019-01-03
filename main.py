# Testing file
from PIL import ImageDraw, Image, ImageFont
#import wiringPi
import epd7in5
#import imagedata
#import epdif
#import bcm2835
import epdif
import RPi.GPIO as GPIO
import spidev
import time
import os
import sys

# defining the size of the ereader
EPD_WIDTH = 640
EPD_HEIGHT = 384

# PIN definitions
CS_PIN = 8
RST_PIN = 17
BUSY_PIN = 24
DC_PIN = 25

# SPI device, bus = 0, device = 0
SPI = spidev.SpiDev(0,0)

EPD_WIDTH = 640
EPD_HEIGHT = 384

def main():
    epd = epd7in5.EPD()
    epd.init()
    
    image = Image.new('1',(EPD_WIDTH,EPD_HEIGHT),1)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
    draw.rectangle((0, 6, 640, 30), fill = 0)
    draw.text((200, 10), 'e-Paper demo', font = font, fill = 255)
    draw.rectangle((200, 80, 600, 280), fill = 0)
    draw.arc((240, 120, 580, 220), 0, 360, fill = 255)
    draw.rectangle((0, 80, 160, 280), fill = 255)
    draw.arc((40, 80, 180, 220), 0, 360, fill = 0)
    epd.display_frame(epd.get_frame_buffer(image))
    
    #epd.display_frame(imagedata.MONOCOLOR_BITMAP)
    im = Image.open('city.bmp')
    epd.display_frame(epd.get_frame_buffer(im))
    #im.rotate(45).show()

if __name__ == '__main__':
    main()
### END OF FILE ###