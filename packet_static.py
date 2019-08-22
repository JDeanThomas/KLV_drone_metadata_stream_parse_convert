#!/usr/bin/env python3

import klvdata


if __name__ == "__main__":
	with open('./DynamicConstantMISMMSPacketData.bin', 'rb') as f:
		for packet in klvdata.StreamParser(f):
			#packet.structure()
			#metadata=packet.MetadataList()
			#print(metadata)
			print(type(packet))
			