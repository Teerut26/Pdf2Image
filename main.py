from pdf2image import convert_from_path
from os import path
import os

scale = 1

class Pdf2Image:
    def __init__(self, inputsPath, outputsPath, filePath):
        self.outputsPath = outputsPath
        self.filePath = filePath
        self.inputsPath = inputsPath
        self.images = convert_from_path(f"{inputsPath}/{filePath}", size=1000 * scale,
                                        poppler_path=r'C:\poppler-0.67.0\bin')

    def main(self):
        if (not path.exists(f"{self.outputsPath}/{self.filePath.split('.')[0]}")):
            os.mkdir(f"{self.outputsPath}/{self.filePath.split('.')[0]}")
            print(f"*****{self.filePath.split('.')[0]}*****")
            for i in range(len(self.images)):
                self.saveImage(self.images[i], f"{self.outputsPath}/{self.filePath.split('.')[0]}/page_{i}.png")

    def saveImage(self, images, path):
        images.save(path, 'PNG')
        print(f"✔ {path}")


class CheckPath:
    def __init__(self):
        self.inputsPath = "inputs"
        self.outputsPath = "outputs"
        self.__main__()

    def __main__(self):
        if (not path.exists(self.inputsPath)):
            os.mkdir(self.inputsPath)
            print(f"[✔] {self.inputsPath} Created.")
            print("[Init] Please run progran again.")
            return

        if (not path.exists(self.outputsPath)):
            os.mkdir(self.outputsPath)
            print(f"[✔] {self.outputsPath} Created.")

        inputFiles = next(os.walk(self.inputsPath))[2]
        outputFiles = next(os.walk(self.outputsPath))[2]

        if (len(inputFiles) == 0): print("[❌] File inputs is null.")

        for inputFile in inputFiles:
            pdf2Image = Pdf2Image(self.inputsPath, self.outputsPath, inputFile)
            pdf2Image.main()



if __name__ == '__main__':
    CheckPath()
