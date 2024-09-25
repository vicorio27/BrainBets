import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.client("dynamodb")

table = dynamodb.Table("YourTableName")


def put_item():
    dynamodb.put_item(
        TableName="YourTableName",
        Item={
            "pk": {"S": "id#1"},
            "sk": {"S": "cart#123"},
            "name": {"S": "SomeName"},
            "inventory": {"N": "500"},
            # ... more attributes ...
        },
    )


def dynamo_to_python(dynamo_object: dict) -> dict:
    deserializer = TypeDeserializer()
    return {k: deserializer.deserialize(v) for k, v in dynamo_object.items()}


def python_to_dynamo(python_object: dict) -> dict:
    serializer = TypeSerializer()
    return {k: serializer.serialize(v) for k, v in python_object.items()}


def query(table_name: str):
    # Construct the query
    response = dynamodb.query(
        TableName=table_name,
        KeyConditionExpression="pk = :pk_val AND begins_with(sk, :sk_val)",
        FilterExpression="#name = :name_val",
        ExpressionAttributeValues={
            ":pk_val": {"S": "id#1"},
            ":sk_val": {"S": "cart#"},
            ":name_val": {"S": "SomeName"},
        },
        ExpressionAttributeNames={
            "#name": "name",
        },
    )


def query_simplified():
    response = table.query(
        KeyConditionExpression=Key("pk").eq("id#1") & Key("sk").begins_with("cart#"),
        FilterExpression=Attr("name").eq("SomeName"),
    )
