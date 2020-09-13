import os
import shutil

from pathlib import Path
from Utilities.simpleScanner.extensionMapper import extensionsToFolder


class SimpleScanner:
    def __init__(self):
        self.extensionsToFolder = extensionsToFolder
        self.inputPath = None
        self.outputPath = None

    @staticmethod
    def __isValidDir(path):
        return os.path.isdir(path)

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
    def __checkAndMove(sourceFile, destination):
        try:
            _ = shutil.move(sourceFile, destination, copy_function=shutil.copytree)
            return 1
        except shutil.Error:
            return 0

    def __moveFilesToTargetFolders(self, rootFiles):
        status = {"Moved": [], "NotMoved": []}

        # iterate in rootFiles
        for file in rootFiles:
            fileExtension = self.__getFileExtension(file)
            if fileExtension in extensionsToFolder:
                folderType = extensionsToFolder[fileExtension]
                completeFolderPath = os.path.join(self.outputPath, folderType)

                if not os.path.exists(completeFolderPath):
                    os.makedirs(completeFolderPath)

                isMoved = self.__checkAndMove(file, completeFolderPath)
                if isMoved:
                    status["Moved"].append(os.path.basename(file))
                else:
                    status["NotMoved"].append(os.path.basename(file))

        return status

    def readDirectory(self, inputPath, outputPath=None):
        """
        :type outputPath: string
        :type inputPath: string
        """
        errorInputPath = "The specified input directory doesn't exist."
        errorOutputPath = "The specified output directory doesn't exist."

        assert self.__isValidDir(inputPath), errorInputPath
        if outputPath is not None:
            assert self.__isValidDir(outputPath), errorOutputPath

        self.inputPath = inputPath
        if (self.outputPath is None) and (outputPath is None):
            self.outputPath = inputPath
        elif outputPath is not None:
            self.outputPath = outputPath

        # print(self.inputPath, inputPath, outputPath)

        #  read input files
        rootFiles = self.__readRootFiles(self.inputPath)

        # move files to targets
        transferStatusDict = self.__moveFilesToTargetFolders(rootFiles)
        return transferStatusDict

    def setOutputPath(self, outputPath):
        error = "The specified output directory doesn't exist."
        assert self.__isValidDir(outputPath), error
        self.outputPath = outputPath
