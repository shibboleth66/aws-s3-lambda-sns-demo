import json
import boto3


################################################
def send_sns(
        topic_arn=None,
        message='Empty Message',
        subject='Empty Subject'
    ):
    """
        SNS Sender.
        
        Required arguments: 'topic_arn'
        Optional arguments: 'message', 'subject'
    """
    
    # Log event.
    print("* Sending SNS message")    
    
    # Connect to service
    client = boto3.client('sns')
    
    # Send message to existing sns topic.
    client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject
    )