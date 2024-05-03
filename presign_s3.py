import boto3
import requests

# Generate s3 presigned url, requires permission

s3_client = boto3.client('s3')

file_key = 'students.csv'
res = s3_client.generate_presigned_post(
    Bucket='nguyendangtruongan.com',
    Key=file_key,
    ExpiresIn=604_800 # 7 days max
)

print(res)

# Sending from client side, can be customized

fin = open(file_key, 'rb')
file = {'file': fin}

try:
    r = requests.post(res['url'], data=res['fields'], files=file)
    print(r.status_code)
finally:
    fin.close()
