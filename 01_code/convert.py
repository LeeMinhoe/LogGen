from header import *
import optparse
import sys
import os
import random
import string
import time
import datetime
import binascii
import socket
import inspect


def ReadJsonFile(options):
	Product = []

	# init target path
	# 파일 이름 입력이 없으면 종료
	current_file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	if options.file == None :
		printe("not input target file variable")
		exit(1)
	
	# 디렉토리 주소 입력 없을때
	if options.path == None :
		target_dir_path = current_file_path + "/../99_JSON"
	# 디렉토리 주소가 절대경로일때
	elif (options.path).startswith("/") == True:
		target_dir_path = options.path
	# 디렉토리 주소가 상대경로일때
	elif (options.path).startswith("/") == False:
		target_dir_path = os.getcwd() + '/' + options.path
	
	# 디렉토리 주소 + 파일 이름
	target_json_path = target_dir_path + '/' + options.file
	print("\n * Target Directory's Path : " + str(target_dir_path))
	print(" * Target Json file's Path : " + str(target_json_path))

	# make file list
	# 파일 리스트 생성
	fileList = []
	if options.file == "header.json" or options.file == "*.json" :
		for f in os.listdir(target_dir_path) :
			if f.endswith(".json") and f != "header.json":
				fileList.append(f)
	elif (options.file).endswith(".json") :
		fileList.append(options.file)
	else :
		printe("file name error")
		exit(1)
	fileList.sort()

	
	# Print List of File Name
	# 파일 리스트 출력
	print("======= File List =======")
	for file_n in fileList:
		print("  * " + file_n)
	print("=========================")


	# change dir
	# 디렉토리 위치 변경
	os.chdir(target_dir_path)


	PKT = []
	for f in fileList :
		if options.file == "header.json" :
			with open("header.json") as data_file:
				DS = json.load(data_file)
			dst_ip = DS["Header"][0]["IP"]
			dst_port = DS["Header"][0]["Port"]
			protocol = DS["Header"][0]["Protocol"]
			pps = DS["Header"][0]["pps"]
			Data = []
			with open(f) as data:
				Data.append(json.load(data)["Data"])
			header_p = Packet_Header(dst_ip, dst_port, protocol)
			data_p = Packet_Data(pps, f, Data)
			packet = Packet(header_p, data_p)
			#packet.print_packet_info()
			PKT.append(packet)

		else :
			with open(f) as data_file:
				DS = json.load(data_file)
			dst_ip = DS["Header"][0]["IP"]
			dst_port = DS["Header"][0]["Port"]
			protocol = DS["Header"][0]["Protocol"]
			pps = DS["Header"][0]["pps"]
			Data = []
			Data.append(DS["Data"])
			header_p = Packet_Header(dst_ip, dst_port, protocol)
			data_p = Packet_Data(pps, f, Data)
			packet = Packet(header_p, data_p)
			#packet.print_packet_info()
			PKT.append(packet)

	return PKT


def identifyMode(options, total_pkt_num) :
	
	# check dummy or pulse time ### product : Thread Num or Time Table	 
	  ## option and 
	if options.thread != None and ( options.steady != None or options.random != None or options.gauss != None ) :
		printe("#0 check dummy or pulse time option")
		exit(1)

	if options.thread != None :
		thread_num = options.thread
		#print("Thread Num : " + str(thread_num))
		return options.thread
	
	elif options.steady != None or options.random != None or options.gauss != None and options.thread == None:
		round_cipher = 4
		Time_table = []
		if options.steady != None and len(Time_table) == 0 :
			for i in range(total_pkt_num):
				Time_table.append(round(options.steady, round_cipher))
		elif options.steady != None and len(Time_table) != 0:
			printe("#1 check dummy or pulse time option")
			exit(1)

		if options.random != None and len(Time_table) == 0 :
			for i in range(total_pkt_num):
				Time_table.append(round(random.uniform(options.random[0], options.random[1]), round_cipher))
		elif options.random != None and len(Time_table) != 0:
			printe("#2 check dummy or pulse time option")
			exit(1)

		if options.gauss != None and len(Time_table) == 0 :
			avg = options.gauss[0]
			sd = options.gauss[1]
			for i in range(total_pkt_num):
				g = random.gauss(avg, sd)
				Time_table.append(round(-1 * g if g < 0 else g, round_cipher))
		elif options.gauss != None and len(Time_table) != 0:
			printe("#3 check dummy or pulse time option")
			exit(1)
	
		#print("Time table : " + str(Time_table))

		return Time_table

	else :
		printe("#4 check dummy or pulse time option")
		exit(1)



