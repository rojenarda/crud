import boto3
import json
import traceback

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("device_serial_table")
        data = json.loads(event["body"])

        print("Attempting to add the data to the table.")
        response = table.put_item(Item=data)

    except Exception:
        return {
            "statusCode": 500,
            "body": traceback.format_exc()
        }

    return {
        "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
        "body": json.dumps(response)
    }