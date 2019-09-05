rm -rf data/*
S1=$1
echo $S1 $S2
./step1.ksh $S1
java -jar genotick.jar reverse=data
./buildp.ksh $S1
./step2.ksh $S1
./executor.ksh $S1 
python advancedate.py $S1
rm -rf savedP*
rm -rf gen*log*.txt
