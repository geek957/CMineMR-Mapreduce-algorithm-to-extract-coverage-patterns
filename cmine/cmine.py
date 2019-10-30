import time
import sys
# import numpy as np


class cmine():
	def __init__(self, minRF, minCS, maxOR, inpfile, outfile):
		self.minRF = minRF
		self.minCS = minCS
		self.maxOR = maxOR
		self.inpfile = inpfile
		self.outfile = outfile
		self.nots = self.getlines(inpfile)
	 	self.fout = open(outfile,'w')
		self.NOk = []
	 	self.items = self.dbscan(inpfile)



	 	sorteditems = sorted(self.items.items(), key = lambda a: (-a[1],a[0]))
		mintracs = self.minRF * 1.0 * self.nots
		freqitems = filter(lambda x: (x[1] >= mintracs), sorteditems)
		print freqitems
		one_size_coverage = filter(lambda x: (x[1] >= minCS*self.nots),freqitems)
		self.freqitems = map(lambda x: x[0], freqitems)

		for i in self.freqitems:
			self.NOk.append([i])
		for i in one_size_coverage:
			self.fout.write("['"+str(i[0])+"']\n")

	def get_overlapratio_cs(self, candidate):
		temp_candidate = []
		for pattern in candidate:
			temp_candidate.append([pattern,0,0,0])
		candidate = temp_candidate
		f = open(self.inpfile,'r')
		row = f.readline()
		while(row!=''):
			row = row.rstrip('\n')
			row = row.split(",")
			if len(row[-1]) == 0:
				row.pop()
			for i in range(len(candidate)):
				flag1 = False
				for item in candidate[i][0][:-1]:
					if item in row:
						candidate[i][1] += 1
						flag1 = True
						break
				if candidate[i][0][-1] in row:
					candidate[i][3] += 1
					if(flag1):
						candidate[i][2] += 1
					else:
						candidate[i][1] += 1
			row = f.readline()
		output = []
		f.close()
		for i in candidate:
			output.append([i[0],i[2]*1.0/i[3],i[1]*1.0/self.nots])
		return output

	def expand(self):
		cnt = 0
		cnt1 = 0
		length = 1
		candidate = []
		while len(self.NOk)>0:
			print "length",length,len(self.NOk)
			temp_NOk = self.NOk
			self.NOk = []
			candidate = []
			for i in range(len(temp_NOk)):
				for j in range(i+1, len(temp_NOk)):
					cnt += 1
					if temp_NOk[i][:-1] == temp_NOk[j][:-1]:
						cnt1 += 1
						newpattern = temp_NOk[i] + [temp_NOk[j][-1]]
						candidate.append(newpattern)
					else:
						break
			length += 1
			print "candidatesize",length,len(candidate)
			cnt1 += len(candidate) 
			candidate =  self.get_overlapratio_cs(candidate)
			for newpattern,overlapratio,cs in candidate:
				if overlapratio <= maxOR:
					self.NOk.append(newpattern)
					if cs >= minCS:
						self.fout.write(str(newpattern)+"\n")
		print "total read, total calculate_or_cs",cnt,cnt1
		self.fout.close()
		return cnt1



	def dbscan(self,inputfile):
		f=open(inputfile,'r')
		a = {}
		database = []
		for row in f:
			row = row.rstrip('\n')
			row = row.split(",")
			if len(row[-1]) == 0:
				row.pop()
			database.append(row)
			for j in row:
				if a.has_key(j):
					a[j] += 1
				else:
					a[j] = 1
		return a

	def getlines(self,filename):
		with open(filename,"r") as f:
			return sum(1 for _ in f)

t1 = time.time()
minRF = float(sys.argv[1])
minCS = float(sys.argv[2])
maxOR = float(sys.argv[3])
inpfile = sys.argv[4]
data = sys.argv[5]
# splitted = inpfile.split("/")
outfile = "./outputs/"+data+"/"+data+"_"+str(minRF)+"_"+str(minCS)+"_"+str(maxOR)+".txt"
obj = cmine(minRF, minCS, maxOR, inpfile, outfile)
t3 = time.time()
print "data read",str(t3-t1)
candidate_patterns = obj.expand()
t2 = time.time()
print "process done",str(t2-t1)
excel = open("./"+data+"_cmine.csv",'a')
excel.write("cmine"+","+str(minRF)+","+str(minCS)+","+str(maxOR)+","+inpfile+","+outfile+","+str(t3-t1)+","+str(t2-t1)+"\n")
excel.close()
