#!/usr/bin/env bash

echo "How many loops Do You Want?"
read LOOPS

COUNT=1
while [ $COUNT -le $LOOPS ]
do
	echo " Loop# $COUNT "
	((COUNT++))
done

