import os
import shutil

from pathlib import Path
from collections import defaultdict
from Utilities.frequencyHeap import frequencyheap


class Scanner:
    def __init__(self):
        self.inputPath = None
        self.depth = 5
        self.outputPath = None
        self.extensionsDict = defaultdict(frequencyheap.MaxFrequency)

    @staticmethod
    def __isValidDir(path):
        assert (os.path.isdir(path))

    @staticmethod
    def __getFileExtension(file):
        extension = Path(file).suffix
        if extension == '':
            extension = os.path.basename(file)

        return extension

    @staticmethod
    def __readRootFiles(inputPath):
        files = []
        for (_, _, filenames) in os.walk(inputPath):
            files.extend(filenames)
            break

        files = [os.path.join(inputPath, file) for file in files]

        return files

    @staticmethod
    def __readAddressRecursively(outputPath, depth):
        fileSeparator = os.sep
        baseDepth = len(outputPath.split(fileSeparator))
        filesList = [(root, dirs, files) for root, dirs, files, in os.walk(outputPath)]
        allFiles = []
        for file in filesList:
            fileDepth = len(file[0].split(fileSeparator))
            if (fileDepth - baseDepth > depth) or (fileDepth - baseDepth == 0):
                continue
            allFiles.append(file)

        baseFiles = []
        for level in allFiles:
            for file in level[2]:
                file = os.path.join(level[0], file)
                baseFiles.append(file)
        return baseFiles

    def __fillExtensionsDict(self, targetAddresses):
        for file in targetAddresses:
            fileExtension = self.__getFileExtension(file)
            fileAddress = os.path.dirname(file)
            self.extensionsDict[fileExtension].appendAddress(fileAddress)

    @staticmethod
    def __checkAndMove(sourceFile, destination):
        try:
            _ = shutil.move(sourceFile, destination, copy_function=shutil.copytree)
        except shutil.Error as e:
            print("{}. File NOT moved.".format(str(e)))

    def __moveFilesToTargetFolders(self, rootFiles):
        # iterate in rootFiles
        for file in rootFiles:
            fileExtension = self.__getFileExtension(file)
            destinationsList = self.extensionsDict[fileExtension].getValueList
            # check if the file ever occurred in the destination path
            if len(destinationsList) == 0:
                destination = self.outputPath
            else:
                destination = self.extensionsDict[fileExtension].getMaxOccurringAddress

            print("Moving '{}' to '{}' folder.".format(os.path.basename(file), destination))
            self.__checkAndMove(file, destination)

    def readDirectory(self, inputPath, depth=5, outputPath=None):
        """
        :type outputPath: string
        :type depth: integer
        :type inputPath: string
        """

        self.inputPath = inputPath
        self.depth = depth
        if (self.outputPath is None) and (outputPath is None):
            self.outputPath = inputPath
        else:
            self.outputPath = outputPath

        print(self.inputPath, inputPath, outputPath)

        try:
            self.__isValidDir(self.inputPath)
        except AssertionError:
            print("Invalid input Path. Please verify and try again.")
            return 0

        try:
            self.__isValidDir(self.outputPath)
        except AssertionError:
            print("Invalid output path. Please verify and try again.")
            return 0

        #  read input files
        rootFiles = self.__readRootFiles(self.inputPath)
        # print(rootFiles)

        #  read target addresses
        targetAddresses = self.__readAddressRecursively(self.outputPath, self.depth)
        # print(targetAddresses)

        #  form extensions dict from target address list
        self.__fillExtensionsDict(targetAddresses)
        # print(self.extensionsDict[".json"].getMaxOccurringAddress)

        # move files to targets
        self.__moveFilesToTargetFolders(rootFiles)

        return 1

    def setOutputPath(self, outputPath):
        try:
            self.__isValidDir(outputPath)
        except AssertionError:
            print("Invalid output path. Please verify and try again.")
        else:
            self.outputPath = outputPath
