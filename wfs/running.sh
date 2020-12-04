N=256
njobs=12

#6_1
A=0

WFS="-1 -4 7 5 -8"
THREADS="4 8 16"

################################################################
#v6_1
PATA=False
REGION=False
WF=-1
PIXTRIP=False
ALLPATA=False
NOL1=False
KEEPDUP=99
KEEPBAD=99
TIMING=False

for((i=0;i<${njobs};i++));
	do
	A=$(($i*$N));
	cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD &
done

#Timings
A=0
for T in 4 8 16;
  do
    cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD
done


################################################################
#v6_2
PATA=True

###Base v6_2
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets
PIXTRIP=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
#Timings
wait && A=0
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#without triplets & with region
PIXTRIP=False
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets & region
PIXTRIP=True
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

###################################
##### Keep duplicates
KEEPDUP=2
PIXTRIP=False
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets
PIXTRIP=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
#Timings
wait && A=0
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#without triplets & with region
PIXTRIP=False
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets & region
PIXTRIP=True
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

###################################
##### Keep bads
KEEPDUP=99
KEEPBAD=2
PIXTRIP=False
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets
PIXTRIP=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
#Timings
wait && A=0
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#without triplets & with region
PIXTRIP=False
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets & region
PIXTRIP=True
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done


###################################
##### Keep bads & dup
KEEPDUP=2
KEEPBAD=2
PIXTRIP=False
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets
PIXTRIP=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
#Timings
wait && A=0
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#without triplets & with region
PIXTRIP=False
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets & region
PIXTRIP=True
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done





################################################################
#v6_3
PATA=True
ALLPATA=True
PIXTRIP=True

###Base v6_2
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets & region
PIXTRIP=True
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

###################################
##### Keep duplicates
KEEPDUP=2
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets & region
PIXTRIP=True
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

###################################
##### Keep bads
KEEPDUP=99
KEEPBAD=2
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets & region
PIXTRIP=True
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done


###################################
##### Keep bads & dup
KEEPDUP=2
KEEPBAD=2
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done

#with triplets & region
PIXTRIP=True
REGION=True
for((i=0;i<${njobs};i++)); do A=$(($i*$N)); cmsRun step3.py wf=$WF n=$N threads=8 skip=$A timing=$TIMING patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD & done
wait && A=0
#Timings
for T in 4 8 16; do cmsRun step3.py wf=$WF n=$N threads=$T skip=$A timing=True patatrack=$PATA doregion=$REGION pixtrip=$PIXTRIP allpata=$ALLPATA nol1=$NOL1 keepDup=$KEEPDUP keepBad=$KEEPBAD ; done
