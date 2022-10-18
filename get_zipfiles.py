# -*- coding: utf-8 -*-
import requests
import zipfile
# Imports the Google Cloud client library
from google.cloud import storage
import os

directory_name = '/home/tcloud_iii_gcp/test-flow/'
#正式站url
x = requests.get('https://manage.tcloud.gov.tw/gdp-backend-api/api/hpc/download',
                 params={"downloadPath": '/apiRecordLog/newst/最新產檔結果.zip',
                         'key': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIvYXBpUmVjb3JkTG9nL25ld3N0L-acgOaWsOeUouaqlOe1kOaenC56aXAiLCJleHAiOjE2OTcwNzAwMDIsImlhdCI6MTY2NTUzNDAwMn0.iGaOd825-CVgw034ME_E7XlopvVpTB2tQ7Cgi1pXIQPTbWHW2zLhWOLaRWHl2JhAkdndH4HxUiuy8JYvDwMcCg',
                         'iv':'1665534002425'
                         })

open('today.zip', 'wb').write(x.content)

with zipfile.ZipFile(directory_name+"today.zip","r") as zip_ref:
    zip_ref.extractall()

with zipfile.ZipFile(directory_name+"最新產檔結果.zip","r") as zip_ref:
    zip_ref.extractall(directory_name)

# 這邊要吃api金鑰
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/tcloud_iii_gcp/front_to_bq.json"
storage_client = storage.Client()

#主要的fuction
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

from datetime import date
today = date.today()
filenm ='最新產檔結果_'+str(today)+'.zip'
print(filenm)

#測試上傳單一檔案，第一個參數是傳送位置(不動)，第二個是檔案路徑，第三個是檔案名稱
upload_blob('tradevan-to-iii',directory_name+'最新產檔結果.zip',filenm)
