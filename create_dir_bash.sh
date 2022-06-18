start=16
end=29
for((i=$start;i<=$end;i++))
do
  mkdir -p "noise2ppg_mimicIII_all_s${i}"/{trainA,trainB,testA,testB}
done
