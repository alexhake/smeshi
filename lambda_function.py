import json
import boto3

def lambda_handler(event, context):
    # Initialize DynamoDB client
    dynamodb = boto3.client('dynamodb')
    
    # DynamoDB table name
    table_name = 'smesh-states'
    
    # Key to retrieve (replace 'your_key_name' and 'your_key_value' with actual values)
    key = {
        'node_id': {'S': event["Node ID"]}
    }
    
    try:
        # Get item from DynamoDB
        response = dynamodb.get_item(
            TableName=table_name,
            Key=key
        )
        
        # Extract data from the response
        item = response.get('Item', {})
        
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    

if __name__ == "__main__":
    event = {"Node ID": "Or0a5gG61i2bvvv33TpylqEKIXIGAsanlkemNMHXtPQ="}
    print(lambda_handler(event, None))