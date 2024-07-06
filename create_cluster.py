import boto3
import time 
# Initialize the Redshift client
redshift = boto3.client('redshift', region_name='us-east-1')
# Create a Redshift cluster
response = redshift.create_cluster(
    ClusterIdentifier='myredshiftclusterone',
    NodeType='dc2.large',
    MasterUsername='awsuserone',
    MasterUserPassword='Sarakarthik2123',
    DBName='dev',
    ClusterType='single-node', 
    PubliclyAccessible = True,


    Port=5439,
    
)

# Extract the cluster identifier from the response
cluster_id = response['Cluster']['ClusterIdentifier']


# Check the cluster status periodically until it becomes available
while True:
        response = redshift.describe_clusters(ClusterIdentifier=cluster_id)
        cluster_status = response['Clusters'][0]['ClusterStatus']
        print("Cluster status: %s", cluster_status)
        if cluster_status == 'available':
                print("Cluster is available.")
                break
        time.sleep(30)

        