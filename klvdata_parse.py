#!/usr/bin/env python3

import os
import sys
import klvdata
import collections

def parse_stream(inf):
    """ Parse KLV metadata from drone mpeg footage, taken as packets from a
    stream (ffmpeg) or a binary file containing the metadata.

    Can be called from a Bash pipeline, or directly on file from Python.
    ----------
    inf : {stream from stdin, binary metadata file} Takes a stream of metadata
    from drone video mpeg file(s) or binary file(s) of drone metadata.

    """
    metadata = collections.OrderedDict()
    for packet in klvdata.StreamParser(inf):
        metadata.update(packet.MetadataList())
        #break #Capture only first packet
    metadata = dict(metadata)
    return metadata
       
            
if __name__ == '__main__':
    """ Detects if the file input is stdin (called from a Bash pipeline or is
    being called dirrecty on a binary file of KLV metadata.

    """
    if sys.stdin.isatty():
        filename = sys.argv[-1]
        inf = open('./' + filename, 'rb')
        out = parse_stream(inf)
        file_out = open("test_2.txt", "w")
        file_out.write(str(out))
        file_out.close()
    else:
        inf = sys.stdin.buffer.read()
        out = parse_stream(inf)
        print(out)
