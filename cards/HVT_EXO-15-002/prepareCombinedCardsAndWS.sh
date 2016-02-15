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
TTJZH8DIR="cards_ZH_8TeV"
LVJWH8DIR="cards_WH_8TeV"
JJVH8DIR="cards_VH_8TeV"

#prepare output
OUTDIR="comb_${MASS}"
mkdir $OUTDIR/

### qqtautau ZprimeZH 8 TeV only
LABEL="ttjzh8"
TTJZH8CARD="datacard_${MASS}_interpolate_ZHadapt.txt"
COMBTTJZH8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
then
python adapt_xsec_ttjZH_8TeV.py ${MASS}
sed -e 's|lumi|lumi_8TeV|g' -e 's|PUReweighting|CMS_pu|g' -e 's|VTag|CMS_eff_tau21_sf|g' -e 's|EleScale|CMS_scale_e|g' -e 's|EleResol|CMS_res_e|g' -e 's|MuoScale|CMS_scale_m|g' -e 's|MuoResol|CMS_res_m|g' -e 's|EleID|CMS_eff_e|g' -e 's|MuoID|CMS_eff_m|g' -e 's|JES|CMS_scale_j|g' -e 's|JER|CMS_res_j|g' -e 's|BTagSyst|CMS_btagger|g' < ${TTJZH8DIR}/${TTJZH8CARD} &> $OUTDIR/${COMBTTJZH8CARD}
fi

### qqtautau WprimeWH 8 TeV only
LABEL="ttjwh8"
TTJWH8CARD="datacard_${MASS}_interpolate_WHadapt.txt"
COMBTTJWH8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
then
python adapt_xsec_ttjWH_8TeV.py ${MASS}
sed -e 's|lumi|lumi_8TeV|g' -e 's|PUReweighting|CMS_pu|g' -e 's|VTag|CMS_eff_tau21_sf|g' -e 's|EleScale|CMS_scale_e|g' -e 's|EleResol|CMS_res_e|g' -e 's|MuoScale|CMS_scale_m|g' -e 's|MuoResol|CMS_res_m|g' -e 's|EleID|CMS_eff_e|g' -e 's|MuoID|CMS_eff_m|g' -e 's|JES|CMS_scale_j|g' -e 's|JER|CMS_res_j|g' -e 's|BTagSyst|CMS_btagger|g' < ${TTJZH8DIR}/${TTJWH8CARD} &> $OUTDIR/${COMBTTJWH8CARD}
fi

### qqtautau VprimeVH 8 TeV only
LABEL="ttjvh8"
TTJVH8CARD="datacard_${MASS}_interpolate_VHadapt.txt"
COMBTTJVH8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
then
python adapt_xsec_ttjVH_8TeV.py ${MASS}
sed -e 's|lumi|lumi_8TeV|g' -e 's|PUReweighting|CMS_pu|g' -e 's|VTag|CMS_eff_tau21_sf|g' -e 's|EleScale|CMS_scale_e|g' -e 's|EleResol|CMS_res_e|g' -e 's|MuoScale|CMS_scale_m|g' -e 's|MuoResol|CMS_res_m|g' -e 's|EleID|CMS_eff_e|g' -e 's|MuoID|CMS_eff_m|g' -e 's|JES|CMS_scale_j|g' -e 's|JER|CMS_res_j|g' -e 's|BTagSyst|CMS_btagger|g' < ${TTJZH8DIR}/${TTJVH8CARD} &> $OUTDIR/${COMBTTJVH8CARD}
fi

### JJ WprimeWH 8 TeV only
LABEL="jjwh8"
JJWH8CARD="CMS_jj_HWqq_${MASS}_8TeV_CMS_jj_HWOnly_adapt.txt"
COMBJJWH8CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1000 ] && [ $MASS -le 2600 ]
then
python adapt_xsec_jjWH_8TeV.py ${MASS}
sed -e 's|datacards/../workspaces/||g' -e 's|datacards/../HbbVqqHwwworkspaces/||g'  -e 's|CMS_Btagging|CMS_doubleBtagging|g' < ${JJVH8DIR}/${JJWH8CARD} &> $OUTDIR/${COMBJJWH8CARD}
cp ${JJVH8DIR}/CMS_jj_*${MASS}*.root ${OUTDIR}/
cp ${JJVH8DIR}/CMS_jj_bkg_8TeV.root ${OUTDIR}/
fi

