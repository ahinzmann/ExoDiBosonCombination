from ROOT import *

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
 scenarios["ALL8TeV"]=["ALL_UL_Asymptotic","xzh_UL_Asymptotic","xvh_UL_Asymptotic","xwh_UL_Asymptotic"]
 scenarios["ALL8TeVfullCLs"]=["ALL_UL_HybridNew","xzh_UL_HybridNew","xvh_UL_HybridNew","xwh_UL_HybridNew"]
 names={}
 names["ALL"]="lvbb, qq#tau#tau, qqbb, qqqqqq (8 TeV)"
 names["SEMILEPT"]="lvbb, qq#tau#tau (8 TeV)"
 names["xvh"]="qqbb, qqqqqq (8 TeV)"
 names["xwh"]="lvbb (8 TeV)"
 names["xzh"]="qq#tau#tau (8 TeV)"
 colors=[4,6,7,8,9]
 styles=[3,4,5,6,7]
 fillstyles=[3007,3007,3007,3007]
 markerstyles=[20,22,23,24]
 for scenario in scenarios.keys():
  files=[]
  canvas=[]
  graph=[]
  graphobs=[]
  for name in scenarios[scenario]:
    print name
    shortname=name.replace("_UL_Asymptotic","").replace("_UL_HybridNew","").replace("ZH","xzh").replace("VH","xvh").replace("WH","xwh")
    files+=[TFile.Open("EXOVH_"+name+".root")]
    if "HybridNew" in name:
      canvas+=[files[-1].Get("c_lim_HybridNew")]
    else:
      canvas+=[files[-1].Get("c_lim_Asymptotic")]
    print [a for a in canvas[-1].GetListOfPrimitives()]
    graph+=[[a for a in canvas[-1].GetListOfPrimitives() if "Limit68CLs" in str(a)][0].Clone("graph_"+name)]
    graphobs+=[[a for a in canvas[-1].GetListOfPrimitives() if "LimitObservedCLs" in str(a)][0].Clone("graph_"+name)]
    if len(files)==1:
      l1=[a for a in canvas[-1].GetListOfPrimitives() if "TLegend" in str(a)][0]
      #print [a for a in l1.GetListOfPrimitives()]
      #l1.GetListOfPrimitives().Remove(l1.GetListOfPrimitives()[-1])
      canvas[-1].SetLogy()
      canvas[-1].Draw()
      l1.AddEntry(graphobs[-1],names[shortname],"")
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
      #graph[-1].Draw("L5")
      l1.AddEntry(graphobs[-1],names[shortname],"lp")
      #canvas[0].Update()
    #graph[0].Draw("LX")
    graphobs[0].Draw("LP")
    l1.Draw()
  canvas[0].SaveAs("EXOVH_compare_"+scenario+".pdf")
