from smesher import Smesher
from smesh_lib import SmeshLib

def start(config):
    smesher = Smesher(config)

    gpu_data = SmeshLib.query_gpu_data()
    smesher.set_gpu_data(gpu_data)

    print(smesher.get_gpu_data())