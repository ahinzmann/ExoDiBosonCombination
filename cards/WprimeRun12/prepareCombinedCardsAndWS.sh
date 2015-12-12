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
ZZDIR="ZZ_cards/${MASS}"
WWDIR="WW_cards"
JJDIR="JJ_cards"
ZZ13DIR="ZZ_cards_13TeV"
WW13DIR="WW_cards_13TeV"
JJ13DIR="JJ_cards_13TeV"

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
sed -e 's|lumi|lumi_8TeV|g' -e 's|PUReweighting|CMS_pu|g' -e 's|VTag|CMS_eff_tau21_sf|g' -e 's|EleScale|CMS_scale_e|g' -e 's|EleResol|CMS_res_e|g' -e 's|MuoScale|CMS_scale_m|g' -e 's|MuoResol|CMS_res_m|g' -e 's|EleID|CMS_eff_e|g' -e 's|MuoID|CMS_eff_m|g' -e 's|JES|CMS_scale_j|g' -e 's|JER|CMS_res_j|g' -e 's|BTagSyst|CMS_btagger|g' < ${ZHDIR}/${COMBRS1ZHCARD} &> $OUTDIR/${COMBZHCARD}
fi

### VH only
LABEL="xvh"
VHCARDORIG="CMS_jj_HVqq_${MASS}_8TeV_CMS_jj_HVCombined_adapt.txt"
COMBVHCARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1000 ] && [ $MASS -le 2600 ]
then
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_vh_Bulk_1200_8TeV_CMS_vh_VH.txt
sed -e 's|datacards/../workspaces/||g' -e 's|datacards/../HbbVqqHwwworkspaces/||g'  -e 's|CMS_Btagging|CMS_doubleBtagging|g' < ${VHDIR}/${VHCARDORIG} &> $OUTDIR/${COMBVHCARD}
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

if [ $MASS -le 2500 ]
    then
    cd ${WHDIR}/
    combineCards.py $EXOWHCARDS &> tmp_XWH_card.txt
    sed -e 's|cards_mu/||g'  -e 's|cards_el/||g'   -e 's|CMS_xwh_prunedmass|CMS_jet_mass|g'   -e 's|CMS_xwh_btagger|CMS_btagger|g' -e 's|CMS_xwh_btag_eff|CMS_doubleBtagging|g' < tmp_XWH_card.txt  > ${COMBWHCARD}
    cd -
    cp ${WHDIR}/${COMBWHCARD} ${OUTDIR}/${COMBWHCARD}
    cp ${WHDIR}/cards_el/${WHBASE}_*workspace.root  ${OUTDIR}/
    cp ${WHDIR}/cards_mu/${WHBASE}_*workspace.root  ${OUTDIR}/
fi

### ZZ only
LABEL="xzz"
COMBZZ8CARD="comb_${LABEL}.${MASS}.txt"
COMBZZHVTCARD="comb_${LABEL}_hvt.${MASS}.txt"

if [ $MASS -le 2500 ]
then
echo "Moving to "${ZZDIR}/
cp ${ZZDIR}/${COMBZZHVTCARD} ${OUTDIR}/${COMBZZ8CARD}
cp ${ZZDIR}/${LABEL}_*input*.root  ${OUTDIR}/
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

### JJ only
LABEL="xjj8"
JJCARDORIG="CMS_jj_HVT_${MASS}_8TeV_CMS_jj_VV.txt" ##Andreas gives us cards with WW and ZZ already merged
COMBJJ8CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1000 ]
then
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards/../workspaces/||g' -e 's|CMS_jj_bkg_8TeV|CMS_jj_bkg_WZ_8TeV|g' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJ8CARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJ8CARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJ8CARD}
    cp ${JJDIR}/workspaces/CMS_jj_WZ*${MASS}*.root ${OUTDIR}/
    cp ${JJDIR}/workspaces/CMS_jj_bkg_8TeV.root ${OUTDIR}/CMS_jj_bkg_WZ_8TeV.root
fi

### JJ 13TeV only
LABEL="xjj13"
JJ13CARDORIG="CMS_jj_WZfix_${MASS}_13TeV_CMS_jj_VVnew.txt"
COMBJJ13CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
    python adapt_xsec_JJ_13TeV.py ${MASS}
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJ13CARDORIG} &> $OUTDIR/${COMBJJ13CARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJ8CARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJ8CARD}
    cp ${JJ13DIR}/CMS_jj_WZ*${MASS}*.root ${OUTDIR}/
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/
fi

### JJ 13TeV only
LABEL="xjj13old"
JJ13oldCARDORIG="CMS_jj_WZfix_${MASS}_13TeV_CMS_jj_VV.txt"
COMBJJ13oldCARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJ13oldCARDORIG} &> $OUTDIR/${COMBJJ13oldCARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJ8CARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJ8CARD}
    cp ${JJ13DIR}/CMS_jj_WZ*${MASS}*.root ${OUTDIR}/
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/
fi

### JJ 13TeV only
LABEL="xjj13hp"
JJ13hpCARDORIG="CMS_jj_WZfix_${MASS}_13TeV_CMS_jj_VVHPnew.txt"
COMBJJ13hpCARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
###sed -e '/CMS_sig_p/ s|0|0.0|g' -e '/CMS_sig_p/ s|1|1.0|g' < CMS_jj_Bulk_1200_8TeV_CMS_jj_VV.txt
sed -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJ13hpCARDORIG} &> $OUTDIR/${COMBJJ13hpCARD}
###    sed -e 's|datacards/../workspaces/||g' -e '/CMS_sig_p/ s|0|0.0|' -e '/CMS_sig_p1/ s|1|1.0|2' -e '/CMS_sig_p2/ s|1|1.0|' < ${JJDIR}/datacards/${JJCARDORIG} &> $OUTDIR/${COMBJJ8CARD}
#    cp ${JJDIR}/datacards/${JJCARDORIG}  $OUTDIR/${COMBJJ8CARD}
    cp ${JJ13DIR}/CMS_jj_WZ*${MASS}*.root ${OUTDIR}/
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/
fi

