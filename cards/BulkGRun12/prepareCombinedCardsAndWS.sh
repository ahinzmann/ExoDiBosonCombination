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
ZZ13DIR="ZZ_cards_13TeV"
WW8DIR="WW_cards"
WW13DIR="WW_cards_13TeV"
#WW13DIR="WW_cards_13TeV_noMassCategory"
#WW13DIR="WW_cards_13TeV_oldSys"
JJ8DIR="JJ_cards"
JJ13DIR="JJ_cards_13TeV"

#prepare output
OUTDIR="comb_${MASS}"
mkdir $OUTDIR/


### ZZ8 only
LABEL="xzz"
EXOZZ8LPCARDS="${LABEL}_ee1JLP=${LABEL}_ee1JLP.${MASS}.txt ${LABEL}_mm1JLP=${LABEL}_mm1JLP.${MASS}.txt"
EXOZZ8HPCARDS="${LABEL}_ee1JHP=${LABEL}_ee1JHP.${MASS}.txt ${LABEL}_mm1JHP=${LABEL}_mm1JHP.${MASS}.txt"
EXOZZ8CARDS="$EXOZZ8HPCARDS $EXOZZ8LPCARDS"
COMBZZ8CARD="comb_${LABEL}.${MASS}.txt"
COMBFIXZZ8CARD="comb_${LABEL}_bulkfix.${MASS}.txt"

if [ $MASS -le 2500 ]
then
echo "Moving to "${ZZ8DIR}/
cd ${ZZ8DIR}/
pwd
combineCards.py $EXOZZ8CARDS &> ${COMBZZ8CARD}
cd -
python adapt_xsec_ZZ.py ${MASS}
cp ${ZZ8DIR}/${COMBFIXZZ8CARD} ${OUTDIR}/${COMBZZ8CARD}
cp ${ZZ8DIR}/${LABEL}_*input*.root  ${OUTDIR}/
fi

### ZZ13 only
LABEL="xzz13"
#EXOZZ13LPCARDS="CMS_ZZ_ELP=CMS_ZZ_${MASS}_ELP_13TeV.txt CMS_ZZ_MLP=CMS_ZZ_${MASS}_MLP_13TeV.txt"
EXOZZ13HPCARDS="CMS_ZZ_EHP=CMS_ZZ_${MASS}_EHP_13TeV.txt CMS_ZZ_MHP=CMS_ZZ_${MASS}_MHP_13TeV.txt"
#EXOZZ13CARDS="$EXOZZ13HPCARDS $EXOZZ13LPCARDS"
COMBZZ13CARD="comb_${LABEL}.${MASS}.txt"
COMBFIXZZ13CARD="comb_${LABEL}_bulkfix.${MASS}.txt"

if [ $MASS -ge 800 ]
then
echo "Moving to "${ZZ13DIR}/
cd ${ZZ13DIR}/
pwd
combineCards.py $EXOZZ13HPCARDS &> ${COMBZZ13CARD}
cd -
python adapt_xsec_ZZ_13TeV.py ${MASS}
cp ${ZZ13DIR}/${COMBFIXZZ13CARD} ${OUTDIR}/${COMBZZ13CARD}
sed -e 's|workSpaces/||g' < ${ZZ13DIR}/${COMBFIXZZ13CARD} &> ${OUTDIR}/${COMBZZ13CARD}
cp ${ZZ13DIR}/CMS_ZZ*.root  ${OUTDIR}/
fi

### JJ 8TeV only
LABEL="xjj8"
JJ8CARDORIG="CMS_jj_Bulkfix_${MASS}_8TeV_CMS_jj_VV.txt" ##Andreas gives us cards with WW and ZZ8 already merged
COMBJJ8CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1000 ] && [ $MASS -le 2900 ]
then
python adapt_xsec_JJ.py ${MASS}
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards/../workspaces/||g' < ${JJ8DIR}/datacards/${JJ8CARDORIG} &> $OUTDIR/${COMBJJ8CARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJCARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJCARD}
    cp ${JJ8DIR}/workspaces/CMS_jj_Bulk*${MASS}*.root ${OUTDIR}/
    cp ${JJ8DIR}/workspaces/CMS_jj_bkg_8TeV.root ${OUTDIR}/
