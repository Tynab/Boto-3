import boto3
from ast import Expression

client = boto3.client('s3')

res = client.select_object_content(
    Bucket='nguyendangtruongan.com',
    Key='students.csv',
    ExpressionType='SQL',
    Expression="SELECT s.name, s.email FROM s3object s",
    InputSerialization={'CSV': {"FileHeaderInfo": "Use"}},
    OutputSerialization={'CSV': {}},
)

print(res['Payload']['Records'])

for event in res['Payload']:
    if 'Records' in event:
        print(event['Records']['Payload'].decode('utf-8'))
    elif 'Stats' in event:
        print(event['Stats']['Details'])
