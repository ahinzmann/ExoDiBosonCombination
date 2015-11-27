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
 scenarios["WW813TeV"]=["WW813","xww","xww13"]
 names={}
 names["ALL"]="lvJ, llJ, JJ (8 TeV)"
 names["WW813"]="lvJ (8+13 TeV)"
 names["xww"]="lvJ (8 TeV)"
 names["xzz"]="llJ (8 TeV)"
 names["xjj"]="JJ (8 TeV)"
 names["xww13"]="lvJ (13 TeV)"
 
 for name in names.keys():
   os.system('root -b -q plot_Significance.C\(true,\\"'+name+'\\"\)')
 
 colors=[4,6,11,28,8,9]
 styles=[3,4,5,6,7,8,9]
 fillstyles=[3007,3007,3007,3007,3007,3007,3007]
 for scenario in scenarios.keys():
  files=[]
  canvas=[]
  graph=[]
  graphobs=[]
  for name in scenarios[scenario]:
    files+=[TFile.Open("EXOVVwprime_"+name+"_Significance.root")]
    canvas+=[files[-1].Get("canSig")]
    print [a for a in canvas[-1].GetListOfPrimitives()]
    graph+=[[a for a in canvas[-1].GetListOfPrimitives() if "Graph" in str(a)][0].Clone("graph_"+name)]
    graphobs+=[[a for a in canvas[-1].GetListOfPrimitives() if "Graph" in str(a)][1].Clone("graph_"+name)]
    if len(files)==1:
      l1=[a for a in canvas[-1].GetListOfPrimitives() if "TLegend" in str(a)][0]
      #print [a for a in l1.GetListOfPrimitives()]
      legendcontent=[a for a in l1.GetListOfPrimitives()]
      for l in legendcontent:
        l1.GetListOfPrimitives().Remove(l)
      canvas[-1].SetLogy()
      canvas[-1].Draw()
      l1.AddEntry(graphobs[-1],names[name],"")
      for l in legendcontent:
           l1.AddEntry(l.GetObject(),l.GetLabel(),l.GetOption())
    else:
      graphobs[-1].SetLineWidth(2)
      graphobs[-1].SetMarkerColor(colors[len(files)-2])
      graphobs[-1].SetMarkerStyle(styles[len(files)-2])
      graphobs[-1].SetLineColor(colors[len(files)-2])
      #graphobs[-1].SetLineStyle(styles[len(files)-2])
      graph[-1].SetLineWidth(2)
      graph[-1].SetLineColor(colors[len(files)-2])
      graph[-1].SetLineStyle(styles[len(files)-2])
      graph[-1].SetFillColor(colors[len(files)-2])
      graph[-1].SetFillStyle(fillstyles[len(files)-2])
      #print graph[-1].GetErrorY(1)
      canvas[0].cd()
      graph[-1].Draw("L3")
      graphobs[-1].Draw("LP")
      l1.AddEntry(graphobs[-1],names[name],"lp")
      #canvas[0].Update()
    graph[0].Draw("L3")
    graphobs[0].Draw("LP")
    l1.Draw()
  canvas[0].SaveAs("EXOVVwprime_compare_"+scenario+"_Significance.pdf")