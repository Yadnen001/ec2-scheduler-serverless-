import boto3

def lambda_handler(event, context):
    # Initializing the EC2 client
    ec2_client = boto3.client('ec2', region_name='ap-south-1') # Check region name

    # Specify the instance ID of the EC2 instance
    instance_id = 'i-051262059d6f6350a' # Replace instance id with our instance.

    # Starting the EC2 instance
    try:
        response = ec2_client.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(f"Starting EC2 instance {instance_id}...")
        print(f"Response: {response}")
        return {
            'statusCode': 200,
            'body': f"EC2 instance {instance_id} is being started."
        }
    except Exception as e:
        print(f"Error starting EC2 instance: {e}")
        return {
            'statusCode': 500,
            'body': f"Error starting EC2 instance: {str(e)}"
        }
