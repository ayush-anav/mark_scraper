# follow syntax properly, thats how it is written with the right spaces
if [ -f lowest_to_highest.txt ]; then 
	rm lowest_to_highest.txt
elif [ -f highest_to_lowest.txt ]; then
	rm highest_to_lowest.txt
else
	echo nothing to delete
fi
