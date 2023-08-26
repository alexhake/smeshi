from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from tabulate import tabulate
from datetime import datetime
import json

table_name = resource('dynamodb').Table('node-states')

def insert_data(pulse, table_name):
    table_name = resource('dynamodb').Table(table_name)

    print(pulse)
    
    response = table_name.put_item(
        Item = {
            'node_id': pulse[0]["Smesher Data"]["Base64 Node ID"],
            'pulse': pulse
        }
    )

    print(response)

    return response

def sanitize_data(pulse):
    return pulse

def display_data(pulse, config):
    # for i in pulse:
    #     json_str = json.dumps(i["Post Data"]["Post Data Size"], indent=4)
    #     print(json_str)

    smesher_data = pulse[-1]['Smesher Data']
    gpu_data = pulse[-1]["GPU Data"]
    post_data = pulse[-1]["Post Data"]
    status_data = pulse[-1]["Status Data"]

    nonce_found = False
    if smesher_data["Nonce"] and smesher_data["Nonce Value"]:
        nonce_found = True

    dt_object = datetime.fromtimestamp(int(pulse[-1]["Heartbeat"]))

    # Format the datetime object as a human-readable string
    human_readable_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Last Updated: {human_readable_time}')

    smesher_data_output = [
        ["Smesher Data", "Value"],
        #["Base64 Node ID", smesher_data["Base64 Node ID"]],
        ["Hex Node ID", smesher_data["Hex Node ID"]],
        #["Base64 Commitment ATX ID", smesher_data["Base64 Commitment ATX ID"]],
        ["Hex Commitment ATX ID", smesher_data["Hex Commitment ATX ID"]],
        ["PoST Data", f'{post_data["Post Data Size GiB"]} of {smesher_data["NumUnits"]*64} GiB ({smesher_data["NumUnits"]} NumUnits)'],
        ["Max File Size", f'{smesher_data["Max File Size"]} GiB'],
        #["Labels Per Unit", smesher_data["Labels Per Unit"]],
        #["Nonce", smesher_data["Nonce"]],
        #["Nonce Value", smesher_data["Nonce Value"]],
        ["Nonce Found", nonce_found],
        ["Hostname", smesher_data["Hostname"]],
        ["Local IP", smesher_data["Local IP"]],
    ]

    # Print CSV-like data to the console
    table = tabulate(smesher_data_output, headers='firstrow', tablefmt='grid')
    if(config["display"]["smesher_data"] == 1):
        print(table + '\n')

    gpu_data_output = [["Name", "GPU Util", "MEM Until", "Temp", "PWR", "PS"]]
    for i in gpu_data:
        gpu_data_output.append([
            i["Name"], 
            i["GPU Utilization"], 
            i['Memory Utilization'],
            i["Temp GPU"],
            i["Power Draw"],
            i["Performance State"]
        ])

    table = tabulate(gpu_data_output, headers='firstrow', tablefmt='grid')
    if(config["display"]["gpu_data"] == 1):
        print(table + '\n')

    status_data_output = [
        ["Status", "Value"],
        ["Hours to Completion", status_data["Hours to Completion"]],
        ["Estimated Completion Time", status_data["Estimated Completion Time"]],
        ["Speed", status_data["Speed"]]
    ]

    table = tabulate(status_data_output, headers='firstrow', tablefmt='grid')

    if(config["display"]["status_data"] == 1):
        print(table + '\n')

