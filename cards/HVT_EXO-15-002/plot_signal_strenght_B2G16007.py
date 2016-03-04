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

def get_palette(mode):

 palette = {}
 palette['gv'] = [] 
 
 colors = ['#40004b','#762a83','#9970ab','#de77ae','#a6dba0','#5aae61','#1b7837','#00441b','#92c5de','#4393c3','#2166ac','#053061']

 for c in colors:
  palette['gv'].append(c)
 
 return palette[mode]


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

 if label == "ALLHVT" or label == "ALLWPRIME" or label == "ALLZPRIME": return
 
 infile = "higgsCombine%s.Asymptotic.TOTAL.root"%label
 mass = [700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,
         2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,
	 3600,3700,3800,3900,4000]
	 
 signal = {}
 signal['ALLHVT138'] = "V'"
 signal['ALLWPRIME138'] = "W'"
 signal['ALLZPRIME138'] = "Z'"
 signal['ALLWVHVT138'] = "V'"
 signal['ALLWVWPRIME138'] = "W'"
 signal['ALLWVZPRIME138'] = "Z'"
 signal['JJLVJHVT13'] = "V'" 
 signal['JJLVJWPRIME13'] = "W'" 
 signal['JJLVJZPRIME13'] = "Z'" 
 signal['ALLWVHVT8'] = "V'"
 signal['ALLWVWPRIME8'] = "W'"
 signal['ALLWVZPRIME8'] = "Z'"
 signal['ALLHVHVT8'] = "V'"
 signal['ALLHVWPRIME8'] = "W'"
 signal['ALLHVZPRIME8'] = "Z'"
 signal['ALLHVT8'] = "V'"
 signal['ALLWPRIME8'] = "W'"
 signal['ALLZPRIME8'] = "Z'"
 signal['lllv8'] = "W'"
 signal['jjwv8'] = "V'"
 signal['jjwz8'] = "W'"
 signal['jjww8'] = "Z'"
 signal['jjwvvh8'] = "V'"
 signal['jjwzwh8'] = "W'"
 signal['jjwwzh8'] = "Z'" 
 signal['lvjwv8'] = "V'"
 signal['lvjwz8'] = "W'"
 signal['lvjww8'] = "Z'"
 signal['lljwz8'] = "W'" 
 signal['lljwzh8'] = "V'" 
 signal['lljzh8'] = "Z'" 
 signal['lvjwv13'] = "V'" 
 signal['lvjwz13'] = "W'"    
 signal['lvjww13'] = "Z'" 
 signal['lvjwvh13'] = "V'" 
 signal['lvjwzh13'] = "W'" 
 signal['jjwv13'] = "V'"
 signal['jjwvvh13'] = "V'"
 signal['jjwz13'] = "W'"
 signal['jjwzwh13'] = "W'"
 signal['jjww13'] = "Z'"
 signal['jjwwzh13'] = "Z'"
 signal['ttjvh8'] = "V'"
 signal['ttjwh8'] = "W'"
 signal['ttjzh8'] = "Z'" 
 signal['jjvh8'] = "V'"
 signal['jjwh8'] = "W'"
 signal['jjzh8'] = "Z'" 
 signal['lvjwh8'] = "W'"
 
 decay = {}
 decay['ALLWVHVT138'] = "WV/VH"
 decay['ALLWVWPRIME138'] = "WZ/WH"
 decay['ALLWVZPRIME138'] = "WW/ZH"
 decay['ALLHVT138'] = "WV/VH"
 decay['ALLWPRIME138'] = "WZ/WH"
 decay['ALLZPRIME138'] = "WW/ZH"
 decay['JJLVJHVT13'] = "WV/VH"
 decay['JJLVJWPRIME13'] = "WZ/WH" 
 decay['JJLVJZPRIME13'] = "WW/ZH" 
 decay['ALLWVHVT8'] = "WV/VH"
 decay['ALLWVWPRIME8'] = "WZ/WH"
 decay['ALLWVZPRIME8'] = "WW/ZH"
 decay['ALLHVHVT8'] = "VH"
 decay['ALLHVWPRIME8'] = "WH"
 decay['ALLHVZPRIME8'] = "ZH"
 decay['ALLHVT8'] = "WZ/VH"
 decay['ALLWPRIME8'] = "WZ/WH"
 decay['ALLZPRIME8'] = "WW/ZH"
 decay['lllv8'] = "WZ"
 decay['jjwv8'] = "WV"
 decay['jjwz8'] = "WZ"
 decay['jjww8'] = "WW"
 decay['jjwvvh8'] = "WV/VH"
 decay['jjwzwh8'] = "WZ/WH"
 decay['jjwwzh8'] = "WW/ZH" 
 decay['lvjwv8'] = "WV"
 decay['lvjwz8'] = "WZ"
 decay['lvjww8'] = "WW"
 decay['lljwz8'] = "WZ"
 decay['lljwzh8'] = "WZ/ZH" 
 decay['lljzh8'] = "ZH" 
 decay['lvjwv13'] = "WV"
 decay['lvjwz13'] = "WZ"
 decay['lvjww13'] = "WW"
 decay['lvjwzh13'] = "WZ/WH"
 decay['lvjwvh13'] = "WV/WH"
 decay['jjwv13'] = "WV"
 decay['jjwz13'] = "WZ"
 decay['jjww13'] = "WW"
 decay['jjwvvh13'] = "WV/VH"
 decay['jjwzwh13'] = "WZ/WH"
 decay['jjwwzh13'] = "WW/ZH"
 decay['ttjvh8'] = "VH"
 decay['ttjwh8'] = "WH"
 decay['ttjzh8'] = "ZH" 
 decay['jjvh8'] = "VH"
 decay['jjwh8'] = "WH"
 decay['jjzh8'] = "ZH" 
 decay['lvjwh8'] = "WH"
 
 names = {}
 names["ALLWVHVT138"]="lllv, lvJ, llJ, JJ (8+13 TeV)"
 names["ALLWVWPRIME138"]="lllv, lvJ, llJ, JJ (8+13 TeV)"
 names["ALLWVZPRIME138"]="lvJ, JJ (8+13 TeV)"
 names['ALLHVT138'] = "lllv, J#tau#tau, lvJ, JJ (8+13 TeV)"
 names['ALLWPRIME138'] = "lllv, J#tau#tau, lvJ, llJ, JJ (8+13 TeV)"
 names['ALLZPRIME138'] = "J#tau#tau, lvJ, JJ (8+13 TeV)"
 names["JJLVJHVT13"]="lvJ, JJ (13 TeV)"
 names["JJLVJWPRIME13"]="lvJ, JJ (13 TeV)"
 names["JJLVJZPRIME13"]="lvJ, JJ (13 TeV)"
 names["ALLWVHVT8"]="lllv, lvJ, llJ, JJ (8 TeV)"
 names["ALLWVWPRIME8"]="lllv, lvJ, llJ, JJ (8 TeV)"
 names["ALLWVZPRIME8"]="lvJ, llJ, JJ (8 TeV)"
 names['ALLHVHVT8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLHVWPRIME8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLHVZPRIME8'] = "J#tau#tau, JJ (8 TeV)"
 names['ALLHVT8'] = "lllv, J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLWPRIME8'] = "lllv, J#tau#tau, lvJ, llJ, JJ (8 TeV)"
 names['ALLZPRIME8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['lllv8']="lllv (8 TeV)"
 names["lvjwv8"]="lvqq (8 TeV)"
 names["lvjwz8"]="lvqq (8 TeV)"
 names["lvjww8"]="lvqq (8 TeV)"
 names["lljwz8"]="llqq (8 TeV)"
 names['lljwzh8']="llqq (8 TeV)"
 names['lljzh8']="llqq (8 TeV)"
 names["jjwv8"]="qqqq (8 TeV)"
 names["jjwz8"]="qqqq (8 TeV)"
 names["jjww8"]="qqqq (8 TeV)"
 names["jjwvvh8"]="qqqq (8 TeV)"
 names["jjwzwh8"]="qqqq (8 TeV)"
 names["jjwwzh8"]="qqqq (8 TeV)" 
 names["jjwv13"]="qqqq (13 TeV)"
 names["jjww13"]="qqqq (13 TeV)"
 names["jjwz13"]="qqqq (13 TeV)"
 names["jjwvvh13"]="qqqq (13 TeV)"
 names["jjwzwh13"]="qqqq (13 TeV)"
 names["jjwwzh13"]="qqqq (13 TeV)"
 names["lvjwv13"]="lvqq (13 TeV)"
 names["lvjwv13"]="lvqq (13 TeV)"
 names["lvjww13"]="lvqq (13 TeV)"
 names["lvjwz13"]="lvqq (13 TeV)"
 names["lvjwzh13"]="lvqq (13 TeV)"
 names["lvjwvh13"]="lvqq (13 TeV)" 
 names['ttjvh8'] = "qq#tau#tau (8 TeV)"
 names['ttjwh8'] = "qq#tau#tau (8 TeV)"
 names['ttjzh8'] = "qq#tau#tau (8 TeV)"
 names['jjvh8'] = "qqbb(4q) (8 TeV)"
 names['jjwh8'] = "qqbb(4q) (8 TeV)"
 names['jjzh8'] = "qqbb(4q) (8 TeV)" 
 names['lvjwh8'] = "lvbb (8 TeV)"
  
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
  ybins_exp.append( curAsymLimits[3] );
  ybins_obs.append( curAsymLimits[0] );
  ybins_2s.append( curAsymLimits[1] );
  ybins_1s.append( curAsymLimits[2] );
  ybins_xs.append( 1 );
  nPoints+=1

 for i in range( len(mass)-1, -1, -1 ):

  curAsymLimits = getAsymLimits(infile,mass[i]);
  if curAsymLimits[0] == -1: continue
  xbins_env.append( mass[i]/1000. );
  ybins_2s.append( curAsymLimits[5] );
  ybins_1s.append( curAsymLimits[4] );

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

 transGreen = gROOT.GetColor(3)
 transGreen.SetAlpha(0.35)
 curGraph_1s.SetFillColor(3)
 curGraph_1s.SetFillStyle(1001)
 curGraph_1s.SetLineStyle(ROOT.kDashed)
 curGraph_1s.SetLineWidth(3)

 transYellow = gROOT.GetColor(5)
 transYellow.SetAlpha(0.5)
 curGraph_2s.SetFillColor(5)
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
 #canv.SaveAs("plots/EXOVVhvt_"+label+"_UL_Asymptotic_log.png")
 #canv.SaveAs("plots/EXOVVhvt_"+label+"_UL_Asymptotic_log.pdf")
 #canv.SaveAs("plots/EXOVVhvt_"+label+"_UL_Asymptotic_log.eps")

def compare_Asympt_limits(labels,unblind,bands):

 palette = get_palette('gv')
 col = TColor()
 
 #line color
 lcol = {}
 if labels[0] != "ALLHVT" and labels[0] != "ALLWPRIME" and labels[0] != "ALLZPRIME":
  lcol["ALLWVHVT138"] = kBlack
  lcol["ALLWVWPRIME138"] = kBlack
  lcol["ALLWVZPRIME138"] = kBlack
  lcol['ALLHVT138'] = kBlack
  lcol['ALLWPRIME138'] = kBlack
  lcol['ALLZPRIME138'] = kBlack  
 else:
  lcol['ALLHVT138'] = col.GetColor(palette[5])
  lcol['ALLWPRIME138'] = col.GetColor(palette[5])
  lcol['ALLZPRIME138'] = col.GetColor(palette[5])  
  lcol["JJLVJHVT13"] = col.GetColor(palette[9])
  lcol["JJLVJWPRIME13"] = col.GetColor(palette[9])
  lcol["JJLVJZPRIME13"] = col.GetColor(palette[9])
  lcol['ALLHVT8'] = col.GetColor(palette[2])
  lcol['ALLWPRIME8'] = col.GetColor(palette[2])
  lcol['ALLZPRIME8'] = col.GetColor(palette[2]) 
  #4 dummy graph
  lcol["ALLHVT"] = 0 
  lcol["ALLWPRIME"] = 0 
  lcol["ALLZPRIME"] = 0 
   
 #lvj13
 lcol["lvjwv13"] = col.GetColor(palette[10])
 lcol["lvjwz13"] = col.GetColor(palette[10])
 lcol["lvjww13"] = col.GetColor(palette[10])
 lcol["lvjwzh13"] = col.GetColor(palette[10])
 lcol["lvjwvh13"] = col.GetColor(palette[10])
 #jj13
 lcol["jjwv13"] = col.GetColor(palette[9])
 lcol["jjwz13"] = col.GetColor(palette[9])
 lcol["jjww13"] = col.GetColor(palette[9])
 lcol["jjwvvh13"] = col.GetColor(palette[9])
 lcol["jjwzwh13"] = col.GetColor(palette[9])
 lcol["jjwwzh13"] = col.GetColor(palette[9]) 
 #lllv8
 lcol['lllv8'] = col.GetColor(palette[0])
 #llj8
 lcol["lljwz8"] = col.GetColor(palette[1])
 lcol['lljwzh8'] = col.GetColor(palette[1])
 lcol['lljzh8'] = col.GetColor(palette[1])
 #lvj8
 lcol["lvjwv8"] = col.GetColor(palette[2])
 lcol["lvjwz8"] = col.GetColor(palette[2])
 lcol["lvjww8"] = col.GetColor(palette[2])
 #lvbb8
 lcol['lvjwh8'] = col.GetColor(palette[3])
 #jj8
 lcol["jjwv8"] = col.GetColor(palette[6])
 lcol["jjwz8"] = col.GetColor(palette[6])
 lcol["jjww8"] = col.GetColor(palette[6])
 lcol["jjwvvh8"] = col.GetColor(palette[6])
 lcol["jjwzwh8"] = col.GetColor(palette[6])
 lcol["jjwwzh8"] = col.GetColor(palette[6])
 #jjvh8
 lcol['jjvh8'] = col.GetColor(palette[5])
 lcol['jjwh8'] = col.GetColor(palette[5])
 lcol['jjzh8'] = col.GetColor(palette[5])
 #ttj8
 lcol['ttjvh8'] = col.GetColor(palette[4])
 lcol['ttjwh8'] = col.GetColor(palette[4])
 lcol['ttjzh8'] = col.GetColor(palette[4])
 
 #marker color
 mcol = {}
 if labels[0] != "ALLHVT" and labels[0] != "ALLWPRIME" and labels[0] != "ALLZPRIME":
  mcol["ALLWVHVT138"] = kBlack
  mcol["ALLWVWPRIME138"] = kBlack
  mcol["ALLWVZPRIME138"] = kBlack
  mcol['ALLHVT138'] = kBlack
  mcol['ALLWPRIME138'] = kBlack
  mcol['ALLZPRIME138'] = kBlack  
  mcol["JJLVJHVT13"] = kBlack
  mcol["JJLVJWPRIME13"] = kBlack
  mcol["JJLVJZPRIME13"] = kBlack
 else:
  mcol['ALLHVT138'] = col.GetColor(palette[5])
  mcol['ALLWPRIME138'] = col.GetColor(palette[5])
  mcol['ALLZPRIME138'] = col.GetColor(palette[5])  
  mcol["JJLVJHVT13"] = col.GetColor(palette[9])
  mcol["JJLVJWPRIME13"] = col.GetColor(palette[9])
  mcol["JJLVJZPRIME13"] = col.GetColor(palette[9])
  mcol['ALLHVT8'] = col.GetColor(palette[2])
  mcol['ALLWPRIME8'] = col.GetColor(palette[2])
  mcol['ALLZPRIME8'] = col.GetColor(palette[2])
  #4 dummy graph
  mcol["ALLHVT"] = 0 
  mcol["ALLWPRIME"] = 0 
  mcol["ALLZPRIME"] = 0 

 #lvj13
 mcol["lvjwv13"] = col.GetColor(palette[10])
 mcol["lvjwz13"] = col.GetColor(palette[10])
 mcol["lvjww13"] = col.GetColor(palette[10])
 mcol["lvjwzh13"] = col.GetColor(palette[10])
 mcol["lvjwvh13"] = col.GetColor(palette[10])
 #jj13
 mcol["jjwv13"] = col.GetColor(palette[9])
 mcol["jjwz13"] = col.GetColor(palette[9])
 mcol["jjww13"] = col.GetColor(palette[9])
 mcol["jjwvvh13"] = col.GetColor(palette[9])
 mcol["jjwzwh13"] = col.GetColor(palette[9])
 mcol["jjwwzh13"] = col.GetColor(palette[9])
 #lllv8
 mcol['lllv8'] = col.GetColor(palette[0])
 #llj8
 mcol["lljwz8"] = col.GetColor(palette[1])
 mcol['lljwzh8'] = col.GetColor(palette[1])
 mcol['lljzh8'] = col.GetColor(palette[1])
 #lvj8 
 mcol["lvjwv8"] = col.GetColor(palette[2]) 
 mcol["lvjwz8"] = col.GetColor(palette[2])
 mcol["lvjww8"] = col.GetColor(palette[2])
 #lvjwh8
 mcol['lvjwh8'] = col.GetColor(palette[3])
 #jj8
 mcol["jjwv8"] = col.GetColor(palette[6])
 mcol["jjwz8"] = col.GetColor(palette[6])
 mcol["jjww8"] = col.GetColor(palette[6])
 mcol["jjwvvh8"] = col.GetColor(palette[6])
 mcol["jjwzwh8"] = col.GetColor(palette[6])
 mcol["jjwwzh8"] = col.GetColor(palette[6])
 #ttj8
 mcol['ttjvh8'] =  col.GetColor(palette[4])
 mcol['ttjwh8'] =  col.GetColor(palette[4])
 mcol['ttjzh8'] =  col.GetColor(palette[4])
 #jjvh8
 mcol['jjvh8'] = col.GetColor(palette[5])
 mcol['jjwh8'] = col.GetColor(palette[5])
 mcol['jjzh8'] = col.GetColor(palette[5])
 
 #marker style
 msty = {}
 #4 dummy graph
 msty["ALLHVT"] = 0 
 msty["ALLWPRIME"] = 0 
 msty["ALLZPRIME"] = 0 
 msty['ALLHVT138'] = 20
 msty['ALLWPRIME138'] = 20
 msty['ALLZPRIME138'] = 20
 msty["ALLWVHVT138"] = 20
 msty["ALLWVWPRIME138"] = 20
 msty["ALLWVZPRIME138"] = 20
 msty["JJLVJHVT13"] = 26
 msty["JJLVJWPRIME13"] = 26
 msty["JJLVJZPRIME13"] = 26
 msty['ALLHVT8'] = 31
 msty['ALLWPRIME8'] = 31
 msty['ALLZPRIME8'] = 31
 #lvj13
 msty["lvjwv13"] = 26
 msty["lvjwz13"] = 26
 msty["lvjww13"] = 26
 msty["lvjwzh13"] = 26
 msty["lvjwvh13"] = 26 
 #jj13
 msty["jjwv13"] = 22
 msty["jjwz13"] = 22
 msty["jjww13"] = 22
 msty["jjwvvh13"] = 22
 msty["jjwzwh13"] = 22
 msty["jjwwzh13"] = 22  
 #lllv8
 msty['lllv8'] = 22
 #llj8
 msty["lljwz8"] = 25
 msty['lljwzh8'] = 25
 msty['lljzh8'] = 25
 #lvj8
 msty["lvjwv8"] = 26
 msty["lvjwz8"] = 26
 msty["lvjww8"] = 26
 #lvbb8
 msty['lvjwh8'] = 31
 #jj8
 msty["jjwv8"] = 22
 msty["jjwz8"] = 22
 msty["jjww8"] = 22
 msty["jjwvvh8"] = 22
 msty["jjwzwh8"] = 22
 msty["jjwwzh8"] = 22 
 #ttj8
 msty['ttjvh8'] = 25
 msty['ttjwh8'] = 25
 msty['ttjzh8'] = 25
 #jjvh8
 msty['jjvh8'] = 31
 msty['jjwh8'] = 31
 msty['jjzh8'] = 31
    
 signal = {}
 signal["ALLWVHVT138"] = "V'"
 signal["ALLWVWPRIME138"] = "W'"
 signal["ALLWVZPRIME138"] = "Z'"
 signal['ALLHVT'] = "V'"
 signal['ALLWPRIME'] = "W'"
 signal['ALLZPRIME'] = "Z'" 
 signal['ALLHVT138'] = "V'"
 signal['ALLWPRIME138'] = "W'"
 signal['ALLZPRIME138'] = "Z'" 
 signal['JJLVJHVT13'] = "V'"
 signal["JJLVJWPRIME13"] = "W'"
 signal["JJLVJZPRIME13"] = "Z'"
 signal['ALLHVT8'] = "V'"
 signal['ALLWPRIME8'] = "W'"
 signal['ALLZPRIME8'] = "Z'"
 
 decay = {}
 decay['ALLWVHVT138'] = "WV/WH"
 decay['ALLWVWPRIME138'] = "WZ/WH"
 decay['ALLWVZPRIME138'] = "WW"
 decay['ALLHVT138'] = "WV/VH"
 decay['ALLWPRIME138'] = "WZ/WH"
 decay['ALLZPRIME138'] = "WW/ZH"  
 decay['ALLHVT'] = "WV/VH"
 decay['ALLWPRIME'] = "WZ/WH"
 decay['ALLZPRIME'] = "WW/ZH" 
 decay['JJLVJHVT13'] = "WV/VH"
 decay['JJLVJWPRIME13'] = "WZ/WH" 
 decay['JJLVJZPRIME13'] = "WW/ZH" 
 decay['ALLHVT8'] = "WV/VH"
 decay['ALLWPRIME8'] = "WZ/WH"
 decay['ALLZPRIME8'] = "WW/ZH"
     
 names = {}
 names['ALLHVT'] = "lllv, J#tau#tau, lvJ, JJ (8+13 TeV)"
 names['ALLWPRIME'] = "lllv, J#tau#tau, lvJ, llJ, JJ (8+13 TeV)"
 names['ALLZPRIME'] = "J#tau#tau, lvJ, JJ (8+13 TeV)"
 names["ALLWVHVT138"]="lllv, lvJ, llJ, JJ (8+13 TeV)"
 names["ALLWVWPRIME138"]="lllv, lvJ, llJ, JJ (8+13 TeV)"
 names["ALLWVZPRIME138"]="lvJ, JJ (8+13 TeV)"
 names['ALLHVT138'] = "lllv, J#tau#tau, lvJ, JJ (8+13 TeV)"
 names['ALLWPRIME138'] = "lllv, J#tau#tau, lvJ, llJ, JJ (8+13 TeV)"
 names['ALLZPRIME138'] = "J#tau#tau, lvJ, llJ, JJ (8+13 TeV)"
 names["JJLVJHVT13"]="lvJ, JJ (13 TeV)"
 names["JJLVJWPRIME13"]="lvJ, JJ (13 TeV)"
 names["JJLVJZPRIME13"]="lvJ, JJ (13 TeV)"
 names['ALLHVT8'] = "lllv, J#tau#tau, lvJ, JJ (8 TeV)"
 names['ALLWPRIME8'] = "lllv, J#tau#tau, lvJ, llJ, JJ (8 TeV)"
 names['ALLZPRIME8'] = "J#tau#tau, lvJ, JJ (8 TeV)"
 names['lllv8']="lllv (8 TeV)"
 names["lvjwv8"]="lvqq (8 TeV)"
 names["lvjwz8"]="lvqq (8 TeV)"
 names["lvjww8"]="lvqq (8 TeV)"
 names["lljwz8"]="llqq (8 TeV)"
 names['lljwzh8']="llqq (8 TeV)"
 names['lljzh8']="llqq (8 TeV)"
 names["jjwv8"]="qqqq (8 TeV)"
 names["jjwz8"]="qqqq (8 TeV)"
 names["jjww8"]="qqqq (8 TeV)"
 names["jjwvvh8"]="qqqq (8 TeV)"
 names["jjwzwh8"]="qqqq (8 TeV)"
 names["jjwwzh8"]="qqqq (8 TeV)" 
 names["jjwv13"]="qqqq (13 TeV)"
 names["jjww13"]="qqqq (13 TeV)"
 names["jjwz13"]="qqqq (13 TeV)"
 names["jjwvvh13"]="qqqq (13 TeV)"
 names["jjwzwh13"]="qqqq (13 TeV)"
 names["jjwwzh13"]="qqqq (13 TeV)"
 names["lvjwv13"]="lvqq (13 TeV)"
 names["lvjwv13"]="lvqq (13 TeV)"
 names["lvjww13"]="lvqq (13 TeV)"
 names["lvjwz13"]="lvqq (13 TeV)"
 names["lvjwzh13"]="lvqq (13 TeV)"
 names["lvjwvh13"]="lvqq (13 TeV)" 
 names['ttjvh8'] = "qq#tau#tau (8 TeV)"
 names['ttjwh8'] = "qq#tau#tau (8 TeV)"
 names['ttjzh8'] = "qq#tau#tau (8 TeV)"
 names['jjvh8'] = "qqbb(4q) (8 TeV)"
 names['jjwh8'] = "qqbb(4q) (8 TeV)"
 names['jjzh8'] = "qqbb(4q) (8 TeV)" 
 names['lvjwh8'] = "lvbb (8 TeV)"
 
 legs1={}
 legs1["ALLHVT"]=[0.55,0.40,0.88,0.43]#[0.45,0.34,0.90,0.45]
 legs1["ALLWPRIME"]=[0.55,0.40,0.88,0.43]#[0.45,0.34,0.90,0.45]
 legs1["ALLZPRIME"]=[0.55,0.40,0.88,0.43]#[0.45,0.34,0.90,0.45]
 legs1["ALLHVT138"]=[0.16,0.75,0.49,0.88]#[0.45,0.34,0.90,0.45]
 legs1["ALLWPRIME138"]=[0.16,0.75,0.49,0.88]#[0.45,0.34,0.90,0.45]
 legs1["ALLZPRIME138"]=[0.16,0.75,0.49,0.88]#[0.45,0.34,0.90,0.45]
 legs1["ALLWVHVT138"]=[0.16,0.75,0.49,0.88]#[0.45,0.34,0.90,0.45]
 legs1["ALLWVWPRIME138"]=[0.16,0.75,0.49,0.88]#[0.45,0.34,0.90,0.45]
 legs1["ALLWVZPRIME138"]=[0.16,0.75,0.49,0.88]#[0.45,0.34,0.90,0.45] 
 legs1["JJLVJHVT13"]=[0.45,0.34,0.90,0.45]
 legs1["JJLVJWPRIME13"]=[0.45,0.34,0.90,0.45]
 legs1["JJLVJZPRIME13"]=[0.45,0.34,0.90,0.45]
 legs1["ALLHVT8"]=[0.45,0.34,0.90,0.45]
 legs1["ALLWPRIME8"]=[0.45,0.34,0.90,0.45]
 legs1["ALLZPRIME8"]=[0.45,0.34,0.90,0.45]
    
 legs2={}
 legs2["ALLHVT"]=[0.37,0.16,0.88,0.33]#[0.31,0.16,0.88,0.31]
 legs2["ALLWPRIME"]=[0.37,0.16,0.88,0.33]#[0.31,0.16,0.88,0.31]
 legs2["ALLZPRIME"]=[0.37,0.16,0.88,0.33]#[0.31,0.16,0.88,0.31]  
 legs2["ALLWVHVT138"]=[0.37,0.18,0.88,0.29]#[0.43,0.18,0.88,0.29]
 legs2["ALLWVWPRIME138"]=[0.37,0.18,0.88,0.29]#[0.43,0.18,0.88,0.29]
 legs2["ALLWVZPRIME138"]=[0.37,0.18,0.88,0.29]#[0.43,0.18,0.88,0.29]
 legs2["ALLHVT138"]=[0.37,0.16,0.88,0.33]#[0.31,0.16,0.88,0.31]
 legs2["ALLWPRIME138"]=[0.37,0.16,0.88,0.33]#[0.31,0.16,0.88,0.31]
 legs2["ALLZPRIME138"]=[0.37,0.16,0.88,0.33]#[0.31,0.16,0.88,0.31]  
 legs2["JJLVJHVT13"]=[0.43,0.25,0.88,0.30]
 legs2["JJLVJWPRIME13"]=[0.43,0.25,0.88,0.30]
 legs2["JJLVJZPRIME13"]=[0.43,0.25,0.88,0.30]
 legs2["ALLHVT8"]=[0.43,0.18,0.88,0.29]
 legs2["ALLWPRIME8"]=[0.43,0.18,0.88,0.29]
 legs2["ALLZPRIME8"]=[0.43,0.18,0.88,0.29]

 legs3={}
 legs3["ALLHVT"]=[0.17,0.66,0.43,0.90]
 legs3["ALLWPRIME"]=[0.17,0.66,0.43,0.90]
 legs3["ALLZPRIME"]=[0.17,0.66,0.43,0.90] 
 legs3["ALLWVHVT138"]=[0.17,0.71,0.43,0.88]
 legs3["ALLWVWPRIME138"]=[0.17,0.71,0.43,0.88]
 legs3["ALLWVZPRIME138"]=[0.17,0.71,0.43,0.88]
 legs3["ALLHVT138"]=[0.17,0.66,0.43,0.90]
 legs3["ALLWPRIME138"]=[0.17,0.66,0.43,0.90]
 legs3["ALLZPRIME138"]=[0.17,0.66,0.43,0.90] 
 legs3["JJLVJHVT13"]=[0.17,0.78,0.43,0.88]
 legs3["JJLVJWPRIME13"]=[0.17,0.78,0.43,0.88]
 legs3["JJLVJZPRIME13"]=[0.17,0.78,0.43,0.88]
 legs3["ALLHVT8"]=[0.17,0.78,0.43,0.88]
 legs3["ALLWPRIME8"]=[0.17,0.78,0.43,0.88]
 legs3["ALLZPRIME8"]=[0.17,0.78,0.43,0.88]
    
 ymin = {}
 ymax = {}  
 ymin["ALLHVT"] = 0.03
 ymax["ALLHVT"] = 100
 ymin["ALLWPRIME"] = 0.03
 ymax["ALLWPRIME"] = 100
 ymin["ALLZPRIME"] = 0.1
 ymax["ALLZPRIME"] = 200   
 ymin["ALLWVHVT138"] = 0.03
 ymax["ALLWVHVT138"] = 100
 ymin["ALLWVWPRIME138"] = 0.03
 ymax["ALLWVWPRIME138"] = 100
 ymin["ALLWVZPRIME138"] = 0.06
 ymax["ALLWVZPRIME138"] = 200
 ymin["ALLHVT138"] = 0.03
 ymax["ALLHVT138"] = 100
 ymin["ALLWPRIME138"] = 0.03
 ymax["ALLWPRIME138"] = 100
 ymin["ALLZPRIME138"] = 0.05
 ymax["ALLZPRIME138"] = 1500
             
 files = []
 canvas = []
 graph_1s = []
 graph_2s = []
 graphexp = []
 graphobs = []
 graphth = []
   
 #files=[TFile.Open("plots/EXOVVhvt_"+l+"_UL_Asymptotic_log.root") for l in labels]
 files = []
 for l in labels:
  if l == "ALLHVT" or l == "ALLWPRIME" or l == "ALLZPRIME": continue
  files.append(TFile.Open("plots/EXOVVhvt_"+l+"_UL_Asymptotic_log.root"))
 #for f in files: print f.GetName()
 canvas=[f.Get("c_lim_Asymptotic") for f in files]

 if labels[0] == 'ALLHVT' or labels[0] == "ALLWPRIME" or labels[0] == "ALLZPRIME":
  dummy = TGraph(1,array('d',[-1]),array('d',[-1000]))
  graph_1s.append(dummy)
  graph_2s.append(dummy) 
  graphexp.append(dummy)
  graphobs.append(dummy)
  graphth.append(dummy)
   
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
   graphobs[g].SetLineWidth(1)
   graphexp[g].SetLineWidth(1)
   graphexp[g].SetLineStyle(1)
   
 leg = ROOT.TLegend(0.46,0.16,0.90,0.33)#(0.3808725,0.166113,0.8959732,0.3803987)
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
 leg2.SetTextSize(0.032)
 leg2.SetLineColor(1)
 leg2.SetLineStyle(1)
 leg2.SetShadowColor(0)
 leg2.SetLineWidth(1)
 leg2.SetFillColor(0)
 leg2.SetTextFont(42)
 if not bands: leg2.SetNColumns(2)
 
 pt = ROOT.TPaveText(0.56,0.85,0.91,0.90,"NDC")#(0.5486577,0.8355482,0.8993289,0.8920266,"NDC")
 pt.SetTextFont(42)
 pt.SetTextSize(0.032)
 pt.SetTextAlign(32)
 pt.SetFillColor(0)
 pt.SetBorderSize(0)
 pt.SetFillStyle(0)
 if labels[0] != "ALLHVT" and labels[0] != "ALLWPRIME" and labels[0] != "ALLZPRIME": text = pt.AddText(names[labels[0]])
 else:
  if unblind: text = pt.AddText("Asympt. CL_{S} Exp.")
  else: text = pt.AddText("Asympt. CL_{S} Obs.")
 text.SetTextFont(62)

 lumi13 = ""
 lumi8 = ""
 if labels[0].find("13") != -1 and labels[0].find("8") == -1:
  if labels[0].find("JJLVJ") != -1: lumi13 = "2.2-2.6"
  elif labels[0].find("jj") != -1: lumi13 = "2.6"
  else: lumi13 = "2.2"
 elif "8" in labels[0] and not "13" in labels[0]:
  lumi8 = "19.7"
 elif "138" in labels[0]:
  lumi13 = "2.2-2.6"
  lumi8 = "19.7"
 else:
  lumi13 = "2.2-2.6"
  lumi8 = "19.7"
          
 canv = get_canvas("c_lim_Asymptotic_compare",lumi8,lumi13)
 canv.cd()
  
 if labels[0] != "ALLHVT" and labels[0] != "ALLWPRIME" and labels[0] != "ALLZPRIME":
  npoints = graphobs[0].GetN()
  x = ROOT.Double(0.)
  y = ROOT.Double(0.)
  graphobs[0].GetPoint(npoints-1,x,y)
 else:
  npoints = graphobs[3].GetN()
  x = ROOT.Double(0.)
  y = ROOT.Double(0.)
  graphobs[3].GetPoint(npoints-1,x,y)
  
 #hrl_SM = canv.DrawFrame(0.75,0.01, x+0.050, 100) 
 hrl_SM = canv.DrawFrame(0.75,ymin[labels[0]], x+0.050, ymax[labels[0]]) 
 
 if labels[0] == "ALLHVT" or labels[0] == "ALLWPRIME" or labels[0] == "ALLZPRIME":
  leg2.SetNColumns(1)
  for g in range(1,len(graphobs)):
   if unblind:
    graphexp[g].Draw("LP") 
    leg2.AddEntry(graphexp[g],names[labels[g]],"LP")
   else:
    graphobs[g].Draw("LP") 
    leg2.AddEntry(graphobs[g],names[labels[g]],"LP")
  graphth[3].SetLineStyle(3)
  graphth[3].Draw("L")
  theoleg = " HVT_{B} (g_{V}=3)"
  leg.AddEntry(graphth[3],theoleg,"L")
 else:   
  if not unblind:  
   leg.AddEntry(graphobs[0],"Asympt. CL_{S} Obs.","LP")
   leg.AddEntry(graphexp[0],"Asympt. CL_{S} Exp.","L")
   for g in range(1,len(graphobs)): leg2.AddEntry(graphobs[g],names[labels[g]],"LP")   
   if bands:
    graph_2s[0].Draw("F")
    graph_1s[0].Draw("Fsame")
    leg.AddEntry(graph_1s[0],"Asympt. CL_{S} Exp. #pm 1#sigma","LF")
    leg.AddEntry(graph_2s[0],"Asympt. CL_{S} Exp. #pm 2#sigma","LF")
   graphexp[0].Draw("Lsame")
   graphobs[0].Draw("LPsame")
   for g in range(1,len(graphobs)): graphobs[g].Draw("LPsame")
  else:
   if bands:   
    graph_2s[0].Draw("F")
    graph_1s[0].Draw("Fsame")
    leg.AddEntry(graphobs[0],"Asympt. CL_{S} Obs.","LP")
    leg.AddEntry(graph_1s[0],"Asympt. CL_{S} Exp. #pm 1#sigma","LF")
    leg.AddEntry(graph_2s[0],"Asympt. CL_{S} Exp. #pm 2#sigma","LF")
    graphobs[0].Draw("LPsame")
   else: leg.AddEntry(graphexp[0],"Asympt. CL_{S} Exp.","L") 
   graphexp[0].Draw("Lsame")  
   for c in range(1,len(graphexp)):
    leg2.AddEntry(graphexp[c],names[labels[c]],"LP")
    graphexp[c].Draw("LPsame")
   
  graphth[0].SetLineStyle(3)
  graphth[0].Draw("Lsame")
  #theoleg = "#sigma_{TH} #times BR_{"+signal[labels[0]]+"#rightarrow "+decay[labels[0]]+"} , HVT_{B}"
  theoleg = " HVT_{B} (g_{V}=3)"
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

 line = TLine(exclMass,ymin[labels[0]],exclMass,ymax[labels[0]])
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
 scenarios["ALLWVHVT138TeV"]=["ALLWVHVT138","lllv8","lljwzh8","lvjwv8","jjwvvh8","lvjwvh13","jjwvvh13"]
 scenarios["ALLWVWPRIME138TeV"]=["ALLWVWPRIME138","lllv8","lljwz8","lvjwz8","jjwzwh8","lvjwzh13","jjwzwh13"]
 scenarios["ALLWVZPRIME138TeV"]=["ALLWVZPRIME138","lvjww8","jjwwzh8","lvjww13","jjwwzh13"]

 #8+13 TeV VH+WV
 scenarios["ALLHVT138TeV"]=["ALLHVT138","lllv8","lljwzh8","lvjwv8","lvjwh8","jjwvvh8","jjvh8","ttjvh8","lvjwvh13","jjwvvh13"]
 scenarios["ALLWPRIME138TeV"]=["ALLWPRIME138","lllv8","lljwz8","lvjwz8","lvjwh8","jjwzwh8","jjwh8","ttjwh8","lvjwzh13","jjwzwh13"]
 scenarios["ALLZPRIME138TeV"]=["ALLZPRIME138","lljzh8","lvjww8","jjwwzh8","jjzh8","ttjzh8","lvjww13","jjwwzh13"]

 #compare all combinations
 scenarios["ALLHVT"]=["ALLHVT","ALLHVT8","JJLVJHVT13","ALLHVT138"]
 scenarios["ALLWPRIME"]=["ALLWPRIME","ALLWPRIME8","JJLVJWPRIME13","ALLWPRIME138"]
 scenarios["ALLZPRIME"]=["ALLZPRIME","ALLZPRIME8","JJLVJZPRIME13","ALLZPRIME138"]
     
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

 if scenarios[sys.argv[1]][0] != "ALLHVT" and scenarios[sys.argv[1]][0] != "ALLWPRIME" and scenarios[sys.argv[1]][0] != "ALLZPRIME":
  compare_Asympt_limits(scenarios[sys.argv[1]],False,False) #only observed
  compare_Asympt_limits(scenarios[sys.argv[1]],False,True) #observed + bands
  compare_Asympt_limits(scenarios[sys.argv[1]],True,False) #only expected 
  compare_Asympt_limits(scenarios[sys.argv[1]],True,True) #expected + observed combination + bands
 else:
  #compare_Asympt_limits(scenarios[sys.argv[1]],False,False) #only observed 
  compare_Asympt_limits(scenarios[sys.argv[1]],True,False) #only observed 
 
