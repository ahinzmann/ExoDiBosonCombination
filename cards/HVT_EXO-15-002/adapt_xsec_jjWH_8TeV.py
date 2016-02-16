from ROOT import *
import ROOT
import array, math
import os
import sys
from array import array

def get_theo_map():

   V_mass = array('d',[])

   brs = {}
   index = {}

   mapping = ["M0","M+","BRWW","BRhZ","BRZW","BRWh","CX+(pb)","CX0(pb)","CX-(pb)"]

   for m in xrange(0,len(mapping)):
      if mapping[m] != "M0" and mapping[m] != "M+":
   	 brs[mapping[m]] = array('d',[])
   	 #print mapping[m]

   f = open('xsect_HVT_8TeV.txt','r')
   for line in f:
      brDict = line.split(",")
      for d in xrange(0,len(brDict)):
   	 if brDict[d].find('\n') != -1:
   	    brDict[d] = brDict[d].split('\n')[0]
   	 for m in xrange(0,len(mapping)):
   	    if brDict[d] == mapping[m]:
   	       index[mapping[m]] = d
   	       #print "%s %i" %(mapping[m],d)
	    
   f.close()

   f = open('xsect_HVT_8TeV.txt','r')
   for line in f:
      if line.find('M0') != -1: continue
      brDict = line.split(",")  	    
      V_mass.append(float(brDict[index['M0']]))
      for m in xrange(0,len(mapping)):
   	 if mapping[m] != "M0" and mapping[m] != "M+":
   	    brs[mapping[m]].append(float(brDict[index[mapping[m]]]))

   f.close()

   return [brs,V_mass]
   
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

masses =[m*100 for m in range(10,26+1)]

if len(sys.argv)>1:
  masses=[int(sys.argv[1])]

thMap = get_theo_map()
xsecMap = thMap[0]
#massMap = thMap[1]

for mass in masses:

 #print "mass = ",mass
 m = int((mass-745)/5) #for jen's 8 TeV theo map 
 #m = int((mass-800)/100) #for jen'2 13 TeV theo map or 8 TeV alternative model B
 
 #fVH=open("cards_VH_8TeV/CMS_jj_HWqq_"+str(mass)+"_8TeV_CMS_jj_HWOnly.txt").readlines()
 fVH=open("cards_VH_8TeV/CMS_jj_HVqq_"+str(mass)+"_8TeV_CMS_jj_HVCombined.txt").readlines()
 outfile="cards_VH_8TeV/CMS_jj_HWqq_"+str(mass)+"_8TeV_CMS_jj_HWOnly_adapt.txt"
 print outfile
 f=open(outfile,"w")

 xsecWH={}
 xsecWH[mass] = (xsecMap['CX-(pb)'][m]+xsecMap['CX+(pb)'][m])*xsecMap['BRWh'][m]
 
 for l in range(len(fVH)):
   if "rate" in fVH[l]:
     line="rate 				    "
     fVHsplit=fVH[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("	"," ").split(" ")
     for s in range(len(fVHsplit)):
       try:
 	 float(fVHsplit[s])
       except: continue
       #signal=(s in [1,4,6,8,11,12,16]) # only change signal Zh 2,5,8,9,13,14,18,19; WH 1,4,7,10,12,15,17,20
       signal=(s in [1,4,7,10,12,15,17,20])
       signalAlt=(s in [2,5,8,9,13,14,18,19])
       numberVH=float(fVHsplit[s])
       if signal: numberVH=numberVH*xsecWH[mass]/0.03
       if signalAlt: numberVH=0
       line+="%.5e  " % numberVH
     line+="\n"
     f.write(line)
   else:
     f.write(fVH[l])