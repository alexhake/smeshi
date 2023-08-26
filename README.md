# smeshi
Spacemesh Monitor. Not quite ready for the big time.

## Setup

### Config
Copy the example config file into config.json

Below are explainations of the various options.
```

"wait_time": 10, # This is how long between updates in seconds. 10 is recommended minimum
"post_data_dir": "/postcli/postdata", # Location of your post data
"max_errors": 5, # Max errors before script quits
"report_data": 1, # 1 if you hook it up to dynamodb
"trailing_average": 10, # How far back to look for speed averages, more for slower GPUs. Must be smaller than pulse_length
"state_table_name": "dynamo-table-name", # Name of dynamo table
"name": "My Name", # Name to be used for tracking
"privacy_mode": 1, # Does nothing but will obfuscate data once public reporting is avail
"password": "test", # Does nothing but will set a password on your public report page
"pulse_length": 10, # How many heartbeats to keep
"display": {
    "gpu_data": 1, # Displays GPU data if 1. 0 to turn off
    "smesher_data": 1, # Displays Smesher data if 1. 0 to turn off
    "status_data": 1 # Displays status data if 1. 0 to turn off
}

```
### Install Requirements
pip install -r requirements.txt

### Run
python3 main.py