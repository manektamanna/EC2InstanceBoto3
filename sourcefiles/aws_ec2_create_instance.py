# Creating EC2 instance using Python Boto3

import boto3


def create_ec2_instance():
    try:
        print("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId='ami-0022f774911c1d690',
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="ec2key"
        )
    except Exception as e:
        print(e)


def describe_ec2_instance():
    try:
        print("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances(InstanceIds=['i-0e5cc034454b01d78'])["Reservations"][0]["Instances"][0][
                  "InstanceId"])
        return str(
            resource_ec2.describe_instances(InstanceIds=['i-0e5cc034454b01d78'])["Reservations"][0]["Instances"][0][
                "InstanceId"])
    except Exception as e:
        print(e)


def reboot_ec2_instance():
    try:
        print("Rebooting EC2 instance")
        instanceid = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        resource_ec2.reboot_instances(InstanceIds=[instanceid])

    except Exception as e:
        print(e)


def stop_ec2_instance():
    try:
        print("Stopping EC2 instance")
        instanceid = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        resource_ec2.stop_instances(InstanceIds=[instanceid])

    except Exception as e:
        print(e)


def start_ec2_instance():
    try:
        print("Starting EC2 instance")
        instanceid = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        resource_ec2.start_instances(InstanceIds=[instanceid])

    except Exception as e:
        print(e)


def terminate_ec2_instance():
    try:
        print("Terminating EC2 instance")
        instanceid = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        resource_ec2.terminate_instances(InstanceIds=[instanceid])

    except Exception as e:
        print(e)

# create_ec2_instance()
# describe_ec2_instance()
# reboot_ec2_instance()
# stop_ec2_instance()
# start_ec2_instance()
# terminate_ec2_instance()
