import os, sys
import array
from ROOT import * 
from os import path
from ROOT import RooStats

gROOT.Reset()
gROOT.SetStyle("Plain")
gStyle.SetOptStat(0)
gStyle.SetOptFit(0)
gStyle.SetTitleOffset(1.2,"Y")
gStyle.SetPadLeftMargin(0.18)
gStyle.SetPadBottomMargin(0.15)
gStyle.SetPadTopMargin(0.08)
gStyle.SetPadRightMargin(0.05)
gStyle.SetMarkerSize(0.5)
gStyle.SetHistLineWidth(1)
gStyle.SetStatFontSize(0.020)
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetNdivisions(510, "XYZ")
gStyle.SetLegendBorderSize(0)

if __name__ == '__main__':

 channels=["JAM13","xjj13ww","xww13"]
 channels=["xjj13zz"]
 sigWW=[]
 masses =[1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900]

 for channel in channels:
    sigWW={}
    for mass in masses:
        sigWW[masses.index(mass)]={}
        print "mass = ",mass
        os.system("grep -a _channel comb_"+str(mass)+"/cra*/res/*.stdout > qwelee.txt")
        f=open("qwelee.txt")
	done=[]
        for l in reversed(f.readlines()):
          if channel in l or channel in l:
            crab=l.split("/")[1]
	    if crab in done: continue
	    done+=[crab]
            print crab
            sigWW[masses.index(mass)]={}
	    for fname in os.listdir("comb_"+str(mass)+"/"+crab+"/res/"):
	      if not "stdout" in fname: continue
     	      logfile=open("comb_"+str(mass)+"/"+crab+"/res/"+fname)
	      seed=0
	      count=0
              for line in logfile.readlines():
	          if "generator seed" in line:
		      seed=int(line.strip("\n").split(" ")[-1])
                  if "Significance:" in line:
                    sigWW[masses.index(mass)][seed*200+count]=float(line.split(":")[1])
		    count+=1
              logfile.close()

    #print "sigWW",[(masses[i],sigWW[i]) for i in range(len(masses))]

    sSigWW=[(masses[i],sigWW[i]) for i in range(len(masses))]

    fWW = open("LEE_13TeV_Sig_"+channel+"_toys.txt", "w")
    fWW.write(str(sSigWW))
    fWW.close()
