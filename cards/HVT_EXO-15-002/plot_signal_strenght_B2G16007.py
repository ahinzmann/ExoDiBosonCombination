import os
import glob
import math
import array
import sys
import time
from array import array
import ROOT
from ROOT import *
import CMS_lumi, tdrstyle
from optparse import OptionParser

def get_theo_map(sqrts):

   V_mass = array('d',[])

   brs = {}
   index = {}

   mapping = ["M0","M+","BRWW","BRhZ","BRZW","BRWh","CX+(pb)","CX0(pb)","CX-(pb)"]

   for m in xrange(0,len(mapping)):
      if mapping[m] != "M0" and mapping[m] != "M+":
   	 brs[mapping[m]] = array('d',[])
   	 #print mapping[m]

   f = open('xsect_HVT_%sTeV.txt'%sqrts,'r')
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

   f = open('xsect_HVT_%sTeV.txt'%sqrts,'r')
   for line in f:
      if line.find('M0') != -1: continue
      brDict = line.split(",")  	    
      V_mass.append(float(brDict[index['M0']]))
      for m in xrange(0,len(mapping)):
   	 if mapping[m] != "M0" and mapping[m] != "M+":
   	    brs[mapping[m]].append(float(brDict[index[mapping[m]]]))

   f.close()

   return [brs,V_mass]

def get_canvas(cname,lumi8,lumi13):

   tdrstyle.setTDRStyle()
   CMS_lumi.lumi_13TeV = "%s fb^{-1}"%lumi13
   CMS_lumi.lumi_8TeV = "%s fb^{-1}"%lumi8
   CMS_lumi.writeExtraText = 1
   CMS_lumi.extraText = "Preliminary"
   CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
   iPos = 0
   if( iPos==0 ): CMS_lumi.relPosX = 0.13
   iPeriod=4

   H_ref = 630 
   W_ref = 600 
   W = W_ref
   H  = H_ref

   T = 0.08*H_ref
   B = 0.12*H_ref 
   L = 0.12*W_ref
   R = 0.04*W_ref

   canvas = ROOT.TCanvas(cname,cname,50,50,W,H)
   canvas.SetFillColor(0)
   canvas.SetBorderMode(0)
   canvas.SetFrameFillStyle(0)
   canvas.SetFrameBorderMode(0)
   canvas.SetLeftMargin( L/W+0.01 )
   canvas.SetRightMargin( R/W+0.03 )
   canvas.SetTopMargin( 0.07 ) #/T/H
   canvas.SetBottomMargin( B/H )
   #canvas.SetGrid()
   canvas.SetLogy()
   
   return canvas

def getAsymLimits(file,mass):
    
    f = ROOT.TFile(file,"READ")
    t = f.Get("limit")
    entries = t.GetEntries()
    
    lims = [-1,-1,-1,-1,-1,-1]
    
    for i in range(entries):
        
        t.GetEntry(i)
        t_quantileExpected = t.quantileExpected
        t_limit = t.limit
	t_mass = t.mh
        
	if t_mass != mass: continue
        #print "mass: ", t_mass , " limit: ", t_limit, ", quantileExpected: ",t_quantileExpected
        
        if t_quantileExpected == -1.: lims[0] = t_limit
        elif t_quantileExpected >= 0.024 and t_quantileExpected <= 0.026: lims[1] = t_limit
        elif t_quantileExpected >= 0.15  and t_quantileExpected <= 0.17:  lims[2] = t_limit
        elif t_quantileExpected == 0.5: lims[3] = t_limit
        elif t_quantileExpected >= 0.83  and t_quantileExpected <= 0.85:  lims[4] = t_limit
        elif t_quantileExpected >= 0.974 and t_quantileExpected <= 0.976: lims[5] = t_limit
        else: print "Unknown quantile!"
    
    return lims

