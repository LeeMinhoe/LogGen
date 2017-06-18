import json
import os
from color import *

#############################################################
# Packet의 해더 관련 부분 Class
class Packet_Header:
	# 초기화 함수
	def __init__(self, dst_ip, dst_port, protocol):
		self.dst_ip = dst_ip
		self.dst_port = int(dst_port)
		self.protocol = protocol
	# Packet Header info 출력문
	def print_Header_info(self):
		print("* IP address : ", self.dst_ip)
		print("* port address : ", self.dst_port)
		print("* protocol : ", self.protocol)
#############################################################


#############################################################
# Packet의 데이터 관련 부분 Class
class Packet_Data:
	# 초기화
	def __init__(self, pps, json_file_name, DataField):
		self.pps = int(pps)
		self.json_file_name = json_file_name
		self.DataField = DataField
	# Packet Data info 출력문
	def print_Data_info(self):
		print("* pps : ", self.pps)
		print("* json_file_name : ", self.json_file_name)
		print("* Data Field in Json")	
		for DS in self.DataField:
			print("#")
			for data in DS:
				print("    " + str(data))
		#print(self.DataField)
		print("##########################")
#############################################################


#############################################################
# Packet Class : Header + Data
# 해더와 데이터 부분을 더한 클래스
class Packet:
	# 초기화
	def __init__(self, Header_part, Data_part):
		self.Header_part = Header_part
		self.Data_part = Data_part
	# Packet Info 출력문
	def print_packet_info(self):
		print("######################")
		print("####Packet Info.######")
		print("######################")
		self.Header_part.print_Header_info()
		self.Data_part.print_Data_info()
#############################################################
