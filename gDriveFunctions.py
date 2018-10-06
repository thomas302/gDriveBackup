from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import shutil
from xmlFunctions import readFromXML
from xmlFunctions import writeToXML
import os
#Functions used to control google drive.
class upload:
    def __init__(self):
        self.gAuth = GoogleAuth()
        self.gAuth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gAuth)
        self.w = writeToXML()
        self.r = readFromXML()
    def uploadFile(self, pathToFile):
        file1 = self.drive.CreateFile()
        file1.SetContentFile(pathToFile)
        file1['parents'] = "1WO7QKKEIL9zCqy7TGhvJSwOdRPB7Cudv"
        file1.Upload()
    def uploadFileReturnID(self, pathToFile):
        file1 = self.drive.CreateFile()
        file1.SetContentFile(pathToFile)
        file1['parents'] = "1WO7QKKEIL9zCqy7TGhvJSwOdRPB7Cudv"
        file1.Upload()
        return file1['id']
    def uploadToDriveID(self, pathToFile, driveID):
        file1 = self.drive.CreateFile()
        file1.SetContentFile(pathToFile)
        file1['parents'] = "1WO7QKKEIL9zCqy7TGhvJSwOdRPB7Cudv"
        file1['id'] = driveID
        file1.Upload() 
    def main(self):
        x = self.r.numberOfDirsInXML()
        for i in range(1,x+1):
            path = self.r.readDirectory(i)
            shutil.make_archive(path, "zip", path)
            if self.r.hasFileId(i) == "None":
                driveID = self.uploadFileReturnID(path+".zip")
                self.w.writeDriveID(i, driveID)
            else:
                driveID = self.r.readDriveID(i)
                self.uploadToDriveID(path+".zip", driveID)
            os.remove(path+".zip")

if __name__=='__main__':
    #Do test stuff
    u = upload()
    u.w.writeDirectory("/home/joel/Programing/PythonProjects/", u.r.numberOfDirsInXML())
    u.w.writeDriveID( 1,"asdf")
    u.main()
