import boto3
region = 'us-east-1'

ec2 = boto3.client('ec2', region_name=region)


rds = boto3.client('rds')
instances = ec2.instances.filter(Filters=[])
def lambda_handler_start(event, context):
    for instance in instances:
        instance.start()
    rds.start_db_instance(DBInstanceIdentifier='')

def lambda_handler_stop(event, context):
    for instance in instances:
        instance.stop()
    rds.stop_db_instance(DBInstanceIdentifier='')