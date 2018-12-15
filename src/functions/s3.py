import json
import boto3
import urllib


###############################################
def get_bucket_and_key(event):
    
    # Get the object from the event and show its content type
    b = event['Records'][0]['s3']['bucket']['name']
    k = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8')) 
    
    return( b, k )


###############################################
def get_s3_object(bucket, key):
    
    # Connect to S3
    s3 = boto3.client('s3')
    
    # Return details of S3 object.
    return s3.get_object(
        Bucket=bucket,
        Key=key
    )    

###############################################
def set_s3_object_data(bucket,key,contents):
    ''' Write content to S3 object '''
    
    # Connect to S3
    s3 = boto3.client('s3')
    
    # Create S3 object.
    obj = s3.Object(bucket,key)
    
    # Push data to object.
    obj.put(Body=contents)
    
    # Log event.
    print('S3 object data written: {}/{}'.format(bucket,key))


######################################
def get_s3_object_data(bucket,key):
    ''' Return content from S3 object '''
    
    # Connect to S3
    s3 = boto3.client('s3')    
    
    # Create S3 object.
    obj = s3.Object(bucket,key)
    
    # Get data from object.
    contents = obj.get()['Body'].read()
    
    # Log event.
    print('S3 object data retrieved: {}/{}'.format(bucket,key))    
    
    # return content.
    return( contents )