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

def getPValueFromCard(file,mass):

    f = ROOT.TFile(file)
    t = f.Get("limit")
    entries = t.GetEntries()
    
    lims = -1
    
    for i in range(entries):
        
     t.GetEntry(i)
     if t.mh != mass: continue
     lims = t.limit
    
    return lims
    
def plot_significance(label):

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
  
 infileObs = "higgsCombine%sObsSignif.ProfileLikelihood.TOTAL.root"%label
 infileExp = "higgsCombine%sExpSignif.ProfileLikelihood.TOTAL.root"%label
 mass = [700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,
       2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,
       3600,3700,3800,3900,4000]
 
 xbins = array('d', [])
 ybins_obs = array('d', [])
 ybins_exp = array('d', [])
 nPoints = 0
 
 lastMass = 800.
 for m in mass:
 
  pvalue_obs = getPValueFromCard(infileObs,m)
  pvalue_exp = getPValueFromCard(infileExp,m)  
  if pvalue_obs == -1: continue
  lastMass = m/1000.
  print m,pvalue_obs,RooStats.PValueToSignificance(pvalue_obs)
  ybins_obs.append(pvalue_obs)        
  ybins_exp.append(pvalue_exp)      
  xbins.append(m/1000.)       
  nPoints+=1  
  #print "mass %i p-value obs %f" %(mass[i],pvalue_obs)

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
  
 canv = get_canvas("c_Significance",lumi8,lumi13)
 canv.cd()

 hrl_SM = canv.DrawFrame(0.75,0.00001, lastMass+0.050, 10) 
 ytitle = "p-value"
 hrl_SM.GetYaxis().SetTitle(ytitle)
 hrl_SM.GetYaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitle("M_{"+signal[label]+"} (TeV)")
      
 gr_pvalue_exp = ROOT.TGraph(nPoints,xbins,ybins_exp)	
 gr_pvalue_exp.SetName("Expected")
 gr_pvalue_exp.SetLineStyle(2)
 gr_pvalue_exp.SetLineWidth(2)
 gr_pvalue_obs = ROOT.TGraph(nPoints,xbins,ybins_obs)
 gr_pvalue_obs.SetName("Observed")
 gr_pvalue_obs.SetLineColor(1)
 gr_pvalue_obs.SetMarkerColor(1)
 gr_pvalue_obs.SetMarkerStyle(20)
 gr_pvalue_obs.SetLineWidth(2)
 gr_pvalue_obs.SetMarkerSize(1.)

 oneSLine = ROOT.TF1("oneSLine","1.58655253931457074e-01",0.75,4.050);
 oneSLine.SetLineColor(ROOT.kRed); oneSLine.SetLineWidth(2); oneSLine.SetLineStyle(3);
 twoSLine = ROOT.TF1("twoSLine","2.27501319481792155e-02",0.75,4.050);
 twoSLine.SetLineColor(ROOT.kRed); twoSLine.SetLineWidth(2); twoSLine.SetLineStyle(3);
 threeSLine = ROOT.TF1("threeSLine","1.34989803163009588e-03",0.75,4.050);
 threeSLine.SetLineColor(ROOT.kRed); threeSLine.SetLineWidth(2); threeSLine.SetLineStyle(3);
 fourSLine = ROOT.TF1("fourSLine","3.16712418331199785e-05",0.75,4.050);
 fourSLine.SetLineColor(ROOT.kRed); fourSLine.SetLineWidth(2); fourSLine.SetLineStyle(3);

 ban1s = TLatex(3.8,1.58655253931457074e-01,("1 #sigma"));
 ban1s.SetTextSize(0.028); ban1s.SetTextColor(2)
 ban2s = TLatex(3.8,2.27501319481792155e-02,("2 #sigma"));
 ban2s.SetTextSize(0.028); ban2s.SetTextColor(2)
 ban3s = TLatex(3.8,1.34989803163009588e-03,("3 #sigma"));
 ban3s.SetTextSize(0.028); ban3s.SetTextColor(2);
 ban4s = TLatex(3.8,3.16712418331199785e-05,("4 #sigma"));
 ban4s.SetTextSize(0.028); ban4s.SetTextColor(2)

 leg2 = ROOT.TLegend(0.4966443,0.2325581,0.8926174,0.3239203)
 leg2.SetBorderSize(0);
 leg2.SetTextSize(0.031);
 leg2.SetLineColor(1);
 leg2.SetLineStyle(1);
 leg2.SetShadowColor(0);
 leg2.SetLineWidth(1);
 leg2.SetFillColor(0);
 leg2.SetTextFont(42)
 leg2.AddEntry( gr_pvalue_obs, "Observed significance", "pl" );
 leg2.AddEntry( gr_pvalue_exp, "Expected significance", "l" );

 pt = ROOT.TPaveText(0.5486577,0.8355482,0.8993289,0.8920266,"NDC")
 pt.SetTextFont(42)
 pt.SetTextSize(0.031)
 pt.SetTextAlign(32)
 pt.SetFillColor(0)
 pt.SetBorderSize(0)
 pt.SetFillStyle(0)
 text = pt.AddText(names[label])
 text.SetTextFont(62)
  
 gr_pvalue_exp.Draw("L")
 gr_pvalue_obs.Draw("LP") 
 oneSLine.Draw("same");
 twoSLine.Draw("same");
 threeSLine.Draw("same");
 fourSLine.Draw("same");
 ban1s.Draw();
 ban2s.Draw();
 ban3s.Draw();
 ban4s.Draw();
 leg2.Draw()
 pt.Draw()

 canv.Update()   
 canv.cd()
 
 period = 4
 if "138" in label: period = 7
 if "8" in label and not "13" in label: period = 2

 CMS_lumi.CMS_lumi(canv, period,11)	      
 canv.cd()
 canv.Update()
 canv.RedrawAxis()
 canv.RedrawAxis("g")
 frame = canv.GetFrame()
 frame.Draw() 
 canv.cd()
 canv.Update()
 
 canv.SaveAs("plots/EXOVVhvt_"+label+"_Significance.root")
 canv.SaveAs("plots/EXOVVhvt_"+label+"_Significance.png")
 canv.SaveAs("plots/EXOVVhvt_"+label+"_Significance.pdf")
 canv.SaveAs("plots/EXOVVhvt_"+label+"_Significance.eps")
     
