import json
import boto3
from boto3.dynamodb.conditions import Key
from theme_config import default_theme

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cms-theme-server-data')

def create(event, context):
    data = json.loads(event['body'])
    theme = data.get('theme', default_theme)  # Use the provided theme or default theme if not provided
    group_name = data.get('groupName')

    if not groupName:
        response = {
            "statusCode": 400,
            "body": json.dumps({"message": "groupName is required"})
        }
        return response
    
    item = {
        'id': str(uuid.uuid4()),
        'groupName': groupName,
        'theme': theme
    }
    
    table.put_item(Item=item)
    
    response = {
        "statusCode": 201,
        "body": json.dumps(item)
    }
    return response

def get(event, context):
    theme_id = event['pathParameters'].get('id')
    group_name = event['queryStringParameters'].get('groupName') if event['queryStringParameters'] else None
    
    if theme_id:
        # Get theme by ID
        result = table.get_item(Key={'id': theme_id})
        if 'Item' in result:
            return {
                "statusCode": 200,
                "body": json.dumps(result['Item'])
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Theme not found"})
            }
    elif group_name:
        # Get themes by groupName using the secondary index
        response = table.query(
            IndexName='GroupNameIndex',
            KeyConditionExpression=Key('groupName').eq(group_name)
        )
        return {
            "statusCode": 200,
            "body": json.dumps(response['Items'])
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "ID or Group Name is required"})
        }

def update(event, context):
    data = json.loads(event['body'])
    theme_id = event['pathParameters']['id']
    
    if 'theme' not in data:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Theme update data is required"})
        }
    
    response = table.update_item(
        Key={'id': theme_id},
        UpdateExpression="set theme = :t",
        ExpressionAttributeValues={
            ':t': data['theme']
        },
        ReturnValues="UPDATED_NEW"
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Theme updated", "updatedAttributes": response['Attributes']})
    }

def delete(event, context):
    theme_id = event['pathParameters']['id']
    
    table.delete_item(
        Key={'id': theme_id}
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Theme deleted"})
    }