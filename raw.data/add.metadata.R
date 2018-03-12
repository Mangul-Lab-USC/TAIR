#!/usr/bin/env Rscript

cdr3.data=read.csv("summary.CDR3.txt")
metadata=read.csv("../metadata/curated.metadata.RNASeq.samples.8555.csv")

data=merge(metadata,cdr3.data,by="fileName")

data$CPM.IGH=(data$nIGH/data$raw.single.reads)*100000
data$CPM.IGK=(data$nIGK/data$raw.single.reads)*100000
data$CPM.IGL=(data$nIGL/data$raw.single.reads)*100000

data$titration.IGH=(data$loadIGH/data$raw.single.reads)*100000
data$titration.IGK=(data$loadIGK/data$raw.single.reads)*100000
data$titration.IGL=(data$loadIGL/data$raw.single.reads)*100000

data$immune.diverity.IGH=data$alphaIGH
data$immune.diverity.IGK=data$alphaIGK
data$immune.diverity.IGL=data$alphaIGL

write.csv(data, file = "../TheAIR.CDR3.csv")


