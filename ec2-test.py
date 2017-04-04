#!/usr/bin/python
 
import boto3
#  Get boto3 EC2 resource
ec2 = boto3.resource('ec2')
for i in ec2.instances.all():
	print i['PublicIpAddress'], i