def compare_significance(labels):
 
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
 legs1["JJLVJHVT13"]=[0.48,0.32,0.90,0.41]
 legs1["JJLVJWPRIME13"]=[0.48,0.32,0.90,0.41]
 legs1["JJLVJZPRIME13"]=[0.48,0.32,0.90,0.41]
 legs1["ALLWVHVT8"]=[0.48,0.28,0.90,0.41]
 legs1["ALLWVWPRIME8"]=[0.48,0.28,0.90,0.41]
 legs1["ALLWVZPRIME8"]=[0.48,0.28,0.90,0.41]
 legs1["ALLWVHVT138"]=[0.48,0.32,0.90,0.41]
 legs1["ALLWVWPRIME138"]=[0.48,0.32,0.90,0.41]
 legs1["ALLWVZPRIME138"]=[0.48,0.32,0.90,0.41]
 legs1["ALLHVHVT8"]=[0.48,0.32,0.90,0.41]
 legs1["ALLHVWPRIME8"]=[0.48,0.32,0.90,0.41]
 legs1["ALLHVZPRIME8"]=[0.48,0.32,0.90,0.41]
 legs1["ALLHVT8"]=[0.48,0.32,0.90,0.41]
 legs1["ALLWPRIME8"]=[0.48,0.32,0.90,0.41]
 legs1["ALLZPRIME8"]=[0.48,0.32,0.90,0.41]
 legs1["ALLHVT138"]=[0.48,0.32,0.90,0.41]
 legs1["ALLWPRIME138"]=[0.48,0.32,0.90,0.41]
 legs1["ALLZPRIME138"]=[0.48,0.32,0.90,0.41]
    
 legs2={}
 legs2["JJLVJHVT13"]=[0.41,0.26,0.88,0.31]
 legs2["JJLVJWPRIME13"]=[0.41,0.26,0.88,0.31]
 legs2["JJLVJZPRIME13"]=[0.41,0.26,0.88,0.31]
 legs2["ALLWVHVT8"]=[0.41,0.19,0.84,0.27]
 legs2["ALLWVWPRIME8"]=[0.41,0.19,0.84,0.27]
 legs2["ALLWVZPRIME8"]=[0.41,0.19,0.84,0.27]
 legs2["ALLWVHVT138"]=[0.41,0.22,0.88,0.31]
 legs2["ALLWVWPRIME138"]=[0.41,0.22,0.88,0.31]
 legs2["ALLWVZPRIME138"]=[0.41,0.22,0.88,0.31]
 legs2["ALLHVHVT8"]=[0.38,0.21,0.88,0.31]
 legs2["ALLHVWPRIME8"]=[0.38,0.21,0.88,0.31]
 legs2["ALLHVZPRIME8"]=[0.38,0.21,0.88,0.31]
 legs2["ALLHVT8"]=[0.41,0.21,0.88,0.31]
 legs2["ALLWPRIME8"]=[0.41,0.21,0.88,0.31]
 legs2["ALLZPRIME8"]=[0.41,0.21,0.88,0.31]
 legs2["ALLHVT138"]=[0.34,0.18,0.85,0.31]
 legs2["ALLWPRIME138"]=[0.34,0.18,0.85,0.31]
 legs2["ALLZPRIME138"]=[0.34,0.18,0.85,0.31]
      
 files = []
 canvas = []
 graphexp = []
 graphobs = []
   
 files=[TFile.Open("plots/EXOVVhvt_"+l+"_Significance.root") for l in labels]
 canvas=[f.Get("c_Significance") for f in files]
 
 for c in range(len(canvas)):
  for p in canvas[c].GetListOfPrimitives():
   if str(p).find("Observed") != -1: graphobs.append(p.Clone("graphObs_%s"%labels[c])) 
   if str(p).find("Expected") != -1: graphexp.append(p.Clone("graphExp_%s"%labels[c]))

 for g in range(len(graphexp)):
  graphexp[g].SetMarkerColor(mcol[labels[g]])
  graphexp[g].SetLineColor(lcol[labels[g]])
  graphexp[g].SetMarkerStyle(msty[labels[g]])
  graphobs[g].SetMarkerColor(mcol[labels[g]])
  graphobs[g].SetLineColor(lcol[labels[g]])
  graphobs[g].SetLineWidth(1)
  graphexp[g].SetLineWidth(1)
  graphobs[g].SetMarkerStyle(msty[labels[g]])
  graphobs[g].SetMarkerSize(0.9)
  if g == 0:
   graphobs[g].SetLineWidth(2)
   graphexp[g].SetLineWidth(2)
   
 leg = ROOT.TLegend(legs1[labels[0]][0],legs1[labels[0]][1],legs1[labels[0]][2],legs1[labels[0]][3])
 leg.SetBorderSize(0)
 leg.SetTextSize(0.031)
 leg.SetLineColor(1)
 leg.SetLineStyle(1)
 leg.SetShadowColor(0)
 leg.SetLineWidth(1)
 leg.SetFillColor(0)
 leg.SetTextFont(42)

 leg2 = ROOT.TLegend(legs2[labels[0]][0],legs2[labels[0]][1],legs2[labels[0]][2],legs2[labels[0]][3])
 leg2.SetBorderSize(0)
 leg2.SetTextSize(0.026)
 leg2.SetLineColor(1)
 leg2.SetLineStyle(1)
 leg2.SetShadowColor(0)
 leg2.SetLineWidth(1)
 leg2.SetFillColor(0)
 leg2.SetTextFont(42)
 leg2.SetNColumns(2)
 leg2.SetTextSize(0.031)
 
 pt = ROOT.TPaveText(0.5486577,0.8438538,0.8993289,0.9003322,"NDC")
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
       
 canv = get_canvas("c_Significance_compare",lumi8,lumi13)
 canv.cd()

 npoints = graphobs[0].GetN()
 x = ROOT.Double(0.)
 y = ROOT.Double(0.)
 graphobs[0].GetPoint(npoints-1,x,y)
  
 hrl_SM = canv.DrawFrame(0.75,0.00001, x+0.050, 3) 
 ytitle = "p-value"
 hrl_SM.GetYaxis().SetTitle(ytitle)
 hrl_SM.GetYaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitle("M_{"+signal[labels[0]]+"} (TeV)")

 leg.AddEntry(graphobs[0],"Observed significance","LP")
 leg.AddEntry(graphobs[0],"Expected significance","L")
 for g in range(1,len(graphobs)): leg2.AddEntry(graphobs[g],names[labels[g]],"LP")   
 for g in range(0,len(graphobs)):
  graphobs[g].Draw("LPsame")
  graphexp[g].Draw("Lsame")

 oneSLine = ROOT.TF1("oneSLine","1.58655253931457074e-01",0.75,4.050);
 oneSLine.SetLineColor(ROOT.kRed); oneSLine.SetLineWidth(2); oneSLine.SetLineStyle(3);
 twoSLine = ROOT.TF1("twoSLine","2.27501319481792155e-02",0.75,4.050);
 twoSLine.SetLineColor(ROOT.kRed); twoSLine.SetLineWidth(2); twoSLine.SetLineStyle(3);
 threeSLine = ROOT.TF1("threeSLine","1.34989803163009588e-03",0.75,4.050);
 threeSLine.SetLineColor(ROOT.kRed); threeSLine.SetLineWidth(2); threeSLine.SetLineStyle(3);
 fourSLine = ROOT.TF1("fourSLine","3.16712418331199785e-05",0.75,4.050);
 fourSLine.SetLineColor(ROOT.kRed); fourSLine.SetLineWidth(2); fourSLine.SetLineStyle(3);

 ban1s = TLatex(3.8,1.58655253931457074e-01,("1 #sigma"));
 ban1s.SetTextSize(0.028); ban1s.SetTextColor(2)
 ban2s = TLatex(3.8,2.27501319481792155e-02,("2 #sigma"));
 ban2s.SetTextSize(0.028); ban2s.SetTextColor(2)
 ban3s = TLatex(3.8,1.34989803163009588e-03,("3 #sigma"));
 ban3s.SetTextSize(0.028); ban3s.SetTextColor(2);
 ban4s = TLatex(3.8,3.16712418331199785e-05,("4 #sigma"));
 ban4s.SetTextSize(0.028); ban4s.SetTextColor(2)
   
 leg.Draw()
 leg2.Draw()
 pt.Draw()
 oneSLine.Draw("same");
 twoSLine.Draw("same");
 threeSLine.Draw("same");
 fourSLine.Draw("same");
 ban1s.Draw();
 ban2s.Draw();
 ban3s.Draw();
 ban4s.Draw();
    
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
 frame = canv.GetFrame()
 frame.Draw()	
 canv.cd()
 canv.Update()
        
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_Significance.root")
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_Significance.png")
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_Significance.pdf")
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_Significance.eps")
                    
