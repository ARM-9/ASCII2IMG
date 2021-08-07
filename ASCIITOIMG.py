from PIL import Image
import numpy


class ASCIIToIMG():

    def __init__(self, file_path = "ASCIIOUT.txt"):
        self.image_path = file_path
        self.line_list = []

        self.ccr = " .:+=£#@"#input("Enter the string of characters that will represent the greyscale( light to dark):   ")
                             #colour character representation
        self.cgsr = {}#character greyscale representation
        self.init_cgsr()

        self.image_matrix = None
        self.image = None

        self.output_path = "Output.png"

        self.convert()

    def init_cgsr(self):
        for i, char in enumerate(self.ccr):
            self.cgsr[char] = 255 - int( ( ( ( ( i / len(self.ccr) ) * 255 ) ) +
                                     ( ( ( (i + 1) / len(self.ccr) ) * 255 ) ) ) / 2  )

    def init_line_list(self):
        with open(self.image_path, "r", encoding = "utf-8") as file:
            lines = file.readlines()
                  
        for i, line in enumerate(lines):
            lines[i] = line.strip("\n")
            self.line_list.append(list(lines[i]))
            self.line_list.append(list(lines[i]))#Doubling each line to compensate for halving height in ASCIIOUT.txt 

    def translate(self):
        for y, line in enumerate(self.line_list):
            for x, pixel in enumerate(line):
                self.line_list[y][x] = self.cgsr[pixel]

    def create(self):
        self.image_matrix = numpy.uint8(numpy.array(self.line_list))
        self.image = Image.fromarray(self.image_matrix, "L")
        self.image.save(self.output_path)

    def convert(self):
        print("\nReading file...")
        self.init_line_list()
        print("Done!")

        print("\nTranslating ASCII to grayscale...")
        self.translate()
        print("Done!")

        print("\nCreating image from grayscale data...")
        self.create()
        
        print("\nProcess complete!\nLook in {} for converted image".format(self.output_path))
