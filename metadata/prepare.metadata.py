import csv

print "Open updated_manifest.csv take only RNA-Seq and make dictionaries"


updated_manifest="updated_manifest.csv"

individuals=set()
tissues=set()
samples=set()
dict__sample__File_Name={}
File_NameSet_RNASeq=set()
dict__sample__body_site_s={}
samplesSet=set()



#samples from gene exppressions
samples_8555=set()
f=open("samples.8555.txt")
reader=csv.reader(f)
for line in reader:
    samples_8555.add(line[0])



#output
file=open("curated.metadata.RNASeq.samples.8555.csv","w")
file.write("fileName,sample,individual,tissue,raw.single.reads")
file.write("\n")

with open(updated_manifest, 'r') as f:
    csvFile = csv.reader(f)
    next(csvFile)
    for line in csvFile:
        
        

        if line[2]=="RNA-Seq":
            individual=line[24]
            sample=line[14]
            tissue=line[16]
            fileName=line[1]
	    n_reads=int(int((line[10]))/75.0*1000000)	            
            if sample in samples_8555:
                file.write(fileName+","+sample+","+individual+","+tissue+","+str(n_reads))
                file.write("\n")
            



	
file.close()






