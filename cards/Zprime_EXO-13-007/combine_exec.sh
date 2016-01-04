#! /bin/bash

myrand=$1
mass=$2

ONED=0
LOG="dummy.log"
if [[ "$4" == "" ]]; then LOG=/dev/null ; else LOG=$4 ;fi;
if [[ "$3" == "" ]]; then ONED=1 ;
else
    if [[ "$3" =~ "LOG=" ]] ; then
	LOG=${3:4} ; ONED=1;
    else
	width=$3 ;
    fi;
fi;

OUTDIR=./
echo "Starting HiggsCombination with seed=$myrand at $( date +%c ) on $hostname." >> ${LOG}

startdir=$( pwd )

#set CMSSW environment
RELEASEDIR=/afs/cern.ch/user/h/hinzmann/workspace/limit_combination/CMSSW_7_1_5/src/
echo "Working release directory: ${RELEASEDIR}"   >> ${LOG}
#algo="MarkovChainMC"
algo="Asymptotic"
#algo="ProfileLikelihood"
hint="ProfileLikelihood" # before the algo method, run the hint method for restricting integration field
label="EXOZH"
ntoys=1000
#WORKDIR=${RELEASEDIR}/HiggsAna/HLLJJCommon/test/fits//${OUTDIR}/${mass}
WORKDIR=/afs/cern.ch/user/h/hinzmann/workspace/limit_combination/CMSSW_7_1_5/src/ExoDiBosonCombination/cards/2015-02-20_EXO-13-007/${OUTDIR}
if [ $ONED -eq 0 ]
    then
    WORKDIR=/afs/cern.ch/user/h/hinzmann/workspace/limit_combination/CMSSW_7_1_5/src/ExoDiBosonCombination/cards/2015-02-20_EXO-13-007/${OUTDIR}
fi
datacard="datacard_${mass}_interpolate"
OUTDIR="output_${label}_${algo}_"${datacard}

cd $RELEASEDIR
export SCRAM_ARCH=slc5_amd64_gcc472
#cmsenv
eval `scramv1 runtime -sh`
cd $startdir

TMPDIR="/tmp/$(whoami)"
mkdir ${TMPDIR}/combine_${myrand}
cd $TMPDIR/combine_${myrand}
cp $WORKDIR"cards_combined/${datacard}.txt" .
echo "I am in $( pwd ) (it should be: $TMPDIR/combine_${myrand} )"   >> ${LOG}
echo  >> ${LOG}


if [ ! -d ${WORKDIR}/$OUTDIR/ ]
    then
    mkdir -p ${WORKDIR}/$OUTDIR/
fi


echo "Datacard: $datacard"   >> ${LOG}
# if algo=HybridNew
#combine -M $algo -n $label -m 400 -s $myrand -t $ntoys -U  -d $WORKDIR/$datacard --freq --singlePoint 1

#if algo="Asymptotic"  ###-t $ntoys
maxBoundary=1000
minBoundary=0.01
 
echo    >> ${LOG}
echo "==== Asymptotic CLs limits ====="   >> ${LOG}
combine -M $algo -n ${label} -m $mass  -s $myrand -d ${datacard}.txt --rMax $maxBoundary --rMin $minBoundary >> ${LOG}

echo "Calculating the significances."  >> ${LOG}

## calc exp signif
echo   >> ${LOG}
echo "==== Expected Significance ====="   >> ${LOG}
combine -M ProfileLikelihood -n ${label}ExpSignif -m $mass  -s $myrand --signif --pvalue --expectSignal=1 -t -1 --toysFreq -d ${datacard}.txt   >> ${LOG}

## calc obs signif
echo    >> ${LOG}
echo "==== Observed Significance ====="  >> ${LOG}
combine -M ProfileLikelihood -n ${label}ObsSignif -m $mass  --signif --pvalue -d ${datacard}.txt  >> ${LOG} 

echo "List of files in $( pwd ):" >> ${LOG}
ls -lh   >> ${LOG}
echo "Moving files into ${WORKDIR}/$OUTDIR/"   >> ${LOG}
mv $TMPDIR/combine_${myrand}/higgsCombine${label}*.root  ${WORKDIR}/$OUTDIR/