### JJ ZprimeZH 8 TeV only
LABEL="jjzh8"
JJZH8CARD="CMS_jj_HZqq_${MASS}_8TeV_CMS_jj_HZOnly_adapt.txt"
COMBJJZH8CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1000 ] && [ $MASS -le 2600 ]
then
python adapt_xsec_jjZH_8TeV.py ${MASS}
sed -e 's|datacards/../workspaces/||g' -e 's|datacards/../HbbVqqHwwworkspaces/||g'  -e 's|CMS_Btagging|CMS_doubleBtagging|g' < ${JJVH8DIR}/${JJZH8CARD} &> $OUTDIR/${COMBJJZH8CARD}
cp ${JJVH8DIR}/CMS_jj_*${MASS}*.root ${OUTDIR}/
cp ${JJVH8DIR}/CMS_jj_bkg_8TeV.root ${OUTDIR}/
fi

### JJ VprimeVH 8 TeV only
LABEL="jjvh8"
JJVH8CARD="CMS_jj_HVqq_${MASS}_8TeV_CMS_jj_HVCombined_adapt.txt"
COMBJJVH8CARD="comb_${LABEL}.${MASS}.txt"
 
if [ $MASS -ge 1000 ] && [ $MASS -le 2600 ]
then
python adapt_xsec_jjVH_8TeV.py ${MASS}
sed -e 's|datacards/../workspaces/||g' -e 's|datacards/../HbbVqqHwwworkspaces/||g'  -e 's|CMS_Btagging|CMS_doubleBtagging|g' < ${JJVH8DIR}/${JJVH8CARD} &> $OUTDIR/${COMBJJVH8CARD}
cp ${JJVH8DIR}/CMS_jj_*${MASS}*.root ${OUTDIR}/
cp ${JJVH8DIR}/CMS_jj_bkg_8TeV.root ${OUTDIR}/
fi    

### LVJ WprimeWH 8 TeV only
LABEL="lvjwh8"
LVJWH8BASE="whlvj_MWp_${MASS}_bb"
LVJWH8ELEBASE="cards_el/${LVJWH8BASE}_el"
LVJWH8MUBASE="cards_mu/${LVJWH8BASE}_mu"
LVJWH8CARDS="${LABEL}_mv1JLP=${LVJWH8MUBASE}_ALLP_unbin.txt ${LABEL}_ev1JLP=${LVJWH8ELEBASE}_ALLP_unbin.txt"
COMBLVJWH8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
    then
    cd ${LVJWH8DIR}/
    combineCards.py $LVJWH8CARDS &> tmp_XWH_card.txt
    sed -e 's|cards_mu/||g'  -e 's|cards_el/||g'   -e 's|CMS_xwh_prunedmass|CMS_jet_mass|g'   -e 's|CMS_xwh_btagger|CMS_btagger|g' -e 's|CMS_xwh_btag_eff|CMS_doubleBtagging|g' < tmp_XWH_card.txt  > ${COMBLVJWH8CARD}
    cd -
    cp ${LVJWH8DIR}/${COMBLVJWH8CARD} ${OUTDIR}/${COMBLVJWH8CARD}
    cp ${LVJWH8DIR}/cards_el/${LVJWH8BASE}_*workspace.root  ${OUTDIR}/
    cp ${LVJWH8DIR}/cards_mu/${LVJWH8BASE}_*workspace.root  ${OUTDIR}/
fi

### LVJ Vprime 8 TeV only
LABEL="lvjwv8"
LVJWV8CARD="comb_xww.${MASS}.txt"
COMBLVJWV8CARD="comb_${LABEL}.${MASS}.txt"
WW8BASE="wwlvj_BulkG_WW_inclusive_c0p2_M${MASS}"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
    then
    python adapt_xsec_lvjWV_8TeV.py ${MASS}
    cp ${LVJ8DIR}/${COMBLVJWV8CARD} ${OUTDIR}/
    cp ${LVJ8DIR}/${WW8BASE}_*workspace.root ${OUTDIR}/
