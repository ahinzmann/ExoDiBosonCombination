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
 fullCLS=False
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
 
 signalstrength='false'
 if len(sys.argv)>1 and "813" in sys.argv[1]:
   signalstrength='true'
 for name in names.keys():
   if fullCLS:
     os.system('root -b -q plot_golfcourse_HybridNew.C\(true,0,\\"'+name+'\\",'+signalstrength+'\)')
     os.system('root -b -q plot_golfcourse_Asymptotic.C\(true,0,\\"'+name+'\\",'+signalstrength+'\)')
   else:
     os.system('root -b -q plot_golfcourse_Asymptotic.C\(true,0,\\"'+name+'\\",'+signalstrength+'\)')
 
 colors=[4,6,11,28,8,9,7]
 styles=[3,4,5,6,7,8,9,10]
 fillstyles=[3007,3007,3007,3007,3007,3007,3007,3007]
 markerstyles=[20,22,23,24,25,26,27,28]
 for scenario in scenarios.keys():
  files=[]
  canvas=[]
  graph=[]
  graphobs=[]
  for name in scenarios[scenario]:
    print name
    shortname=name.replace("_UL_Asymptotic","").replace("_UL_HybridNew","")
    if (name=="JAM13") and fullCLS:
      files+=[TFile.Open("EXOVVwprime_"+name+"_UL_HybridNew.root")]
      canvas+=[files[-1].Get("c_lim_HybridNew")]
    else:
      files+=[TFile.Open("EXOVVwprime_"+name+"_UL_Asymptotic.root")]
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
      graphobs[-1].SetMarkerColor(colors[stylelist[shortname]])
      graphobs[-1].SetMarkerStyle(markerstyles[stylelist[shortname]])
      graphobs[-1].SetLineColor(colors[stylelist[shortname]])
      #graphobs[-1].SetLineStyle(styles[len(files)-2])
      graph[-1].SetLineColor(colors[stylelist[shortname]])
      graph[-1].SetLineStyle(styles[stylelist[shortname]])
      graph[-1].SetFillColor(colors[stylelist[shortname]])
      graph[-1].SetFillStyle(fillstyles[stylelist[shortname]])
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
