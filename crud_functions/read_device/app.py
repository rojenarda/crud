import boto3
import json
import traceback
from decimal import Decimal

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

    def decimal_handler(obj):
        if isinstance(obj, Decimal):
            if float(obj).is_integer():
                return int(obj)
            else:
                return float(obj)
        else:
            return obj

    return {
        "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
        "body": json.dumps(response["Item"], default=decimal_handler)
    }