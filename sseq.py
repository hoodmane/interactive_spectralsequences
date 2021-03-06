#!./jython
import sys
import os
sys.path.append("..\\resolution\\resolution.jar")
sys.path.append(os.path.join('resolution', 'resolution.jar'))

infinity = 10000

from code import *
from sseq_definition import *



def initialize(settings):
    global sseq 
    global startDisplay 
    sseq = Sseq()
    startDisplay = SpectralSequenceDisplay.constructFrontend(sseq,settings).start
    return sseq
    
def getSettingsObject():
    settings = DisplaySettings()
    settings.windowName = "Interactive Spectral Sequences"
    return settings

if(len(sys.argv) > 1):
    exec(open(sys.argv[1],"r").read())
else:
    settings = getSettingsObject()
    settings.prime = 2
    settings.xscale = 1
    settings.yscale = 2
    settings.xmin = -50
    settings.xmax = 50
    settings.ymin = 0
    settings.ymax = 30
    settings.xgridstep = 5
    settings.ygridstep = 5
    settings.T_max = 100
    settings.x_full_range = True
    settings.page_list = [0,5,9,17,33,65]
    sseq = initialize(settings)

console1 = InteractiveConsole(locals=globals())
sseq.setInterpreter(console1)
console = InteractiveConsole(locals=globals())
sseq.disp = startDisplay()

def run_repl():
    console.interact() 
    sys.exit()

run_repl()
