import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import ClientError

def s3_connect():
    load_dotenv()
    session = boto3.Session(aws_access_key_id=os.getenv('CLE_ACCES_S3'), 
                            aws_secret_access_key=os.getenv('CLE_ACCES_SECRET_S3'))

    s3 = session.resource("s3")
    # for bucket in s3.buckets.all():
    #     print(bucket.name)
    s3_client = session.client('s3')

    print("Sauvegarde des températures ...")
    try:
        response = s3_client.upload_file('./data/wheather.csv', 'dsfs-od-11-bucket','wheather.csv')
    except ClientError as e:
        print(e)
    print("Done ...")

    print("Sauvegarde des hotels ...")
    try:
        response = s3_client.upload_file('./data/hotels.csv', 'dsfs-od-11-bucket','hotels.csv')
    except ClientError as e:
        print(e)
    print("Done ...")

    print("Sauvegarde des lat et lon des villes ...")
    try:
        response = s3_client.upload_file('./data/city_lat_lon.txt', 'dsfs-od-11-bucket','city_lat_lon.txt')
    except ClientError as e:
        print(e)
    print("Done ...")