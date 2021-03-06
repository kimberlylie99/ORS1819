
# Testing file
from PIL import ImageDraw, Image, ImageFont
#import wiringPi
import epd7in5
#import imagedata
import epdif
#import bcm2835
import epdif
import RPi.GPIO as GPIO
import spidev
import time
import os
import sys
#import string

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

def next_page(d, file):
    x = len(file);
    newfile = file[0:x-5]+'2.bmp'
    return newfile

def main():
    epd = epd7in5.EPD()
    epd.init()

    image = Image.new('1',(EPD_WIDTH,EPD_HEIGHT),1)
    draw = ImageDraw.Draw(image)
    font_path = 
    draw.rectangle((0, 6, 640, 30), fill = 0)
    draw.text((200, 10), 'e-Paper demo', font = font, fill = 255)
    draw.rectangle((200, 80, 600, 280), fill = 0)
    draw.arc((240, 120, 580, 220), 0, 360, fill = 255)
    draw.rectangle((0, 80, 160, 280), fill = 255)
    draw.arc((40, 80, 180, 220), 0, 360, fill = 0)
    epd.display_frame(epd.get_frame_buffer(image))

    ##implementing dictionary##
    ## idea: whenever user drops a file, automatically add file into diction and update for user

    #name = input('Enter File Name: ')
    #pages = input('Enter Number of Pages: ')

    #file = 'GT logo.bmp'
    #im = Image.open(file)
    #epd.display_frame(epd.get_frame_buffer(im))

    #file = 'TheHelpConversion.txt'

    #test = True
    #change = 0
    #while test:
        #change = input('Press 1 to change')
        #if change = 1
            #test = False
            #im = Image.open(file)
            #epd.display_frame(epd.get_frame_buffer(im))

    image = Image.new('1', (640, 384), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    newfile = open("TheHelpConversion.txt","rb")
    j = 0
    i = 0 # what line to read from file
    tfont = ImageFont.truetype(font_path, 20)
    n = 1
    all_lines = newfile.readlines()
    numLines = len(all_lines)

    while True:
        while i < 30*n:
            line = all_lines[i]
            print(line)
            # change fill and font
            draw.text((0, j), line, tfont, fill = (255,255,255,255)
            j= j + 12.5
            if i+1 <= numLines:
                i = i+1
        epd.display_frame(epd.get_frame_buffer(image))
        change = 0
        while change != 1 and change != 2:
            change = input("Press 1 to go forward or 2 to go backward: ")
            j = 0
        if change == 1: #updated
            #print("in 1 statement")
            if i != numLines:
                n = n + 1
        elif change == 2: #updated
            if n != 1: #updated
                n = n - 1 #updated
                i = i - 60 #updated
            else:
                i = 0

        image = Image.new('1', (640, 384), 255) # 255: clear the frame
        draw = ImageDraw.Draw(image)

    #if userInput == 'YES' or userInput == 'Y':
    #     file = next_page(d,file)
    #     d = d+1
    #     im = Image.open(file)
    #     epd.display_frame(epd.get_frame_buffer(im))
    #im.rotate(45).show()

if __name__ == '__main__':
    main()
### END OF FILE ###
