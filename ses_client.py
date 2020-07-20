import json
import boto3
from botocore.exceptions import ClientError

config_json = open('./email/email_config.json', mode='r', encoding='UTF-8')
config_data = json.load(config_json)
config_json.close()

SENDER = config_data['sender']
CHARSET = config_data['charset']
REGION = config_data['region']

client = boto3.client('ses', region_name=REGION)


def send(recipient, subject, body):
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [recipient],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body,
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': subject,
                }
            },
            Source=SENDER
        )

        print('Email sent to : ' + recipient + ' | Message ID: ' + response['MessageId'])

    except ClientError as e:
        print(e.response['Error']['Message'])
