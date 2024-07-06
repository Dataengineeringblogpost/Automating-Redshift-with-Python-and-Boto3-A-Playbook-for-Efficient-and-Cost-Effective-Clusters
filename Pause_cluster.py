import boto3

# Replace with your cluster identifier
cluster_identifier = "redshift-cluster-2"

# Create a Redshift client
redshift_client = boto3.client('redshift',region_name='us-east-1')

try:
  # Pause the cluster
  response = redshift_client.pause_cluster(ClusterIdentifier=cluster_identifier)
  print("Cluster paused successfully:", response)
except Exception as e:
  print(f"Error pausing cluster: {e}")
