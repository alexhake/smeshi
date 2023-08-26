from smesher import Smesher
from smesh_lib import SmeshLib
import time
import subprocess
import utils

def start(config):
    smesher = Smesher(config)
    subprocess.call('clear', shell=True) # Clear Shell

    print(f'Waiting {config["wait_time"]} seconds to get data...')


    while True:
        
        time.sleep(config['wait_time'])
        subprocess.call('clear', shell=True) # Clear Shell
        pulse = smesher.get_pulse()

        gpu_data = SmeshLib.query_gpu_data()
        smesher.set_gpu_data(gpu_data)

        smesher_data = SmeshLib.query_smesher_data(config["post_data_dir"])
        smesher.set_smesher_data(smesher_data)

        post_data = SmeshLib.query_post_data(config["post_data_dir"])
        smesher.set_post_data(post_data)

        status_data = SmeshLib.query_status_data(config, pulse)
        smesher.set_status_data(status_data)

        smesher.set_pulse()

        pulse = smesher.get_pulse()

        if(config["report_data"] == 1):
            utils.insert_data(pulse, config["state_table_name"])
            print('Data sent to cloud')

        utils.display_data(pulse, config)


