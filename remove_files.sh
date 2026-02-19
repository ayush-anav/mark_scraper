# follow syntax properly, thats how it is written with the right spaces
if [ -f lowest_to_highest.txt ]; then 
	rm lowest_to_highest.txt
	echo lowest_to_highest.txt deleted
elif [ -f highest_to_lowest.txt ]; then
	rm highest_to_lowest.txt
	echo highest_to_lowest.txt deleted
else
	echo nothing to delete
fi
