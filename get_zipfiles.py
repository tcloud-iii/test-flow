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

