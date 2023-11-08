import boto3
# Explicitly set AWS credentials
session = boto3.Session(
    aws_access_key_id='enter access_key_id',
    aws_secret_access_key='enter_aws_access_key',
    region_name='us-east-1'  # Set your preferred AWS region
)

ec2 = session.client('ec2')

# Rest of your script


# Initialize a Boto3 EC2 client
ec2 = boto3.client('ec2')

# Get a list of available instance types
instance_types = ec2.describe_instance_types()

# Print available instance types for the user
print("Available EC2 instance types:")
for instance_type in instance_types['InstanceTypes']:
    print(instance_type['InstanceType'])

# Get user input for EC2 instance details
instance_type = input("Enter the instance type you want to create: ")
ami_id = input("Enter the AMI ID for the instance: ")
key_name = input("Enter the key pair name for SSH access: ")
security_group_id = input("Enter the security group ID: ")
subnet_id = input("Enter the subnet ID: ")

# Create the EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=[security_group_id],
    SubnetId=subnet_id,
    MinCount=1,
    MaxCount=1
)

# Extract the instance ID from the response
instance_id = response['Instances'][0]['InstanceId']

print(f"Instance {instance_id} is being created. You can check the status in the AWS Management Console.")
