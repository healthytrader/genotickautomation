rm -rf results.txt
rm -rf data/xxx.csv
rm -rf data/rev*
cp xxx.csv data
python genoa2.py $1 $2
java -jar genotick.jar reverse=data
java -jar genotick.jar input=file:input.txt > output.txt
#python genob.py $2 >> results.txt
python analyzer2.py $1
