#! /bin/bash

# define input
if [ $# -lt 1 ]
    then
    echo "Need one input: mass point"
    exit 1
fi

MASS=$1
echo "Merging M=${MASS}"
ZHDIR="cards_ZH"
WHDIR="cards_WH"
VHDIR="cards_VH"

#prepare output
OUTDIR="comb_${MASS}"
mkdir $OUTDIR/


### ZH only
LABEL="xzh"
COMBZHCARD="comb_${LABEL}.${MASS}.txt"
COMBRS1ZHCARD="datacard_${MASS}_interpolate_adapt.txt"

if [ $MASS -le 2500 ]
then
echo "Moving to "${ZHDIR}/
cp ${ZHDIR}/${COMBRS1ZHCARD} ${OUTDIR}/${COMBZHCARD}
fi

### VH only
LABEL="xvh"
#VHCARDORIG="CMS_jj_HZqq_${MASS}_8TeV_CMS_jj_HZCombined.txt"
VHCARDORIG="CMS_jj_HWqq_${MASS}_8TeV_CMS_jj_HWCombined.txt"
COMBVHCARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1000 ] && [ $MASS -le 2600 ]
then
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_vh_Bulk_1200_8TeV_CMS_vh_VH.txt
sed -e 's|datacards/../workspaces/||g' -e 's|datacards/../HbbVqqHwwworkspaces/||g' < ${VHDIR}/${VHCARDORIG} &> $OUTDIR/${COMBVHCARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${VHDIR}/datacards/${VHCARDORIG} &> $OUTDIR/${COMBVHCARD}
#    cp ${VHDIR}/datacards/${VHCARDORIG}  $OUTDIR/${COMBVHCARD}
    cp ${VHDIR}/CMS_jj_*${MASS}*.root ${OUTDIR}/
    cp ${VHDIR}/CMS_jj_bkg_8TeV.root ${OUTDIR}/
fi

### WH only
LABEL="xwh"
WHBASE="whlvj_MWp_${MASS}_bb"
WHELEBASE="cards_el/${WHBASE}_el"
WHMUBASE="cards_mu/${WHBASE}_mu"
EXOWHCARDS="${LABEL}_mv1JLP=${WHMUBASE}_ALLP_unbin.txt ${LABEL}_ev1JLP=${WHELEBASE}_ALLP_unbin.txt"
COMBWHCARD="comb_${LABEL}.${MASS}.txt"
COMBRS1WHCARD="comb_${LABEL}_hvt.${MASS}.txt"

if [ $MASS -le 2500 ]
    then
    cd ${WHDIR}/
    combineCards.py $EXOWHCARDS &> tmp_XWH_card.txt
    sed -e 's|cards_mu/||g'  -e 's|cards_el/||g' < tmp_XWH_card.txt  > ${COMBWHCARD}
    cd -
    cp ${WHDIR}/${COMBWHCARD} ${OUTDIR}/${COMBWHCARD}
    cp ${WHDIR}/cards_el/${WHBASE}_*workspace.root  ${OUTDIR}/
    cp ${WHDIR}/cards_mu/${WHBASE}_*workspace.root  ${OUTDIR}/
fi

###put things together
cd $OUTDIR/

COMB3CHANCARD="comb_ALL.${MASS}.txt"
COMBSEMILEPCARD="comb_SEMILEPT.${MASS}.txt"

if [ $MASS -lt 1000 ]
    then
    combineCards.py $COMBWHCARD $COMBZHCARD &>  $COMB3CHANCARD
    combineCards.py $COMBWHCARD $COMBZHCARD &>  $COMBSEMILEPCARD
elif [ $MASS -gt 2500 ]
    then
    combineCards.py $COMBVHCARD &>  $COMB3CHANCARD
else 
    combineCards.py $COMBVHCARD $COMBWHCARD $COMBZHCARD &>  $COMB3CHANCARD
    combineCards.py $COMBWHCARD $COMBZHCARD &>  $COMBSEMILEPCARD
fi
