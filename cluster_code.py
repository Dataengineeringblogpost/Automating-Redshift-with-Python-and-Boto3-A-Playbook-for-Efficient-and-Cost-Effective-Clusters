import boto3
import time

# Initialize a Redshift client using Boto3
redshift = boto3.client('redshift', region_name='us-east-1')

# Describe all clusters
response = redshift.describe_clusters()

# Iterate through each cluster in the response
for cluster in response['Clusters']:
    # Print the current status of the cluster
    print(cluster['ClusterStatus'])
    
    # Check if the cluster status is "available"
    if cluster['ClusterStatus'] == "available":
        # Get the cluster identifier
        cluster_identifier = cluster['ClusterIdentifier']
        
        # Pause the cluster
        response = redshift.pause_cluster(ClusterIdentifier=cluster_identifier)
        
        # Print a success message with the response
        print("Cluster paused successfully:", response)
