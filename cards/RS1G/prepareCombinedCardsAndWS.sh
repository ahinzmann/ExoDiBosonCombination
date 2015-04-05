#! /bin/bash

# define input
if [ $# -lt 1 ]
    then
    echo "Need one input: mass point"
    exit 1
fi

MASS=$1
echo "Merging M=${MASS}"
ZZ8DIR="ZZ_cards/${MASS}"
WW8DIR="WW_cards"
WW13DIR="WW_cards_13TeV_1fb"
JJ8DIR="JJ_8TeV"
JJ13DIR="JJ_13TeV_1fb"

#prepare output
OUTDIR="comb_${MASS}"
mkdir $OUTDIR/


### ZZ8 only
LABEL="xzz"
EXOZZ8LPCARDS="${LABEL}_ee1JLP=${LABEL}_ee1JLP.${MASS}.txt ${LABEL}_mm1JLP=${LABEL}_mm1JLP.${MASS}.txt"
EXOZZ8HPCARDS="${LABEL}_ee1JHP=${LABEL}_ee1JHP.${MASS}.txt ${LABEL}_mm1JHP=${LABEL}_mm1JHP.${MASS}.txt"
EXOZZ8CARDS="$EXOZZ8HPCARDS $EXOZZ8LPCARDS"
COMBZZ8CARD="comb_${LABEL}.${MASS}.txt"
COMBRS1ZZ8CARD="comb_${LABEL}_rs1.${MASS}.txt"

if [ $MASS -le 2500 ]
then
echo "Moving to "${ZZ8DIR}/
cd ${ZZ8DIR}/
pwd
combineCards.py $EXOZZ8CARDS &> ${COMBZZ8CARD}
cd -
python adapt_xsec_ZZ.py ${MASS}
cp ${ZZ8DIR}/${COMBRS1ZZ8CARD} ${OUTDIR}/${COMBZZ8CARD}
cp ${ZZ8DIR}/${LABEL}_*input*.root  ${OUTDIR}/
fi

### JJ 8TeV only
LABEL="xjj8"
JJ8CARDORIG="CMS_jj_RS1_${MASS}_8TeV_CMS_jj_VV.txt" ##Andreas gives us cards with WW and ZZ8 already merged
COMBJJ8CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1050 ] && [ $MASS -le 2900 ]
then
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards/../workspaces/||g' < ${JJ8DIR}/${JJ8CARDORIG} &> $OUTDIR/${COMBJJ8CARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJCARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJCARD}
    cp ${JJ8DIR}/CMS_jj_RS1*${MASS}*.root ${OUTDIR}/
    cp ${JJ8DIR}/CMS_jj_bkg_8TeV.root ${OUTDIR}/
fi

### JJ 13TeV only
LABEL="xjj13"
JJ13CARDORIG="CMS_jj_RS1_${MASS}_13TeV_CMS_jj_VVHP.txt" ##Andreas gives us cards with WW and ZZ8 already merged
COMBJJ13CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|../workspaces/||g' < ${JJ13DIR}/${JJ13CARDORIG} &> $OUTDIR/${COMBJJ13CARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJCARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJCARD}
    cp ${JJ13DIR}/CMS_jj_RS1*${MASS}*.root ${OUTDIR}/
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/
fi

### WW only
LABEL="xww"
WW8BASE="wwlvj_BulkG_WW_inclusive_c0p2_M${MASS}"
WW8ELEBASE="${WW8BASE}_el_10_00"
WW8MUBASE="${WW8BASE}_mu_10_00"
EXOWW8LPCARDS="${LABEL}_ev1JLP=${WW8ELEBASE}_LP_unbin.txt ${LABEL}_mv1JLP=${WW8MUBASE}_LP_unbin.txt"
EXOWW8HPCARDS="${LABEL}_ev1JHP=${WW8ELEBASE}_HP_unbin.txt ${LABEL}_mv1JHP=${WW8MUBASE}_HP_unbin.txt"
EXOWW8CARDS="$EXOWW8HPCARDS $EXOWW8LPCARDS"
COMBWW8CARD="comb_${LABEL}.${MASS}.txt"
COMBRS1WW8CARD="comb_${LABEL}_rs1.${MASS}.txt"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
    then
    cd ${WW8DIR}/
    combineCards.py $EXOWW8CARDS &> tmp_XWW8_card.txt
    sed -e 's|1.072/0.891|1.080/0.920|g'  -e 's|1.303/1.277|0.70/1.30|g' < tmp_XWW8_card.txt  > ${COMBWW8CARD}
    cd -
    python adapt_xsec_WW.py ${MASS}
    cp ${WW8DIR}/${COMBRS1WW8CARD} ${OUTDIR}/${COMBWW8CARD}
    cp ${WW8DIR}/${WW8BASE}_*workspace.root  ${OUTDIR}/
