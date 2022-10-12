# -*- coding: utf-8 -*-

import pandas as pd
import os

directory_name = '/home/tcloud_iii_gcp/test-flow'

for file_name in os.listdir(directory_name):
  if '關於供應商資訊' in file_name:
    supplierfile = os.path.join(directory_name, file_name)
  elif '關於供應商方案資訊' in file_name:
    solutionfile = os.path.join(directory_name, file_name)
 


supplier = pd.read_csv(supplierfile,header='infer')
solutions = pd.read_csv(solutionfile,header='infer')

supplier=supplier[['統一編號', '公司名稱', '公司地址', '領域名稱', '設立登記日期', '實收資本額', '資本額', '異動日期',
       '營業項目(資訊軟體服務業)', '營業項目(資料處理服務業)', '營業項目(電子資訊供應服務業)', '狀態', '建立日期']]

solutions =solutions[['統一編號', '公司名稱', '解決方案代碼', '解決方案中文名稱', '主分類代碼', '主分類名稱', '子分類代碼',
       '子分類名稱', '異動日期', '狀態', '所屬專區名稱', '所屬專區代碼', '是否顯示點數補助', '建立日期']]

supplier_col = ['supplier_ban', 'supplier_name', 'supplier_address', 'field_name', 'supplier_est_date', 'real_revenue', 'capital',
'change_date', 'operation_software_service', 'operation_software_supply', 'operation_software_process','supplier_status','supplier_built_date']
solution_col = ['supplier_ban','supplier_name', 'solution_uuid','solution_name','main_cate_code','main_categ_name','sub_cate_code',
'sub_categ_name','change_date','solution_status', 'where_display_code','where_display','avialalbe_in_points','sol_built_date']

supplier.columns = supplier_col
solutions.columns = solution_col

supplier.to_csv(directory_name+'/'+'supplier.csv')
solutions.to_csv(directory_name+'/'+'solution.csv')

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

upload_blob('tcloud_bq_files', directory_name + '/supplier.csv','supplier.csv')
upload_blob('tcloud_bq_files',directory_name + '/solution.csv','solution.csv')

print('Supplier & Solution files have done!')
