import boto3
import requests
import tempfile
import os

#https://ds2002-lct4am.s3.amazonaws.com/Sunflower_sky_backdrop.jpg?AWSAccessKeyId=ASIA3FLD5C6KKFXMT5A5&Signature=IlganbYZTmpoRTdFNlcvsxiQ0XY%3D&x-amz-security-token=FwoGZXIvYXdzEDcaDB8ZaMjNuFawoQBpdCLEATXjQtfKi0Eaig6xiWiRRjfw%2FIf5lQuU2cBtCxmfiAUOX2mqhTfynnp8u6EINcdn73sZ%2BTZ2xO%2FdbUgg%2FJyJ5CDx4%2FDUdRCptKVGQ6y5IwGQdkFOLWUVi54Rdz0lfH6Jzek86juGnzGspLGiby8smL6Hvtwi1AezPzHx3DSpgUtzaSQC8CCBF7bAxgHrO3Ms5%2B1dhzHiZROxouAEeEEVnY5spDSJK%2BeG7v%2BVfzhSNfa0PtA7Pggcc6g%2FebESlDY08g2NkA4otemDrwYyLTsDtCHY%2FcXmXMlasZnAXonEIWEezSOgi89t827pc7mpm7UWuJACllcNYbxkrg%3D%3D&Expires=1709852411

file_url = "https://upload.wikimedia.org/wikipedia/commons/4/40/Sunflower_sky_backdrop.jpg"
response = requests.get(file_url).content

bucket_name = "ds2002-lct4am"
object_name = "Sunflower_sky_backdrop.jpg"

expires_in = 604800

s3 = boto3.client('s3')
response = s3.put_object(
        Body = response,
        Bucket = bucket_name,
        Key = object_name,
        ACL = 'public-read'
)

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print("Presigned URL:", response)