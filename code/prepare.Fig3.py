import csv
import statistics
import sys

file=open("TheAIR.CDR3.csv")

reader=csv.reader(file)


tissues=set()

IGH_dict={}
n_reads_IGH={}

N_raw_reads={}



#"","fileName","sample","individual","tissue","raw.single.reads","nIGH","nIGK","nIGL","nTCRA","nTCRB","nTCRD","nTCRG","loadIGH","loadIGK","loadIGL","loadTCRA","loadTCRB","loadTCRD","loadTCRG","alphaIGH","alphaIGK","alphaIGL","alphaTCRA","alphaTCRB","alphaTCRD","alphaTCRG","CPM.IGH","CPM.IGK","CPM.IGL","titration.IGH","titration.IGK","titration.IGL","immune.diverity.IGH","immune.diverity.IGK","immune.diverity.IGL"

next(reader, None)  # skip the headers

for line in reader:
    tissue=line[4]
    if "Brain" in tissue:
        tissues.add("Brain")
    else:
        tissues.add(tissue)


print (len(tissues))

file.close()


for t in tissues:
    IGH_dict[t]=[]
    n_reads_IGH[t]=[]


file=open("TheAIR.CDR3.csv")
reader=csv.reader(file)
next(reader, None)  # skip the headers


for line in reader:
    n_raw_reads=float(line[5])
    tissue=line[4]
    nIGH=1000000*int(line[6])/n_raw_reads
    loadIGH = 1000000*int(line[13])/n_raw_reads
    if "Brain" in tissue:
        tissue="Brain"
        IGH_dict[tissue].append(nIGH)
        n_reads_IGH[tissue].append(loadIGH)
    else:
        IGH_dict[tissue].append(nIGH)
        n_reads_IGH[tissue].append(loadIGH)


file.close()


fileOut=open("Fig3.raw.data.csv","w")
fileOut.write("tissue,median.IGH,median.IGH.reads")
fileOut.write("\n")

for key, value in IGH_dict.items():
    if (len(value)>10):
        medianIGH=statistics.median(value)
        medianIGH_n_reads=statistics.median(n_reads_IGH[key])
        fileOut.write(key+","+str(medianIGH)+","+str(medianIGH_n_reads))
        fileOut.write("\n")
fileOut.close()