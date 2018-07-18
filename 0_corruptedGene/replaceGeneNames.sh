for i in ../1_correlationData/*.csv
do
    echo $i
    python3 replaceCorruptedGenes.py $i
    echo $i
done
