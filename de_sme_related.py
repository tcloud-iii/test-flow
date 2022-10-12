# -*- coding: utf-8 -*-
import pandas as pd
import os

directory_name = '/home/tcloud_iii_gcp/test-flow'

for file_name in os.listdir(directory_name):
  if '關於SME資訊與申請與點數' in file_name:
    objfile = os.path.join(directory_name, file_name)



sme = pd.read_csv(objfile, header='infer')
#sme.head(5)
town = pd.read_csv('/home/tcloud_iii_gcp/dataengineer/Taiwan_town-town.csv', header='infer')

sme_basic = sme[['統一編號', '公司名稱', '公司地址', '行業類別代碼', '行業大類代碼', '行業中類代碼', '行業小類代碼',
       '行業細類代碼', '行業子類代碼', '設立登記日期', '實收資本額', '員工人數', '異動日期', '狀態', '參考的解決方案']]

sme_basic_colnm= ['sme_ban', 'sme_name', 'sme_address',  'ind_class', 'ind_large', 'ind_medium', 'ind_small',
 'ind_division', 'ind_sub', 'estabilish_data', 'capital', 'employee_count', 'chage_date', 'apply_status', 'ref_solution']
#換標頭
sme_basic.columns = sme_basic_colnm

#sme_basic.fillna('NA',inplace=True)
#新增一個鄉鎮市區欄位
distr_ls = town['district_name'].tolist()

def add_district(address):
  for j in range(len(distr_ls)):
    if distr_ls[j] in address:
      return distr_ls[j]
    else:continue
  return 'notfound'

districtls= []
for i in range(len(sme_basic)):
  districtls.append(add_district(sme_basic['sme_address'][i]))

sme_basic['district']=districtls

sme_questionnaire =sme[['統一編號', '公司名稱','請問貴公司所屬的產業類別？', '請問公司主要產品/營業項目？', '請問貴公司目前的組織規模？',
       '請問貴公司主要經營的市場？', '請問貴公司今年度投入使用雲端服務或數位化工具的預算數為？',
       '請問貴公司未來導入雲端服務或數位化工具的時程規劃？',
       '請問貴公司在內部日常營運方面，目前已使用的雲端服務或數位化工具，大約在以下哪個階段？',
       '承上題，請問貴公司在內部日常營運方面，目前已使用的雲端服務或數位化工具，未來2年內希望提升到以下哪個階段？',
       '請問貴公司在產品排程方面，目前已使用的雲端服務或數位化工具，大約在以下哪個階段？',
       '承上題，請問貴公司在產品排程方面，目前已使用的雲端服務或數位化工具，未來2年內希望發展到以下哪個階段？',
       '因應疫情，請問貴公司在「遠距辦公線上協作」方面，目前有使用下列哪些線上協作工具？(可複選)',
       '承上題，請問貴公司在「遠距辦公線上協作」方面，未來2年內希望持續使用並嘗試導入下列哪些線上協作工具？(可複選)',
       '請問貴公司在「資訊安全」方面，目前有使用下列哪些方式/工具？(可複選)',
       '承上題，請問貴公司在「資訊安全」方面，未來2年內希望持續使用並嘗試導入下列哪些方式/工具？(可複選)',
       '請問貴公司在銷售管理與通路方面，目前有使用下列哪些方式/工具？(可複選)',
       '承上題，請問貴公司在銷售通路與管理方面，未來2年內希望持續使用並嘗試導入下列哪些方式/工具？(可複選)',
       '請問貴公司在行銷與客戶管理方面，目前有使用下列哪些方式/工具？(可複選)',
       '承上題，請問貴公司在行銷與客戶管理方面，未來2年內希望持續使用並嘗試導入下列哪些方式/工具？(可複選)',
       '請問貴公司在導入雲端服務或數位化工具的過程中，是否有遭遇過困難？', '請問貴公司遭遇過的困難包含以下哪些？(可複選)',
       '自評分數_內部日常營運', '自評分數_行銷與客戶管理', '自評分數_銷售管理與通路', '自評分數_資訊安全',
       '自評分數_遠距辦公線上協作', '自評分數_產品排程']]
sme_points =sme[['統一編號', '公司名稱','申請點數次數', '現有實際點數', '返還點數給平台', '點數狀態',
       'SME建立日期', '點數建立日期', '點數異動日期', '點數異動原因', '點數到期日期', '認證方式', '點數來源',
       '僅稅籍登記']]

sme_q_col =['sme_ban', 'sme_name','q_industry',
'q_mainproduct',
'q_organizationsize',
'q_marketplace',
'q_budget',
'q_planningtime',
'q_operation_now',
'q_operation_2y',
'q_schecule_now',
'q_schecule_2y',
'q_remote_now',
'q_remote_2y',
'q_security_now',
'q_security_2y',
'q_sales_now',
'q_sales_2y',
'q_marketing_now',
'q_marketing_2y',
'q_problems',
'q_difficulty',
'score_operation',
'score_marketing',
'score_sales',
'score_security',
'score_remote',
'score_schedule']

sme_questionnaire.columns = sme_q_col
sme_questionnaire[['q_industry',
'q_mainproduct',
'q_organizationsize',
'q_marketplace',
'q_budget',
'q_planningtime',
'q_operation_now',
'q_operation_2y',
'q_schecule_now',
'q_schecule_2y',
'q_remote_now',
'q_remote_2y',
'q_security_now',
'q_security_2y',
'q_sales_now',
'q_sales_2y',
'q_marketing_now',
'q_marketing_2y',
'q_problems',
'q_difficulty',]].fillna('NA', inplace=True)


sme_point_col =['sme_ban',
'sme_name',
'apply_time',
'points',
'return_points',
'point_status',
'sme_est_date',
'point_est_date',
'point_change_date',
'point_change_reason',
'point_due_date',
'authen_method',
'point_source',
'tax_applier']

sme_points.columns = sme_point_col

sme_basic.to_csv(directory_name+'/'+'sme_basic.csv')
sme_questionnaire.to_csv(directory_name+'/'+'sme_questionnaire.csv')
sme_points.to_csv(directory_name+'/'+'sme_points.csv')

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

smebasicpth= directory_name+ '/sme_basic.csv'
smeptpth =directory_name +'/sme_points.csv'
smequpath = directory_name + '/sme_questionnaire.csv'

upload_blob('tcloud_bq_files',smebasicpth,'sme_basic.csv')
upload_blob('tcloud_bq_files',smeptpth,'sme_points.csv')
upload_blob('tcloud_bq_files',smequpath,'sme_questionnaire.csv')
