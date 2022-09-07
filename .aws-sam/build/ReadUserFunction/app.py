import boto3
import json
import traceback

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("user_id_table")
        identity_id = json.loads(event["body"])["identity_id"]

        print("Attempting to read the data from the table.")
        try:
            response = table.get_item( Key={ "identity_id": identity_id} )
        except:
            print("KeyError")
            return {
                "statusCode": 406,
                "body": "Item with the specified identity id not found."
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