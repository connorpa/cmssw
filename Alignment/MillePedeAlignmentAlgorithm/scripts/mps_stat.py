import mpslib.Mpslibclass as mpslib
import os

#use mps_update.pl in shell and push output to nirvana
os.system("mps_update.py")  #add >| /dev/null

lib = mpslib.jobdatabase()	#create object of class jobdatabase
lib.read_db()				#read mps.db into the jobdatabase
lib.print_memdb()			#print the jobdatabase in memory
