import boto3

# Replace with your cluster identifier
cluster_identifier = "redshift-cluster-2"

# Create a Redshift client
redshift_client = boto3.client('redshift',region_name='us-east-1')

try:
  # Resume the cluster
  response = redshift_client.resume_cluster(ClusterIdentifier=cluster_identifier)
  print("Cluster resumed successfully:", response)

  
except Exception as e:
  print(f"Error resuming cluster: {e}")
