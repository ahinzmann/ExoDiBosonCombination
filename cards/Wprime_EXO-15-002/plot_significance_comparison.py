from ROOT import *
import os
import sys

gROOT.Reset()
gROOT.SetStyle("Plain")
gROOT.SetBatch(True)
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
 scenarios["JJ813TeVold"]=["xjj13","xjj13old","xjj13hp","xjj8"]
 scenarios["ZZ813TeV"]=["ZZ813","xzz","xzz13"]
 scenarios["WW813TeV"]=["WW813","xww","xww13"]
 scenarios["ALL813TeV"]=["ALL813","xww","xzz","xjj8","xjj13","xww13","xzz13"]
 scenarios["ALL13TeV"]=["ALL13","xjj13","xww13","xzz13"]
 scenarios["JAM813TeV"]=["JAM813","xww","xzz","xjj8","xww13","xjj13"]
 scenarios["JAM13TeV"]=["JAM13","xww13","xjj13"]
 if len(sys.argv)>1:
    scenarios_arg={}
    scenarios_arg[sys.argv[1]]=scenarios[sys.argv[1]]
    scenarios=scenarios_arg
 names={}
 names["ALL"]="lvJ, llJ, JJ (8 TeV)"
 names["xww"]="lvJ (8 TeV)"
 names["xjj8"]="JJ (8 TeV)"
 names["xzz"]="llJ (8 TeV)"
 names["JJ813"]="JJ (8+13 TeV)"
 names["xjj13"]="JJ (13 TeV)"
 names["xjj13old"]="JJ  (no W/Z cat) (13 TeV)"
 names["xjj13hp"]="JJ (only HP) (13 TeV)"
 names["ZZ813"]="llJ (8+13 TeV)"
 names["xzz13"]="llJ (13 TeV)"
 names["WW813"]="lvJ (8+13 TeV)"
 names["xww13"]="lvJ (13 TeV)"
 names["ALL813"]="lvJ, llJ, JJ (8+13 TeV)"
 names["ALL13"]="lvJ, llJ, JJ (13 TeV)"
 names["JAM813"]="lvJ, llJ, JJ (8+13 TeV)"
 names["JAM13"]="lvJ, JJ (13 TeV)"

 stylelist={}
 stylelist["xww"]=0
 stylelist["xjj8"]=1
 stylelist["xzz"]=2
 stylelist["xjj13"]=3
 stylelist["xzz13"]=4
 stylelist["xww13"]=5
 stylelist["xjj13"]=6
 stylelist["xjj13old"]=0
 stylelist["xjj13hp"]=2
 
 if len(sys.argv)==1:
  for name in names.keys():
   os.system('root -b -q plot_Significance.C\(true,\\"'+name+'\\"\)')
 
 colors=[4,6,11,28,8,9,7]
 styles=[3,4,5,6,7,8,9,10]
 fillstyles=[3007,3007,3007,3007,3007,3007,3007,3007]
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
      graphobs[-1].SetMarkerColor(colors[stylelist[name]])
      graphobs[-1].SetMarkerStyle(styles[stylelist[name]])
      graphobs[-1].SetLineColor(colors[stylelist[name]])
      #graphobs[-1].SetLineStyle(styles[len(files)-2])
      graph[-1].SetLineWidth(2)
      graph[-1].SetLineColor(colors[stylelist[name]])
      graph[-1].SetLineStyle(styles[stylelist[name]])
      graph[-1].SetFillColor(colors[stylelist[name]])
      graph[-1].SetFillStyle(fillstyles[stylelist[name]])
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
