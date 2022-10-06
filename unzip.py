import os
import zipfile
directory_name = '/home/tcloud_iii_gcp/test-flow'

for file_name in os.listdir(directory_name):
    i = os.path.join(directory_name, file_name)
    if os.path.isfile(i):
        print(i)

os.listdir(directory_name)
for file in os.listdir(directory_name):
  if '.zip' in file:
    zip_path = directory_name+'/'+file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
      zip_ref.extractall(directory_name)
