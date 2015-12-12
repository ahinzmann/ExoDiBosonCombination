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

masses =[m*100 for m in range(10,29+1)]

if len(sys.argv)>1:
  masses=[int(sys.argv[1])]

for mass in masses:
        print "mass = ",mass

	fVV=open("JJ_cards/datacards/CMS_jj_Bulk_"+str(mass)+"_8TeV_CMS_jj_VV.txt").readlines()
	outfile="JJ_cards/datacards/CMS_jj_Bulkfix_"+str(mass)+"_8TeV_CMS_jj_VV.txt"
	print outfile
        f=open(outfile,"w")

	for l in range(len(fVV)):
	  if "rate" in fVV[l]:
	    line="rate                                     "
	    fVVsplit=fVV[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
	    for s in range(len(fVVsplit)):
	      try:
	        float(fVVsplit[s])
	      except: continue
	      signal=(s in [1,2,4,5]) # only change signal
              numberVV=float(fVVsplit[s])
	      if signal:
                numberVV=numberVV/4.
              line+="%.5e  " % numberVV
	    line+="\n"
	    f.write(line)
	  else:
	    f.write(fVV[l])
