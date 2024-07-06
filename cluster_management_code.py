import boto3
import time
import redshift_connector

# Replace with your cluster identifier
CLUSTER_IDENTIFIER = "redshift-cluster-2"
REGION = 'us-east-1'
HOST_NAME = 'redshift-cluster-2.czcdbl82hrrx.us-east-1.redshift.amazonaws.com'
DB_NAME = "dev"
DB_USER = 'awsuser'
DB_PASSWORD = 'Karthiksara2123'
NEW_DB_NAME = "My_redshift_cluster_management_DB"
RETRY_INTERVAL = 30  # seconds

# Create a Redshift client
redshift_client = boto3.client('redshift', region_name=REGION)

try:
    # Resume the cluster
    response = redshift_client.resume_cluster(ClusterIdentifier=CLUSTER_IDENTIFIER)
    print("Cluster resumed successfully:", response)
    
    cluster_id = response['Cluster']['ClusterIdentifier']
    
    # Wait for the cluster to become available
    while True:
        response = redshift_client.describe_clusters(ClusterIdentifier=cluster_id)
        cluster_status = response['Clusters'][0]['ClusterStatus']
        print(f"Cluster status: {cluster_status}")
        
        if cluster_status == 'available':
            print("Cluster is available.")
            break
        
        time.sleep(RETRY_INTERVAL)
        
    print("Cluster is Available now")
        
    # Connect to the Redshift cluster
    conn = redshift_connector.connect(
        host=HOST_NAME,
        port=5439,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    cursor.execute(f"CREATE DATABASE {NEW_DB_NAME}")
    print(f"Database '{NEW_DB_NAME}' created successfully.")
    
    time.sleep(RETRY_INTERVAL)
    


    # Pause the cluster after operations are complete

    # Create a manual snapshot
    snapshot_identifier = f"{CLUSTER_IDENTIFIER}-manual-snapshot"
    response = redshift_client.create_cluster_snapshot(
        SnapshotIdentifier=snapshot_identifier,
        ClusterIdentifier=CLUSTER_IDENTIFIER
    )
    print("Manual snapshot created successfully:", response)
    
    # Wait for the snapshot to be available
    while True:
        response = redshift_client.describe_cluster_snapshots(SnapshotIdentifier=snapshot_identifier)
        snapshot_status = response['Snapshots'][0]['Status']
        print(f"Snapshot status: {snapshot_status}")
        
        if snapshot_status == 'available':
            print("Snapshot is available.")
            break
        
        time.sleep(RETRY_INTERVAL)
    
    time.sleep(RETRY_INTERVAL)

    response = redshift_client.pause_cluster(ClusterIdentifier=CLUSTER_IDENTIFIER)
    print("Cluster paused successfully:", response)

except Exception as e:
    print(f"Error: {e}")
finally:
    # Ensure the connection is closed if it was opened
    try:
        if conn:
            conn.close()
            print("Connection closed.")
    except NameError:
        pass
