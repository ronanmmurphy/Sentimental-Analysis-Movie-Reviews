i=1
with open('full_test.txt', 'r', encoding ="utf8") as istr:
    with open('test1.txt', 'w') as ostr:
        for line in istr:
            if(i<=12500):
                line = line.rstrip('\n') + '\t1'
            else:
                line = line.rstrip('\n') + '\t0'
            print(line, file=ostr)
            i+=1
			
		