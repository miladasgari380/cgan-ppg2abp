start=16
end=29
for((i=$start;i<=$end;i++))
do
	#python train.py --dataroot "/home/milad/pyPPG-ABP/noise2ppg_mimicIII_all_s${i}" --name "ppg2abp_mimicIII_all_s${i}" --model cycle_gan --n_epochs=20 --n_epochs_decay=5 --gpu_ids 0,1,2,3 --batch_size 16 --norm instance
	python test.py --dataroot "/home/milad/pyPPG-ABP/noise2ppg_mimicIII_all_s${i}" --name "ppg2abp_mimicIII_all_s${i}" --model cycle_gan --num_test=6000
done
