import json
import base64
import boto3

# The name of the deployed model
ENDPOINT = 'image-classification-2023-07-08-11-29-06-937'

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])
    
    runtime_client = boto3.client('sagemaker-runtime')
    
    response = runtime_client.invoke_endpoint(
        EndpointName=ENDPOINT,    # Endpoint Name
        Body=image,               # Decoded Image Data as Input
        ContentType='image/png'   # Type of inference input data - Content type (Eliminates the need of serializer)
    )
    
    # Make a prediction:
    inferences = json.loads(response['Body'].read().decode('utf-8'))
    
    # Pass the data back to the Step Function
    event["body"]["inferences"] = inferences
    return {
        'statusCode': 200,
        'body': event["body"]
    }