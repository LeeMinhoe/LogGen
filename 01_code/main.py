# -*- coding: utf-8 -*-

from header import *
import optparse
import sys
import os
import random

def run():

	parser = optparse.OptionParser('main.py')

	# Target option
	parser.add_option("-d", dest="path", metavar="target dir path", help="target's Directory path")
	parser.add_option("-f", dest="file", metavar="target json file name", help="target Json file name")

	# dummy option
	parser.add_option("-t", dest="thread", metavar="thread num", type='int', help="Threads num")

	# pulse time option
	parser.add_option("-s", dest="steady", metavar="sec", type='float', help="input : float - steady pulse time (sec)")
	parser.add_option("-r", dest="random", metavar="from to", type='int', nargs=2, help="input : int ,int - random pulse time range from (int) to (int)")
	parser.add_option("-g", dest="gauss", metavar="avg sd", type='int', nargs = 2, help="input : int, int - Average, Standard Deviation / According to gaussian distributions")

	# loop option
	parser.add_option("-l", dest="loop", metavar="loop num", type='int', help="input : -1(infinite loop), n(Packet Scenario repeat")
	
	(options, args) = parser.parse_args()
	# Need Modi
	# 입력인자가 없다면 종료
	if len(sys.argv)-1 == 0:
		printe(parser.usage)
		exit(1)
	
	# Make Class Packet and Store Information
	# 파일을 읽어서 패킷 리스트로 읽음
	PKT_List = ReadJsonFile(options)

	# Find Total Packet Number in Packet List
	total_pkt_num = 0
	for pkt in PKT_List:
		total_pkt_num += pkt.Data_part.pps

	# Find Loop Count (need exception)
	loopCount = options.loop

	'''
	# check loop num
	if options.loop == None :
		printe("insert loop option")
		exit(1)
	'''


	######### Insert Loop Here #########



	# Identify Dummy mode or Pulse time mode in this Scenario
	ThOrTime = identifyMode(options, total_pkt_num)
	
	
	# Verification and Convertion
	for p in PKT_List :
		veri_type_checker(p.Data_part.DataField)
		RandToValue(p.Data_part.DataField)
		Converter(p.Data_part.DataField)
		veri_range_checker(p.Data_part.DataField)

	# Transmission  Here

	#for pkt in PKT_List :
	#	pkt.print_packet_info()

	# Print Result 
	print(" * Total Packet Number : " + str(total_pkt_num))
	if type(ThOrTime) == int :
		print(" *     Tread Number    : " + str(ThOrTime))
	elif type(ThOrTime) == list :
		print(" *     Time Table      : " + str(ThOrTime))
	print(" *     Loop   Count    : " + str(loopCount))


if __name__ == "__main__":
	run()
