import boto3

# Replace with your cluster identifier
cluster_identifier = "redshift-cluster-2"

# Create a Redshift client
redshift_client = boto3.client('redshift',region_name='us-east-1')

# Get the list of snapshots
response = redshift_client.describe_cluster_snapshots(
    ClusterIdentifier=cluster_identifier
)

# Print information about each snapshot
print("Cluster Snapshots:")
for snapshot in response['Snapshots']:
    snapshot_id = snapshot['SnapshotIdentifier']
    snapshot_status = snapshot['Status']


    print(f"\tSnapshot ID: {snapshot_id}")
    print(f"\tStatus: {snapshot_status}")

