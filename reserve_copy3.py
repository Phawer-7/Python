import os
import time

run = True
while run:
	source = ['/media/kali/a7f546ed-d5e9-4fcc-84f6-02ea72e4bb78/home/kamol/Python/a_byte_of_py/reserve_copy2/'] #файлы которых необходимо скопировать
	target_dir='/media/kali/a7f546ed-d5e9-4fcc-84f6-02ea72e4bb78/home/kamol/Kali/' #путь, куда необходимо скопировать файлов

	today=target_dir+os.sep+time.strftime('%Y%m%a%H%M%S')

	now=time.strftime('%H%M%S')

	comment=input('Enter the comment:')
	if len(comment)==0:
		target=today+os.sep+now+'.zip'
	else:
		target=today+os.sep+now+'_'+ \
			comment.replace(' ','_')+'.zip'

	if not os.path.exists(today):
		os.mkdir(today)
		print('COMPLETED, your zip file:',today)

	zip_command="zip -qr {0} {1}".format(target, '  '.join(source))

	if os.system(zip_command)==0:
		print('COMPLETED, your zip file:', target)
	else:
		print('FAILED')

	runOrNo = input('stop the programm? (Y/n)')
	if runOrNo=='Y' or len(runOrNo)==0:
		print('Closing the programm')
		run = False
	elif runOrNo == 'n':
		print('Ok!')
	else:
		run=False

def help():
	'''Программа создает резервные копии всех наших важных файлов'''







