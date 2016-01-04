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

masses =[m*100 for m in range(8,40+1)]

if len(sys.argv)>1:
  masses=[int(sys.argv[1])]

for mass in masses:
        print "mass = ",mass
        try:
	  fWW=open("WW_cards_13TeV/wwlvj_Wprime_WZ_lvjj_M"+str(mass)+"_combo_ALLP_unbin.txt").readlines()
	except:
	  print "could not open"
	  continue
	outfile="WW_cards_13TeV/wwlvj_Wprimefix_WZ_lvjj_M"+str(mass)+"_combo_ALLP_unbin.txt"
	print outfile
        f=open(outfile,"w")

	WprimeWZ={}
	for line in open("theory_HVT_WZ_13TeV.txt").readlines():
	   split=line.replace("\n","").split(" ")
	   WprimeWZ[int(split[0])]=float(split[1])*(0.322*0.6991)

	for l in range(len(fWW)):
	  if "rate" in fWW[l]:
	    line="rate                                     "
	    fWWsplit=fWW[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
	    for s in range(len(fWWsplit)):
	      try:
	        float(fWWsplit[s])
	      except: continue
	      signal=(s in [1,6,11,16,21,26,31,36]) # only change signal
              numberWW=float(fWWsplit[s])
	      if signal:
                numberWW=numberWW*WprimeWZ[mass]*100. # cards from Jennnifer are in units of 0.01 pb
              line+="%.5e  " % numberWW
	    line+="\n"
	    f.write(line)
	  else:
	    f.write(fWW[l])
