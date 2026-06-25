actual_bytes=$(du -shb ..  | awk '{print $1}')
B="$(( actual_bytes%1024 ))"
KB=$(( (actual_bytes/1024)%1024 ))
MB=$(( (actual_bytes/1024/1024)%1024 ))
GB=$(( actual_bytes/1024/1024/1024 ))


echo "The directory size is ${GB}GB ${MB}MB ${KB}KB ${B}Bytes" 