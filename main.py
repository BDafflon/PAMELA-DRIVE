from gui.pamelaView import PamGui
from simulation.simulation import SimulationMas

print("start")
def runSimpleSimulation(pathEnv="", pathSce="", pathStock=""):
    s = SimulationMas()
    g = PamGui(s)
    s.Gui = g


runSimpleSimulation("./test.json", "", "")

