from django.http import HttpResponse, HttpRequest
from utils.s3_client import S3Client
from os import getenv
from asyncio import run

s3 = S3Client(
    getenv('S3_ACCESS_KEY'),
    getenv('S3_SECRET_KEY'),
    endpoint_url=getenv("S3_ENDPOINT_URL"),
    bucket_name=getenv("S3_BUCKET_NAME")
)


def index(request: HttpRequest):
    return HttpResponse("Hello")