import subprocess
import json
from base64 import b64decode

def get_highest_atx():
    command = 'grpcurl --plaintext -d "{}" localhost:9092 spacemesh.v1.ActivationService.Highest'
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    json_result = json.loads(result.stdout.strip())
    highest_atx = b64decode(json_result["atx"]["id"]["id"]).hex()
    print(highest_atx)

if __name__ == "__main__":
    get_highest_atx()