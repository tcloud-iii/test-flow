import os
#下載、解壓縮、檔案zip送到GCS
os.system('python3 /home/tcloud_iii_gcp/test-flow/get_zipfiles.py')

#資料轉格式
directory_name = '/home/tcloud_iii_gcp/test-flow'

for file in os.listdir(directory_name):
    if 'de_' in file:
      pyfile = 'python3 '+'directory_name'+'/'+file
      os.system(pyfile)
print("Files proceed done!")

#清除檔案
os.system('python3 /home/tcloud_iii_gcp/test-flow/file_remove.py')
