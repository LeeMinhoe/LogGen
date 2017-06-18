import json
import os
from color import *

#############################################################
# Packet�� �ش� ���� �κ� Class
class Packet_Header:
	# �ʱ�ȭ �Լ�
	def __init__(self, dst_ip, dst_port, protocol):
		self.dst_ip = dst_ip
		self.dst_port = int(dst_port)
		self.protocol = protocol
	# Packet Header info ��¹�
	def print_Header_info(self):
		print("* IP address : ", self.dst_ip)
		print("* port address : ", self.dst_port)
		print("* protocol : ", self.protocol)
#############################################################


#############################################################
# Packet�� ������ ���� �κ� Class
class Packet_Data:
	# �ʱ�ȭ
	def __init__(self, pps, json_file_name, DataField):
		self.pps = int(pps)
		self.json_file_name = json_file_name
		self.DataField = DataField
	# Packet Data info ��¹�
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
# �ش��� ������ �κ��� ���� Ŭ����
class Packet:
	# �ʱ�ȭ
	def __init__(self, Header_part, Data_part):
		self.Header_part = Header_part
		self.Data_part = Data_part
	# Packet Info ��¹�
	def print_packet_info(self):
		print("######################")
		print("####Packet Info.######")
		print("######################")
		self.Header_part.print_Header_info()
		self.Data_part.print_Data_info()
#############################################################
