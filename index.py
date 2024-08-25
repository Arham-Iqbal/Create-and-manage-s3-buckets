import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the S3 client
s3 = boto3.client('s3')

def create_s3_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def list_s3_buckets():
    try:
        response = s3.list_buckets()
        if not response['Buckets']:
            print("No S3 buckets found.")
        else:
            print("S3 Buckets:")
            for bucket in response['Buckets']:
                print(f"  - {bucket['Name']}")
    except Exception as e:
        print(f"Error listing buckets: {e}")

def delete_s3_bucket(bucket_name):
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting bucket: {e}")

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    try:
        if object_name is None:
            object_name = file_name
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"File '{file_name}' uploaded to bucket '{bucket_name}' as '{object_name}'.")
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_file_from_s3(bucket_name, object_name, file_name):
    try:
        s3.download_file(bucket_name, object_name, file_name)
        print(f"File '{object_name}' downloaded from bucket '{bucket_name}' to '{file_name}'.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except Exception as e:
        print(f"Error downloading file: {e}")

def delete_file_from_s3(bucket_name, object_name):
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"File '{object_name}' deleted from bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Example usage:
create_s3_bucket('my-unique-bucket-name')
list_s3_buckets()
upload_file_to_s3('myfile.txt', 'my-unique-bucket-name')
download_file_from_s3('my-unique-bucket-name', 'myfile.txt', 'downloaded_myfile.txt')
delete_file_from_s3('my-unique-bucket-name', 'myfile.txt')
delete_s3_bucket('my-unique-bucket-name')
