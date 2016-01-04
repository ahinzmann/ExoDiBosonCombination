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
	  fWZ=open("JJ_cards_13TeV/CMS_jj_WZ_"+str(mass)+"_13TeV_CMS_jj_VVnew.txt").readlines()
	except:
	  print "could not open"
	  continue
	outfile="JJ_cards_13TeV/CMS_jj_WZfix_"+str(mass)+"_13TeV_CMS_jj_VVnew.txt"
	print outfile
        f=open(outfile,"w")

	WprimeWZ={}
	for line in open("theory_HVT_WZ_13TeV.txt").readlines():
	   split=line.replace("\n","").split(" ")
	   WprimeWZ[int(split[0])]=float(split[1])*(0.6991*0.6760)*(0.6991*0.6760)

	for l in range(len(fWZ)):
	  if "rate" in fWZ[l]:
	    line="rate                                     "
	    fWZsplit=fWZ[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
	    for s in range(len(fWZsplit)):
	      try:
	        float(fWZsplit[s])
	      except: continue
	      signal=(s in [2,6,10,14,18,22]) # only change signal
              numberWZ=float(fWZsplit[s])
	      if signal:
                numberWZ=numberWZ*WprimeWZ[mass]*100. # cards from Thea are in units of 100. pb
              line+="%.5e  " % numberWZ
	    line+="\n"
	    f.write(line)
	  else:
	    f.write(fWZ[l])
