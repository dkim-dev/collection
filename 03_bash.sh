#!/bin/bash
i=1
biggest_num=$(ls | grep "log.[0-9]$" | sed 's/^.*\.//' | tail -1)
latest_num=$(( $biggest_num + 1 ))

while [ $latest_num -ne $i ] 
do
mv error.log.$biggest_num error.log.$latest_num
latest_num=$(( $latest_num - 1 ))
biggest_num=$(( $biggest_num - 1 ))
done
mv error.log error.log.1
touch error.log