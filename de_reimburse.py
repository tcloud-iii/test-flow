# -*- coding: utf-8 -*-

import pandas as pd
import os

directory_name = '/home/tcloud_iii_gcp/test-flow'


for file_name in os.listdir(directory_name):
  if '每日可核銷訂單清單' in file_name:
      if '.xlsx' in file_name:
          reimfile = os.path.join(directory_name, file_name)


reimburse = pd.read_excel(reimfile)

reim_col =['supplier_ban', 'sme_ban', 'order_num', 'order_status', 'reimburse_status',
 'reimburse_num', 'contract_start_date', 'contract_end_date', 'solution_uuid', 'solution_name', 
 'solution_spec', 'solution_duration', 'sol_price', 'sol_point', 'sol_selfpay', 
 'return_point', 'return_pay','last_reim_point', 'now_reim_point', 'rest_point', 'receipt_status', 
 'reimburse_submit_date', 'reim_change_date', 'order_change_date', 'sme_name', 'supplier_name', 
 'reimburseful_date', 'solution_satisfaction', 'reviews', 'invoice1', 'invoice_check1', 'invoice2', 
 'invoice_check2', 'point_source', 'point_source_code', 'unreimbuse_point', 'invoice_date1', 
 'invoice_date2', 'invoice_price1', 'invoice_price2']

reimburse.columns =reim_col


reimburse.to_csv('reimburse.csv')

# Imports the Google Cloud client library
from google.cloud import storage
import os
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

upload_blob('tcloud_bq_files',directory_name+'/reimburse.csv','reimburse.csv')

print('Reimburse file has done!')
