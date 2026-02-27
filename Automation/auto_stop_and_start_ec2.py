import boto3

client=boto3.client("ec2")

#print(client)

ec2_Reservations=client.describe_instances()
#print(ec2_instance)

ec2_instances=ec2_Reservations['Reservations']

print(ec2_instances)
for ec2 in range(len(ec2_instances)):
    print(ec2)
    print()