def plot_Asympt_limits(label,signalstrenght):

 infile = "HVTdefault/higgsCombine%s.Asymptotic.TOTAL.root"%label
 mass = [700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,
         2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,
	 3600,3700,3800,3900,4000]
	 
 signal = {}
 signal['JJLVJHVT13'] = "V'" 
 signal['JJLVJWPRIME13'] = "W'" 
 signal['JJLVJZPRIME13'] = "Z'" 
 signal['ALLWVHVT8'] = "V'"
 signal['ALLWVWPRIME8'] = "W'"
 signal['ALLWVZPRIME8'] = "Z'"
 signal['ALLWVHVT138'] = "V'"
 signal['ALLWVWPRIME138'] = "W'"
 signal['ALLWVZPRIME138'] = "Z'"
 signal['ALLHVHVT8'] = "V'"
 signal['ALLHVWPRIME8'] = "W'"
 signal['ALLHVZPRIME8'] = "Z'"
 signal['ALLHVT8'] = "V'"
 signal['ALLWPRIME8'] = "W'"
 signal['ALLZPRIME8'] = "Z'"
 signal['ALLHVT138'] = "V'"
 signal['ALLWPRIME138'] = "W'"
 signal['ALLZPRIME138'] = "Z'"
 signal['jjwv8'] = "V'"
 signal['jjwz8'] = "W'"
 signal['jjww8'] = "Z'"
 signal['lvjwv8'] = "V'"
 signal['lvjwz8'] = "W'"
 signal['lvjww8'] = "Z'"
 signal['lljwz8'] = "W'" 
 signal['lljwzh8'] = "V'" 
 signal['lljzh8'] = "Z'" 
 signal['lvjwv13'] = "V'" 
 signal['lvjwz13'] = "W'"    
 signal['lvjww13'] = "Z'" 
 signal['jjwv13'] = "V'"
 signal['jjwz13'] = "W'"
 signal['jjww13'] = "Z'"
 signal['ttjvh8'] = "V'"
 signal['ttjwh8'] = "W'"
 signal['ttjzh8'] = "Z'" 
 signal['jjvh8'] = "V'"
 signal['jjwh8'] = "W'"
 signal['jjzh8'] = "Z'" 
 signal['lvjwh8'] = "W'"
 
 decay = {}
 decay['JJLVJHVT13'] = "WV"
 decay['JJLVJWPRIME13'] = "WZ" 
 decay['JJLVJZPRIME13'] = "WW" 
 decay['ALLWVHVT8'] = "WV"
 decay['ALLWVWPRIME8'] = "WZ"
 decay['ALLWVZPRIME8'] = "WW"
 decay['ALLWVHVT138'] = "WV"
 decay['ALLWVWPRIME138'] = "WZ"
 decay['ALLWVZPRIME138'] = "WW"
 decay['ALLHVHVT8'] = "VH"
 decay['ALLHVWPRIME8'] = "WH"
 decay['ALLHVZPRIME8'] = "ZH"
 decay['ALLHVT8'] = "VH"
 decay['ALLWPRIME8'] = "WH"
 decay['ALLZPRIME8'] = "ZH"
 decay['ALLHVT138'] = "VH"
 decay['ALLWPRIME138'] = "WH"
 decay['ALLZPRIME138'] = "ZH"
 decay['jjwv8'] = "WV"
 decay['jjwz8'] = "WZ"
 decay['jjww8'] = "WW"
 decay['lvjwv8'] = "WV"
 decay['lvjwz8'] = "WZ"
 decay['lvjww8'] = "WW"
 decay['lljwz8'] = "WZ"
 decay['lljwzh8'] = "WZ/ZH" 
 decay['lljzh8'] = "ZH" 
 decay['lvjwv13'] = "WV"
 decay['lvjwz13'] = "WZ"
 decay['lvjww13'] = "WW"
 decay['jjwv13'] = "WV"
 decay['jjwz13'] = "WZ"
 decay['jjww13'] = "WW"
 decay['ttjvh8'] = "VH"
 decay['ttjwh8'] = "WH"
 decay['ttjzh8'] = "ZH" 
 decay['jjvh8'] = "VH"
 decay['jjwh8'] = "WH"
 decay['jjzh8'] = "ZH" 
 decay['lvjwh8'] = "WH"
 
 names = {}
 names["JJLVJHVT13"]="lvJ, JJ (13 TeV)"
 names["JJLVJWPRIME13"]="lvJ, JJ (13 TeV)"
 names["JJLVJZPRIME13"]="lvJ, JJ (13 TeV)"
 names["ALLWVHVT8"]="lvJ, llJ, JJ (8 TeV)"
 names["ALLWVWPRIME8"]="lvJ, llJ, JJ (8 TeV)"
 names["ALLWVZPRIME8"]="lvJ, JJ (8 TeV)"
 names["ALLWVHVT138"]="lvJ, llJ, JJ (13+8 TeV)"
 names["ALLWVWPRIME138"]="lvJ, llJ, JJ (8+13 TeV)"
 names["ALLWVZPRIME138"]="lvJ, JJ (8+13 TeV)"
 names['ALLHVHVT8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLHVWPRIME8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLHVZPRIME8'] = "J#tau#tau, JJ (8 TeV)"
 names['ALLHVT8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLWPRIME8'] = "J#tau#tau, lvJ, llJ, JJ (8 TeV)"
 names['ALLZPRIME8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLHVT138'] = "J#tau#tau, lvJ, JJ (8+13 TeV)"
 names['ALLWPRIME138'] = "J#tau#tau, lvJ, llJ, JJ (8+13 TeV)"
 names['ALLZPRIME138'] = "J#tau#tau, lvJ, JJ (8+13 TeV)"
 names["lvjwv8"]="lvqq (8 TeV)"
 names["lvjwz8"]="lvqq (8 TeV)"
 names["lvjww8"]="lvqq (8 TeV)"
 names["lljwz8"]="llqq (8 TeV)"
 names['lljwzh8']="llqq (8 TeV)"
 names['lljzh8']="llqq (8 TeV)"
 names["jjwv8"]="qqqq (8 TeV)"
 names["jjwz8"]="qqqq (8 TeV)"
 names["jjww8"]="qqqq (8 TeV)"
 names["jjwv13"]="qqqq (13 TeV)"
 names["jjww13"]="qqqq (13 TeV)"
 names["jjwz13"]="qqqq (13 TeV)"
 names["lvjwv13"]="lvqq (13 TeV)"
 names["lvjwv13"]="lvqq (13 TeV)"
 names["lvjww13"]="lvqq (13 TeV)"
 names["lvjwz13"]="lvqq (13 TeV)"
 names['ttjvh8'] = "qq#tau#tau (8 TeV)"
 names['ttjwh8'] = "qq#tau#tau (8 TeV)"
 names['ttjzh8'] = "qq#tau#tau (8 TeV)"
 names['jjvh8'] = "qqbb(4q) (8 TeV)"
 names['jjwh8'] = "qqbb(4q) (8 TeV)"
 names['jjzh8'] = "qqbb(4q) (8 TeV)" 
 names['lvjwh8'] = "lvbb (8 TeV)"
   
 thMap13 = get_theo_map("13")
 xsecMap13 = thMap13[0]
 massMap13 = thMap13[1]
 thMap8 = get_theo_map("8")
 xsecMap8 = thMap8[0]
 massMap8 = thMap8[1]
 
 #idx = int((2000-800)/100)
 #idx2 = int((2000-800)/100)
 #print "13 TeV xsec_W'- : ",xsecMap13['CX-(pb)'][idx]
 #print "13 TeV xsec_W'+ : ",xsecMap13['CX+(pb)'][idx]
 #print "13 TeV xsec_Z' : ",xsecMap13['CX0(pb)'][idx]
 #print "13 TeV BR_WZ : ",xsecMap13['BRZW'][idx]
 #print "13 TeV BR_WW : ",xsecMap13['BRWW'][idx]
 #print "13 TeV BR_WH : ",xsecMap13['BRWh'][idx]
 #print "13 TeV BR_ZH : ",xsecMap13['BRhZ'][idx]
 #print "8 TeV xsec_W'- : ",xsecMap8['CX-(pb)'][idx2]
 #print "8 TeV xsec_W'+ : ",xsecMap8['CX+(pb)'][idx2]
 #print "8 TeV xsec_Z' : ",xsecMap8['CX0(pb)'][idx2]
 #print "8 TeV BR_WZ : ",xsecMap8['BRZW'][idx2]
 #print "8 TeV BR_WW : ",xsecMap8['BRWW'][idx2]
 #print "8 TeV BR_WH : ",xsecMap8['BRWh'][idx2]
 #print "8 TeV BR_ZH : ",xsecMap8['BRhZ'][idx2]
 #sys.exit()
  	     
 scale = {}
 scale['JJLVJHVT13'] = {}
 scale['JJLVJWPRIME13'] = {}
 scale['JJLVJZPRIME13'] = {}
 scale['ALLWVHVT8'] = {}
 scale['ALLWVWPRIME8'] = {}
 scale['ALLWVZPRIME8'] = {}
 scale['ALLWVHVT138'] = {}
 scale['ALLWVWPRIME138'] = {}
 scale['ALLWVZPRIME138'] = {}
 scale['ALLHVHVT8'] = {}
 scale['ALLHVWPRIME8'] = {}
 scale['ALLHVZPRIME8'] = {}
 scale['ALLHVT8'] = {}
 scale['ALLWPRIME8'] = {}
 scale['ALLZPRIME8'] = {}
 scale['ALLHVT138'] = {}
 scale['ALLWPRIME138'] = {}
 scale['ALLZPRIME138'] = {}
 scale['jjwv8'] = {}
 scale['jjwz8'] = {}
 scale['jjww8'] = {}
 scale['lvjwv8'] = {}
 scale['lvjwz8'] = {}
 scale['lvjww8'] = {}
 scale['lljwz8'] = {}
 scale['lljwzh8']={}
 scale['lljzh8']={}
 scale['lvjwv13'] = {}
 scale['lvjwz13'] = {}
 scale['lvjww13'] = {}	     
 scale['jjwv13'] = {}
 scale['jjwz13'] = {}
 scale['jjww13'] = {}
 scale['ttjvh8'] = {}
 scale['ttjwh8'] = {}
 scale['ttjzh8'] = {}
 scale['jjvh8'] = {}
 scale['jjwh8'] = {}
 scale['jjzh8'] = {}
 scale['lvjwh8'] = {}
 for m in mass:
   idx = int((m-800)/100)
   idx2 = int((m-745)/5)
   if signalstrenght:
    scale['JJLVJHVT13'][m] = 1
    scale['JJLVJWPRIME13'][m] = 1
    scale['JJLVJZPRIME13'][m] = 1
    scale['ALLWVHVT8'][m] = 1
    scale['ALLWVWPRIME8'][m] = 1
    scale['ALLWVZPRIME8'][m] = 1
    scale['ALLWVHVT138'][m] = 1
    scale['ALLWVWPRIME138'][m] = 1
    scale['ALLWVZPRIME138'][m] = 1
    scale['ALLHVHVT8'][m] = 1
    scale['ALLHVWPRIME8'][m] = 1
    scale['ALLHVZPRIME8'][m] = 1
    scale['ALLHVT8'][m] = 1
    scale['ALLWPRIME8'][m] = 1
    scale['ALLZPRIME8'][m] = 1
    scale['ALLHVT138'][m] = 1
    scale['ALLWPRIME138'][m] = 1
    scale['ALLZPRIME138'][m] = 1
    scale['lvjwv8'][m] = 1
    scale['lvjwz8'][m] = 1
    scale['lvjww8'][m] = 1 
    scale['lljwz8'][m] = 1
    scale['lljwzh8'][m]=1
    scale['lljzh8'][m]=1
    scale['jjwv8'][m] = 1
    scale['jjwz8'][m] = 1
    scale['jjww8'][m] = 1
    scale['lvjwv13'][m] = 1
    scale['lvjwz13'][m] = 1
    scale['lvjww13'][m] = 1
    scale['jjwv13'][m] = 1
    scale['jjwz13'][m] = 1
    scale['jjww13'][m] = 1
    scale['ttjvh8'][m] = 1
    scale['ttjwh8'][m] = 1
    scale['ttjzh8'][m] = 1
    scale['jjvh8'][m] = 1
    scale['jjwh8'][m] = 1
    scale['jjzh8'][m] = 1
    scale['lvjwh8'][m] = 1
   else: 
    scale['JJLVJHVT13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['JJLVJWPRIME13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx]
    scale['JJLVJZPRIME13'][m] = xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['lvjwv13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['lvjwz13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx]
    scale['lvjww13'][m] = xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['jjwv13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['jjwz13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx]
    scale['jjww13'][m] = xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]        
    if m < 3000:
     scale['ALLWVHVT8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2]
     scale['ALLWVWPRIME8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2]
     scale['ALLWVZPRIME8'][m] = xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2]
     scale['ALLHVHVT8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRWh'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['ALLHVWPRIME8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRWh'][idx2]
     scale['ALLHVZPRIME8'][m] = xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['ALLHVT8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRWh'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['ALLWPRIME8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRWh'][idx2]
     scale['ALLZPRIME8'][m] = xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['lljwz8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2]
     scale['lljwzh8'][m]=(xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['lljzh8'][m]=xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['lvjwv8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2]
     scale['lvjwz8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2]
     scale['lvjww8'][m] = xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2]
     scale['jjwv8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2]
     scale['jjwz8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2]
     scale['jjww8'][m] = xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2]
     scale['ttjvh8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRWh'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['ttjwh8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRWh'][idx2]
     scale['ttjzh8'][m] = xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['jjvh8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRWh'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['jjwh8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRWh'][idx2]
     scale['jjzh8'][m] = xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRhZ'][idx2]
     scale['lvjwh8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRWh'][idx2]
     scale['ALLWVHVT138'][m] = ((xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx])+((xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2])
     scale['ALLHVT138'][m] = ((xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx])+((xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*(xsecMap8['BRZW'][idx2]+xsecMap8['BRWh'][idx2]) + xsecMap8['CX0(pb)'][idx2]*(xsecMap8['BRWW'][idx2]+xsecMap8['BRhZ'][idx2]))
    else:
     scale['ALLWVHVT8'][m] = 1
     scale['ALLWVWPRIME8'][m] = 1
     scale['ALLWVZPRIME8'][m] = 1
     scale['ALLHVHVT8'][m] = 1
     scale['ALLHVWPRIME8'][m] = 1
     scale['ALLHVZPRIME8'][m] = 1
     scale['ALLHVT8'][m] = 1
     scale['ALLWPRIME8'][m] = 1
     scale['ALLZPRIME8'][m] = 1
     scale['lljwz8'][m] = 1
     scale['lvjwv8'][m] = 1
     scale['lvjwz8'][m] = 1
     scale['lvjww8'][m] = 1
     scale['lljwzh8'][m]=1
     scale['lljzh8'][m]=1
     scale['jjwv8'][m] = 1
     scale['jjwz8'][m] = 1
     scale['jjww8'][m] = 1
     scale['ttjvh8'][m] = 1
     scale['ttjwh8'][m] = 1
     scale['ttjzh8'][m] = 1
     scale['jjvh8'][m] = 1
     scale['jjwh8'][m] = 1
     scale['jjzh8'][m] = 1
     scale['lvjwh8'][m] = 1
     scale['ALLWVHVT138'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
     scale['ALLHVT138'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]

 nPoints = 0

 xbins	   = array('d', [])
 xbins_env = array('d', [])
 ybins_exp = array('d', [])
 ybins_obs = array('d', [])
 ybins_1s  = array('d', [])
 ybins_2s  = array('d', [])
 ybins_xs  = array('d', [])

 lastMass = 800.
 for m in mass:

  curAsymLimits = getAsymLimits(infile,m);
  if curAsymLimits[0] == -1: continue
  #print m,curAsymLimits[3]*scale[label][m]
  lastMass = m/1000.
  xbins.append( m/1000. );
  xbins_env.append( m/1000. );
  ybins_exp.append( curAsymLimits[3]*scale[label][m] );
  ybins_obs.append( curAsymLimits[0]*scale[label][m] );
  ybins_2s.append( curAsymLimits[1]*scale[label][m] );
  ybins_1s.append( curAsymLimits[2]*scale[label][m] );
  ybins_xs.append( scale[label][m] );
  nPoints+=1

 for i in range( len(mass)-1, -1, -1 ):

  curAsymLimits = getAsymLimits(infile,mass[i]);
  if curAsymLimits[0] == -1: continue
  xbins_env.append( mass[i]/1000. );
  ybins_2s.append( curAsymLimits[5]*scale[label][mass[i]] );
  ybins_1s.append( curAsymLimits[4]*scale[label][mass[i]] );

 lumi13 = ""
 lumi8 = ""
 if label.find("13") != -1 and label.find("8") == -1:
  if label.find("JJLVJ") != -1: lumi13 = "2.2-2.6"
  elif label.find("jj") != -1: lumi13 = "2.6"
  else: lumi13 = "2.2"
 if "8" in label and not "13" in label:
  lumi8 = "19.7"
 if "138" in label:
  lumi13 = "2.2-2.6"
  lumi8 = "19.7"
  
 canv = get_canvas("c_lim_Asymptotic",lumi8,lumi13)
 canv.cd()
      
 curGraph_exp	 = ROOT.TGraphAsymmErrors(nPoints,xbins,ybins_exp)
 curGraph_exp.SetName("LimitExpectedCLs")
 curGraph_obs	 = ROOT.TGraphAsymmErrors(nPoints,xbins,ybins_obs)
 curGraph_obs.SetName("LimitObservedCLs")
 curGraph_xs	 = ROOT.TGraph(nPoints,xbins,ybins_xs)
 curGraph_xs.SetName("CrossSectionTheo")
 curGraph_1s	 = ROOT.TGraphAsymmErrors(nPoints*2,xbins_env,ybins_1s)
 curGraph_1s.SetName("Limit68CLs")
 curGraph_2s	 = ROOT.TGraphAsymmErrors(nPoints*2,xbins_env,ybins_2s)
 curGraph_2s.SetName("Limit95CLs")
 
 curGraph_obs.SetMarkerStyle(20)
 curGraph_obs.SetLineWidth(3)
 curGraph_obs.SetLineStyle(1)
 curGraph_obs.SetMarkerSize(1)
 curGraph_exp.SetMarkerSize(1.3)
 curGraph_exp.SetMarkerColor(ROOT.kBlack)

 curGraph_exp.SetLineStyle(2)
 curGraph_exp.SetLineWidth(3)
 curGraph_exp.SetMarkerSize(2)
 curGraph_exp.SetMarkerStyle(24)
 curGraph_exp.SetMarkerColor(ROOT.kBlack)

 curGraph_xs.SetLineStyle(ROOT.kSolid)
 curGraph_xs.SetFillStyle(3344)
 curGraph_xs.SetLineWidth(2)
 curGraph_xs.SetMarkerSize(2)
 curGraph_xs.SetLineColor(ROOT.kRed)

 curGraph_1s.SetFillColor(ROOT.kGreen)
 curGraph_1s.SetFillStyle(1001)
 curGraph_1s.SetLineStyle(ROOT.kDashed)
 curGraph_1s.SetLineWidth(3)

 curGraph_2s.SetFillColor(ROOT.kYellow)
 curGraph_2s.SetFillStyle(1001)
 curGraph_2s.SetLineStyle(ROOT.kDashed)
 curGraph_2s.SetLineWidth(3)

 hrl_SM = canv.DrawFrame(0.75,1e-03, lastMass+0.050, 100)
 if signalstrenght: hrl_SM = canv.DrawFrame(0.75,0.01, lastMass+0.050, 100) 
 
 ytitle = "#sigma_{95%} #times BR_{"+signal[label]+"#rightarrow "+decay[label]+"} (pb)"
 hrl_SM.GetYaxis().SetTitle(ytitle)
 hrl_SM.GetYaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitle("M_{"+signal[label]+"} (TeV)")
     
 curGraph_2s.Draw("F")
 curGraph_1s.Draw("Fsame")
 curGraph_exp.Draw("Lsame")
 curGraph_obs.Draw("LPsame")
 curGraph_xs.Draw("Csame")

 leg2 = ROOT.TLegend(0.3724832,0.5963455,0.8875839,0.7973422)
 if signalstrenght: leg2 = ROOT.TLegend(0.3691275,0.1993355,0.8842282,0.4003322)
 leg2.SetBorderSize(0);
 leg2.SetTextSize(0.031);
 leg2.SetLineColor(1);
 leg2.SetLineStyle(1);
 leg2.SetShadowColor(0);
 leg2.SetLineWidth(1);
 leg2.SetFillColor(0);
 leg2.SetTextFont(42)

 leg2.AddEntry(curGraph_obs,"Asympt. CL_{S} Observed","LP")
 leg2.AddEntry(curGraph_1s,"Asympt. CL_{S} Expected #pm 1#sigma","LF")
 leg2.AddEntry(curGraph_2s,"Asympt. CL_{S} Expected #pm 2#sigma","LF")
 theoleg = "#sigma_{TH} #times BR_{"+signal[label]+"#rightarrow "+decay[label]+"} , HVT_{B}"
 leg2.AddEntry(curGraph_xs,theoleg,"L")     
 leg2.Draw()

 pt = ROOT.TPaveText(0.5486577,0.8355482,0.8993289,0.8920266,"NDC")
 pt.SetTextFont(42)
 pt.SetTextSize(0.031)
 pt.SetTextAlign(32)
 pt.SetFillColor(0)
 pt.SetBorderSize(0)
 pt.SetFillStyle(0)
 text = pt.AddText(names[label])
 text.SetTextFont(62)
  	  
 canv.Update()   
 canv.cd()
 
 period = 4
 if "138" in label: period = 7
 if "8" in label and not "13" in label: period = 2
 
 CMS_lumi.CMS_lumi(canv, period,0)   	
 canv.cd()
 canv.Update()
 canv.RedrawAxis()
 canv.RedrawAxis("g")
 leg2.Draw("same")
 pt.Draw("same")
 frame = canv.GetFrame()
 frame.Draw()	
 canv.cd()
 canv.Update() 
  
 canv.SaveAs("plots/EXOVVhvt_"+label+"_UL_Asymptotic_log.root")
 canv.SaveAs("plots/EXOVVhvt_"+label+"_UL_Asymptotic_log.png")
 canv.SaveAs("plots/EXOVVhvt_"+label+"_UL_Asymptotic_log.pdf")
 canv.SaveAs("plots/EXOVVhvt_"+label+"_UL_Asymptotic_log.eps")

def compare_Asympt_limits(labels,unblind,bands):
 
 #line color
 lcol = {}
 lcol["JJLVJHVT13"] = kBlack
 lcol["JJLVJWPRIME13"] = kBlack
 lcol["JJLVJZPRIME13"] = kBlack
 lcol["ALLWVHVT8"] = kBlack
 lcol["ALLWVWPRIME8"] = kBlack
 lcol["ALLWVZPRIME8"] = kBlack
 lcol["ALLWVHVT138"] = kBlack
 lcol["ALLWVWPRIME138"] = kBlack
 lcol["ALLWVZPRIME138"] = kBlack
 lcol['ALLHVHVT8'] = kBlack
 lcol['ALLHVWPRIME8'] = kBlack
 lcol['ALLHVZPRIME8'] = kBlack
 lcol['ALLHVT8'] = kBlack
 lcol['ALLWPRIME8'] = kBlack
 lcol['ALLZPRIME8'] = kBlack
 lcol['ALLHVT138'] = kBlack
 lcol['ALLWPRIME138'] = kBlack
 lcol['ALLZPRIME138'] = kBlack
 lcol["lvjwv13"] = 4
 lcol["lvjwz13"] = 4
 lcol["lvjww13"] = 4
 lcol["jjwv13"] = 6
 lcol["jjwz13"] = 6
 lcol["jjww13"] = 6
 lcol["lvjwv8"] = 11
 lcol["lvjwz8"] = 11
 lcol["lvjww8"] = 11
 lcol["jjwv8"] = 28
 lcol["jjwz8"] = 28
 lcol["jjww8"] = 28
 lcol["lljwz8"] = 8
 lcol['lljwzh8'] = 8
 lcol['lljzh8'] = 8
 lcol['ttjvh8'] = 9
 lcol['ttjwh8'] = 9
 lcol['ttjzh8'] = 9
 lcol['jjvh8'] = 7
 lcol['jjwh8'] = 7
 lcol['jjzh8'] = 7
 lcol['lvjwh8'] = kRed
 #marker color
 mcol = {}
 mcol["JJLVJHVT13"] = kBlack
 mcol["JJLVJWPRIME13"] = kBlack
 mcol["JJLVJZPRIME13"] = kBlack
 mcol["ALLWVHVT8"] = kBlack
 mcol["ALLWVWPRIME8"] = kBlack
 mcol["ALLWVZPRIME8"] = kBlack
 mcol["ALLWVHVT138"] = kBlack
 mcol["ALLWVWPRIME138"] = kBlack
 mcol["ALLWVZPRIME138"] = kBlack
 mcol['ALLHVHVT8'] = kBlack
 mcol['ALLHVWPRIME8'] = kBlack
 mcol['ALLHVZPRIME8'] = kBlack
 mcol['ALLHVT8'] = kBlack
 mcol['ALLWPRIME8'] = kBlack
 mcol['ALLZPRIME8'] = kBlack
 mcol['ALLHVT138'] = kBlack
 mcol['ALLWPRIME138'] = kBlack
 mcol['ALLZPRIME138'] = kBlack
 mcol["lvjwv13"] = 4
 mcol["lvjwz13"] = 4
 mcol["lvjww13"] = 4
 mcol["jjwv13"] = 6
 mcol["jjwz13"] = 6
 mcol["jjww13"] = 6
 mcol["lvjwv8"] = 11
 mcol["lvjwz8"] = 11
 mcol["lvjww8"] = 11
 mcol["jjwv8"] = 28
 mcol["jjwz8"] = 28
 mcol["jjww8"] = 28
 mcol["lljwz8"] = 8
 mcol['lljwzh8'] = 8
 mcol['lljzh8'] = 8
 mcol['ttjvh8'] = 9
 mcol['ttjwh8'] = 9
 mcol['ttjzh8'] = 9
 mcol['jjvh8'] = 7
 mcol['jjwh8'] = 7
 mcol['jjzh8'] = 7
 mcol['lvjwh8'] = kRed
 #marker style
 msty = {}
 msty["JJLVJHVT13"] = 20
 msty["JJLVJWPRIME13"] = 20
 msty["JJLVJZPRIME13"] = 20
 msty["ALLWVHVT8"] = 20
 msty["ALLWVWPRIME8"] = 20
 msty["ALLWVZPRIME8"] = 20
 msty["ALLWVHVT138"] = 20
 msty["ALLWVWPRIME138"] = 20
 msty["ALLWVZPRIME138"] = 20
 msty['ALLHVHVT8'] = 20
 msty['ALLHVWPRIME8'] = 20
 msty['ALLHVZPRIME8'] = 20
 msty['ALLHVT8'] = 20
 msty['ALLWPRIME8'] = 20
 msty['ALLZPRIME8'] = 20
 msty['ALLHVT138'] = 20
 msty['ALLWPRIME138'] = 20
 msty['ALLZPRIME138'] = 20
 msty["lvjwv13"] = 21
 msty["lvjwz13"] = 21
 msty["lvjww13"] = 21
 msty["jjwv13"] = 22
 msty["jjwz13"] = 22
 msty["jjww13"] = 22
 msty["lvjwv8"] = 24
 msty["lvjwz8"] = 24
 msty["lvjww8"] = 24
 msty["jjwv8"] = 25
 msty["jjwz8"] = 25
 msty["jjww8"] = 25
 msty["lljwz8"] = 26
 msty['lljwzh8'] = 26
 msty['lljzh8'] = 26
 msty['ttjvh8'] = 27
 msty['ttjwh8'] = 27
 msty['ttjzh8'] = 27
 msty['jjvh8'] = 28
 msty['jjwh8'] = 28
 msty['jjzh8'] = 28
 msty['lvjwh8'] = 29
    
 signal = {}
 signal['JJLVJHVT13'] = "V'"
 signal["JJLVJWPRIME13"] = "W'"
 signal["JJLVJZPRIME13"] = "Z'"
 signal["ALLWVHVT8"] = "V'"
 signal["ALLWVWPRIME8"] = "W'"
 signal["ALLWVZPRIME8"] = "Z'"
 signal["ALLWVHVT138"] = "V'"
 signal["ALLWVWPRIME138"] = "W'"
 signal["ALLWVZPRIME138"] = "Z'"
 signal['ALLHVHVT8'] = "V'"
 signal['ALLHVWPRIME8'] = "W'"
 signal['ALLHVZPRIME8'] = "Z'"
 signal['ALLHVT8'] = "V'"
 signal['ALLWPRIME8'] = "W'"
 signal['ALLZPRIME8'] = "Z'"
 signal['ALLHVT138'] = "V'"
 signal['ALLWPRIME138'] = "W'"
 signal['ALLZPRIME138'] = "Z'"
 decay = {}
 decay['JJLVJHVT13'] = "WV"
 decay['JJLVJWPRIME13'] = "WZ" 
 decay['JJLVJZPRIME13'] = "WW" 
 decay['ALLWVHVT8'] = "WV"
 decay['ALLWVWPRIME8'] = "WZ"
 decay['ALLWVZPRIME8'] = "WW"
 decay['ALLWVHVT138'] = "WV"
 decay['ALLWVWPRIME138'] = "WZ"
 decay['ALLWVZPRIME138'] = "WW"
 decay['ALLHVHVT8'] = "VH"
 decay['ALLHVWPRIME8'] = "WH"
 decay['ALLHVZPRIME8'] = "ZH"
 decay['ALLHVT8'] = "VH"
 decay['ALLWPRIME8'] = "WH"
 decay['ALLZPRIME8'] = "ZH"
 decay['ALLHVT138'] = "VH"
 decay['ALLWPRIME138'] = "WH"
 decay['ALLZPRIME138'] = "ZH"
     
 names = {}
 names["JJLVJHVT13"]="lvJ, JJ (13 TeV)"
 names["JJLVJWPRIME13"]="lvJ, JJ (13 TeV)"
 names["JJLVJZPRIME13"]="lvJ, JJ (13 TeV)"
 names["ALLWVHVT8"]="lvJ, llJ, JJ (8 TeV)"
 names["ALLWVWPRIME8"]="lvJ, llJ, JJ (8 TeV)"
 names["ALLWVZPRIME8"]="lvJ, JJ (8 TeV)"
 names["ALLWVHVT138"]="lvJ, llJ, JJ (8 TeV)"
 names["ALLWVWPRIME138"]="lvJ, llJ, JJ (8+13 TeV)"
 names["ALLWVZPRIME138"]="lvJ, JJ (8+13 TeV)"
 names['ALLHVHVT8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLHVWPRIME8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLHVZPRIME8'] = "J#tau#tau, JJ (8 TeV)"
 names['ALLHVT8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLWPRIME8'] = "J#tau#tau, lvJ, llJ, JJ (8 TeV)"
 names['ALLZPRIME8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLHVT138'] = "J#tau#tau, lvJ, JJ (8+13 TeV)"
 names['ALLWPRIME138'] = "J#tau#tau, lvJ, llJ, JJ (8+13 TeV)"
 names['ALLZPRIME138'] = "J#tau#tau, lvJ, JJ (8+13 TeV)"
 names["lvjwv8"]="lvqq (8 TeV)"
 names["lvjwz8"]="lvqq (8 TeV)"
 names["lvjww8"]="lvqq (8 TeV)"
 names["lljwz8"]="llqq (8 TeV)"
 names['lljwzh8']="llqq (8 TeV)"
 names['lljzh8']="llqq (8 TeV)"
 names["jjwv8"]="qqqq (8 TeV)"
 names["jjwz8"]="qqqq (8 TeV)"
 names["jjww8"]="qqqq (8 TeV)"
 names["jjwv13"]="qqqq (13 TeV)"
 names["jjww13"]="qqqq (13 TeV)"
 names["jjwz13"]="qqqq (13 TeV)"
 names["lvjwv13"]="lvqq (13 TeV)"
 names["lvjwv13"]="lvqq (13 TeV)"
 names["lvjww13"]="lvqq (13 TeV)"
 names["lvjwz13"]="lvqq (13 TeV)"
 names['ttjvh8'] = "qq#tau#tau (8 TeV)"
 names['ttjwh8'] = "qq#tau#tau (8 TeV)"
 names['ttjzh8'] = "qq#tau#tau (8 TeV)"
 names['jjvh8'] = "qqbb(4q) (8 TeV)"
 names['jjwh8'] = "qqbb(4q) (8 TeV)"
 names['jjzh8'] = "qqbb(4q) (8 TeV)" 
 names['lvjwh8'] = "lvbb (8 TeV)"
 
 legs1={}
 legs1["JJLVJHVT13"]=[0.45,0.34,0.90,0.45]
 legs1["JJLVJWPRIME13"]=[0.45,0.34,0.90,0.45]
 legs1["JJLVJZPRIME13"]=[0.45,0.34,0.90,0.45]
 legs1["ALLWVHVT8"]=[0.47,0.31,0.90,0.42]
 legs1["ALLWVWPRIME8"]=[0.47,0.31,0.90,0.42]
 legs1["ALLWVZPRIME8"]=[0.47,0.31,0.90,0.42]
 legs1["ALLWVHVT138"]=[0.45,0.34,0.90,0.45]
 legs1["ALLWVWPRIME138"]=[0.45,0.34,0.90,0.45]
 legs1["ALLWVZPRIME138"]=[0.45,0.34,0.90,0.45]
 legs1["ALLHVHVT8"]=[0.45,0.29,0.90,0.40]
 legs1["ALLHVWPRIME8"]=[0.45,0.29,0.90,0.40]
 legs1["ALLHVZPRIME8"]=[0.45,0.29,0.90,0.40]
 legs1["ALLHVT8"]=[0.45,0.34,0.90,0.45]
 legs1["ALLWPRIME8"]=[0.45,0.34,0.90,0.45]
 legs1["ALLZPRIME8"]=[0.45,0.34,0.90,0.45]
 legs1["ALLHVT138"]=[0.45,0.34,0.90,0.45]
 legs1["ALLWPRIME138"]=[0.45,0.34,0.90,0.45]
 legs1["ALLZPRIME138"]=[0.45,0.34,0.90,0.45]
    
 legs2={}
 legs2["JJLVJHVT13"]=[0.43,0.25,0.88,0.30]
 legs2["JJLVJWPRIME13"]=[0.43,0.25,0.88,0.30]
 legs2["JJLVJZPRIME13"]=[0.43,0.25,0.88,0.30]
 legs2["ALLWVHVT8"]=[0.44,0.17,0.88,0.27]
 legs2["ALLWVWPRIME8"]=[0.44,0.17,0.88,0.27]
 legs2["ALLWVZPRIME8"]=[0.44,0.17,0.88,0.27]
 legs2["ALLWVHVT138"]=[0.43,0.18,0.88,0.29]
 legs2["ALLWVWPRIME138"]=[0.43,0.18,0.88,0.29]
 legs2["ALLWVZPRIME138"]=[0.43,0.18,0.88,0.29]
 legs2["ALLHVHVT8"]=[0.43,0.15,0.88,0.26]
 legs2["ALLHVWPRIME8"]=[0.43,0.15,0.88,0.26]
 legs2["ALLHVZPRIME8"]=[0.43,0.15,0.88,0.26]
 legs2["ALLHVT8"]=[0.43,0.18,0.88,0.29]
 legs2["ALLWPRIME8"]=[0.43,0.18,0.88,0.29]
 legs2["ALLZPRIME8"]=[0.43,0.18,0.88,0.29]
 legs2["ALLHVT138"]=[0.31,0.16,0.88,0.31]
 legs2["ALLWPRIME138"]=[0.31,0.16,0.88,0.31]
 legs2["ALLZPRIME138"]=[0.31,0.16,0.88,0.31]

 legs3={}
 legs3["JJLVJHVT13"]=[0.17,0.78,0.43,0.88]
 legs3["JJLVJWPRIME13"]=[0.17,0.78,0.43,0.88]
 legs3["JJLVJZPRIME13"]=[0.17,0.78,0.43,0.88]
 legs3["ALLWVHVT8"]=[0.17,0.75,0.43,0.88]
 legs3["ALLWVWPRIME8"]=[0.17,0.75,0.43,0.88]
 legs3["ALLWVZPRIME8"]=[0.17,0.75,0.43,0.88]
 legs3["ALLWVHVT138"]=[0.17,0.71,0.43,0.88]
 legs3["ALLWVWPRIME138"]=[0.17,0.71,0.43,0.88]
 legs3["ALLWVZPRIME138"]=[0.17,0.71,0.43,0.88]
 legs3["ALLHVHVT8"]=[0.17,0.75,0.43,0.88]
 legs3["ALLHVWPRIME8"]=[0.17,0.75,0.43,0.88]
 legs3["ALLHVZPRIME8"]=[0.17,0.75,0.43,0.88]
 legs3["ALLHVT8"]=[0.17,0.78,0.43,0.88]
 legs3["ALLWPRIME8"]=[0.17,0.78,0.43,0.88]
 legs3["ALLZPRIME8"]=[0.17,0.78,0.43,0.88]
 legs3["ALLHVT138"]=[0.17,0.66,0.43,0.90]
 legs3["ALLWPRIME138"]=[0.17,0.66,0.43,0.90]
 legs3["ALLZPRIME138"]=[0.17,0.66,0.43,0.90]
           
 files = []
 canvas = []
 graph_1s = []
 graph_2s = []
 graphexp = []
 graphobs = []
 graphth = []
   
 files=[TFile.Open("plots/EXOVVhvt_"+l+"_UL_Asymptotic_log.root") for l in labels]
 for f in files: print f.GetName()
 canvas=[f.Get("c_lim_Asymptotic") for f in files]
 
 for c in range(len(canvas)):
  for p in canvas[c].GetListOfPrimitives():
   if str(p).find("Limit68CLs") != -1: graph_1s.append(p.Clone("graph1s_%s"%labels[c])) 
   if str(p).find("Limit95CLs") != -1: graph_2s.append(p.Clone("graph2s_%s"%labels[c]))
   if str(p).find("LimitExpectedCLs") != -1: graphexp.append(p.Clone("graphexp_%s"%labels[c]))
   if str(p).find("LimitObservedCLs") != -1: graphobs.append(p.Clone("graphobs_%s"%labels[c]))
   if str(p).find("CrossSectionTheo") != -1: graphth.append(p.Clone("graphth_%s"%labels[c]))
 
 for g in range(len(graphexp)):
  graphexp[g].SetMarkerColor(mcol[labels[g]])
  graphexp[g].SetLineColor(lcol[labels[g]])
  graphexp[g].SetMarkerStyle(msty[labels[g]])
  graphexp[g].SetMarkerSize(0.7)
  graphobs[g].SetMarkerColor(mcol[labels[g]])
  graphobs[g].SetLineColor(lcol[labels[g]])
  graphobs[g].SetMarkerStyle(msty[labels[g]])
  graphobs[g].SetMarkerSize(0.9)  
  if g != 0:
   graphobs[g].SetLineWidth(2)
   graphexp[g].SetLineWidth(2)
   
 leg = ROOT.TLegend(0.3808725,0.166113,0.8959732,0.3803987)
 if not bands: leg = ROOT.TLegend(legs1[labels[0]][0],legs1[labels[0]][1],legs1[labels[0]][2],legs1[labels[0]][3])#ROOT.TLegend(0.4211409,0.3654485,0.8724832,0.4518272)
 leg.SetBorderSize(0)
 leg.SetTextSize(0.031)
 leg.SetLineColor(1)
 leg.SetLineStyle(1)
 leg.SetShadowColor(0)
 leg.SetLineWidth(1)
 leg.SetFillColor(0)
 leg.SetTextFont(42)

 leg2 = ROOT.TLegend(legs2[labels[0]][0],legs2[labels[0]][1],legs2[labels[0]][2],legs2[labels[0]][3])#ROOT.TLegend(0.4345638,0.2059801,0.8758389,0.3239203)
 if bands: leg2 = ROOT.TLegend(legs3[labels[0]][0],legs3[labels[0]][1],legs3[labels[0]][2],legs3[labels[0]][3])
 leg2.SetBorderSize(0)
 leg2.SetTextSize(0.026)
 if bands: leg2.SetTextSize(0.031)
 leg2.SetLineColor(1)
 leg2.SetLineStyle(1)
 leg2.SetShadowColor(0)
 leg2.SetLineWidth(1)
 leg2.SetFillColor(0)
 leg2.SetTextFont(42)
 if not bands:
  leg2.SetNColumns(2)
  leg2.SetTextSize(0.031)
 
 pt = ROOT.TPaveText(0.5486577,0.8355482,0.8993289,0.8920266,"NDC")
 pt.SetTextFont(42)
 pt.SetTextSize(0.031)
 pt.SetTextAlign(32)
 pt.SetFillColor(0)
 pt.SetBorderSize(0)
 pt.SetFillStyle(0)
 text = pt.AddText(names[labels[0]])
 text.SetTextFont(62)

 lumi13 = ""
 lumi8 = ""
 if labels[0].find("13") != -1 and labels[0].find("8") == -1:
  if labels[0].find("JJLVJ") != -1: lumi13 = "2.2-2.6"
  elif labels[0].find("jj") != -1: lumi13 = "2.6"
  else: lumi13 = "2.2"
 if "8" in labels[0] and not "13" in labels[0]:
  lumi8 = "19.7"
 if "138" in labels[0]:
  lumi13 = "2.2-2.6"
  lumi8 = "19.7"
       
 canv = get_canvas("c_lim_Asymptotic_compare",lumi8,lumi13)
 canv.cd()
  
 npoints = graphobs[0].GetN()
 x = ROOT.Double(0.)
 y = ROOT.Double(0.)
 graphobs[0].GetPoint(npoints-1,x,y)

 hrl_SM = canv.DrawFrame(0.75,0.01, x+0.050, 100) 
    
 if not unblind:  
  leg.AddEntry(graphobs[0],"Asympt. CL_{S} Observed","LP")
  leg.AddEntry(graphexp[0],"Asympt. CL_{S} Expected","L")
  for g in range(1,len(graphobs)): leg2.AddEntry(graphobs[g],names[labels[g]],"LP")   
  if bands:
   graph_2s[0].Draw("F")
   graph_1s[0].Draw("Fsame")
   leg.AddEntry(graph_1s[0],"Asympt. CL_{S} Expected #pm 1#sigma","LF")
   leg.AddEntry(graph_2s[0],"Asympt. CL_{S} Expected #pm 2#sigma","LF")
  graphexp[0].Draw("Lsame")
  graphobs[0].Draw("LPsame")
  for g in range(1,len(graphobs)): graphobs[g].Draw("LPsame")
 else:
  if bands:   
   graph_2s[0].Draw("F")
   graph_1s[0].Draw("Fsame")
   leg.AddEntry(graphobs[0],"Asympt. CL_{S} Observed","LP")
   leg.AddEntry(graph_1s[0],"Asympt. CL_{S} Expected #pm 1#sigma","LF")
   leg.AddEntry(graph_2s[0],"Asympt. CL_{S} Expected #pm 2#sigma","LF")
   graphobs[0].Draw("LPsame")
  else: leg.AddEntry(graphexp[0],"Asympt. CL_{S} Expected","L") 
  graphexp[0].Draw("Lsame")  
  for c in range(1,len(graphexp)):
   leg2.AddEntry(graphexp[c],names[labels[c]],"L")
   graphexp[c].Draw("Lsame")
   
 graphth[0].SetLineStyle(3)
 graphth[0].Draw("Lsame")
 theoleg = "#sigma_{TH} #times BR_{"+signal[labels[0]]+"#rightarrow "+decay[labels[0]]+"} , HVT_{B}"
 leg.AddEntry(graphth[0],theoleg,"L") 

 ytitle = "#sigma_{95%}/#sigma_{theory}"
 hrl_SM.GetYaxis().SetTitle(ytitle)
 hrl_SM.GetYaxis().SetTitleSize(0.05)
 hrl_SM.GetXaxis().SetTitleSize(0.05)
 hrl_SM.GetXaxis().SetLabelSize(0.04)
 hrl_SM.GetYaxis().SetLabelSize(0.04)
 hrl_SM.GetYaxis().SetTitleOffset(1.2)
 hrl_SM.GetXaxis().SetTitleOffset(1)
 hrl_SM.GetXaxis().SetTitle("M_{"+signal[labels[0]]+"} (TeV)")
 hrl_SM.GetXaxis().SetNdivisions(505)

 i=0.9
 exclMass = 0
 while i < 3.:
  i+=0.01 
  if not unblind or (unblind and bands): y = graphobs[0].Eval(i)
  else: y = graphexp[0].Eval(i) 
  if y > 1:
   print "Excluded mass is ",i," TeV with signal strenght ",y
   exclMass = i
   break

 line = TLine(exclMass,0.01,exclMass,100)
 line.SetLineStyle(7)
 line.SetLineColor(kBlue) 
 line.Draw()
             
 canv.Update()   
 canv.cd()
 
 period = 4
 if "138" in labels[0]: period = 7
 if "8" in labels[0] and not "13" in labels[0]: period = 2
 CMS_lumi.CMS_lumi(canv, period,0) 
  	
 canv.cd()
 canv.Update()
 canv.RedrawAxis()
 canv.RedrawAxis("g")
 leg.Draw("same")
 leg2.Draw("same")
 pt.Draw("same")
 frame = canv.GetFrame()
 frame.Draw()	
 canv.cd()
 canv.Update() 

 suffix = "observed"
 if unblind and not bands: suffix = "expected"
 if bands and not unblind: suffix = "bands"
 if bands and unblind: suffix = "final"
 
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_"+suffix+".root")
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_"+suffix+".png")
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_"+suffix+".pdf")
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_"+suffix+".eps")
    
#************************************************************************************************
if __name__ == '__main__':

 gROOT.SetBatch(ROOT.kTRUE)
 
 scenarios={} 
 
 # 8 + 13 TeV LLJ+LVJ+JJ (WV)
 scenarios["ALLWVHVT138TeV"]=["ALLWVHVT138","lvjwv8","lljwz8","jjwv8","jjwv13","lvjwv13"]
 scenarios["ALLWVWPRIME138TeV"]=["ALLWVWPRIME138","lvjwz8","lljwz8","jjwz8","jjwz13","lvjwz13"]
 scenarios["ALLWVZPRIME138TeV"]=["ALLWVZPRIME138","lvjww8","jjww8","jjww13","lvjww13"]

 #8+13 TeV VH+WV
 scenarios["ALLHVT138TeV"]=["ALLHVT138","ttjvh8","jjvh8","lvjwh8","lvjwv8","lljwzh8","jjwv8","jjwv13","lvjwv13"]
 scenarios["ALLWPRIME138TeV"]=["ALLWPRIME138","ttjwh8","jjwh8","lvjwh8","lvjwz8","lljwz8","jjwz8","jjwz13","lvjwz13"]
 scenarios["ALLZPRIME138TeV"]=["ALLZPRIME138","ttjzh8","jjzh8","lvjww8","jjww8","lljzh8","jjww13","lvjww13"]
     
 if len(sys.argv)>1:
    scenarios_arg={}
    scenarios_arg[sys.argv[1]]=scenarios[sys.argv[1]]
    scenarios=scenarios_arg
 else:
    print "Need input: <scenario>"
    sys.exit()

 for name in scenarios[sys.argv[1]]:
  print name
  plot_Asympt_limits(name,True)

 compare_Asympt_limits(scenarios[sys.argv[1]],False,False) #only observed
 compare_Asympt_limits(scenarios[sys.argv[1]],False,True) #observed + bands
 compare_Asympt_limits(scenarios[sys.argv[1]],True,False) #only expected 
 compare_Asympt_limits(scenarios[sys.argv[1]],True,True) #expected + observed combination + bands
 
 for name in scenarios[sys.argv[1]]:
  print name
  if "138" in name: plot_Asympt_limits(name,True)
  else: plot_Asympt_limits(name,False)