fi

### JJ 8TeV only
LABEL="xjj8ww"
JJ8CARDORIG="CMS_jj_BulkWWfix_${MASS}_8TeV_CMS_jj_VV.txt" ##Andreas gives us cards with WW and ZZ8 already merged
COMBJJWW8CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1000 ] && [ $MASS -le 2900 ]
then
python adapt_xsec_JJ_BulkWW.py ${MASS}
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards/../workspaces/||g' < ${JJ8DIR}/datacards/${JJ8CARDORIG} &> $OUTDIR/${COMBJJWW8CARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJCARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJCARD}
    cp ${JJ8DIR}/workspaces/CMS_jj_Bulk*${MASS}*.root ${OUTDIR}/
    cp ${JJ8DIR}/workspaces/CMS_jj_bkg_8TeV.root ${OUTDIR}/
fi

### JJ 8TeV only
LABEL="xjj8zz"
JJ8CARDORIG="CMS_jj_BulkZZfix_${MASS}_8TeV_CMS_jj_VV.txt" ##Andreas gives us cards with WW and ZZ8 already merged
COMBJJZZ8CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1000 ] && [ $MASS -le 2900 ]
then
python adapt_xsec_JJ_BulkZZ.py ${MASS}
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards/../workspaces/||g' < ${JJ8DIR}/datacards/${JJ8CARDORIG} &> $OUTDIR/${COMBJJZZ8CARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJCARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJCARD}
    cp ${JJ8DIR}/workspaces/CMS_jj_Bulk*${MASS}*.root ${OUTDIR}/
    cp ${JJ8DIR}/workspaces/CMS_jj_bkg_8TeV.root ${OUTDIR}/
fi

### JJ 13TeV only
LABEL="xjj13ww"
JJ13CARDORIG="CMS_jj_BulkWWfix_${MASS}_13TeV_CMS_jj_VVnew.txt"
COMBJJWW13CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
    python adapt_xsec_JJ_BulkWW_13TeV.py ${MASS}
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards_withPDFuncertainties/../workspaces/||g' -e 's|datacards_backup/../workspaces/||g' -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJ13CARDORIG} &> $OUTDIR/${COMBJJWW13CARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJCARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJCARD}
    cp ${JJ13DIR}/CMS_jj_Bulk*${MASS}*.root ${OUTDIR}/
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/
fi

### JJ 13TeV only
LABEL="xjj13zz"
JJ13CARDORIG="CMS_jj_BulkZZfix_${MASS}_13TeV_CMS_jj_VVnew.txt"
COMBJJZZ13CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
    python adapt_xsec_JJ_BulkZZ_13TeV.py ${MASS}
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards_withPDFuncertainties/../workspaces/||g' -e 's|datacards_backup/../workspaces/||g' -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJ13CARDORIG} &> $OUTDIR/${COMBJJZZ13CARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJCARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJCARD}
    cp ${JJ13DIR}/CMS_jj_Bulk*${MASS}*.root ${OUTDIR}/
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/
fi

### JJ 13TeV only
LABEL="xjj13old"
JJ13oldCARDORIG="CMS_jj_BulkWWfix_${MASS}_13TeV_CMS_jj_VV.txt"
COMBJJ13oldCARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards_withPDFuncertainties/../workspaces/||g' -e 's|datacards_backup/../workspaces/||g' -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJ13oldCARDORIG} &> $OUTDIR/${COMBJJ13oldCARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJCARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJCARD}
    cp ${JJ13DIR}/CMS_jj_Bulk*${MASS}*.root ${OUTDIR}/
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/
fi