#************************************************************************************************
if __name__ == '__main__':

 gROOT.SetBatch(ROOT.kTRUE)
 
 scenarios={}
 
 # 13 TeV LVJ+JJ only
 scenarios["JJLVJHVT13TeV"]=["JJLVJHVT13","jjwv13","lvjwv13"]
 scenarios["JJLVJWPRIME13TeV"]=["JJLVJWPRIME13","jjwz13","lvjwz13"]
 scenarios["JJLVJZPRIME13TeV"]=["JJLVJZPRIME13","jjww13","lvjww13"]
 
 # 8 TeV LLJ+LVJ+JJ (WV) only
 scenarios["ALLWVHVT8TeV"]=["ALLWVHVT8","lvjwv8","lljwz8","jjwv8"]
 scenarios["ALLWVWPRIME8TeV"]=["ALLWVWPRIME8","lvjwz8","lljwz8","jjwz8"]
 scenarios["ALLWVZPRIME8TeV"]=["ALLWVZPRIME8","lvjww8","jjww8"]
 
 # 8 + 13 TeV LLJ+LVJ+JJ (WV)
 scenarios["ALLWVHVT138TeV"]=["ALLWVHVT138","lvjwv8","lljwz8","jjwv8","jjwv13","lvjwv13"]
 scenarios["ALLWVWPRIME138TeV"]=["ALLWVWPRIME138","lvjwz8","lljwz8","jjwz8","jjwz13","lvjwz13"]
 scenarios["ALLWVZPRIME138TeV"]=["ALLWVZPRIME138","lvjww8","jjww8","jjww13","lvjww13"]

 #8 TeV VH only
 scenarios["ALLHVHVT8TeV"]=["ALLHVHVT8","ttjvh8","jjvh8","lvjwh8"]
 scenarios["ALLHVWPRIME8TeV"]=["ALLHVWPRIME8","ttjwh8","jjwh8","lvjwh8"]
 scenarios["ALLHVZPRIME8TeV"]=["ALLHVZPRIME8","ttjzh8","jjzh8"]

 #8 TeV VH+WV
 scenarios["ALLHVT8TeV"]=["ALLHVT8","ttjvh8","jjvh8","lvjwh8","lvjwv8","lljwz8","jjwv8"]
 scenarios["ALLWPRIME8TeV"]=["ALLWPRIME8","ttjwh8","jjwh8","lvjwh8","lvjwz8","lljwz8","jjwz8"]
 scenarios["ALLZPRIME8TeV"]=["ALLZPRIME8","ttjzh8","jjzh8","lvjww8","jjww8"]

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
  plot_significance(name)

 compare_significance(scenarios[sys.argv[1]])

