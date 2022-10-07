# -*- coding: utf-8 -*-

import pandas as pd
import time
import os
from google.cloud import bigquery

directory_name = '/home/tcloud_iii_gcp/test-flow'

for file_name in os.listdir(directory_name):
  if '點數監控' and 'xlsx' in file_name:
    objfile = os.path.join(directory_name, file_name)

point_mon = pd.read_excel(objfile)

point_mon_col = ['budget_source',
'date',
'budget_in_total',
'cumul_sme',
'cumul_point_to_sme',
'cumul_sme_usedpt',
'pt_on_sme',
'return_sme_1m',
'return_point_1m',
'return_point_3m',
'cumul_unreimbuse_point',
'cumul_return_pt',
'real_sme',
'real_pt',
'real_sme_ptused',
'rest_pt',
'total_sale_price',
'cumul_reim_pt',
'culmul_reiming_pt',
'reimable_pt',
'unreimable_pt',
'ratio_reim_order',
'ratio_reim_order_done',
'ratio_apply_reim',
'total_pt_2nd',
'pt_ratio_2nd',
'ratio_2nd_pt_out',
'ratio_2nd_pt_rest']
point_mon.columns =point_mon_col

point_mon['date']=pd.to_datetime(point_mon['date'])

credentials_path = "/home/tcloud_iii_gcp/front_to_bq.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
client = bigquery.Client()
table_id = 'tcloud-data-analysis.tcloud_analytic_db.budget_monitor'
 
job = client.load_table_from_dataframe(point_mon, table_id)
job.result()  #等待寫入完成