### JJ 13TeV only
LABEL="xjj13hp"
JJ13hpCARDORIG="CMS_jj_BulkWWfix_${MASS}_13TeV_CMS_jj_VVHPnew.txt"
COMBJJ13hpCARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards_withPDFuncertainties/../workspaces/||g' -e 's|datacards_backup/../workspaces/||g' -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJ13hpCARDORIG} &> $OUTDIR/${COMBJJ13hpCARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJCARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJCARD}
    cp ${JJ13DIR}/CMS_jj_Bulk*${MASS}*.root ${OUTDIR}/
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
COMBFIXWW8CARD="comb_${LABEL}_bulkfix.${MASS}.txt"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
    then
    cd ${WW8DIR}/
    combineCards.py $EXOWW8CARDS &> tmp_XWW8_card.txt
    sed -e 's|1.072/0.891|1.080/0.920|g'  -e 's|1.303/1.277|0.70/1.30|g' < tmp_XWW8_card.txt  > ${COMBWW8CARD}
    cd -
    python adapt_xsec_WW.py ${MASS}
    cp ${WW8DIR}/${COMBFIXWW8CARD} ${OUTDIR}/${COMBWW8CARD}
    cp ${WW8DIR}/${WW8BASE}_*workspace.root  ${OUTDIR}/
fi

