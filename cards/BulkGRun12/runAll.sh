for M in $( cat masses.txt ); do ./prepareCombinedCardsAndWS.sh $M ; done

for M in $( cat masses813.txt ); do ./parallelizeCombine.sh $M xww13; done &
for M in $( cat masses813.txt ); do ./parallelizeCombine.sh $M xzz13; done &
for M in $( cat masses813.txt ); do ./parallelizeCombine.sh $M WW813; done &
for M in $( cat masses813.txt ); do ./parallelizeCombine.sh $M ZZ813; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xww; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xzz; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xjj8; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M ALL; done

for M in $( cat masses813.txt ); do ./mergeCombinationTrees.sh $M xww13; done &
for M in $( cat masses813.txt ); do ./mergeCombinationTrees.sh $M xzz13; done &
for M in $( cat masses813.txt ); do ./mergeCombinationTrees.sh $M WW813; done &
for M in $( cat masses813.txt ); do ./mergeCombinationTrees.sh $M ZZ813; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xww; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xzz; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xjj8; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALL; done

./mergeHarvestedCombinationTrees.sh xww13
./mergeHarvestedCombinationTrees.sh xzz13
./mergeHarvestedCombinationTrees.sh WW813
./mergeHarvestedCombinationTrees.sh ZZ813
./mergeHarvestedCombinationTrees.sh xww
./mergeHarvestedCombinationTrees.sh xzz
./mergeHarvestedCombinationTrees.sh xjj8
./mergeHarvestedCombinationTrees.sh ALL
