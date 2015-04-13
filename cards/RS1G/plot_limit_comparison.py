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
 scenarios["ALL8TeV"]=["ALL","xww","xzz","xjj8"]
 scenarios["JJ813TeV"]=["JJ813","xjj8","xjj13"]
 scenarios["WW813TeV"]=["WW813","xww","xww13"]
 scenarios["ALL813TeV"]=["ALL813","ALL","ALL13"]
 scenarios["ALL13TeV"]=["ALL13","xww13","xjj13"]
 names={}
 names["ALL"]="lvJ, llJ, JJ (8 TeV)"
 names["xww"]="lvJ (8 TeV)"
 names["xjj8"]="JJ (8 TeV)"
 names["xzz"]="llJ (8 TeV)"
 names["JJ813"]="JJ (8+13 TeV)"
 names["xjj13"]="JJ (13 TeV)"
 names["WW813"]="lvJ (8+13 TeV)"
 names["xww13"]="lvJ (13 TeV)"
 names["ALL813"]="lvJ, llJ, JJ (8+13 TeV)"
 names["ALL13"]="lvJ, llJ, JJ (13 TeV)"
 colors=[4,6,7,8,9]
 styles=[3,4,5,6,7]
 fillstyles=[3007,3007,3007,3007]
 for scenario in scenarios.keys():
  files=[]
  canvas=[]
  graph=[]
  for name in scenarios[scenario]:
    files+=[TFile.Open("EXOVV_"+name+"_UL_Asymptotic.root")]
    canvas+=[files[-1].Get("c_lim_Asymptotic")]
    print [a for a in canvas[-1].GetListOfPrimitives()]
    graph+=[[a for a in canvas[-1].GetListOfPrimitives() if "Limit68CLs" in str(a)][0].Clone("graph_"+name)]
    if len(files)==1:
      l1=[a for a in canvas[-1].GetListOfPrimitives() if "TLegend" in str(a)][0]
      #print [a for a in l1.GetListOfPrimitives()]
      #l1.GetListOfPrimitives().Remove(l1.GetListOfPrimitives()[-1])
      canvas[-1].SetLogy()
      canvas[-1].Draw()
      l1.AddEntry(graph[-1],names[name],"lf")
    else:
      graph[-1].SetLineColor(colors[len(files)-2])
      graph[-1].SetLineStyle(styles[len(files)-2])
      graph[-1].SetFillColor(colors[len(files)-2])
      graph[-1].SetFillStyle(fillstyles[len(files)-2])
      #print graph[-1].GetErrorY(1)
      canvas[0].cd()
      graph[-1].Draw("L3")
      l1.AddEntry(graph[-1],names[name],"lf")
      #canvas[0].Update()
  canvas[0].SaveAs("EXOVV_compare_"+scenario+"_UL_Asymptotic.pdf")