### WW 13 TeV only
LABEL="xww13"
EXOWW13CARDS="wwlvj_BulkGfix_WW_lvjj_M${MASS}_combo_ALLP_unbin.txt"
#LABEL="xww13nomasscategory"
#EXOWW13CARDS="wwlvj_BulkGfix_WW_lvjj_M${MASS}_noMassCat_combo_ALLP_unbin.txt"
#LABEL="xww13oldsys"
#EXOWW13CARDS="wwlvj_BulkGfix_WW_lvjj_M${MASS}_oldSys_combo_ALLP_unbin.txt"
COMBWW13CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 800 ]
    then
    python adapt_xsec_WW_13TeV.py ${MASS}
    sed -e 's|cards_mu_HPW/||g' -e 's|cards_mu_HP/||g' -e 's|cards_mu_LP/||g' -e 's|cards_el_HP/||g' -e 's|cards_el_LP/||g' -e 's|cards_mu_HPZ/||g'  -e 's|cards_mu_LPW/||g' -e 's|cards_mu_LPZ/||g' -e 's|cards_el_HPW/||g' -e 's|cards_el_HPZ/||g' -e 's|cards_el_LPW/||g' -e 's|cards_el_LPZ/||g' < ${WW13DIR}/${EXOWW13CARDS} &> $OUTDIR/${COMBWW13CARD}
    cp ${WW13DIR}/cards_*/*.root ${OUTDIR}/
fi

###put things together
cd $OUTDIR/

COMBALLCARD="comb_ALL.${MASS}.txt"
COMBSEMILEPCARD="comb_SEMILEPT.${MASS}.txt"
COMBSEMILEP813CARD="comb_SEMILEPT813.${MASS}.txt"
COMBJJ813CARD="comb_JJ813.${MASS}.txt"
COMBJJWW813CARD="comb_JJWW813.${MASS}.txt"
COMBJJZZ813CARD="comb_JJZZ813.${MASS}.txt"
COMBWW813CARD="comb_WW813.${MASS}.txt"
COMBZZ813CARD="comb_ZZ813.${MASS}.txt"
COMBALL13CARD="comb_ALL13.${MASS}.txt"
COMBALL813CARD="comb_ALL813.${MASS}.txt"
COMBJAM13CARD="comb_JAM13.${MASS}.txt"
COMBJAM813CARD="comb_JAM813.${MASS}.txt"
COMBJAMZZ813CARD="comb_JAMZZ813.${MASS}.txt"

if [ $MASS -lt 800 ]
    then
    combineCards.py $COMBZZ8CARD &>  $COMBZZ813CARD
    combineCards.py $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBZZ8CARD &>  $COMBALL813CARD

    combineCards.py $COMBZZ8CARD &>  $COMBJAMZZ813CARD
elif [ $MASS -lt 1000 ]
    then
    combineCards.py $COMBZZ8CARD $COMBZZ13CARD &>  $COMBZZ813CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD &>  $COMBWW813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBZZ13CARD $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ13CARD $COMBZZ8CARD &>  $COMBALL813CARD
    combineCards.py $COMBWW13CARD &>  $COMBJAM13CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD &>  $COMBJAM813CARD
    combineCards.py $COMBZZ8CARD &>  $COMBJAMZZ813CARD
elif [ $MASS -lt 1200 ]
    then
    combineCards.py $COMBJJ8CARD &> $COMBJJ813CARD
    combineCards.py $COMBJJWW8CARD &> $COMBJJWW813CARD
    combineCards.py $COMBJJZZ8CARD &> $COMBJJZZ813CARD
    combineCards.py $COMBZZ8CARD $COMBZZ13CARD &>  $COMBZZ813CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD &>  $COMBWW813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBZZ13CARD $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBWW13CARD $COMBZZ13CARD $COMBZZ8CARD &>  $COMBALL813CARD
    combineCards.py $COMBWW13CARD &>  $COMBJAM13CARD
    combineCards.py $COMBJJWW8CARD $COMBWW8CARD $COMBWW13CARD &>  $COMBJAM813CARD
    combineCards.py $COMBJJZZ8CARD $COMBZZ8CARD &>  $COMBJAMZZ813CARD
elif [ $MASS -le 2500 ]
    then
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD &>  $COMBJJ813CARD
    combineCards.py $COMBJJWW8CARD $COMBJJWW13CARD &>  $COMBJJWW813CARD
    combineCards.py $COMBJJZZ8CARD $COMBJJZZ13CARD &>  $COMBJJZZ813CARD
    combineCards.py $COMBZZ8CARD $COMBZZ13CARD &>  $COMBZZ813CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD &>  $COMBWW813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBJJ13CARD $COMBZZ13CARD $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ13CARD $COMBJJ8CARD $COMBWW8CARD $COMBZZ13CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBALL813CARD
    combineCards.py $COMBJJWW13CARD $COMBWW13CARD &>  $COMBJAM13CARD
    combineCards.py $COMBJJWW13CARD $COMBJJWW8CARD $COMBWW8CARD $COMBWW13CARD &>  $COMBJAM813CARD
    combineCards.py $COMBJJZZ13CARD $COMBJJZZ8CARD $COMBZZ8CARD &>  $COMBJAMZZ813CARD
elif [ $MASS -le 2900 ]
    then
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD &>  $COMBJJ813CARD
    combineCards.py $COMBJJWW8CARD $COMBJJWW13CARD &>  $COMBJJWW813CARD
    combineCards.py $COMBJJZZ8CARD $COMBJJZZ13CARD &>  $COMBJJZZ813CARD
    combineCards.py $COMBZZ13CARD &>  $COMBZZ813CARD
    combineCards.py $COMBWW13CARD &>  $COMBWW813CARD

    combineCards.py $COMBWW13CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBJJ8CARD &>  $COMBALLCARD
    combineCards.py $COMBJJ13CARD $COMBZZ13CARD $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ13CARD $COMBJJ8CARD $COMBZZ13CARD $COMBWW13CARD &>  $COMBALL813CARD
    combineCards.py $COMBJJWW13CARD $COMBWW13CARD &>  $COMBJAM13CARD
    combineCards.py $COMBJJWW13CARD $COMBJJWW8CARD $COMBWW13CARD &>  $COMBJAM813CARD
    combineCards.py $COMBJJZZ13CARD $COMBJJZZ8CARD &>  $COMBJAMZZ813CARD
else
    combineCards.py $COMBJJ13CARD &>  $COMBJJ813CARD
    combineCards.py $COMBJJWW13CARD &>  $COMBJJWW813CARD
    combineCards.py $COMBJJZZ13CARD &>  $COMBJJZZ813CARD
    combineCards.py $COMBZZ13CARD &>  $COMBZZ813CARD
    combineCards.py $COMBWW13CARD &>  $COMBWW813CARD

    combineCards.py $COMBWW13CARD &>  $COMBSEMILEP813CARD

    combineCards.py $COMBJJ13CARD $COMBZZ13CARD $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ13CARD $COMBZZ13CARD $COMBWW13CARD &>  $COMBALL813CARD
    combineCards.py $COMBJJWW13CARD $COMBWW13CARD &>  $COMBJAM13CARD
    combineCards.py $COMBJJWW13CARD $COMBWW13CARD &>  $COMBJAM813CARD
    combineCards.py $COMBJJZZ13CARD &>  $COMBJAMZZ813CARD
fi
