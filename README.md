# s3-lambda-sns-demo

Simple event-based architecture to show chaining of AWS services.

Serverless Application Model (SAM) template creates the following:

    S3 Bucket
    SNS Topic
    Lambda Function
    IAM Role
    

SNS Topic 'arn' is supplied as an Environment Variable to the Lambda Function.
Topic must be 'manually' subscribed to via the AWS console.

S3 Bucket is configured to trigger Lambda function following 'any' ObjectCreated event.

IAM Role allows Lambda to 'Get' S3 objects and 'Publish' to SNS.

Any file uploaded to S3 bucket will results in file details being sent to SNS Subscripton endpoint.
Lambda code (python 2.7) can be modified to change response.