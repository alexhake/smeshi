import subprocess

class SmeshLib:

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