from PIL import Image
import numpy


class IMGToASCII():
    
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path).convert("L")
        
        self.sr = int(input("Enter the size in Px that a character will represent:   "))#scaled resolution (pixels per character)
        self.ccr = " .:+=£#@"#input("Enter the string of characters that will represent the greyscale (light to dark):   ")
                             #character colour representation (string of characters to represent greyscale)
        self.out_file = "ASCIIOUT.txt"#input("Enter the path to the output file:   ")
        self.out_string = ""

        self.width, self.height = self.image.size
        self.width -= self.width % self.sr#Trimming image to make it easier to process
        self.height -= self.height % (self.sr * 2)#SR * 2 as this gives the best output in notepad
        
        self.pixel_sequence = numpy.array(self.image)
        self.scaled_sequence = []

        self.convert()

    def scale(self):
        for y in range(0, self.height, self.sr * 2):
            row = []
            
            for x in range(0, self.width, self.sr):
                row.append(self.pixel_sequence[y][x])
            
            self.scaled_sequence.append(row)    

    def invert(self):
        for y in range(len(self.scaled_sequence)):
            for x in range(len(self.scaled_sequence[y])):
                self.scaled_sequence[y][x] = 256 - self.scaled_sequence[y][x]

    def translate(self):
        x = 256 / (len(self.ccr) - 1)
        for row in self.scaled_sequence:
            for px in row:
                character = self.ccr[int(px / x)]
                self.out_string += character
            self.out_string += "\n"

    def write(self):
        with open(self.out_file, "w", encoding = "utf-8") as file:
            file.write(self.out_string)        

    def convert(self):
        print("\nScaling image...")
        self.scale()
        print("Done!")

        print("\nInverting colours...")
        self.invert()
        print("Done!")

        print("\nTranslating to ASCII...")
        self.translate()
        print("Done!")

        print("\nWriting translated image to text file...")
        self.write()

        print("\nProcess complete!\nLook in {} for converted image".format(self.out_file))
