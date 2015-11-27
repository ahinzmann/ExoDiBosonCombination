from ROOT import *
import os

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
 scenarios={}
 scenarios["WW813TeV"]=["WW813_UL_Asymptotic","xww_UL_Asymptotic","xww13_UL_Asymptotic"]
 names={}
 names["ALL"]="lvJ, llJ, JJ (8 TeV)"
 names["WW813"]="lvJ (8+13 TeV)"
 names["xww"]="lvJ (8 TeV)"
 names["xzz"]="llJ (8 TeV)"
 names["xjj"]="JJ (8 TeV)"
 names["xww13"]="lvJ (13 TeV)"
 
 for name in names.keys():
   os.system('root -b -q plot_golfcourse_Asymptotic.C\(true,0,\\"'+name+'\\"\)')
 
 colors=[4,6,11,28,8,9]
 styles=[3,4,5,6,7,8,9]
 fillstyles=[3007,3007,3007,3007,3007,3007,3007]
 markerstyles=[20,22,23,24,25,26,27,28]
 for scenario in scenarios.keys():
  files=[]
  canvas=[]
  graph=[]
  graphobs=[]
  for name in scenarios[scenario]:
    print name
    shortname=name.replace("_UL_Asymptotic","").replace("_UL_HybridNew","")
    files+=[TFile.Open("EXOVVwprime_"+name+".root")]
    if "HybridNew" in name:
      canvas+=[files[-1].Get("c_lim_HybridNew")]
    else:
      canvas+=[files[-1].Get("c_lim_Asymptotic")]
    print [a for a in canvas[-1].GetListOfPrimitives()]
    graph+=[[a for a in canvas[-1].GetListOfPrimitives() if "Limit68CLs" in str(a)][0].Clone("graph_"+name)]
    graphobs+=[[a for a in canvas[-1].GetListOfPrimitives() if "LimitObservedCLs" in str(a)][0].Clone("graph_"+name)]
    #canvas[-1].GetListOfPrimitives().Remove([a for a in canvas[-1].GetListOfPrimitives() if "Limit95CLs" in str(a)][0])
    #canvas[-1].GetListOfPrimitives().Remove([a for a in canvas[-1].GetListOfPrimitives() if "Limit68CLs" in str(a)][0])
    #canvas[-1].GetListOfPrimitives().Remove([a for a in canvas[-1].GetListOfPrimitives() if "LimitObservedCLs" in str(a)][0])
    if len(files)==1:
      l1=[a for a in canvas[-1].GetListOfPrimitives() if "TLegend" in str(a)][0]
      #print [a for a in l1.GetListOfPrimitives()]
      legendcontent=[a for a in l1.GetListOfPrimitives()]
      for l in legendcontent:
        l1.GetListOfPrimitives().Remove(l)
      #legendcontent=legendcontent[1:2]+legendcontent[3:]
      canvas[-1].SetLogy()
      canvas[-1].Draw()
      l1.AddEntry(graphobs[-1],names[shortname],"")
      for l in legendcontent[:-1]:
        l1.AddEntry(l.GetObject(),l.GetLabel().replace("Frequentist ",""),l.GetOption())
      l1.AddEntry(graph[-1],names[shortname],"lp")
    else:
      graphobs[-1].SetMarkerColor(colors[len(files)-2])
      graphobs[-1].SetMarkerStyle(markerstyles[len(files)-2])
      graphobs[-1].SetLineColor(colors[len(files)-2])
      #graphobs[-1].SetLineStyle(styles[len(files)-2])
      graph[-1].SetLineColor(colors[len(files)-2])
      graph[-1].SetLineStyle(styles[len(files)-2])
      graph[-1].SetFillColor(colors[len(files)-2])
      graph[-1].SetFillStyle(fillstyles[len(files)-2])
      #print graph[-1].GetErrorY(1)
      canvas[0].cd()
      graphobs[-1].Draw("LP")
      #graph[-1].Draw("LX")
      l1.AddEntry(graphobs[-1],names[shortname]+" CL_{S} Observed","lp")
      #canvas[0].Update()
  graph[0].Draw("LX")
  #graphobs[0].Draw("LP")
  l1.AddEntry(legendcontent[-1].GetObject(),legendcontent[-1].GetLabel(),legendcontent[-1].GetOption())
  l1.Draw()
  canvas[0].SaveAs("EXOVVwprime_compare_"+scenario+"_band.pdf")