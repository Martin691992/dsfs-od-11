import boto3
import os
from dotenv import load_dotenv

load_dotenv()
session = boto3.Session(aws_access_key_id=os.getenv('CLE_ACCES_S3'), 
                        aws_secret_access_key=os.getenv('CLE_ACCES_SECRET_S3'))

s3 = session.resource("s3")
for bucket in s3.buckets.all():
    print(bucket.name)