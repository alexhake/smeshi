class Smesher:
    def __init__(self, config):
        self.smesher_data = {
            "Base64 Commitment ATX ID": None,
            "Base64 Node ID": None,
            "Hex Commitment ATX ID": None,
            "Hex Node ID": None,
            "Hostname": None,
            "Labels Per Unit": None,
            "Local IP": None,
            "Max File Size": None,
            "Nonce": None,
            "Nonce Value": None,
            "Num Units": None
        }
        self.gpu_data = {
            "Fan Speed": None,
            "GPU Name": None,
            "GPU Utilization": None,
            "Memory Utilization": None,
            "Power Draw": None,
            "Temperature": None
        }
        self.post_data = {
            "File Metadata": [],
            "Post Data Size": None
        }
        self.status_data = {
            "Estimated Completion Time": None,
            "Hours to Completion": None,
            "Smesh Speed": None,
            "Last Heartbeat": None,
            "Post Data Completed": None,
        }
        self.pulse = []
        self.config = config
        
    def get_smesher_data(self):
        return self.smesher_data
    
    def get_gpu_data(self):
        return self.gpu_data
    
    def get_post_data(self):
        return self.post_data
    
    def get_status_data(self):
        return self.status_data
    
    def get_pulse(self):
        return self.pulse