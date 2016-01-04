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

 #masses =[1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900]
 #channels=["JAM13"]
 #masses =[1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3200,3400,3600,3700]
 #channels = ["xww13"]
 #masses =[1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700]
 #channels = ["xjj13ww"]
 #masses =[1300,1400,1600,1900,2000,2100,2200,2300,2400,2500,2700]
 channels = ["xjj13zz"]
 masses =[1200,1300,1400,1500,1600,1800,1900,2000,2100,2200,2300,2400]

 for channel in channels:
  if channel=="JAM13": start=16
  if channel=="xjj13ww": start=7
  if channel=="xww13": start=3
  if channel=="xjj13zz": start=3

  files=["LEE_13TeV_Sig_"+channel+"_toys.txt"]

  colors=[1,2,4,7,6,8,9,10]
  styles=[1,2,3,4,1,2,3,4]

  for f in files:
    print f
    fWW=eval(file(f).readlines()[0].replace("i","-1").replace("n","").replace("f",""))

    xpoints1=array.array('d')
    ypoints1=array.array('d')
    xerrors1=array.array('d')
    yerrors1=array.array('d')
    
    print len(fWW[start][1])
    
    for i in range(2,20):
       x=i*0.25
       ys=[]
       missing_toys={}
       for toy in fWW[start][1].keys():
           ymax=0
           missing_toy=False
           for mass,significances in fWW:
	     if mass in masses:
               try:
        	  ymax=max(ymax,significances[toy])
               except:
	          missing_toy=True
	          if not mass in missing_toys.keys():
		     missing_toys[mass]=1
		  else:
        	     missing_toys[mass]+=1
		  pass
           if not missing_toy:
	       ys+=[ymax]
       print "Missing toys in ",missing_toys
       print "Total toys ",len(ys)
       y=RooStats.PValueToSignificance(float(len([s for s in ys if s>=x]))/len(ys))
       if y>10 or y<-10: continue
       xpoints1.append(x)
       ypoints1.append(y)
       xerrors1.append(0)
       if len([s for s in ys if s>=x])>0:
          yerror=2*(y-RooStats.PValueToSignificance(float(sqrt(len([s for s in ys if s>=x]))+len([s for s in ys if s>=x]))/len(ys)))
       else:
          yerror=y
       yerrors1.append(yerror)
       print x,y,yerror
    
    canvas = TCanvas("","",0,0,200,200)
    
    legend=TLegend(0.3,0.7,0.95,0.90,"")

    hist=TH1F("h","h",9,0.5,5)
    hist.SetTitle("")
    graph1=TGraphErrors(len(xpoints1),xpoints1,ypoints1,xerrors1,yerrors1)
    graph1.SetTitle("")
    graph1.SetLineColor(1)
    graph1.SetLineStyle(1)
    graph1.SetLineWidth(2)
    graph1.SetFillStyle(0)
    graph1.SetMarkerStyle(0)
    hist.GetXaxis().SetTitle("local signficance")
    hist.GetYaxis().SetTitle("global signficance")
    hist.GetYaxis().SetRangeUser(0.5,5)
    hist.Draw("")
    graph1.Draw("same")
    line=TLine(0.5,0.5,5,5)
    line.SetLineColor(2)
    line.Draw("same")
    legend.AddEntry(graph1,channel,"l")

    legend.SetTextSize(0.04)
    legend.SetFillStyle(0)
    #legend.Draw("same")

    canvas.SaveAs(f.replace(".txt",".pdf"))
    canvas.SaveAs(f.replace(".txt",".root"))
