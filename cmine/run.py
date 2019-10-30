import os

# bmspos
# data = "bmspos"
# print data
# for i in range(10,100,10):
#     maxOR = str(i/100.0)
#     os.system("python cmine.py 0.060 0.4 "+maxOR+" ../dataset/"+data+".txt "+data)

# for i in range(10,100,10):
#     minCS = str(i/100.0)
#     os.system("python cmine.py 0.060 "+minCS+" 0.7 ../dataset/"+data+".txt "+data)

# mushroom
# data = "mushroom"
# print data
# for i in range(10,100,10):
#     maxOR = str(i/100.0)
#     os.system("python cmine.py 0.1 0.3 "+maxOR+" ../dataset/"+data+".txt "+data)

# for i in range(10,100,10):
#     minCS = str(i/100.0)
#     os.system("python cmine.py 0.1 "+minCS+" 0.5 ../dataset/"+data+".txt "+data)

# synthetic
data = "synthetic"
print data
# for i in range(5,51,5):
#     maxOR = str(i/100.0)
#     os.system("python cmine.py 0.045 0.3 "+maxOR+" ../dataset/"+data+".txt "+data)

for i in range(10,100,10):
    minCS = str(i/100.0)
    os.system("python cmine.py 0.045 "+minCS+" 0.25 ../dataset/"+data+".txt "+data)

#kosarak
# data = "kosarak"
# print data
# for i in range(10,100,10):
#     maxOR = str(i/100.0)
#     os.system("python cmine.py 0.025 0.5 "+maxOR+" ../dataset/"+data+".txt "+data)

# for i in range(10,100,10):
#     minCS = str(i/100.0)
#     os.system("python cmine.py 0.025 "+minCS+" 0.5 ../dataset/"+data+".txt "+data)

