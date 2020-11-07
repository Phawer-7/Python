import os
import time

source = ['']

target_dir=''

target=target_dir+os.sep+time.strftime('%Y%m%a%H%M%S') + '.zip'

zip_command="zip -qr {0} {1}".format(target, '  '.join(source))

if os.system(zip_command)==0:
	print('COMPLETED, your zip file:', target)
else:
	print('FAILED')
