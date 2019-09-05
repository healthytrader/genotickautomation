for i in {1..600}
do
	java -jar genotick.jar input=random
done
python uploader.py $1
