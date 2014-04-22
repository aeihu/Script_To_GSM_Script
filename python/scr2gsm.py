import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import codecs

def scr2gsm (filename, boxname):
	f = codecs.open(filename,"r","utf-8")
	strs = []
	while True:
		line = f.readline()
		if len(line) == 0: 
			break
		strs.append(line[0:len(line)-1])
		
	f.close() 
	
	length = len(strs)
	if length != 0:
		if strs[0].find(codecs.BOM_UTF8) == 0:
			strs[0] = strs[0][3:]
			
		outfile = codecs.open("out_"+filename,"w","utf-8")
		
		for i in range(0,length):
			if strs[i].find('                              ') == 0: #name
				offset = 1
				cmd = '@msg -n \"' + boxname + '\" -s \"' + strs[i][30:len(strs[i])-1] + '\" -m \"'
				
				while strs[i+offset].find('                    ') == 0:#word
					cmd += strs[i+offset][20:len(strs[i+offset])-1]
					offset+=1
					if i+offset >= length:
						offset-=1
						break
						
				cmd += '\";\r\n'
				i+=offset
				outfile.write(cmd)

		outfile.close()