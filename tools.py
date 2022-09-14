from ast import Str
import pickle
import os.path
from xmlrpc.client import Boolean
import openpyxl as xl
import openpyxl.worksheet.worksheet as xl

def saveObject(fileName, obj):
    with open(fileName, 'wb') as saveFile:
        pickle.dump(obj, saveFile)

def loadObject(fileName, defaultObj):
    if os.path.isfile(fileName):
        with open(fileName, 'rb') as loadFile:
            newObj = pickle.load(loadFile)
        return newObj
    return defaultObj

def getCellCode(row: int, col: int) -> Str:
    return chr(ord('A') + col) + str(row + 1)

def isColumnEmpty(sh: xl.Worksheet, col: int, startinfRow = 0) -> Boolean:
    for r in range(startinfRow, 300):
        cellCode = getCellCode(r, col)
        cell = sh[cellCode]
        if cell.value is not None:
            return False
    return True