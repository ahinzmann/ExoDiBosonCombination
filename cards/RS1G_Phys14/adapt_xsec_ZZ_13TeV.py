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

masses =[m*100 for m in range(6,25+1)]

if len(sys.argv)>1:
  masses=[int(sys.argv[1])]

for mass in masses:
        print "mass = ",mass

	fZZ=open("ZZ_cards_13TeV_1fb/CMS_ZZ_"+str(mass)+"_13TeV.txt").readlines()
	outfile="ZZ_cards_13TeV_1fb/comb_xzz13_rs1."+str(mass)+".txt"
	print outfile
        f=open(outfile,"w")

	RS1ZZ={}
	for line in open("theory_RS1_ZZ_8TeV.txt").readlines():
	   split=line.replace("\n","").split(" ")
	   RS1ZZ[int(split[0])]=float(split[1])

	for l in range(len(fZZ)):
	  if "rate" in fZZ[l]:
	    line="rate                                     "
	    fZZsplit=fZZ[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
	    for s in range(len(fZZsplit)):
	      try:
	        float(fZZsplit[s])
	      except: continue
	      signal=(s in [1,3,5,7]) # only change signal
              numberZZ=float(fZZsplit[s])
	      if signal:
                numberZZ=numberZZ*RS1ZZ[mass]*1000.
              line+="%.5e  " % numberZZ
	    line+="\n"
	    f.write(line)
	  else:
	    f.write(fZZ[l])