def str_generator(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))



def RandToValue(DataStructure):

	# DataStructure is Json format data list
	# DataStructure's type is short, unsigned short, int, unsigned int, long long
		# value is just value -> Random value in this value's type range
		# value type is list -> Random value in this list
		# value is "Random" -> Random value from Random Min to Random Max
	
		
	# DataStructure tour
	# Integer Random value
	for DS in DataStructure:
		for Data in DS:

			## List input (list random)
			if type(Data["value"]) is list:
				Data["value"] = random.sample(Data["value"], 1)[0]
			## is Integer
			if (Data["Type"] == "short" or Data["Type"] == "unsigned short"
			or Data["Type"] == "int" or Data["Type"] == "unsigned int"
			or Data["Type"] == "long long" or Data["Type"] == "unsigned long long") :
				if Data["value"] == "random":
					Data["value"] = random.randint(Data["random min"], Data["random max"])

				elif type(Data["value"]) is int:
					pass

			## is str
			elif (Data["Type"] == "str"):
				if type(Data["value"]) is int :
					Data["value"] = str_generator(Data["value"])
				
				elif type(Data["value"]) is str:
					pass

			## is time
			elif (Data["Type"] == "time"):
				if Data["value"] == "Random" :
					Data["value"] = random.randint(0, int(time.time()))
			
			## is str
			elif (Data["Type"] == "struct in_addr"):
				
				if Data["value"].count("Random") :
					if Data["value"][0] == 'B':	Data["value"] = 'B'
					else : Data["value"] = ''
					#print(Data["value"])
					Data["value"] += '.'.join('%s'%random.randint(0, 255) for i in range(4))

				elif Data["value"] == "random" :
					min = int((binascii.hexlify(socket.inet_aton(Data["addr min"]))).decode(), 16)
					max = int((binascii.hexlify(socket.inet_aton(Data["addr max"]))).decode(), 16)
					randip = random.randint(min, max)
					randip_hex_str = str(hex(randip)).split('0x')[1]
					if len(randip_hex_str) != 8: 
						for i in range(8-len(randip_hex_str)):
							randip_hex_str = '0'+ randip_hex_str
					randip_list = []
					for i in range(4):
						randip_list.append(str(int('0x' + randip_hex_str[i*2:i*2+2], 16)))
					Data["value"] = '.'.join(randip_list)

			## is hex
			elif (Data["Type"] == "hex"):
				if Data["value"] == "Random":
					#print(Data["value"])
					#print(Data["Type"])
					Data["value"] = hex(random.randint(int(Data["random min"], 16), int(Data["random max"], 16)))
					
					
			## is MAC addr
			elif (Data["Type"] == "MAC addr"):
				if Data["value"] == "Random" :
					x = []
					for i in range(6):
						k = hex(random.randint(0,255)).split('0x')[1]
						if len(k) == 2:
							pass
						else : 
							for j in range(2-len(k)):
								k = '0' + k
						x.append(k)
					Data["value"] = ':'.join(x)
				elif Data["value"] == "random" :
					min = int(Data["addr min"].replace(':', ''), 16)
					max = int(Data["addr max"].replace(':', ''), 16)

					r = hex(random.randint(min, max)).split('0x')[1]

					if len(r) != 12:
						for i in range(12-len(r)):
							r = '0' + r
			
					Data["value"] = ':'.join([r[i:i+2] for i in range(0, len(r), 2)])
					



def Converter(DataStructure):

	for DS in DataStructure:
		for Data in DS:

			if (Data["Type"] == "char" and type(Data["value"]) is int):
				Data["value"] = chr(Data["value"])

			elif Data["Type"] == "time" :
				if Data["value"] == "now":
					Data["value"] = int(time.time())
				elif type(Data["value"]) is str:
					d = datetime.datetime.strptime(Data["value"], '%Y-%m-%d %H:%M:%S')
					Data["value"] = int(time.mktime(d.timetuple()))

			elif Data["Type"] == "bool" :
				if Data["value"] == 1:
					Data["value"] = True
				elif Data["value"] == 0:
					Data["value"] = False