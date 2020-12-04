N=256
njobs=12

#6_1
A=0

for((i=0;i<${njobs};i++)); 
	do  
	A=$(($i*$N)); 
	cmsRun step3.py wf=-1 n=$N threads=8 skip=$A timing=False patatrack=False doregion=False pixtrip=False allpata=False nol1=False keepDup=99 keepBad=99 & 
done

wait 

cmsRun step3.py wf=-1 n=$N threads=4 skip=$A timing=True patatrack=False doregion=False pixtrip=False allpata=False nol1=False keepDup=99 keepBad=99 &&

wait

cmsRun step3.py wf=-1 n=$N threads=8 skip=$A timing=True patatrack=False doregion=False pixtrip=False allpata=False nol1=False keepDup=99 keepBad=99 && 

wait

cmsRun step3.py wf=-1 n=$N threads=16 skip=$A timing=True patatrack=False doregion=False pixtrip=False allpata=False nol1=False keepDup=99 keepBad=99 && 


#6_2
for((i=0;i<${njobs};i++));
        do
        A=$(($i*$N));
        cmsRun step3.py wf=-1 n=$N threads=8 skip=$A timing=False patatrack=True doregion=False pixtrip=False allpata=False nol1=False keepDup=99 keepBad=99 &
done

wait

A=0

cmsRun step3.py wf=-1 n=$N threads=4 skip=$A timing=True patatrack=True doregion=False pixtrip=False allpata=False nol1=False keepDup=99 keepBad=99 &&

wait

cmsRun step3.py wf=-1 n=$N threads=8 skip=$A timing=True patatrack=True doregion=False pixtrip=False allpata=False nol1=False keepDup=99 keepBad=99 &&

wait

cmsRun step3.py wf=-1 n=$N threads=16 skip=$A timing=True patatrack=True doregion=False pixtrip=False allpata=False nol1=False keepDup=99 keepBad=99 &&



#6_3 no dup
for((i=0;i<${njobs};i++));
        do
        A=$(($i*$N));
        cmsRun step3.py wf=-1 n=$N threads=8 skip=$A timing=False patatrack=True doregion=False pixtrip=True allpata=True nol1=False keepDup=99 keepBad=99 &
done

wait

A=0

cmsRun step3.py wf=-1 n=$N threads=8 skip=$A timing=True patatrack=True doregion=False pixtrip=True allpata=True nol1=False keepDup=99 keepBad=99 &

wait

cmsRun step3.py wf=-1 n=$N threads=8 skip=$A timing=True patatrack=True doregion=False pixtrip=True allpata=True nol1=False keepDup=99 keepBad=99 &

wait

cmsRun step3.py wf=-1 n=$N threads=8 skip=$A timing=True patatrack=True doregion=False pixtrip=True allpata=True nol1=False keepDup=99 keepBad=99 &

#6_3 
for((i=0;i<${njobs};i++));
        do
        A=$(($i*$N));
        cmsRun step3.py wf=-1 n=$N threads=8 skip=$A timing=False patatrack=True doregion=False pixtrip=True allpata=True nol1=False keepDup=2 keepBad=2 &
done

wait

cmsRun step3.py wf=-1 n=$N threads=4 skip=0 timing=True patatrack=True doregion=False pixtrip=True allpata=True nol1=False keepDup=2 keepBad=2 &

wait

cmsRun step3.py wf=-1 n=$N threads=8 skip=0 timing=True patatrack=True doregion=False pixtrip=True allpata=True nol1=False keepDup=2 keepBad=2 &

wait

cmsRun step3.py wf=-1 n=$N threads=16 skip=0 timing=True patatrack=True doregion=False pixtrip=True allpata=True nol1=False keepDup=2 keepBad=2 &

