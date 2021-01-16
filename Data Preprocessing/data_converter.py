import glob
import os
#path = "/test"
#read_files = glob.glob(os.path.join(path, "*.txt"))
"""
with open("XXX.txt", "w") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            outfile.write(infile.read())
            outfile.write("1")
"""	
			
			
path = '/test'
i=0
with open("out.txt","w") as outfile:
   for filename in glob.glob(os.path.join(path, '*.txt')):
	    outfile.write(filename)





#with open(os.path.join(os.cwd(), filename), 'r') as f:
#i+=1
#outfile.write(i)
#outfile.write(filename)