def delblankline(infile, outfile):
 infopen = open(infile, 'r')
 outfopen = open(outfile, 'w')

 lines = infopen.readlines()
 for line in lines:
  if line.split():
   outfopen.writelines(line)
  else:
   outfopen.writelines("")

 infopen.close()
 outfopen.close()

delblankline("/home/wode/roll.txt", "/home/wode/roll1.txt")