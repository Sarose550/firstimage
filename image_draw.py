def DoIt(filename):
	foutput = open(filename, 'w')
	foutput.write("P3 500 500 255\n")
	for i in range(500):
		for j in range(500):
			foutput.write(str((i+j)%256) + " " + str((i+255*j)%256) + " " + str(j % 256))
			if(not(i == 500 and j == 500)):
				foutput.write(" ")
	foutput.close()


DoIt("image.ppm")
