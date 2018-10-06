#!/usr/bin/python3
from xmlFunctions import readFromXML
from xmlFunctions import writeToXML
from gDriveFunctions import upload
import os
import shutil
import click
r = readFromXML()
w = writeToXML()
u = upload()
@click.group()
def cli():
    pass
@click.command()
@click.option('--path', default='invalid path', help='Path to directory')
def addDir(path):
    '''Adds a directory to  the dirList.xml file'''
    if os.path.exists(path):
        w.writeDirectory(path)
    else:
        print("Please enter a valid path")
@click.command()
@click.option('--path', default=None, help='Path to directory')
def upload(path):
    '''Uploads files to Google Drive, either from the dirList.xml or from a defined path'''
    if path is None:
        u.main()
    else:
        if os.path.exists(path):
            shutil.make_archive(path, "zip", path)
            u.uploadFile(path+".zip")
            os.remove(path+".zip")
        else:
            print("Please enter a  valid path")
cli.add_command(upload)
cli.add_command(addDir)

if __name__ == '__main__':
    cli()