fi

### LVJ Wprime 8 TeV only
LABEL="lvjwz8"
LVJWZ8CARD="comb_xww.${MASS}.txt"
COMBLVJWZ8CARD="comb_${LABEL}.${MASS}.txt"
WW8BASE="wwlvj_BulkG_WW_inclusive_c0p2_M${MASS}"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
    then
    python adapt_xsec_lvjWZ_8TeV.py ${MASS}
    cp ${LVJ8DIR}/${COMBLVJWZ8CARD} ${OUTDIR}/
    cp ${LVJ8DIR}/${WW8BASE}_*workspace.root ${OUTDIR}/
fi

### LVJ Zprime 8 TeV only
LABEL="lvjww8"
LVJWW8CARD="comb_xww.${MASS}.txt"
COMBLVJWW8CARD="comb_${LABEL}.${MASS}.txt"
WW8BASE="wwlvj_BulkG_WW_inclusive_c0p2_M${MASS}"

if [ $MASS -ge 800 ] && [ $MASS -le 2500 ]
    then
    python adapt_xsec_lvjWW_8TeV.py ${MASS}
    cp ${LVJ8DIR}/${COMBLVJWW8CARD} ${OUTDIR}/
    cp ${LVJ8DIR}/${WW8BASE}_*workspace.root ${OUTDIR}/
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
JJWV8CARD="CMS_jj_WVfix_${MASS}_8TeV_CMS_jj_VV.txt"
COMBJJWV8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 1000 ] && [ $MASS -lt 3000 ]
    then
    python adapt_xsec_jjWV_8TeV.py ${MASS}
    sed -e 's|datacards/../workspaces/||g' -e 's|CMS_jj_bkg_8TeV|CMS_jj_bkg_WZ_8TeV|g' < ${JJ8DIR}/datacards/${JJWV8CARD} &> $OUTDIR/${COMBJJWV8CARD}
    cp ${JJ8DIR}/workspaces/CMS_jj_WZ*${MASS}*.root ${OUTDIR}/
    cp ${JJ8DIR}/workspaces/CMS_jj_bkg_8TeV.root ${OUTDIR}/CMS_jj_bkg_WZ_8TeV.root
fi

### JJ Zprime 8 TeV only
LABEL="jjww8"
JJWW8CARD="CMS_jj_WWfix_${MASS}_8TeV_CMS_jj_VV.txt"
COMBJJWW8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 1000 ] && [ $MASS -lt 3000 ]
    then
    python adapt_xsec_jjWW_8TeV.py ${MASS}
    sed -e 's|datacards/../workspaces/||g' -e 's|CMS_jj_bkg_8TeV|CMS_jj_bkg_WZ_8TeV|g' < ${JJ8DIR}/datacards/${JJWW8CARD} &> $OUTDIR/${COMBJJWW8CARD}
    cp ${JJ8DIR}/workspaces/CMS_jj_WZ*${MASS}*.root ${OUTDIR}/
    cp ${JJ8DIR}/workspaces/CMS_jj_bkg_8TeV.root ${OUTDIR}/CMS_jj_bkg_WZ_8TeV.root
fi

### JJ Wprime 8 TeV only
LABEL="jjwz8"
JJWZ8CARD="CMS_jj_WZfix_${MASS}_8TeV_CMS_jj_VV.txt"
COMBJJWZ8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 1000 ] && [ $MASS -lt 3000 ]
    then
    python adapt_xsec_jjWZ_8TeV.py ${MASS}
    sed -e 's|datacards/../workspaces/||g' -e 's|CMS_jj_bkg_8TeV|CMS_jj_bkg_WZ_8TeV|g' < ${JJ8DIR}/datacards/${JJWZ8CARD} &> $OUTDIR/${COMBJJWZ8CARD}
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

