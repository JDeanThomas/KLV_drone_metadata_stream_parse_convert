### A bash program that uses Python and ffmpeg and converts drone footage to .MP4 and extracts KLV metadata by frame from MPEG video stream. Takes a directory as input and converts all files of the appropriate type.

### Python program also takes binary files of KLV metadata and parses them. Can be called from Bash program or by calling Python program klvdata_parser.py dirrectly on binary file. 

### Examples:

#### From bash script (takes directory as input):
```bash
bash klv.sh
```
#### From Python on static binary files:
```bash
python3 klvdata_parse.py Data/DynamicConstantMISMMSPacketData.bin
```

### Video sample:
```bash
$ wget http://samples.ffmpeg.org/MPEG2/mpegts-klv/Day%20Flight.mpg
```

### Binary metadata sample:
```bash
$ wget https://raw.githubusercontent.com/paretech/klvdata/master/data/DynamicConstantMISMMSPacketData.bin
```