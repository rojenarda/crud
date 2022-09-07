import boto3
import json
import traceback

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("user_id_table")

        print("Attempting to read items from the table.")
        print(table.item_count)
        # if table.item_count == 0:
        #     return {
        #         "statusCode": 406,
        #         "body": "There are no items in the table."
        #     }

        response = table.scan()
        items = response["Items"]
        while "LastEvaluatedKey" in response:
            response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
            items.extend(response["Items"])

    except Exception:
        return {
            "statusCode": 500,
            "body": traceback.format_exc()
        }

    return {
        "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
        "body": json.dumps(items)
    }