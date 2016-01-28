#for M in $( cat masses.txt ); do ./prepareCombinedCardsAndWS.sh $M ; done

#rm comb_*/output_* -r
#rm -r comb_*/logs

#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjwz13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjww13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjwv13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjwz13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjww13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjwv13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M JJLVJHVT13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjwv8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lljwz8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjwv8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M JJLVJHVT138; done

#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjwz13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjww13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjwv13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjwz13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjww13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjwv13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M JJLVJHVT13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjwv8; done
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lljwz8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjwv8; done
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M JJLVJHVT138; done

#./mergeHarvestedCombinationTrees.sh lvjwz13
#./mergeHarvestedCombinationTrees.sh lvjww13
#./mergeHarvestedCombinationTrees.sh lvjwv13
#./mergeHarvestedCombinationTrees.sh jjwz13
#./mergeHarvestedCombinationTrees.sh jjww13
#./mergeHarvestedCombinationTrees.sh jjwv13
#./mergeHarvestedCombinationTrees.sh JJLVJHVT13
#./mergeHarvestedCombinationTrees.sh lvjwv8
./mergeHarvestedCombinationTrees.sh lljwz8
#./mergeHarvestedCombinationTrees.sh jjwv8
./mergeHarvestedCombinationTrees.sh JJLVJHVT138

#rm -rf plots
#mkdir plots
#python plot_limits_jen.py LVJHVT13TeV
#python plot_limits_jen.py JJHVT13TeV
#python plot_limits_jen.py JJLVJHVT13TeV
