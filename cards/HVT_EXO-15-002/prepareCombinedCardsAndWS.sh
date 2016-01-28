#! /bin/bash

# define input
if [ $# -lt 1 ]
    then
    echo "Need one input: mass point"
    exit 1
fi

MASS=$1
echo "Merging M=${MASS}"
LVJ8DIR="LVJ_cards_8TeV"
LVJ13DIR="LVJ_cards_13TeV"
JJ13DIR="JJ_cards_13TeV"
JJ8DIR="JJ_cards_8TeV"
LLJ8DIR="LLJ_cards_8TeV"

#prepare output
OUTDIR="comb_${MASS}"
mkdir $OUTDIR/

### LVJ Vprime 8 TeV only
LABEL="lvjwv8"
LVJWV8CARD="comb_xww.${MASS}.txt"
COMBLVJWV8CARD="comb_${LABEL}.${MASS}.txt"
WW8BASE="wwlvj_BulkG_WW_inclusive_c0p2_M${MASS}"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
    then
    python adapt_xsec_lvjWV_8TeV.py ${MASS}
    cp ${LVJ8DIR}/${COMBLVJWV8CARD} ${OUTDIR}/${COMBWW8CARD}
    cp ${LVJ8DIR}/${WW8BASE}_*workspace.root  ${OUTDIR}
fi

### LVJ Wprime 13 TeV only
LABEL="lvjwz13"
LVJWZ13CARD="wwlvj_Wprimefix_WZ_lvjj_M${MASS}_combo_ALLP_unbin.txt"
COMBLVJWZ13CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 800 ]
    then
    python adapt_xsec_lvjWZ_13TeV.py ${MASS}
    sed -e 's|cards_mu_HPW/||g' -e 's|cards_mu_HPZ/||g'  -e 's|cards_mu_LPW/||g' -e 's|cards_mu_LPZ/||g' -e 's|cards_el_HPW/||g' -e 's|cards_el_HPZ/||g' -e 's|cards_el_LPW/||g' -e 's|cards_el_LPZ/||g' < ${LVJ13DIR}/${LVJWZ13CARD} &> $OUTDIR/${COMBLVJWZ13CARD}
    cp ${LVJ13DIR}/cards_*/*_M${MASS}_*.root ${OUTDIR}/
fi

### LVJ Zprime 13 TeV only
LABEL="lvjww13"
LVJWW13CARD="wwlvj_Zprimefix_WW_lvjj_M${MASS}_combo_ALLP_unbin.txt"
COMBLVJWW13CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 800 ]
    then
    python adapt_xsec_lvjWW_13TeV.py ${MASS}
    sed -e 's|cards_mu_HPW/||g' -e 's|cards_mu_HPZ/||g'  -e 's|cards_mu_LPW/||g' -e 's|cards_mu_LPZ/||g' -e 's|cards_el_HPW/||g' -e 's|cards_el_HPZ/||g' -e 's|cards_el_LPW/||g' -e 's|cards_el_LPZ/||g' < ${LVJ13DIR}/${LVJWW13CARD} &> $OUTDIR/${COMBLVJWW13CARD}
    cp ${LVJ13DIR}/cards_*/*_M${MASS}_*.root ${OUTDIR}/
fi

