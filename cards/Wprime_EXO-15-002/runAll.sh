for M in $( cat masses.txt ); do ./prepareCombinedCardsAndWS.sh $M ; done

rm comb_*/output_* -r

for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xww13; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xjj13; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M WW813; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M JJ813; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xww; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xzz; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M xjj8; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M ALL; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M ALL13; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M ALL813; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M JAM13; done &
for M in $( cat masses.txt ); do ./parallelizeCombine.sh $M JAM813; done

for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xww13; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xjj13; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M WW813; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M JJ813; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xww; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xzz; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M xjj8; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALL; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALL13; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M ALL813; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M JAM13; done &
for M in $( cat masses.txt ); do ./mergeCombinationTrees.sh $M JAM813; done

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
./mergeHarvestedCombinationTrees.sh JAM13
./mergeHarvestedCombinationTrees.sh JAM813

python plot_limit_comparison_expected.py
python plot_limit_comparison_expected.py JJ813TeV
python plot_limit_comparison_expected.py ZZ813TeV
python plot_limit_comparison_expected.py WW813TeV
python plot_limit_comparison_expected.py ALL8TeV
python plot_limit_comparison_expected.py ALL13TeV
python plot_limit_comparison_expected.py ALL813TeV
python plot_limit_comparison_expected.py JAM13TeV
python plot_limit_comparison_expected.py JAM813TeV
python plot_limit_comparison_band.py
python plot_limit_comparison_band.py JJ813TeV
python plot_limit_comparison_band.py ZZ813TeV
python plot_limit_comparison_band.py WW813TeV
python plot_limit_comparison_band.py ALL8TeV
python plot_limit_comparison_band.py ALL13TeV
python plot_limit_comparison_band.py ALL813TeV
python plot_limit_comparison_band.py JAM13TeV
python plot_limit_comparison_band.py JAM813TeV
python plot_significance_comparison.py
python plot_significance_comparison.py JJ813TeV
python plot_significance_comparison.py ZZ813TeV
python plot_significance_comparison.py WW813TeV
python plot_significance_comparison.py ALL8TeV
python plot_significance_comparison.py ALL13TeV
python plot_significance_comparison.py ALL813TeV
python plot_significance_comparison.py JAM13TeV
python plot_significance_comparison.py JAM813TeV
