import tools
import os.path

class Workspace:

    mainWindowX = 0
    mainWindowY = 0
    rootFolder = ''
    def getName(self):
        return os.path.basename(self.rootFolder)

    def getMasterFileName(self):
        return self.rootFolder + '/Client Files/summary_masterfile.xlsx'

workspace = Workspace()


def save():
    global workspace
    tools.saveObject('workspace.bin', workspace)

def load():
    global workspace
    workspace = tools.loadObject('workspace.bin', Workspace())