### LVJ Vprime 13 TeV only
LABEL="lvjwv13"
LVJWV13CARD="wwlvj_Vprimefix_WV_lvjj_M${MASS}_combo_ALLP_unbin.txt"
COMBLVJWV13CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 800 ]
    then
    python adapt_xsec_lvjWV_13TeV.py ${MASS}
    sed -e 's|cards_mu_HPW/||g' -e 's|cards_mu_HPZ/||g'  -e 's|cards_mu_LPW/||g' -e 's|cards_mu_LPZ/||g' -e 's|cards_el_HPW/||g' -e 's|cards_el_HPZ/||g' -e 's|cards_el_LPW/||g' -e 's|cards_el_LPZ/||g' < ${LVJ13DIR}/${LVJWV13CARD} &> $OUTDIR/${COMBLVJWV13CARD}
    cp ${LVJ13DIR}/cards_*/*_M${MASS}_*.root ${OUTDIR}/
fi

### JJ Vprime 8 TeV only
LABEL="jjwv8"
JJWV8CARD="CMS_jj_WZfix_${MASS}_8TeV_CMS_jj_VV.txt"
COMBJJWV8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 1000 ] && [ $MASS -lt 3000 ]
    then
    python adapt_xsec_jjWV_8TeV.py ${MASS}
    sed -e 's|datacards/../workspaces/||g' -e 's|CMS_jj_bkg_8TeV|CMS_jj_bkg_WZ_8TeV|g' < ${JJ8DIR}/datacards/${JJWV8CARD} &> $OUTDIR/${COMBJJWV8CARD}
    echo ${JJWV8CARD}
    echo ${COMBJJWV8CARD}
    cp ${JJ8DIR}/workspaces/CMS_jj_WZ*${MASS}*.root ${OUTDIR}/
    cp ${JJ8DIR}/workspaces/CMS_jj_bkg_8TeV.root ${OUTDIR}/CMS_jj_bkg_WZ_8TeV.root
fi

### JJ Wprime 13 TeV only
LABEL="jjwz13"
JJWZ13CARD="CMS_jj_WZfix_${MASS}_13TeV_CMS_jj_VVnew.txt"
COMBJJWZ13CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
    python adapt_xsec_jjWZ_13TeV.py ${MASS}
    sed -e 's|datacards_withPDFuncertainties/../workspaces/||g' -e 's|datacards_backup/../workspaces/||g' -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJWZ13CARD} &> $OUTDIR/${COMBJJWZ13CARD}
    cp ${JJ13DIR}/CMS_jj_WZ_*${MASS}*.root ${OUTDIR}/.
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/.
fi

### JJ Zprime 13 TeV only
LABEL="jjww13"
JJWW13CARD="CMS_jj_ZprimeWWfix_${MASS}_13TeV_CMS_jj_VVnew.txt"
COMBJJWW13CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
    python adapt_xsec_jjWW_13TeV.py ${MASS}
    sed -e 's|datacards_withPDFuncertainties/../workspaces/||g' -e 's|datacards_backup/../workspaces/||g' -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJWW13CARD} &> $OUTDIR/${COMBJJWW13CARD}
    cp ${JJ13DIR}/CMS_jj_ZprimeWW_*${MASS}*.root ${OUTDIR}/.
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/.
fi

### JJ Vprime 13 TeV only
LABEL="jjwv13"
JJWV13CARD="CMS_jj_VprimeWVfix_${MASS}_13TeV.txt"
COMBJJWV13CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1200 ]
then
    python adapt_xsec_jjWV_13TeV.py ${MASS}
    sed -e 's|datacards_withPDFuncertainties/../workspaces/||g' -e 's|datacards_backup/../workspaces/||g' -e 's|datacards/../workspaces/||g' -e 's|../workspaces/||g' < ${JJ13DIR}/${JJWV13CARD} &> $OUTDIR/${COMBJJWV13CARD}
    cp ${JJ13DIR}/CMS_jj_ZprimeWW_*${MASS}*.root ${OUTDIR}/.
    cp ${JJ13DIR}/CMS_jj_WZ_*${MASS}*.root ${OUTDIR}/.
    cp ${JJ13DIR}/CMS_jj_bkg_13TeV.root ${OUTDIR}/.
fi

### LL Wprime 8 TeV only
LABEL="lljwz8"
LLJWZ8CARD="comb_xzz.${MASS}.txt"
COMBLLJWZ8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 600 ] && [ $MASS -le 2500 ]
    then
    python adapt_xsec_lljWZ_8TeV.py ${MASS}
    cp ${LLJ8DIR}/${MASS}/${COMBLLJWZ8CARD} ${OUTDIR}/
    cp ${LLJ8DIR}/${MASS}/*HP.input*.root  ${OUTDIR}/
fi

###put things together
cd $OUTDIR/

COMBJJLVJHVT13="comb_JJLVJHVT13.${MASS}.txt"
COMBJJLVJHVT138="comb_JJLVJHVT138.${MASS}.txt"
COMBALLHVT138="comb_ALLHVT138.${MASS}.txt"

if [ $MASS -lt 800 ]
    then
    combineCards.py $COMBLLJWZ8CARD &> $COMBALLHVT138
elif [ $MASS -lt 1000 ]
    then
    combineCards.py $COMBLVJWV13CARD &>  $COMBJJLVJHVT13
    combineCards.py $COMBLVJWV8CARD $COMBLVJWV13CARD &> $COMBJJLVJHVT138  
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZ8CARD $COMBLVJWV13CARD &> $COMBALLHVT138  
elif [ $MASS -lt 1200 ]
    then
    combineCards.py $COMBLVJWV13CARD &>  $COMBJJLVJHVT13
    combineCards.py $COMBLVJWV8CARD $COMBLVJWV13CARD $COMBJJWV8CARD &> $COMBJJLVJHVT138
    combineCards.py $COMBLVJWV8CARD $COMBLVJWV13CARD $COMBJJWV8CARD $COMBLLJWZ8CARD &> $COMBALLHVT138
elif [ $MASS -le 2500 ]
    then
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &>  $COMBJJLVJHVT13
    combineCards.py $COMBLVJWV8CARD $COMBLVJWV13CARD $COMBJJWV8CARD $COMBJJWV13CARD &> $COMBJJLVJHVT138
    combineCards.py $COMBLVJWV8CARD $COMBLVJWV13CARD $COMBJJWV8CARD $COMBLLJWZ8CARD $COMBJJWV13CARD &> $COMBALLHVT138
elif [ $MASS -lt 3000 ]
    then
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &>  $COMBJJLVJHVT13
    combineCards.py $COMBLVJWV13CARD $COMBJJWV8CARD $COMBJJWV13CARD &> $COMBJJLVJHVT138
    combineCards.py $COMBLVJWV13CARD $COMBJJWV8CARD $COMBJJWV13CARD &> $COMBALLHVT138
elif [ $MASS -le 4000 ]
    then
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &>  $COMBJJLVJHVT13
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBJJLVJHVT138
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBALLHVT138
fi     
