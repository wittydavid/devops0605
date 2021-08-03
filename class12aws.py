import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances()

for r in response['Reservations']:
    for i in r['Instances']:
        if i["State"]["Name"] == "running":
            input_from_user = input(f"should I stop {i['InstanceId']} ? ")
            if input_from_user == "yes":
                result = ec2_client.stop_instances(InstanceIds=[i['InstanceId']])
