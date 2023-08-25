import subprocess
import json
from base64 import b64decode
import socket
import netifaces

class SmeshLib:

    @staticmethod
    def _get_local_ip():
        # Get a list of all network interfaces
        interfaces = netifaces.interfaces()
        local_ip = None

        # Find the local IP address of the first non-loopback network interface
        for interface in interfaces:
            if interface != 'lo':
                addrs = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addrs:
                    local_ip = addrs[netifaces.AF_INET][0]['addr']
                    break

        return local_ip

    @staticmethod
    def query_gpu_data():
        # Run nvidia-smi to get GPU information
        nvidia_smi_output = subprocess.check_output(
            [
                'nvidia-smi', 
                '--query-gpu=utilization.gpu,utilization.memory,memory.total,memory.free,memory.used,clocks.current.graphics,clocks.current.memory,temperature.gpu,temperature.memory,fan.speed,power.draw,power.limit,pstate,name', 
                '--format=csv,noheader'
            ], universal_newlines=True
        )

        # Split the output by lines
        gpu_data_lines = nvidia_smi_output.strip().split('\n')

        # Process the GPU information
        gpu_data = []

        for line in gpu_data_lines:
            gpu_utilization, memory_utilization, memory_total, memory_free, memory_used, clock_graphics, clock_memory, temp_gpu, temp_memory, fan_speed, power_draw, power_limit, performance_state, name = line.strip().split(', ')

            gpu_data.append({
                "GPU Utilization": gpu_utilization,
                "Memory Utilization": memory_utilization,
                "Memory Total": memory_total,
                "Memory Free": memory_free,
                "Memory Used": memory_used,
                "Clock Graphics": clock_graphics,
                "Clock Memory": clock_memory,
                "Temp GPU": temp_gpu,
                "Temp Memory": temp_memory,
                "Fan Speed": fan_speed,
                "Power Draw": power_draw,
                "Power Limit": power_limit,
                "Performance State": performance_state,
                "Name": name
        })

        return gpu_data

    def query_smesher_data(config):
        post_data_dir = config["post_data_dir"]
        nonce = None
        nonce_value = None

        with open(post_data_dir + '/postdata_metadata.json') as f:
            metadata = f.read()

        parsed_metadata = json.loads(metadata)

        base64_node_id = parsed_metadata['NodeId']

        # Convert Base64 to Hex
        hex_node_id = b64decode(base64_node_id).hex()

        base64_commitment_atx_id = parsed_metadata['CommitmentAtxId']

        # Convert Base64 to Hex
        hex_commitment_atx_id = b64decode(base64_commitment_atx_id).hex()

        num_units = parsed_metadata['NumUnits']

        max_file_size = parsed_metadata['MaxFileSize']

        labels_per_unit = parsed_metadata['LabelsPerUnit']

        hostname = socket.gethostname()

        local_ip = SmeshLib._get_local_ip()

        # Nonce isn't always there, so we will skip it if it doesn't exist
        try:
            nonce = parsed_metadata['nonce']
        except:
            pass

        try:
            nonce_value = parsed_metadata['NonceValue']
        except:
            pass

        return {
            "Base64 Node ID": base64_node_id,
            "Hex Node ID": hex_node_id,
            "Base64 Commitment ATX ID": base64_commitment_atx_id,
            "Hex Commitment ATX ID": hex_commitment_atx_id,
            "NumUnits": num_units,
            "Max File Size": max_file_size,
            "Labels Per Unit": labels_per_unit,
            "Nonce": nonce,
            "Nonce Value": nonce_value,
            "Hostname": hostname,
            "Local IP": local_ip
        }

    def query_post_data():
        pass

    def query_status_data():
        pass