for M in $( cat masses.txt ); do ./prepareCombinedCardsAndWS.sh $M ; done

#rm comb_*/output_* -r
#rm -r comb_*/logs

# 13 TeV LVJ+JJ only
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M JJLVJHVT13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M JJLVJWPRIME13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M JJLVJZPRIME13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjwv13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjwz13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjww13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjwv13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjwz13; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjww13; done

#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M JJLVJHVT13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M JJLVJWPRIME13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M JJLVJZPRIME13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjwv13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjwz13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjww13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjwv13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjwz13; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjww13; done

#./mergeHarvestedCombinationTrees.sh JJLVJHVT13
#./mergeHarvestedCombinationTrees.sh JJLVJWPRIME13
#./mergeHarvestedCombinationTrees.sh JJLVJZPRIME13
#./mergeHarvestedCombinationTrees.sh lvjwv13
#./mergeHarvestedCombinationTrees.sh lvjwz13
#./mergeHarvestedCombinationTrees.sh lvjww13
#./mergeHarvestedCombinationTrees.sh jjwv13
#./mergeHarvestedCombinationTrees.sh jjwz13
#./mergeHarvestedCombinationTrees.sh jjww13

# 8 TeV LLJ+LVJ+JJ (WV) only
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLWVHVT8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLWVWPRIME8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLWVZPRIME8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjwv8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjwz8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjww8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjwv8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjwz8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjww8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lljwz8; done

#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLWVHVT8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLWVWPRIME8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLWVZPRIME8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjwv8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjwz8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjww8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjwv8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjwz8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjww8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lljwz8; done

#./mergeHarvestedCombinationTrees.sh ALLWVHVT8
#./mergeHarvestedCombinationTrees.sh ALLWVWPRIME8
#./mergeHarvestedCombinationTrees.sh ALLWVZPRIME8
#./mergeHarvestedCombinationTrees.sh lvjwv8
#./mergeHarvestedCombinationTrees.sh lvjwz8
#./mergeHarvestedCombinationTrees.sh lvjww8
#./mergeHarvestedCombinationTrees.sh jjwv8
#./mergeHarvestedCombinationTrees.sh jjwz8
#./mergeHarvestedCombinationTrees.sh jjww8
#./mergeHarvestedCombinationTrees.sh lljwz8

#8 + 13 TeV LLJ+LVJ+JJ (WV)
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLWVHVT138; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLWVWPRIME138; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLWVZPRIME138; done

#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLWVHVT138; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLWVWPRIME138; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLWVZPRIME138; done

#./mergeHarvestedCombinationTrees.sh ALLWVHVT138
#./mergeHarvestedCombinationTrees.sh ALLWVWPRIME138
#./mergeHarvestedCombinationTrees.sh ALLWVZPRIME138

#8 TeV VH only
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLHVHVT8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLHVWPRIME8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLHVZPRIME8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ttjvh8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ttjwh8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ttjzh8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjvh8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjwh8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M jjzh8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lvjwh8; done

#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLHVHVT8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLHVWPRIME8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLHVZPRIME8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ttjvh8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ttjwh8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ttjzh8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjvh8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjwh8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M jjzh8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lvjwh8; done

#./mergeHarvestedCombinationTrees.sh ALLHVHVT8
#./mergeHarvestedCombinationTrees.sh ALLHVWPRIME8
#./mergeHarvestedCombinationTrees.sh ALLHVZPRIME8
#./mergeHarvestedCombinationTrees.sh ttjvh8
#./mergeHarvestedCombinationTrees.sh ttjwh8
#./mergeHarvestedCombinationTrees.sh ttjzh8
#./mergeHarvestedCombinationTrees.sh jjvh8
#./mergeHarvestedCombinationTrees.sh jjwh8
#./mergeHarvestedCombinationTrees.sh jjzh8
#./mergeHarvestedCombinationTrees.sh lvjwh8

#8 TeV VH+WV
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLHVT8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLWPRIME8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLZPRIME8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lljzh8; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M lljwzh8; done

#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLHVT8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLWPRIME8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLZPRIME8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lljzh8; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M lljwzh8; done

#./mergeHarvestedCombinationTrees.sh ALLHVT8
#./mergeHarvestedCombinationTrees.sh ALLWPRIME8
#./mergeHarvestedCombinationTrees.sh ALLZPRIME8
#./mergeHarvestedCombinationTrees.sh lljzh8
#./mergeHarvestedCombinationTrees.sh lljwzh8

#8 + 13 TeV VH+WV
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLHVT138; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLWPRIME138; done
#for M in $( cat masses.txt ); do ./parallelizeCombine_T3.sh $M ALLZPRIME138; done

#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLHVT138; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLWPRIME138; done
#for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALLZPRIME138; done

#./mergeHarvestedCombinationTrees.sh ALLHVT138
#./mergeHarvestedCombinationTrees.sh ALLWPRIME138
#./mergeHarvestedCombinationTrees.sh ALLZPRIME138



#rm -rf plots
#mkdir plots
#python plot_limits_jen.py LVJHVT13TeV
#python plot_limits_jen.py JJHVT13TeV
#python plot_limits_jen.py JJLVJHVT13TeV
