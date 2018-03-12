echo "Number of receptor derived reads"
awk -F "," '{s+=$9+$10+$11} END {print s}' ../summary.CDR3.txt 

echo "Number of receptor derived reads VDJ"
awk -F "," '{s+=$9+$10+$11} END {print s}' ../summary.VDJ.txt

