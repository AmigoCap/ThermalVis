#!/usr/bin/python

#from Adafruit_Thermal import *
#from printImage import *
#from timetemp import *
from PrinterProject_book_recommend import recommand_book
from PrinterProject_book_recommend import gray_Scale

def Text():
    printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
    # Test inverse on & off
    printer.inverseOn()
    printer.println("Inverse ON")
    printer.inverseOff()
    # Test character double-height on & off
    printer.doubleHeightOn()
    printer.println("Double Height ON")
    printer.doubleHeightOff()
    # Set justification (right, center, left) -- accepts 'L', 'C', 'R'
    printer.justify('R')
    printer.println("Right justified")
    printer.justify('C')
    printer.println("Center justified")
    printer.justify('L')
    printer.println("Left justified")
    # Test more styles
    printer.boldOn()
    printer.println("Bold text")
    printer.boldOff()
    printer.underlineOn()
    printer.println("Underlined text")
    printer.underlineOff()
    printer.setSize('L')   # Set type size, accepts 'S', 'M', 'L'
    printer.println("Large")
    printer.setSize('M')
    printer.println("Medium")
    printer.setSize('S')
    printer.println("Small")
    printer.justify('C')
    printer.println("normal\nline\nspacing")
    printer.setLineHeight(50)
    printer.println("Taller\nline\nspacing")
    printer.setLineHeight() # Reset to default
    printer.justify('L')
    # Barcode examples
    printer.feed(1)
    # CODE39 is the most common alphanumeric barcode
    printer.printBarcode("ADAFRUT", printer.CODE39)
    printer.setBarcodeHeight(100)
    # Print UPC line on product barcodes
    printer.printBarcode("123456789123", printer.UPC_A)

  
    printer.sleep()      # Tell printer to sleep
    printer.wake()       # Call wake() before printing again, even if reset
    printer.setDefault() # Restore printer to defaults

if __name__ == '__main__':
    #printImage()
    #timetemp()
    #Text()
    recommended_book, recommanded_theme_of_recommanded_book = recommand_book()
    print(recommended_book)
    print(recommanded_theme_of_recommanded_book)
    imgGray = gray_Scale("images/piechart")
    

