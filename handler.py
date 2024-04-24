import json
import boto3
import uuid
import logging
from decimal import Decimal
from boto3.dynamodb.conditions import Key
from theme_config import default_theme

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# TODO: move to seperate file. 
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)  # or use str(obj) if precision is very important
        return super(DecimalEncoder, self).default(obj)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cms-theme-server-data')

def create(event, context):
    logger.info(f"Event received in create: {event}")
    data = json.loads(event['body'])
    theme = data.get('theme', default_theme)  # Use the provided theme or default theme if not provided
    group_name = data.get('groupName')

    if not group_name:
        logger.error("No groupName provided in create function.")
        response = {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps({"message": "groupName is required"})
        }
        return response
    
    item = {
        'id': str(uuid.uuid4()),
        'groupName': group_name,
        'theme': theme
    }
    table.put_item(Item=item)
    logger.info(f"Item created successfully: {item}")

    response = {
        "statusCode": 201,
        "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
        "body": json.dumps(item)
    }
    return response

def get(event, context):
    logger.info(f"Event received in get: {event}")
    path_parameters = event.get('pathParameters', {})
    theme_id = path_parameters.get('id') if path_parameters else None
    query_string_parameters = event.get('queryStringParameters', {})
    group_name = query_string_parameters.get('groupName') if query_string_parameters else None

    if theme_id:
        logger.info(f"Fetching theme by ID: {theme_id}")
        result = table.get_item(Key={'id': theme_id})
        if 'Item' in result:
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Credentials": True,
                },
                "body": json.dumps(result['Item'], cls=DecimalEncoder) 
            }
        else:
            logger.warning(f"No theme found for ID: {theme_id}")
            return {
                "statusCode": 404,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Credentials": True,
                },
                "body": json.dumps({"message": "Theme not found"}, cls=DecimalEncoder) 
            }
    elif group_name:
        logger.info(f"Fetching themes by groupName: {group_name}")
        response = table.query(
            IndexName='GroupNameIndex',
            KeyConditionExpression=Key('groupName').eq(group_name)
        )
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(response['Items'], cls=DecimalEncoder) 
        }
    else:
        logger.error


def update(event, context):
    logger.info(f"Event received in update: {event}")
    data = json.loads(event['body'])
    theme_id = event['pathParameters']['id']
    
    if 'theme' not in data:
        logger.error("No theme data provided to update.")
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
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
    
    logger.info(f"Theme updated successfully: {theme_id}")
    return {
        "statusCode": 200,
        "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
        "body": json.dumps({"message": "Theme updated", "updatedAttributes": response['Attributes']})
    }

def delete(event, context):
    logger.info(f"Event received in delete: {event}")
    theme_id = event['pathParameters']['id']
    
    table.delete_item(
        Key={'id': theme_id}
    )
    
    logger.info(f"Theme deleted successfully: {theme_id}")
    return {
        "statusCode": 200,
        "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
        "body": json.dumps({"message": "Theme deleted"})
    }
