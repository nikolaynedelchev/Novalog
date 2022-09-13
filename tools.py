import pickle
import os.path

def saveObject(fileName, obj):
    with open(fileName, 'wb') as saveFile:
        pickle.dump(obj, saveFile)

def loadObject(fileName, defaultObj):
    if os.path.isfile(fileName):
        with open(fileName, 'rb') as loadFile:
            newObj = pickle.load(loadFile)
        return newObj
    return defaultObj
