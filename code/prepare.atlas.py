import csv
import statistics
import sys

file=open("TheAIR.CDR3.csv")

reader=csv.reader(file)


tissues=set()

IGH_dict={}
n_reads_IGH={}

N_raw_reads={}


fileOut_IGH=open("../TheAIR.CDR3.IGH.csv","w")
fileOut_IGK=open("../TheAIR.CDR3.IGK.csv","w")
fileOut_IGL=open("../TheAIR.CDR3.IGL.csv","w")


#"","fileName","sample","individual","tissue","raw.single.reads","nIGH","nIGK","nIGL","nTCRA","nTCRB","nTCRD","nTCRG","loadIGH","loadIGK","loadIGL","loadTCRA","loadTCRB","loadTCRD","loadTCRG","alphaIGH","alphaIGK","alphaIGL","alphaTCRA","alphaTCRB","alphaTCRD","alphaTCRG","CPM.IGH","CPM.IGK","CPM.IGL","titration.IGH","titration.IGK","titration.IGL","immune.diverity.IGH","immune.diverity.IGK","immune.diverity.IGL"

fileOut_IGH.write("sample,fileName,individual,tissue,n.raw.reads,CPM,igRPM,immune.diversity\n")
fileOut_IGK.write("sample,fileName,individual,tissue,n.raw.reads,CPM,igRPM,immune.diversity\n")
fileOut_IGL.write("sample,fileName,individual,tissue,n.raw.reads,CPM,igRPM,immune.diversity\n")



next(reader, None)  # skip the headers

for line in reader:
    fileName=line[1]
    sample=line[2]
    individual=line[3]
    tissue=line[4]
    raw_single_reads=float(line[5])
    nIGH=int(line[6])
    nIGK=int(line[7])
    nIGL = int(line[9])
    loadIGH=int(line[13])
    loadIGK = int(line[14])
    loadIGL = int(line[15])
    alphaIGH = float(line[20])
    alphaIGK = float(line[21])
    alphaIGL = float(line[22])

    CPM_IGH=1000000*nIGH/raw_single_reads
    CPM_IGK = 1000000 * nIGK / raw_single_reads
    CPM_IGL = 1000000 * nIGL / raw_single_reads

    IGHRPM=1000000*loadIGH/raw_single_reads
    IGKRPM = 1000000 * loadIGK / raw_single_reads
    IGLRPM = 1000000 * loadIGH / raw_single_reads

    fileOut_IGH.write(sample+","+ fileName + ","+ individual + ","+ tissue +","+ str(raw_single_reads)+ ","+str(CPM_IGH)+ "," + str(IGHRPM)+ "," + str(alphaIGH))
    fileOut_IGH.write("\n")
    fileOut_IGK.write(sample+","+ fileName + ","+ individual + ","+ tissue +","+ str(raw_single_reads)+ ","+str(CPM_IGK)+ "," + str(IGKRPM)+ "," + str(alphaIGK))
    fileOut_IGK.write("\n")
    fileOut_IGL.write(sample+","+ fileName + ","+ individual + ","+ tissue +","+ str(raw_single_reads)+ ","+str(CPM_IGL)+ "," + str(IGLRPM)+ "," + str(alphaIGL))
    fileOut_IGL.write("\n")


fileOut_IGH.close()
fileOut_IGK.close()
fileOut_IGL.close()

file.close()