### WW only
LABEL="xww"
WWBASE="wwlvj_BulkG_WW_inclusive_c0p2_M${MASS}"
COMBWW8CARD="comb_${LABEL}.${MASS}.txt"
COMBWWHVTCARD="comb_${LABEL}_hvt.${MASS}.txt"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
    then
    cp ${WWDIR}/${COMBWWHVTCARD} ${OUTDIR}/${COMBWW8CARD}
    cp ${WWDIR}/${WWBASE}_*workspace.root  ${OUTDIR}/
fi

### WW 13 TeV only
LABEL="xww13"
EXOWW13CARDS="wwlvj_Wprimefix_WZ_lvjj_M${MASS}_combo_ALLP_unbin.txt"
COMBWW13CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 800 ]
    then
    python adapt_xsec_WW_13TeV.py ${MASS}
    sed -e 's|cards_mu_HPW/||g' -e 's|cards_mu_HPZ/||g'  -e 's|cards_mu_LPW/||g' -e 's|cards_mu_LPZ/||g' -e 's|cards_el_HPW/||g' -e 's|cards_el_HPZ/||g' -e 's|cards_el_LPW/||g' -e 's|cards_el_LPZ/||g' < ${WW13DIR}/${EXOWW13CARDS} &> $OUTDIR/${COMBWW13CARD}
    cp ${WW13DIR}/cards_*/*.root ${OUTDIR}/
fi

###put things together
cd $OUTDIR/

COMBALLCARD="comb_ALL.${MASS}.txt"
COMBSEMILEPCARD="comb_SEMILEPT.${MASS}.txt"
COMBSEMILEP813CARD="comb_SEMILEPT813.${MASS}.txt"
COMBJJ813CARD="comb_JJ813.${MASS}.txt"
COMBWW813CARD="comb_WW813.${MASS}.txt"
COMBZZ813CARD="comb_ZZ813.${MASS}.txt"
COMBALL13CARD="comb_ALL13.${MASS}.txt"
COMBALL813CARD="comb_ALL813.${MASS}.txt"
COMBJAM13CARD="comb_JAM13.${MASS}.txt"
COMBJAM813CARD="comb_JAM813.${MASS}.txt"

if [ $MASS -lt 800 ]
    then
    combineCards.py $COMBZZ8CARD &>  $COMBZZ813CARD
    combineCards.py $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBZZ8CARD &>  $COMBALL813CARD
    combineCards.py $COMBZZ8CARD &>  $COMBJAM813CARD
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
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBJAM813CARD
elif [ $MASS -lt 1200 ]
    then
    combineCards.py $COMBJJ8CARD &> $COMBJJ813CARD
    combineCards.py $COMBZZ8CARD $COMBZZ13CARD &>  $COMBZZ813CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD &>  $COMBWW813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBZZ13CARD $COMBWW13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBWW13CARD $COMBZZ13CARD $COMBZZ8CARD &>  $COMBALL813CARD
    combineCards.py $COMBWW13CARD &>  $COMBJAM13CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBJAM813CARD
elif [ $MASS -le 2500 ]
    then
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD &>  $COMBJJ813CARD
    combineCards.py $COMBZZ8CARD $COMBZZ13CARD &>  $COMBZZ813CARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD &>  $COMBWW813CARD
    combineCards.py $COMBWW8CARD $COMBZZ8CARD &>  $COMBSEMILEPCARD
    combineCards.py $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBJJ8CARD $COMBWW8CARD $COMBZZ8CARD &>  $COMBALLCARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD $COMBZZ13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD $COMBZZ13CARD &>  $COMBALL813CARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD &>  $COMBJAM13CARD
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD $COMBWW8CARD $COMBWW13CARD $COMBZZ8CARD &>  $COMBJAM813CARD
elif [ $MASS -le 2900 ]
    then
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD &>  $COMBJJ813CARD
    combineCards.py $COMBZZ13CARD &>  $COMBZZ813CARD
    combineCards.py $COMBWW13CARD &>  $COMBWW813CARD

    combineCards.py $COMBWW13CARD &>  $COMBSEMILEP813CARD
    combineCards.py $COMBJJ8CARD &>  $COMBALLCARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD $COMBZZ13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD $COMBWW13CARD $COMBZZ13CARD &>  $COMBALL813CARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD &>  $COMBJAM13CARD
    combineCards.py $COMBJJ8CARD $COMBJJ13CARD $COMBWW13CARD &>  $COMBJAM813CARD
else
    combineCards.py $COMBJJ13CARD &>  $COMBJJ813CARD
    combineCards.py $COMBZZ13CARD &>  $COMBZZ813CARD
    combineCards.py $COMBWW13CARD &>  $COMBWW813CARD

    combineCards.py $COMBWW13CARD &>  $COMBSEMILEP813CARD

    combineCards.py $COMBJJ13CARD $COMBWW13CARD $COMBZZ13CARD &>  $COMBALL13CARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD $COMBZZ13CARD &>  $COMBALL813CARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD &>  $COMBJAM13CARD
    combineCards.py $COMBJJ13CARD $COMBWW13CARD &>  $COMBJAM813CARD
fi
