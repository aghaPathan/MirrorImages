import os
import cv2
from PIL import Image
from PIL import ImageOps



class Mirror():
    """ This module will create mirror image of an image in that same Directory, [file-wise and folder-wise].
        as instructed. if there is an extension problem, feel free to update constructor self.extensions 
        with repect to the library PIL.Image supports """
    
    def __init__(self):
        self.extensions = ['.jpeg','.png','.jpg','.bmp']
        
    def MirrorFolder(self,folderPath):
        
        # getting directory path
        self.folderPath = os.path.dirname(folderPath)
        # changing working directory
        os.chdir(self.folderPath)
        for File in os.listdir(self.folderPath):
            self.pathToFile = File
            # getting filename and it's extension
            self.filename, self.file_extension = os.path.splitext(File)
            # checking extension
            if self.file_extension in self.extensions:
                self.mirroring()
        print('Mirrored')
    
    def MirrorFile(self,filePath):
        
        # getting file path
        self.pathToFile = filePath
        # getting directory path
        self.folderPath = os.path.dirname(filePath)
        # changing working directory
        os.chdir(self.folderPath)
        # getting filename and it's extension
        self.filename, self.file_extension = os.path.splitext(filePath)
        # checking extension
        if self.file_extension in self.extensions:
            self.mirroring()
            print('Mirrored')
        else:
            print('check class constructor for update extensions')
        
    def mirroring(self):

        # creating mirror file's name
        mirrorFilename = self.filename+' (mirror)'+self.file_extension
        # creating mirror file Path
        mirrorFilePath =  os.path.join(self.folderPath,mirrorFilename)
        # Loading original Image
        img = Image.open(self.pathToFile)
        # Mirroring original Image
        mirror_img = ImageOps.mirror(img)
        # Saving Mirrored Image
        mirror_img.save(mirrorFilePath)
