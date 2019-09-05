for i in {1..7}
do
	CURRENT_POP=$(python getpopulation.py $i $1)
	echo $CURRENT_POP
	./step3.ksh $CURRENT_POP $1
done
