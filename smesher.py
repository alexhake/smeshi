import time
from decimal import Decimal

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
        self.is_completed = False
        self.completion_time = None
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
    
    def get_completion_time(self):
        return self.completion_time
    
    def get_is_completed(self):
        return self.is_completed
    
    def set_smesher_data(self, smesher_data):
        self.smesher_data = smesher_data
    
    def set_gpu_data(self, gpu_data):
        self.gpu_data = gpu_data

    def set_post_data(self, post_data):
        self.post_data = post_data

    def set_status_data(self, status_data):
        self.status_data = status_data

    def set_completion_time(self, completion_time):
        self.completion_time = completion_time

    def set_is_completed(self, is_completed):
        self.is_completed = is_completed

    def set_pulse(self):
        self.pulse.append({
            "Smesher Data": self.smesher_data,
            "GPU Data": self.gpu_data,
            "Post Data": self.post_data,
            "Status Data": self.status_data,
            "Heartbeat": Decimal(time.time()),
            "Completed": self.is_completed,
            "Completion Time": self.completion_time
        })

        # Remove oldest entry
        if len(self.pulse) > self.config["pulse_length"]:
            self.pulse.pop(0)