### LLJ WprimeWZ 8 TeV only
LABEL="lljwz8"
LLJWZ8CARD="comb_xzz.${MASS}.txt"
COMBLLJWZ8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 600 ] && [ $MASS -le 2500 ]
    then
    python adapt_xsec_lljWZ_8TeV.py ${MASS}
    cp ${LLJ8DIR}/${MASS}/${COMBLLJWZ8CARD} ${OUTDIR}/
    cp ${LLJ8DIR}/${MASS}/*HP.input*.root  ${OUTDIR}/
fi

### LLJ Vprime (WZ/ZH) 8 TeV only
LABEL="lljwzh8"
LLJWZH8CARD="comb_xzz.${MASS}.txt"
COMBLLJWZH8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 600 ] && [ $MASS -le 2500 ]
    then
    python adapt_xsec_lljWZ_VH_8TeV.py ${MASS}
    cp ${LLJ8DIR}/${MASS}/${COMBLLJWZH8CARD} ${OUTDIR}/
    cp ${LLJ8DIR}/${MASS}/*HP.input*.root  ${OUTDIR}/
fi

### LLJ Zprime (ZH) 8 TeV only
LABEL="lljzh8"
LLJZH8CARD="comb_xzz.${MASS}.txt"
COMBLLJZH8CARD="comb_${LABEL}.${MASS}.txt"

if [ $MASS -ge 600 ] && [ $MASS -le 2500 ]
    then
    python adapt_xsec_lljZH_8TeV.py ${MASS}
    cp ${LLJ8DIR}/${MASS}/${COMBLLJZH8CARD} ${OUTDIR}/
    cp ${LLJ8DIR}/${MASS}/*HP.input*.root  ${OUTDIR}/
fi

###put things together
cd $OUTDIR/

# 13 TeV LVJ+JJ only
COMBJJLVJHVT13="comb_JJLVJHVT13.${MASS}.txt" #triplet
COMBJJLVJWPRIME13="comb_JJLVJWPRIME13.${MASS}.txt" #charged singlet
COMBJJLVJZPRIME13="comb_JJLVJZPRIME13.${MASS}.txt" #neutral singlet
# 8 TeV LLJ+LVJ+JJ (WV) only
COMBALLWVHVT8="comb_ALLWVHVT8.${MASS}.txt" #triplet
COMBALLWVWPRIME8="comb_ALLWVWPRIME8.${MASS}.txt" #charged singlet
COMBALLWVZPRIME8="comb_ALLWVZPRIME8.${MASS}.txt" #neutral singlet
#8 + 13 TeV LLJ+LVJ+JJ (WV)
COMBALLWVHVT138="comb_ALLWVHVT138.${MASS}.txt" #triplet
COMBALLWVWPRIME138=="comb_ALLWVWPRIME138.${MASS}.txt" #charged singlet
COMBALLWVZPRIME138=="comb_ALLWVZPRIME138.${MASS}.txt" #neutral singlet
#8 TeV VH only
COMBALLHVHVT8="comb_ALLHVHVT8.${MASS}.txt" #triplet
COMBALLHVWPRIME8="comb_ALLHVWPRIME8.${MASS}.txt" #charged singlet
COMBALLHVZPRIME8="comb_ALLHVZPRIME8.${MASS}.txt" #neutral singlet
#8 TeV VH+WV
COMBALLHVT8="comb_ALLHVT8.${MASS}.txt" #triplet
COMBALLWPRIME8="comb_ALLWPRIME8.${MASS}.txt" #charged singlet
COMBALLZPRIME8="comb_ALLZPRIME8.${MASS}.txt" #neutral singlet
#8 + 13 TeV VH+WV
COMBALLHVT138="comb_ALLHVT138.${MASS}.txt" #triplet
COMBALLWPRIME138="comb_ALLWPRIME138.${MASS}.txt" #charged singlet
COMBALLZPRIME138="comb_ALLZPRIME138.${MASS}.txt" #neutral singlet

#if [ $MASS -lt 800 ]
#    then
#    combineCards.py $COMBLLJWZ8CARD &> $COMBALLHVT138
#    combineCards.py $COMBLLJWZ8CARD &> $COMBALLHVT8
if [ $MASS -lt 1000 ] #800-900
    then
    
    # 13 TeV LVJ+JJ only
    combineCards.py $COMBLVJWV13CARD &> $COMBJJLVJHVT13
    combineCards.py $COMBLVJWZ13CARD &> $COMBJJLVJWPRIME13
    combineCards.py $COMBLVJWW13CARD &> $COMBJJLVJZPRIME13
    
    # 8 TeV LLJ+LVJ+JJ (WV) only
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZ8CARD &> $COMBALLWVHVT8
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD &> $COMBALLWVWPRIME8
    combineCards.py $COMBLVJWW8CARD &> $COMBALLWVZPRIME8
    
    #8 + 13 TeV LLJ+LVJ+JJ (WV)
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZ8CARD $COMBLVJWV13CARD &> $COMBALLWVHVT138
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBLVJWZ13CARD &> $COMBALLWVWPRIME138
    combineCards.py $COMBLVJWW8CARD $COMBLVJWW13CARD &> $COMBALLWVZPRIME138
    
    #8 TeV VH only
    combineCards.py $COMBTTJVH8CARD $COMBLVJWH8CARD &> $COMBALLHVHVT8
    combineCards.py $COMBTTJWH8CARD $COMBLVJWH8CARD &> $COMBALLHVWPRIME8
    combineCards.py $COMBTTJZH8CARD &> $COMBALLHVZPRIME8
    
    #8 TeV VH+WV
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZH8CARD $COMBTTJVH8CARD $COMBLVJWH8CARD &> $COMBALLHVT8
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBTTJWH8CARD $COMBLVJWH8CARD &> $COMBALLWPRIME8
    combineCards.py $COMBLVJWW8CARD $COMBTTJZH8CARD $COMBLLJZH8CARD &> $COMBALLZPRIME8
      
    #8 + 13 TeV VH+WV
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZH8CARD $COMBLVJWV13CARD $COMBTTJVH8CARD $COMBLVJWH8CARD &> $COMBALLHVT138
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBLVJWZ13CARD $COMBTTJWH8CARD $COMBLVJWH8CARD &> $COMBALLWPRIME138
    combineCards.py $COMBLVJWW8CARD $COMBLVJWW13CARD $COMBLLJZH8CARD $COMBTTJZH8CARD &> $COMBALLZPRIME138
      
elif [ $MASS -lt 1200 ] #1000-1100
    then
    
    # 13 TeV LVJ+JJ only
    combineCards.py $COMBLVJWV13CARD &> $COMBJJLVJHVT13
    combineCards.py $COMBLVJWZ13CARD &> $COMBJJLVJWPRIME13
    combineCards.py $COMBLVJWW13CARD &> $COMBJJLVJZPRIME13

    # 8 TeV LLJ+LVJ+JJ (WV) only
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZ8CARD $COMBJJWV8CARD &> $COMBALLWVHVT8
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBJJWZ8CARD &> $COMBALLWVWPRIME8
    combineCards.py $COMBLVJWW8CARD $COMBJJWW8CARD &> $COMBALLWVZPRIME8
 
    #8 + 13 TeV LLJ+LVJ+JJ (WV)
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZ8CARD $COMBJJWV8CARD $COMBLVJWV13CARD &> $COMBALLWVHVT138
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBJJWZ8CARD $COMBLVJWZ13CARD &> $COMBALLWVWPRIME138
    combineCards.py $COMBLVJWW8CARD $COMBJJWW8CARD $COMBLVJWW13CARD &> $COMBALLWVZPRIME138

    #8 TeV VH only
    combineCards.py $COMBTTJVH8CARD $COMBLVJWH8CARD $COMBJJVH8CARD &> $COMBALLHVHVT8
    combineCards.py $COMBTTJWH8CARD $COMBLVJWH8CARD $COMBJJWH8CARD &> $COMBALLHVWPRIME8
    combineCards.py $COMBTTJZH8CARD $COMBJJZH8CARD &> $COMBALLHVZPRIME8

    #8 TeV VH+WV
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZH8CARD $COMBJJWV8CARD $COMBTTJVH8CARD $COMBLVJWH8CARD $COMBJJVH8CARD &> $COMBALLHVT8
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBJJWZ8CARD $COMBTTJWH8CARD $COMBLVJWH8CARD $COMBJJWH8CARD &> $COMBALLWPRIME8
    combineCards.py $COMBLVJWW8CARD $COMBJJWW8CARD $COMBTTJZH8CARD $COMBJJZH8CARD $COMBLLJZH8CARD &> $COMBALLZPRIME8

    #8 + 13 TeV VH+WV
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZH8CARD $COMBJJWV8CARD $COMBLVJWV13CARD $COMBTTJVH8CARD $COMBLVJWH8CARD $COMBJJVH8CARD &> $COMBALLHVT138
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBJJWZ8CARD $COMBLVJWZ13CARD $COMBTTJWH8CARD $COMBLVJWH8CARD $COMBJJWH8CARD &> $COMBALLWPRIME138
    combineCards.py $COMBLVJWW8CARD $COMBJJWW8CARD $COMBLVJWW13CARD $COMBTTJZH8CARD $COMBJJZH8CARD $COMBLLJZH8CARD &> $COMBALLZPRIME138     
             
elif [ $MASS -le 2500 ] #1200-2500
    then

    # 13 TeV LVJ+JJ only
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBJJLVJHVT13
    combineCards.py $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBJJLVJWPRIME13
    combineCards.py $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBJJLVJZPRIME13

    # 8 TeV LLJ+LVJ+JJ (WV) only
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZ8CARD $COMBJJWV8CARD &> $COMBALLWVHVT8
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBJJWZ8CARD &> $COMBALLWVWPRIME8
    combineCards.py $COMBLVJWW8CARD $COMBJJWW8CARD &> $COMBALLWVZPRIME8

    #8 + 13 TeV LLJ+LVJ+JJ (WV)
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZ8CARD $COMBJJWV8CARD $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBALLWVHVT138
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBJJWZ8CARD $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBALLWVWPRIME138
    combineCards.py $COMBLVJWW8CARD $COMBJJWW8CARD $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBALLWVZPRIME138

    #8 TeV VH only
    combineCards.py $COMBTTJVH8CARD $COMBLVJWH8CARD $COMBJJVH8CARD &> $COMBALLHVHVT8
    combineCards.py $COMBTTJWH8CARD $COMBLVJWH8CARD $COMBJJWH8CARD &> $COMBALLHVWPRIME8
    combineCards.py $COMBTTJZH8CARD $COMBJJZH8CARD &> $COMBALLHVZPRIME8

    #8 TeV VH+WV
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZH8CARD $COMBJJWV8CARD $COMBTTJVH8CARD $COMBLVJWH8CARD $COMBJJVH8CARD &> $COMBALLHVT8
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBJJWZ8CARD $COMBTTJWH8CARD $COMBLVJWH8CARD $COMBJJWH8CARD &> $COMBALLWPRIME8
    combineCards.py $COMBLVJWW8CARD $COMBJJWW8CARD $COMBTTJZH8CARD $COMBJJZH8CARD $COMBLLJZH8CARD &> $COMBALLZPRIME8

    #8 + 13 TeV VH+WV
    combineCards.py $COMBLVJWV8CARD $COMBLLJWZH8CARD $COMBJJWV8CARD $COMBLVJWV13CARD $COMBJJWV13CARD $COMBTTJVH8CARD $COMBLVJWH8CARD $COMBJJVH8CARD &> $COMBALLHVT138
    combineCards.py $COMBLVJWZ8CARD $COMBLLJWZ8CARD $COMBJJWZ8CARD $COMBLVJWZ13CARD $COMBJJWZ13CARD $COMBTTJWH8CARD $COMBLVJWH8CARD $COMBJJWH8CARD &> $COMBALLWPRIME138
    combineCards.py $COMBLVJWW8CARD $COMBJJWW8CARD $COMBLVJWW13CARD $COMBJJWW13CARD $COMBTTJZH8CARD $COMBJJZH8CARD $COMBLLJZH8CARD &> $COMBALLZPRIME138
                 
elif [ $MASS -le 2600 ] #2600
    then
    
    # 13 TeV LVJ+JJ only
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBJJLVJHVT13
    combineCards.py $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBJJLVJWPRIME13
    combineCards.py $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBJJLVJZPRIME13

    # 8 TeV LLJ+LVJ+JJ (WV) only
    combineCards.py $COMBJJWV8CARD &> $COMBALLWVHVT8
    combineCards.py $COMBJJWZ8CARD &> $COMBALLWVWPRIME8
    combineCards.py $COMBJJWW8CARD &> $COMBALLWVZPRIME8

    #8 + 13 TeV LLJ+LVJ+JJ (WV)
    combineCards.py $COMBJJWV8CARD $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBALLWVHVT138
    combineCards.py $COMBJJWZ8CARD $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBALLWVWPRIME138
    combineCards.py $COMBJJWW8CARD $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBALLWVZPRIME138

    #8 TeV VH only
    combineCards.py $COMBJJVH8CARD &> $COMBALLHVHVT8
    combineCards.py $COMBJJWH8CARD &> $COMBALLHVWPRIME8
    combineCards.py $COMBJJZH8CARD &> $COMBALLHVZPRIME8

    #8 TeV VH+WV
    combineCards.py $COMBJJWV8CARD $COMBJJVH8CARD &> $COMBALLHVT8
    combineCards.py $COMBJJWZ8CARD $COMBJJWH8CARD &> $COMBALLWPRIME8
    combineCards.py $COMBJJWW8CARD $COMBJJZH8CARD &> $COMBALLZPRIME8

    #8 + 13 TeV VH+WV
    combineCards.py $COMBJJWV8CARD $COMBLVJWV13CARD $COMBJJWV13CARD $COMBJJVH8CARD &> $COMBALLHVT138
    combineCards.py $COMBJJWZ8CARD $COMBLVJWZ13CARD $COMBJJWZ13CARD $COMBJJWH8CARD &> $COMBALLWPRIME138
    combineCards.py $COMBJJWW8CARD $COMBLVJWW13CARD $COMBJJWW13CARD $COMBJJZH8CARD &> $COMBALLZPRIME138
                         
elif [ $MASS -lt 3000 ] #2500-2900
    then
    
    # 13 TeV LVJ+JJ only
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBJJLVJHVT13
    combineCards.py $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBJJLVJWPRIME13
    combineCards.py $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBJJLVJZPRIME13

    # 8 TeV LLJ+LVJ+JJ (WV) only
    combineCards.py $COMBJJWV8CARD &> $COMBALLWVHVT8
    combineCards.py $COMBJJWZ8CARD &> $COMBALLWVWPRIME8
    combineCards.py $COMBJJWW8CARD &> $COMBALLWVZPRIME8

    #8 + 13 TeV LLJ+LVJ+JJ (WV)
    combineCards.py $COMBJJWV8CARD $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBALLWVHVT138
    combineCards.py $COMBJJWZ8CARD $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBALLWVWPRIME138
    combineCards.py $COMBJJWW8CARD $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBALLWVZPRIME138

    #8 TeV VH+WV
    combineCards.py $COMBJJWV8CARD &> $COMBALLHVT8
    combineCards.py $COMBJJWZ8CARD &> $COMBALLWPRIME8
    combineCards.py $COMBJJWW8CARD &> $COMBALLZPRIME8
    
    #8 + 13 TeV VH+WV
    combineCards.py $COMBJJWV8CARD $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBALLHVT138
    combineCards.py $COMBJJWZ8CARD $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBALLWPRIME138
    combineCards.py $COMBJJWW8CARD $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBALLZPRIME138
     
elif [ $MASS -le 4000 ] #3000-4000
    then
    
    # 13 TeV LVJ+JJ only
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBJJLVJHVT13
    combineCards.py $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBJJLVJWPRIME13
    combineCards.py $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBJJLVJZPRIME13
    
    #8 + 13 TeV LLJ+LVJ+JJ (WV)
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBALLWVHVT138
    combineCards.py $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBALLWVWPRIME138
    combineCards.py $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBALLWVZPRIME138

    #8 + 13 TeV VH+WV
    combineCards.py $COMBLVJWV13CARD $COMBJJWV13CARD &> $COMBALLHVT138
    combineCards.py $COMBLVJWZ13CARD $COMBJJWZ13CARD &> $COMBALLWPRIME138
    combineCards.py $COMBLVJWW13CARD $COMBJJWW13CARD &> $COMBALLZPRIME138
     
fi  
