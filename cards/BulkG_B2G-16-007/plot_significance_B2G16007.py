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
 
 names = {}
 names["ALL13"]="lvJ, JJ (13 TeV)"
 names["ALL8"]="lvJ, llJ, JJ (8 TeV)"
 names["ALL813"]="lvJ, llJ, JJ (8+13 TeV)"
 names["xww"]="lvqq (8 TeV)"
 names['xzz']="llqq (8 TeV)"
 names["xjj8"]="qqqq (8 TeV)"
 names["xjj13"]="qqqq (13 TeV)"
 names["xww13"]="lvqq (13 TeV)"
  
 infileObs = "results/higgsCombine%sObsSignif.ProfileLikelihood.TOTAL.root"%label
 infileExp = "results/higgsCombine%sExpSignif.ProfileLikelihood.TOTAL.root"%label
 mass = [800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,
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
  #print m,pvalue_obs,RooStats.PValueToSignificance(pvalue_obs)
  ybins_obs.append(pvalue_obs)        
  ybins_exp.append(pvalue_exp)      
  xbins.append(m/1000.)       
  nPoints+=1  

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
 hrl_SM.GetXaxis().SetTitle("M_{G_{bulk}} (TeV)")
      
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
 
 canv.SaveAs("plots/EXOVVbulkg_"+label+"_Significance.root")
 #canv.SaveAs("plots/EXOVVbulkg_"+label+"_Significance.png")
 #canv.SaveAs("plots/EXOVVbulkg_"+label+"_Significance.pdf")
 #canv.SaveAs("plots/EXOVVbulkg_"+label+"_Significance.eps")
     
def compare_significance(labels):
 
 palette = get_palette('gv')
 col = TColor()
  
 #line color
 lcol = {}
 lcol["ALL813"] = kBlack
 lcol["ALL13"] = kBlack
 lcol["ALL8"] = kBlack
 lcol["xww13"] = col.GetColor(palette[10])
 lcol["xjj13"] = col.GetColor(palette[9])
 lcol["xww"] = col.GetColor(palette[2])
 lcol["xjj8"] = col.GetColor(palette[6])
 lcol["xzz"] = col.GetColor(palette[1])
 #marker color
 mcol = {}
 mcol["ALL813"] = kBlack
 mcol["ALL13"] = kBlack
 mcol["ALL8"] = kBlack
 mcol["xww13"] = col.GetColor(palette[10])
 mcol["xjj13"] = col.GetColor(palette[9])
 mcol["xww"] = col.GetColor(palette[2])
 mcol["xjj8"] = col.GetColor(palette[6])
 mcol["xzz"] = col.GetColor(palette[1])  
 #marker style
 msty = {}
 msty["ALL813"] = 20
 msty["ALL13"] = 20
 msty["ALL8"] = 20
 msty["xww13"] = 26
 msty["xjj13"] = 22
 msty["xww"] = 26
 msty["xjj8"] = 22
 msty["xzz"] = 25
     
 names = {}
 names["ALL13"]="lvJ, JJ (13 TeV)"
 names["ALL8"]="lvJ, llJ, JJ (8 TeV)"
 names["ALL813"]="lvJ, llJ, JJ (8+13 TeV)"
 if "813" in labels[0]:
  names["xww"]="lvqq (8 TeV)"
  names['xzz']="llqq (8 TeV)"
  names["xjj8"]="qqqq (8 TeV)"
  names["xjj13"]="qqqq (13 TeV)"
  names["xww13"]="lvqq (13 TeV)"
 else:
  names["xww"]="lvqq"
  names['xzz']="llqq"
  names["xjj8"]="qqqq"
  names["xjj13"]="qqqq"
  names["xww13"]="lvqq"
  
 legs1={}
 legs1["ALL13"]=[0.47,0.37,0.88,0.45]
 legs1["ALL8"]=[0.47,0.48,0.89,0.56]
 legs1["ALL813"]=[0.47,0.37,0.88,0.45]
    
 legs2={}
 legs2["ALL13"]=[0.48,0.26,0.72,0.34]
 legs2["ALL8"]=[0.48,0.34,0.72,0.45]
 legs2["ALL813"]=[0.34,0.22,0.81,0.32]
  
 ncols={}
 ncols["ALL13"] = 1
 ncols["ALL8"] = 1
 ncols["ALL813"] = 2
       
 files = []
 canvas = []
 graphexp = []
 graphobs = []
   
 files=[TFile.Open("plots/EXOVVbulkg_"+l+"_Significance.root") for l in labels]
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
 leg2.SetLineColor(1)
 leg2.SetLineStyle(1)
 leg2.SetShadowColor(0)
 leg2.SetLineWidth(1)
 leg2.SetFillColor(0)
 leg2.SetTextFont(42)
 leg2.SetTextSize(0.031)
 leg2.SetNColumns(ncols[labels[0]])
 
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
  
 hrl_SM = canv.DrawFrame(0.75,0.00001, x+0.050, 1) 
 ytitle = "p-value"
 hrl_SM.GetYaxis().SetTitle(ytitle)
 hrl_SM.GetYaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetTitleSize(0.045)
 hrl_SM.GetXaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetLabelSize(0.035)
 hrl_SM.GetYaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitleOffset(1.1)
 hrl_SM.GetXaxis().SetTitle("M_{G_{bulk}} (TeV)")

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
 #pt.Draw()
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
        
 canv.SaveAs("plots/EXOVVbulkg_compare_"+labels[0]+"_Significance.root")
 canv.SaveAs("plots/EXOVVbulkg_compare_"+labels[0]+"_Significance.png")
 canv.SaveAs("plots/EXOVVbulkg_compare_"+labels[0]+"_Significance.pdf")
 canv.SaveAs("plots/EXOVVbulkg_compare_"+labels[0]+"_Significance.eps")
                    
#************************************************************************************************
if __name__ == '__main__':

 gROOT.SetBatch(ROOT.kTRUE)
 
 scenarios={}
 
 # 13 TeV BulkG
 scenarios["ALL13TeV"]=["ALL13","xww13","xjj13"]

 # 8 TeV BulkG
 scenarios["ALL8TeV"]=["ALL8","xzz","xww","xjj8"]

 # 8+13 TeV BulkG
 scenarios["ALL813TeV"]=["ALL813","xzz","xww13","xww","xjj13","xjj8"]
    
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

