import boto3
import json
import traceback

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("device_serial_table")
        device_serial = json.loads(event["body"])["device_serial"]

        print("Attempting to read the data from the table.")

        try:
            response = table.get_item( Key={ "device_serial": device_serial} )
        except:
            print("KeyError")
            return {
                "statusCode": 406,
                "body": "Item with the specified device serial not found."
            }

    except Exception:
        return {
            "statusCode": 500,
            "body": traceback.format_exc()
        }

    return {
        "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
        "body": json.dumps(response["Item"])
    }