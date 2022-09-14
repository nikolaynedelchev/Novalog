from doctest import master
import settings
import tools
import data_types
import openpyxl as xl



def doTest():
    masterFileWB = xl.load_workbook(settings.workspace.getMasterFileName())

    cell = masterFileWB['Frial']['K3']

    for sheet in masterFileWB:
        for col in range(0, 20):
            print(f"Title: {sheet.title}, Column: {chr(ord('A') + col)}, is empty: {tools.isColumnEmpty(sheet, col, 1)}")
            



for c in range(ord('A'), ord('F') + 1):
    print(chr(c))

settings.load()

doTest()