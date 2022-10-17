# -*- coding: utf-8 -*-

import pandas as pd
import os


directory_name = '/home/tcloud_iii_gcp/test-flow'

for file_name in os.listdir(directory_name):
  if '關於SME下單' in file_name:
    orderfile = os.path.join(directory_name, file_name)



order = pd.read_csv(orderfile, header='infer')
order = order[['統一編號', '公司名稱', '公司地址', '訂單日期', '訂單編號', '訂單狀態', '解決方案UUID', '解決方案中文名稱',
       '方案名稱', '方案價格', '使用點數', '自付額', '建立日期', '異動日期', '退還點數', '退回自付額', '請領狀態',
       '發票1查驗狀態', '發票2查驗狀態', '是否有評價', '方案期程', '合約起始日(起)', '合約起始日(迄)', '折讓單總金額',
       '折讓單日期', '不可核銷點數', '點數來源']]

order_col =['sme_ban', 'sme_name', 'sme_address', 'order_date', 'order_num', 'order_status', 'solution_uuid', 
'solution_name', 'solution_spec', 'sol_price', 'sol_point', 'sol_selfpay', 'order_est_date', 'order_change_date',
'return_point', 'return_pay', 'reimburse_status', 'invoice_check1', 'invoice_check2', 'review_status', 'solution_duration',
'contract_start_date', 'contract_end_date', 'allowence_price', 'allowence_date', 'unreimbuse_point', 'point_source']

order.columns = order_col
#改欄位型別
datetp =['order_date', 'order_est_date', 'order_change_date','contract_start_date','contract_end_date']
for i in datetp:
  order[i] = pd.to_datetime(order[i])

strtp =['sme_ban', 'order_num']
for j in strtp:
    order[j] = order[j].astype('str') 

#分成兩個表

order_basic = order[['sme_ban', 'sme_name', 'sme_address', 'order_date', 'order_num',
       'order_status', 'solution_uuid', 'solution_name', 'solution_spec',
       'sol_price', 'sol_point', 'sol_selfpay', 'order_est_date',
       'order_change_date', 'return_point', 'return_pay', 'solution_duration', 'contract_start_date', 'contract_end_date','point_source']]
order_further = order[['sme_ban','order_num','order_status', 'solution_uuid', 'solution_name','reimburse_status','invoice_check1', 'invoice_check2', 'review_status','allowence_price', 'allowence_date', 'unreimbuse_point']]

order_basic.to_csv(directory_name+'/'+'order_basic.csv')
order_further.to_csv(directory_name+'/'+'order_further.csv')

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



upload_blob('tcloud_bq_files',directory_name+'/order_basic.csv','order_basic.csv')
upload_blob('tcloud_bq_files',directory_name+'/order_further.csv','order_further.csv')

print('Order file has done!')


#to bigquery
from google.cloud import bigquery
credentials_path = "/home/tcloud_iii_gcp/front_to_bq.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
client = bigquery.Client()
#table_id = 'tcloud-data-analysis.tcloud_analytic_db.order_basic'
 
#job = client.load_table_from_dataframe(point_mon, table_id)
#job.result()  #等待寫入完成

#order_basic
dataset_ref = client.dataset('tcloud_analytic_db')
table_ref = dataset_ref.table('order_basic')
table_ref1 = dataset_ref.table('order_futher')
job_config = bigquery.job.LoadJobConfig()
job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
client.load_table_from_dataframe(order_basic, table_ref, job_config=job_config)
client.load_table_from_dataframe(order_further, table_ref1, job_config=job_config)


print('Order files have sent to Bigquery!')
