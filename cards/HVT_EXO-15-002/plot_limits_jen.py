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

def get_canvas(cname):

   tdrstyle.setTDRStyle()
   CMS_lumi.lumi_13TeV = "2.2 fb^{-1}"
   CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
   CMS_lumi.writeExtraText = 1
   CMS_lumi.extraText = "Preliminary"
   CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
   iPos = 11
   if( iPos==0 ): CMS_lumi.relPosX = 0.12
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
   canvas.SetTopMargin( T/H )
   canvas.SetBottomMargin( B/H+0.03 )
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

 infile = "higgsCombine%s.Asymptotic.TOTAL.root"%label
 mass = [700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,
         2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,
	 3600,3700,3800,3900,4000]
 signal = {}
 signal['JJLVJHVT13'] = "V'"
 signal['ALLHVT138'] = "V'"
 signal['jjwv8'] = "V'"
 signal['lvjwv8'] = "V'"
 signal['lvjwv13'] = "V'"
 signal['lljwz8'] = "W'"
 signal['lvjwz13'] = "W'"	
 signal['lvjww13'] = "Z'"
 signal['jjwv13'] = "V'"
 signal['jjwz13'] = "W'"	
 signal['jjww13'] = "Z'"
 decay = {}
 decay['JJLVJHVT13'] = "WV"
 decay['ALLHVT138'] = "WV"
 decay['jjwv8'] = "WV"
 decay['lvjwv8'] = "WV"
 decay['lvjwv13'] = "WV"
 decay['lljwz8'] = "WZ"
 decay['lvjwz13'] = "WZ"
 decay['lvjww13'] = "WW"
 decay['jjwv13'] = "WV"
 decay['jjwz13'] = "WZ"
 decay['jjww13'] = "WW"

 names = {}
 names["JJLVJHVT13"]="lvJ, JJ (13 TeV)"
 names["ALLHVT138"]="lvJ, JJ (8+13 TeV)"
 names["ALLHVT138"]="lvJ, llJ, JJ (8+13 TeV)"
 names["lvjwv8"]="lvJ (8 TeV)"
 names["lljwz8"]="llJ (8 TeV)"
 names["jjwv8"]="JJ (8 TeV)"
 names["lvjwv13"]="lvJ (13 TeV)"
 names["jjwv13"]="JJ (13 TeV)"
 names["jjww13"]="JJ Z'(13 TeV)"
 names["jjwz13"]="JJ W' (13 TeV)"
 names["lvjww13"]="lvJ Z' (13 TeV)"
 names["lvjwz13"]="lvJ W' (13 TeV)"
 
 thMap13 = get_theo_map("13")
 xsecMap13 = thMap13[0]
 massMap13 = thMap13[1]
 thMap8 = get_theo_map("8")
 xsecMap8 = thMap8[0]
 massMap8 = thMap8[1]
 	     
 scale = {}
 scale['JJLVJHVT13'] = {}
 scale['ALLHVT138'] = {}
 scale['jjwv8'] = {}
 scale['lvjwv8'] = {}
 scale['lljwz8'] = {}
 scale['lvjwv13'] = {}
 scale['lvjwz13'] = {}
 scale['lvjww13'] = {}	     
 scale['jjwv13'] = {}
 scale['jjwz13'] = {}
 scale['jjww13'] = {}
 for m in mass:
   idx = int((m-800)/100)
   idx2 = int((m-745)/5)
   if signalstrenght:
    scale['JJLVJHVT13'][m] = 1
    scale['ALLHVT138'][m] = 1
    scale['lvjwv8'][m] = 1
    scale['lljwz8'][m] = 1
    scale['jjwv8'][m] = 1
    scale['lvjwv13'][m] = 1
    scale['lvjwz13'][m] = 1
    scale['lvjww13'][m] = 1
    scale['jjwv13'][m] = 1
    scale['jjwz13'][m] = 1
    scale['jjww13'][m] = 1
   else: 
    scale['JJLVJHVT13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['lvjwv13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['lvjwz13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]#(xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx]
    scale['lvjww13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]#xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['jjwv13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['jjwz13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]#(xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx]
    scale['jjww13'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]#xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    scale['ALLHVT138'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]#((xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx])+((xsecMap8['CX-(pb)'][idx]+xsecMap8['CX+(pb)'][idx])*xsecMap8['BRZW'][idx] + xsecMap8['CX0(pb)'][idx]*xsecMap8['BRWW'][idx])
    
    if m <= 3000:
     scale['lljwz8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2]
     scale['lvjwv8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2]
     scale['jjwv8'][m] = (xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2]
     scale['ALLHVT138'][m] = ((xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx])+((xsecMap8['CX-(pb)'][idx2]+xsecMap8['CX+(pb)'][idx2])*xsecMap8['BRZW'][idx2] + xsecMap8['CX0(pb)'][idx2]*xsecMap8['BRWW'][idx2])
    else:
     scale['lljwz8'][m] = 1
     scale['lvjwv8'][m] = 1
     scale['jjwv8'][m] = 1
     scale['ALLHVT138'][m] = (xsecMap13['CX-(pb)'][idx]+xsecMap13['CX+(pb)'][idx])*xsecMap13['BRZW'][idx] + xsecMap13['CX0(pb)'][idx]*xsecMap13['BRWW'][idx]
    
 nPoints = 0

 xbins	   = array('d', [])
 xbins_env = array('d', [])
 ybins_exp = array('d', [])
 ybins_obs = array('d', [])
 ybins_1s  = array('d', [])
 ybins_2s  = array('d', [])
 ybins_xs  = array('d', [])

 #br = 0.322*0.6760    
 for m in mass:

  curAsymLimits = getAsymLimits(infile,m);
  if curAsymLimits[0] == -1: continue
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

 canv = get_canvas("c_lim_Asymptotic")
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

 hrl_SM = canv.DrawFrame(0.75,1e-03, 4.050, 100)
 if signalstrenght: hrl_SM = canv.DrawFrame(0.75,0.01, 4.050, 100) 
 
 ytitle = "#sigma_{95%} #times BR_{"+signal[label]+"#rightarrow "+decay[label]+"} (pb)"
 hrl_SM.GetYaxis().SetTitle(ytitle)
 hrl_SM.GetYaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitle("M_{"+signal[label]+"} (GeV)")
 #hrl_SM.SetMinimum(0.0001)
 #hrl_SM.SetMaximum(100)
 #hrl_SM.GetYaxis().SetNdivisions(505)
     
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
 
 CMS_lumi.CMS_lumi(canv, period,11)   	
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
 lcol["ALLHVT138"] = kBlack
 lcol["lvjwv13"] = kBlack
 lcol["lvjwz13"] = kMagenta
 lcol["lvjww13"] = kBlue
 lcol["jjwv13"] = kBlack
 lcol["jjwz13"] = kMagenta
 lcol["jjww13"] = kBlue
 if "JJLVJ" in labels[0] or "ALL" in labels[0]:
  lcol["lvjwv13"] = 4#kMagenta
  lcol["jjwv13"] = 6#kBlue
  lcol["lvjwv8"] = 11#210
  lcol["jjwv8"] = 28#kBlue-9
  lcol["lljwz8"] = 8#kOrange
 #marker color
 mcol = {}
 mcol["JJLVJHVT13"] = kBlack
 mcol["ALLHVT138"] = kBlack
 mcol["lvjwv13"] = kBlack
 mcol["lvjwz13"] = kMagenta
 mcol["lvjww13"] = kBlue  
 mcol["jjwv13"] = kBlack
 mcol["jjwz13"] = kMagenta
 mcol["jjww13"] = kBlue  
 if "JJLVJ" in labels[0] or "ALL" in labels[0]:
  mcol["lvjwv13"] = 4#kMagenta
  mcol["jjwv13"] = 6#kBlue
  mcol["lvjwv8"] = 11#210
  mcol["jjwv8"] = 28#kBlue-9
  mcol["lljwz8"] = 8#kOrange
 #marker style
 msty = {}
 msty["JJLVJHVT13"] = 20
 msty["ALLHVT138"] = 20
 msty["lvjwv13"] = 20
 msty["lvjwz13"] = 23
 msty["lvjww13"] = 32
 msty["jjwv13"] = 20
 msty["jjwz13"] = 23
 msty["jjww13"] = 32
 if "JJLVJ" in labels[0] or "ALL" in labels[0]:
  msty["lvjwv13"] = 20
  msty["jjwv13"] = 22
  msty["lvjwv8"] = 24
  msty["jjwv8"] = 25
  msty["lljwz8"] = 26
   
 signal = {}
 signal['JJLVJHVT13'] = "V'"
 signal['ALLHVT138'] = "V'"
 signal['lvjwv13'] = "V'"
 signal['lvjwz13'] = "W'"	
 signal['lvjww13'] = "Z'"
 signal['jjwv13'] = "V'"
 signal['jjwz13'] = "W'"	
 signal['jjww13'] = "Z'"
 decay = {}
 decay['JJLVJHVT13'] = "WV"
 decay['ALLHVT138'] = "WV"
 decay['lvjwv13'] = "WV"
 decay['lvjwz13'] = "WZ"
 decay['lvjww13'] = "WW"
 decay['jjwv13'] = "WV"
 decay['jjwz13'] = "WZ"
 decay['jjww13'] = "WW"
 
 names = {}
 names["JJLVJHVT13"]="lvJ, JJ (13 TeV)"
 names["ALLHVT138"]="lvJ, llJ, JJ (8+13 TeV)"
 names["lvjwv8"]="lvJ (8 TeV)"
 names["lljwz8"]="llJ (8 TeV)"
 names["jjwv8"]="JJ (8 TeV)"
 names["lvjwv13"]="lvJ (13 TeV)"
 names["jjwv13"]="JJ (13 TeV)"
 names["jjww13"]="JJ Z'(13 TeV)"
 names["jjwz13"]="JJ W' (13 TeV)"
 names["lvjww13"]="lvJ Z' (13 TeV)"
 names["lvjwz13"]="lvJ W' (13 TeV)"
    
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
  graphobs[g].SetMarkerColor(mcol[labels[g]])
  graphobs[g].SetLineColor(lcol[labels[g]])
  graphobs[g].SetMarkerStyle(msty[labels[g]])
  graphobs[g].SetMarkerSize(0.9)
  if g != 0:
   graphobs[g].SetLineWidth(2)
   graphexp[g].SetLineWidth(2)
   
 leg = ROOT.TLegend(0.3808725,0.2026578,0.8959732,0.4169435)#0.3724832,0.4933555,0.8875839,0.872093
 if not bands: leg = ROOT.TLegend(0.4211409,0.3654485,0.8724832,0.4518272)
 leg.SetBorderSize(0)
 leg.SetTextSize(0.031)
 leg.SetLineColor(1)
 leg.SetLineStyle(1)
 leg.SetShadowColor(0)
 leg.SetLineWidth(1)
 leg.SetFillColor(0)
 leg.SetTextFont(42)

 leg2 = ROOT.TLegend(0.4345638,0.2059801,0.8758389,0.3239203)
 if bands: leg2 = ROOT.TLegend(0.1694631,0.6312292,0.340604,0.7774086)
 leg2.SetBorderSize(0)
 leg2.SetTextSize(0.026)
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
     
 canv = get_canvas("c_lim_Asymptotic_compare")
 canv.cd()
  
 hrl_SM = canv.DrawFrame(0.75,1e-03, 4.050, 100) 
 if "138" in labels[0]: hrl_SM = canv.DrawFrame(0.75,0.01, 4.050, 100) 
 #grtmp = ROOT.TGraph(1,array('d',[0]),array('d',[0]))
 #grtmp.SetLineColor(kWhite)
 #grtmp.SetMarkerColor(kWhite)
 #grtmp.SetMarkerSize(0)
 #leg.AddEntry(grtmp,names[labels[0]],"LP") 
    
 if not unblind:  
  leg.AddEntry(graphobs[0],"Asympt. CL_{S} Observed","LP")
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
  graphexp[0].Draw("L")
  leg.AddEntry(graphexp[0],"Asympt. CL_{S} Expected","L")
  for c in range(1,len(graphexp)):
   leg2.AddEntry(graphexp[c],names[labels[c]],"L")
   graphexp[c].Draw("L")

 graphth[0].Draw("Lsame")
 theoleg = "#sigma_{TH} #times BR_{"+signal[labels[0]]+"#rightarrow "+decay[labels[0]]+"} , HVT_{B}"
 leg.AddEntry(graphth[0],theoleg,"L") 

 ytitle = "#sigma_{95%} #times BR_{"+signal[labels[0]]+"#rightarrow "+decay[labels[0]]+"} (pb)"
 if "138" in labels[0]: ytitle = "#sigma_{95%}/#sigma_{theory}"
 hrl_SM.GetYaxis().SetTitle(ytitle)
 hrl_SM.GetYaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitle("M_{"+signal[labels[0]]+"} (GeV)")
 hrl_SM.GetXaxis().SetNdivisions(505)
         
 canv.Update()   
 canv.cd()
 
 period = 4
 if "138" in labels[0]: period = 7
 if "8" in labels[0] and not "13" in labels[0]: period = 2
 CMS_lumi.CMS_lumi(canv, period,11) 
  	
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
 if unblind: suffix = "expected"
 if bands: suffix = "bands"
 
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_"+suffix+".root")
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_"+suffix+".png")
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_"+suffix+".pdf")
 canv.SaveAs("plots/EXOVVhvt_compare_"+labels[0]+"_"+suffix+".eps")
    
#************************************************************************************************
if __name__ == '__main__':

 gROOT.SetBatch(ROOT.kTRUE)
 scenarios={}
 scenarios["LVJHVT13TeV"]=["lvjwv13","lvjwz13","lvjww13"]
 scenarios["JJHVT13TeV"]=["jjwv13","jjwz13","jjww13"]
 scenarios["JJLVJHVT13TeV"]=["JJLVJHVT13","jjwv13","lvjwv13"]
 scenarios["ALLHVT138TeV"]=["ALLHVT138","lvjwv8","lljwz8","jjwv8","jjwv13","lvjwv13"]
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

 compare_Asympt_limits(scenarios[sys.argv[1]],False,False)
 compare_Asympt_limits(scenarios[sys.argv[1]],False,True)
 compare_Asympt_limits(scenarios[sys.argv[1]],True,False) 

 for name in scenarios[sys.argv[1]]:
  print name
  plot_Asympt_limits(name,False)
  #if "138" in name: plot_Asympt_limits(name,True)
  #else: plot_Asympt_limits(name,False)
