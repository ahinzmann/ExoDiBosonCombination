for M in $( cat masses.txt ); do ./prepareCombinedCardsAndWS.sh $M ; done

for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xww13; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xjj13; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M WW813; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M JJ813; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xww; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xzz; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xjj8; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M ALL; done
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M ALL13; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M ALL813; done

for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xww13; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xjj13; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M WW813; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M JJ813; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xww; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xzz; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xjj8; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALL; done
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALL13; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALL813; done

./mergeHarvestedCombinationTrees.sh xww13
./mergeHarvestedCombinationTrees.sh xjj13
./mergeHarvestedCombinationTrees.sh WW813
./mergeHarvestedCombinationTrees.sh JJ813
./mergeHarvestedCombinationTrees.sh xww
./mergeHarvestedCombinationTrees.sh xzz
./mergeHarvestedCombinationTrees.sh xjj8
./mergeHarvestedCombinationTrees.sh ALL
./mergeHarvestedCombinationTrees.sh ALL13
./mergeHarvestedCombinationTrees.sh ALL813
