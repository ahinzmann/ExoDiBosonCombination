## prepare hadronic cards
python interpolate_cards_hadronic.py

## prepare leptonic cards
cd cards_leptonics
root MakeDatacards_fineBinning.C
cd ..
python interpolate_cards_leptonic.py

## combine cards
#1: for M in $( cat masses.txt ); do ./combine_cards.sh $M ; done

## run limits
#2: edit paths and names in combine_exec.sh
#3: edit paths and names in parallelizeCombine.sh
#4: for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M ; done
#5: wait for the jobs on LXB to be finished
#6: edit paths and names in mergeCombinationTrees.sh
#7: edit paths and names in mergeHarvestedCombinationTrees.sh
#8: for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ; done
#9: ./mergeHarvestedCombinationTrees.sh
#10: edit paths and names in plot_golfcourse_Asymptotic.C
#11: run with root: $> root -b
     .L plot_golfcourse_Asymptotic.C+
     plot_golfcourse_Asymptotic()
#12: edit paths and names in plot_Significance.C
#13: run with root: $> root -b
     .L plot_Significance.C+
     plot_Significance()
