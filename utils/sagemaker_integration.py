import subprocess
import os
from from_root import from_root
import boto3
import mlflow.sagemaker as mfs
import json


def upload(s3_bucket_name = None, mlruns_dir = None):
    try: 
        output = subprocess.run([
            "aws", "s3", "sync", "{}".format(mlruns_dir),
            "s3://{}".format(s3_bucket_name)
        ], stdout= subprocess.PIPE, encoding="utf-8")

        print("\n Saved to Bucket: ", s3_bucket_name)
        return f"Uploaded Successfully! : {output.stdout}"
    
    except Exception as e:
        return f"Error Occured while uploading : {e.__str__()}"