fi

### WW 13 TeV only
LABEL="xww13"
WW13BASE="wwlvj_RS1G_WW_lvjj_M${MASS}"
WW13ELEBASE="${WW13BASE}_el"
WW13MUBASE="${WW13BASE}_mu"
#EXOWW13LPCARDS="${LABEL}_ev1JLP=${WW13ELEBASE}_LP_unbin.txt ${LABEL}_mv1JLP=${WW13MUBASE}_LP_unbin.txt"
EXOWW13HPCARDS="${LABEL}_ev1JHP=${WW13ELEBASE}_HP_unbin.txt ${LABEL}_mv1JHP=${WW13MUBASE}_HP_unbin.txt"
EXOWW13CARDS="$EXOWW13HPCARDS" # $EXOWW13LPCARDS
COMBWW13CARD="comb_${LABEL}.${MASS}.txt"
COMBRS1WW13CARD="comb_${LABEL}_rs1.${MASS}.txt"

if [ $MASS -eq 1000 ] || [ $MASS -eq 2000 ] || [ $MASS -eq 3000 ] || [ $MASS -eq 4000 ]
    then
    cd ${WW13DIR}/
    combineCards.py $EXOWW13CARDS &> tmp_XWW13_card.txt
    sed -e 's|1.072/0.891|1.080/0.920|g'  -e 's|1.303/1.277|0.70/1.30|g' < tmp_XWW13_card.txt  > ${COMBWW13CARD}
    cd -
    python adapt_xsec_WW_13TeV.py ${MASS}
    cp ${WW13DIR}/${COMBRS1WW13CARD} ${OUTDIR}/${COMBWW13CARD}
    cp ${WW13DIR}/${WW13BASE}_*workspace.root  ${OUTDIR}/
fi

###put things together
cd $OUTDIR/

COMBALLCARD="comb_ALL.${MASS}.txt"
COMBSEMILEPCARD="comb_SEMILEPT.${MASS}.txt"
COMBSEMILEP813CARD="comb_SEMILEPT813.${MASS}.txt"
COMBJJ813CARD="comb_JJ813.${MASS}.txt"
COMBWW813CARD="comb_WW813.${MASS}.txt"
COMBALL13CARD="comb_ALL13.${MASS}.txt"
COMBALL813CARD="comb_ALL813.${MASS}.txt"

if [ $MASS -lt 800 ]
    then

    combineCards.py $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBZZ8CARD &>  $COMBALL813CARD
elif [ $MASS -lt 1050 ]
    then

    combineCards.py $COMBWW8CARD $COMBWW13CARD &>  $COMBWW813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBALL813CARD
elif [ $MASS -lt 1200 ]
    then
    combineCards.py $COMBJJ8CARD &>  $COMBJJ813CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD &>  $COMBWW813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBALL813CARD
elif [ $MASS -gt 2900 ]
    then
    combineCards.py $COMBJJ13CARD &>  $COMBJJ813CARD
    combineCards.py $COMBWW13CARD &>  $COMBWW813CARD

    combineCards.py $COMBWW13CARD &>  $COMBSEMILEP813CARD

    combineCards.py $COMBJJ13CARD $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD &>  $COMBALL813CARD
elif [ $MASS -gt 2500 ]
    then
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD &>  $COMBJJ813CARD
    combineCards.py $COMBWW13CARD &>  $COMBWW813CARD

    combineCards.py $COMBWW13CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBJJ8CARD &>  $COMBALLCARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD $COMBWW13CARD &>  $COMBALL813CARD
else 
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD &>  $COMBJJ813CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD &>  $COMBWW813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBALL813CARD
fi
