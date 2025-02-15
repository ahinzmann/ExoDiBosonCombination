#! /bin/bash

if [ $# -lt 1 ]
then
    echo "Usage: ./parallelizeCombine.sh <mass> [width]"
    exit 1
fi

RUN_LOCALLY=0 #if 1 -> do not submit, run locally

startdir=$( pwd )
NMAXJOBS=1
mass=$1
queue="dummyqueue"
OUTDIR=$startdir
LOGDIRNAME="logs"

queue=1nh


if [ $# -gt 1 ]
then
    width=$2
    twod=1
else
    twod=0
fi

if [ $twod -eq 1 ]
    then
    mkdir -p ${OUTDIR}/comb_${mass}_${width}/${LOGDIRNAME}
else
    mkdir -p ${OUTDIR}/comb_${mass}/${LOGDIRNAME}
fi

ijob=1
chmod 744 combine_exec.sh

while [ $ijob -le $NMAXJOBS ]
do

  myrand=$RANDOM #random number generator (short integer: [0-32767])
  JOBNAME="combine_${myrand}_${mass}"
  LOGFILE="${LOGDIRNAME}/log_parallelizeCombine_${myrand}.out"
  LOGFULL=${OUTDIR}/comb_${mass}/$LOGFILE
  echo $LOGFULL

  if [ $twod -eq 1 ]
    then
      JOBNAME=${JOBNAME}"_${width}"
      LOGFULL=${OUTDIR}/comb_${mass}_${width}/$LOGFILE
  fi



  if [ $RUN_LOCALLY -eq 1 ]
      then
      if [ $twod -eq 1 ]
	  then
	  ${startdir}/combine_exec.sh $myrand $mass $width LOG=${LOGFULL}
      else
	  ${startdir}/combine_exec.sh $myrand $mass LOG=${LOGFULL}
      fi

  else
      if [ $twod -eq 1 ]
	  then
	  bsub -q $queue -J $JOBNAME -oo ${LOGFULL} ${startdir}/combine_exec.sh $myrand $mass $width LOG=${LOGFULL}
      else
	  bsub -q $queue -J $JOBNAME -oo ${LOGFULL} ${startdir}/combine_exec.sh $myrand $mass LOG=${LOGFULL}
      fi
  fi
  let ijob=ijob+1
done


