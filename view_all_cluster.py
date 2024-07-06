import boto3
import time 
redshift = boto3.client('redshift', region_name='us-east-1')

response = redshift.describe_clusters()

for cluster in response['Clusters']:
    print(cluster['ClusterIdentifier'])

        