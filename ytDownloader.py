import os

try:
	import pytube
except:
	print ('Downloading pytube model - (REQUIRED)')
	os.system('pip install pytube')
	import pytube
	os.system('cls')



def show_progress_bar(stream, file_handle, bytes_remaining):
	contentSize = video.filesize
	size = contentSize - bytes_remaining

	print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
	'█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')



while True:
	try:
		ytLink = input ('Enter youtube video link to download (q=exit) : ')					# FOR PYTHON 3
		#ytLink = raw_input ('Enter youtube video link to download (q=exit) : ')			# FOR PYTHON 2
		if ytLink == 'q' or ytLink == 'Q':
			exit()
		yt = pytube.YouTube(ytLink, on_progress_callback=show_progress_bar)
		break
	except SystemExit:
		print ('Exited...')
		exit()
	except:
		print ('Link is incorrenct!!! Or probably something else went wrong ¯\_(ツ)_/¯')	


req_streams = yt.streams.filter(subtype='mp4')
only_audio = req_streams.filter(only_audio=True)
video_audio = req_streams.filter(progressive=True)
only_video = req_streams.filter(only_video=True)

v_a = 'Video + Audio'
v = 'Video'
a = 'Audio'

os.system('cls')

print ('----------------------------------------------------------------')

print ()

for st in video_audio.order_by('resolution'):
	print ('Code {0} : {1}  {2}'.format(st.itag, st.resolution, v_a))

print ()

for st in only_video.order_by('resolution'):
	print ('Code {0} : {1}  {2}'.format(st.itag, st.resolution, v))

print ()

for st in only_audio:
	print ('Code {0} : {1}  {2}'.format(st.itag, st.abr, a))

print ()

print ('----------------------------------------------------------------')

print ()


while True:
	try:
		download_code = input ('Enter a code to download (q=exit) :')			# FOR PYTHON 3
		#download_code = raw_input ('Enter a code to download (q=exit) :')		# FOR PYTHON 2
		if download_code == 'q' or download_code == 'Q':
			exit()
		if req_streams.get_by_itag(download_code):
			break
		else:
			print ('Code is incorrect!')	
	except SystemExit:
		print ('Exited...')
		exit()
	except:
		print ('Watch your language! I only read integers.')


print ()

try:
	video = req_streams.get_by_itag(download_code)
	video.download()
except:
	print ('Something went wrong! ¯\_(ツ)_/¯')
