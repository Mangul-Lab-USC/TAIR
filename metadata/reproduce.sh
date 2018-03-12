
#Download GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.gct GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.gct from GTEx browser (publicly available)

head -n 3 GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.gct GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.gct GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.gct GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.header.gct

sed 's/\t/\n/g' GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.header.gct | grep -v Name | grep -v Description >samples.8555.txt

python prepare.metadata.py
#metadata of 8555 GTEx RNA-Seq samples is here curated.metadata.RNASeq.samples.8555.csv

#extract file names
awk -F "," '{print $1}' curated.metadata.RNASeq.samples.8555.csv > FileNames.RNASeq.8555.txt
