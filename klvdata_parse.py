#!/usr/bin/env python3

import os
import sys
import klvdata
import collections

def parse_stream(inf):
    """ Compute the grid of alpha values for elastic net parameter search
    Parameters
    ----------
    inf : {stream from stdin, binary metadata file} Takes a stream of metadata
    from drone video mpeg file(s) or binary file(s) of drone metadata.

    """
    metadata = collections.OrderedDict()
    for packet in klvdata.StreamParser(inf):
    #for packet in klvdata.StreamParser(sys.stdin.buffer.read()):
        metadata.update(packet.MetadataList())
        #break #Capture only first packet
    metadata = dict(metadata)
    return metadata
       
            
if __name__ == '__main__':
    if sys.stdin.isatty():
        filename = sys.argv[-1]
        print(filename)
        inf = open('./' + filename, 'rb')
    else:
        print("is stdin")
        inf = sys.stdin.buffer.read()
    out = parse_stream(inf)
    #print(out)

    file_out = open("test_2.txt","w")
    file_out.write(str(out))
    file_out.close()
