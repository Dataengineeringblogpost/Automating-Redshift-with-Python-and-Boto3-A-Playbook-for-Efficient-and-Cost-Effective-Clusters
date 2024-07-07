import boto3

redshift = boto3.client('redshift', region_name='us-east-1')
cluster_identifier = "myredshiftcluster"
response = redshift.delete_cluster(
            ClusterIdentifier=cluster_identifier,
            SkipFinalClusterSnapshot=True
        )


print(f"Cluster {cluster_identifier} deletion initiated. Status: {response['Cluster']['ClusterStatus']}")