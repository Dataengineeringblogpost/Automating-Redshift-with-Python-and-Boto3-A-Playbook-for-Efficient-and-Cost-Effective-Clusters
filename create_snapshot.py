import boto3
import time

# Replace with your cluster identifier
CLUSTER_IDENTIFIER = "redshift-cluster-2"
REGION = 'us-east-1'
SNAPSHOT_IDENTIFIER = f"{CLUSTER_IDENTIFIER}-new-manual-snapshot"

# Create a Redshift client
redshift_client = boto3.client('redshift', region_name=REGION)

try:
    # Create a manual snapshot
    print("Creating manual snapshot...")
    response = redshift_client.create_cluster_snapshot(
        SnapshotIdentifier=SNAPSHOT_IDENTIFIER,
        ClusterIdentifier=CLUSTER_IDENTIFIER
    )
    print("Manual snapshot creation initiated:", response)

    # Wait for the snapshot to become available
    while True:
        response = redshift_client.describe_cluster_snapshots(SnapshotIdentifier=SNAPSHOT_IDENTIFIER)
        snapshot_status = response['Snapshots'][0]['Status']
        print(f"Snapshot status: {snapshot_status}")

        if snapshot_status == 'available':
            print("Snapshot is available.")
            break

        time.sleep(30)  # Retry interval

except Exception as e:
    print(f"Error: {e}")
