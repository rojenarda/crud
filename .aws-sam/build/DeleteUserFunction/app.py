import boto3
import json
import traceback

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("user_id_table")
        user_id = json.loads(event["body"])["identity_id"]

        print("Attempting to delete the data from the table.")
        response = table.delete_item( Key={ "identity_id": user_id } )

    except Exception:
        return {
            "statusCode": 500,
            "body": traceback.format_exc()
        }

    return {
        "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
        "body": json.dumps(response)
    }