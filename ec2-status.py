#!/usr/bin/python
 
import boto3
import datetime
now = datetime.datetime.now()
print "Run Date: " 
print now.strftime('%Y/%m/%d %H:%M:%S')

session = boto3.Session(profile_name='wh-sandbox')
#  Get boto3 EC2 resource
ec2 = boto3.resource('ec2')
for i in ec2.instances.all():
	print i.state['Name'], i
