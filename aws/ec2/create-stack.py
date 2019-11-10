#/usr/bin/python
import boto.ec2
conn = boto.ec2.connect_to_region("us-east-1")
conn.run_instances(
    'ami-04842d7f071c46f73',
    key_name='Linux-sandbox',
    instance_type='t1.micro',
    security_groups=['default']
)
