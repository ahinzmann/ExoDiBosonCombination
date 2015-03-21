#! /bin/bash

MASS=$1

combineCards.py cards_hadronic/counting_BoostedTausFullyHadronic_M${MASS}_card_interpolate.txt cards_leptonic/datacard_EleEle_${MASS}_interpolate.txt cards_leptonic/datacard_EleMuo_${MASS}_interpolate.txt cards_leptonic/datacard_EleTau_${MASS}_interpolate.txt cards_leptonic/datacard_MuoMuo_${MASS}_interpolate.txt cards_leptonic/datacard_MuoTau_${MASS}_interpolate.txt > cards_combined/datacard_${MASS}_interpolate.txt
