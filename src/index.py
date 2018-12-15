from __future__ import print_function
import json
import boto3
import os
from functions import *

print('Loading S3-Lambda-SNS-Demo function')

# Get SNS Topic ARN from environment variables.
sns_topic_arn = os.getenv('SNSTopic', 'unset')


###############################################
def lambda_handler(event, context):
    
    # Print contents of 'event' to cloudwatch logs.
    print("Received event: " + json.dumps(event, indent=2, default=str))

    # Get bucket & key from passed event.
    bucket, key = get_bucket_and_key(event)
    
    try:
        # Get details of S3 object.
        response = get_s3_object(bucket, key)
        
        # Print object details to cloudwatch logs.
        print("Object Details: " + json.dumps(response, indent=2, default=str))
        
        # Publish message to SNS.
        if sns_topic_arn is not 'unset':
            
            # Set SNS Subject (works for email subscriptions)
            sns_subject = "File {} uploaded".format(response['ContentType'])
            
            # Set SNS message (works for all subscriptions)
            sns_message = "New file in S3: {}/{}".format(bucket, key)
            
            # Send message.
            send_sns(
                topic_arn=sns_topic_arn,
                message=sns_message,
                subject=sns_subject
            )
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}.').format(key, bucket)
        print('Make sure they exist and your bucket is in the same region as this function.')
        raise e