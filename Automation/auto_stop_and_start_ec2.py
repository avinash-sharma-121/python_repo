import boto3

client=boto3.client("ec2")

instace_list=[]

def getInstanceDetails():

    ec2_Reservations=client.describe_instances()
    all_ec2_instances=ec2_Reservations['Reservations']
    #print(all_ec2_instances)
    if len(all_ec2_instances) > 0:
        for reservation in all_ec2_instances:
            ec2_details=reservation["Instances"]
            for ec2 in ec2_details:
                #print(ec2)
                instace_id=ec2['InstanceId']
                #public_ip1=ec2['PublicIpAddress']
                private_ip1=ec2['PrivateIpAddress']
                instance_type=ec2['InstanceType']
                instance_status=ec2['State']['Name']
                instace_list.append(instace_id)
                print(instace_id,private_ip1,instance_type,instance_status)

#getInstanceDetails()
    
def stopInstance():
    getInstanceDetails()
    print(instace_list)
    #print(type(instace_list[0]))
    response = client.stop_instances(
        InstanceIds=instace_list,
        #SkipOsShutdown=True,
        Force=True
    )

    #print(response)

def startInstance():
    getInstanceDetails()
    print(instace_list)
    response=client.start_instances(
        InstanceIds=instace_list
    )
    #print(response)

#stopInstance()
startInstance()