from ROOT import *
import ROOT
import array, math
import os
import sys

gROOT.Reset()
gROOT.SetStyle("Plain")
gStyle.SetOptStat(0)
gStyle.SetOptFit(0)
gStyle.SetTitleOffset(1.2,"Y")
gStyle.SetPadLeftMargin(0.18)
gStyle.SetPadBottomMargin(0.15)
gStyle.SetPadTopMargin(0.03)
gStyle.SetPadRightMargin(0.05)
gStyle.SetMarkerSize(1.5)
gStyle.SetHistLineWidth(1)
gStyle.SetStatFontSize(0.020)
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetNdivisions(510, "XYZ")
gStyle.SetLegendBorderSize(0)

masses =[m*100 for m in range(8,25+1)]

if len(sys.argv)>1:
  masses=[int(sys.argv[1])]

for mass in masses:
        print "mass = ",mass

	fWW=open("WW_cards/comb_xww."+str(mass)+".txt").readlines()
	outfile="WW_cards/comb_xww_bulkfix."+str(mass)+".txt"
	print outfile
        f=open(outfile,"w")

	for l in range(len(fWW)):
	  if "rate" in fWW[l]:
	    line="rate                                     "
	    fWWsplit=fWW[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
	    for s in range(len(fWWsplit)):
	      try:
	        float(fWWsplit[s])
	      except: continue
	      signal=(s in [1,6,11,16]) # only change signal
              numberWW=float(fWWsplit[s])
	      if signal:
                numberWW=numberWW/4.
              line+="%.5e  " % numberWW
	    line+="\n"
	    f.write(line)
	  else:
	    f.write(fWW[l])