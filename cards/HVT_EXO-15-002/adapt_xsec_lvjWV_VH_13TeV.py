from array import array
import sys
from ROOT import *

def get_xsec_unc(mass):

   uncs = {}
   
   fin = TFile.Open('XsecUnc/xsec-unc-13TeV.root','READ')   
   cin = fin.Get('c')
   for p in cin.GetListOfPrimitives():
    if p.InheritsFrom("TMultiGraph"):
     for g in p.GetListOfGraphs(): uncs[g.GetName()] = g.Eval(mass) 
   fin.Close() 
   
   return uncs
   
def get_efficiency(mass):

   dEff = {}
   effs = []
   
   fElHP = TFile.Open('Wprime_WH_efficiency_el_HP.root','R')
   cElHP = fElHP.Get('eff_HPV')
   for p in cElHP.GetListOfPrimitives():
    if p.InheritsFrom("TMultiGraph"):
     for g in p.GetListOfGraphs(): dEff[g.GetName()] = g.Eval(mass/1000.) 
   fElHP.Close()
   
   fElLP = TFile.Open('Wprime_WH_efficiency_el_LP.root','R')
   cElLP = fElLP.Get('eff_LPV')
   for p in cElLP.GetListOfPrimitives():
    if p.InheritsFrom("TMultiGraph"):
     for g in p.GetListOfGraphs(): dEff[g.GetName()] = g.Eval(mass/1000.) 
   fElLP.Close()
   
   fMuHP = TFile.Open('Wprime_WH_efficiency_mu_HP.root','R')
   cMuHP = fMuHP.Get('eff_HPV')
   for p in cMuHP.GetListOfPrimitives():
    if p.InheritsFrom("TMultiGraph"):
     for g in p.GetListOfGraphs(): dEff[g.GetName()] = g.Eval(mass/1000.) 
   fMuHP.Close()
   
   fMuLP = TFile.Open('Wprime_WH_efficiency_mu_LP.root','R')
   cMuLP = fMuLP.Get('eff_LPV')
   for p in cMuLP.GetListOfPrimitives():
    if p.InheritsFrom("TMultiGraph"):
     for g in p.GetListOfGraphs(): dEff[g.GetName()] = g.Eval(mass/1000.) 
   fMuLP.Close()
   
   #keep this order of channels
   effs.append( dEff['mu_HPW'] )
   effs.append( dEff['mu_HPZ'] )
   effs.append( dEff['mu_LPW'] )
   effs.append( dEff['mu_LPZ'] )
   effs.append( dEff['el_HPW'] )
   effs.append( dEff['el_HPZ'] )
   effs.append( dEff['el_LPW'] )
   effs.append( dEff['el_LPZ'] )
   
   return effs
   
def get_theo_map():

   V_mass = array('d',[])

   brs = {}
   index = {}

   mapping = ["M0","M+","BRWW","BRhZ","BRZW","BRWh","CX+(pb)","CX0(pb)","CX-(pb)"]

   for m in xrange(0,len(mapping)):
      if mapping[m] != "M0" and mapping[m] != "M+":
   	 brs[mapping[m]] = array('d',[])
   	 #print mapping[m]

   f = open('xsect_HVT_13TeV.txt','r')
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

   f = open('xsect_HVT_13TeV.txt','r')
   for line in f:
      if line.find('M0') != -1: continue
      brDict = line.split(",")  	    
      V_mass.append(float(brDict[index['M0']]))
      for m in xrange(0,len(mapping)):
   	 if mapping[m] != "M0" and mapping[m] != "M+":
   	    brs[mapping[m]].append(float(brDict[index[mapping[m]]]))

   f.close()

   return [brs,V_mass]


thMap = get_theo_map()
xsecMap = thMap[0]
massMap = thMap[1]

masses =[m*100 for m in range(8,40+1)]

if len(sys.argv)>1:
  masses=[int(sys.argv[1])]

ZprimeWW={}
WprimeWZ={}
WprimeWH={}

for mass in masses:

 m = int((mass-800)/100)
 #print "mass = ",mass
 
 try:
   fWW=open("LVJ_cards_13TeV/wwlvj_Zprime_WW_lvjj_M"+str(mass)+"_combo_ALLP_unbin.txt").readlines()
   fWZ=open("LVJ_cards_13TeV/wwlvj_Wprime_WZ_lvjj_M"+str(mass)+"_combo_ALLP_unbin.txt").readlines()
 except:
   print "could not open"
   continue
   
 outfile="LVJ_cards_13TeV/wwlvj_Vprimefix_WV_VH_lvjj_M"+str(mass)+"_combo_ALLP_unbin.txt"
 print outfile
 f=open(outfile,"w")

 ZprimeWW[mass]=xsecMap['CX0(pb)'][m]*xsecMap['BRWW'][m]*2*0.322*0.6760
 WprimeWZ[mass]=(xsecMap['CX-(pb)'][m]+xsecMap['CX+(pb)'][m])*xsecMap['BRZW'][m]*0.322*0.6991
 WprimeWH[mass]=(xsecMap['CX-(pb)'][m]+xsecMap['CX+(pb)'][m])*xsecMap['BRWh'][m]*0.322*0.577
 WHeff = get_efficiency(mass)

 xsecUnc =  get_xsec_unc(mass)
 pdf_Wprime = 1+xsecUnc['qq_PDF_Wprime']
 pdf_Zprime = 1+xsecUnc['qq_PDF_Zprime']
 scale_Wprime = 1+xsecUnc['qq_scale_Wprime']
 scale_Zprime = 1+xsecUnc['qq_scale_Zprime']
  
 yieldsWprime = []
 sysWprime = {}
 sysZprime = {}
 sysWJets = {}
 sysTTbar = {}
 sysVV = {}
 sysSTop = {}
 sysWprime['CMS_XS_qq_PDF'] = []
 sysWprime['CMS_XS_qq_scale'] = []
 
 for l in range(len(fWZ)):
  if "kmax" in fWZ[l]:
   fWZsplit = fWZ[l].split(' ') 
   fWZ[l] = fWZ[l].replace(fWZsplit[1],str(int(fWZsplit[1])+1))
  if "CMS_xww_XS_Wprime_WZ_13TeV" in fWZ[l]: continue
  if "rate" in fWZ[l]:
   fWZsplit=fWZ[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
   i=0
   for s in range(len(fWZsplit)):
    try:
     float(fWZsplit[s])
    except: continue
    signal=(s in [1,6,11,16,21,26,31,36]) # only change signal
    numberWZ=float(fWZsplit[s])
    if signal:
     yieldsWprime.append(numberWZ*WprimeWZ[mass]*100.+WHeff[i]*WprimeWH[mass]*2197.956) # cards from Jennnifer are in units of 0.01 pb 
     i+=1   
  elif (("CMS_" in fWZ[l]) and ("lnN" in fWZ[l])) or ("lumi_13TeV" in fWZ[l]):
   fWZsplit=fWZ[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
   sysWprime[fWZsplit[0]] = []
   sysWJets[fWZsplit[0]] = []
   sysSTop[fWZsplit[0]] = []
   sysVV[fWZsplit[0]] = []
   sysTTbar[fWZsplit[0]] = []
   for s in range(len(fWZsplit)):
    signal=(s in [2,7,12,17,22,27,32,37])
    wjets=(s in [3,8,13,18,23,28,33,38])
    stop=(s in [4,9,14,19,24,29,34,39])
    vv=(s in [5,10,15,20,25,30,35,40])
    ttbar=(s in [6,11,16,21,26,31,36,41])
    if signal:
     sysWprime[fWZsplit[0]].append(fWZsplit[s]) 
    if wjets:
     sysWJets[fWZsplit[0]].append(fWZsplit[s])  
    if stop:
     sysSTop[fWZsplit[0]].append(fWZsplit[s]) 
    if vv:
     sysVV[fWZsplit[0]].append(fWZsplit[s]) 
    if ttbar:
     sysTTbar[fWZsplit[0]].append(fWZsplit[s]) 

 for s in range(len(sysWprime['CMS_scale_m_13TeV'])):
  sysWprime['CMS_XS_qq_PDF'].append(pdf_Wprime)     
  sysWprime['CMS_XS_qq_scale'].append(scale_Wprime)
  
 sysZprime['CMS_XS_qq_PDF'] = []
 sysZprime['CMS_XS_qq_scale'] = []
 for l in range(len(fWW)):
  if "CMS_xww_XS_Zprime_WW_13TeV" in fWW[l]: continue
  if (("CMS_" in fWW[l]) and ("lnN" in fWW[l])) or ("lumi_13TeV" in fWW[l]):
   fWWsplit=fWW[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
   sysZprime[fWWsplit[0]] = []
   for s in range(len(fWWsplit)):
    signal=(s in [2,7,12,17,22,27,32,37])
    if signal:
     sysZprime[fWWsplit[0]].append(fWWsplit[s]) 

 for s in range(len(sysZprime['CMS_scale_m_13TeV'])):
  sysZprime['CMS_XS_qq_PDF'].append(pdf_Zprime)     
  sysZprime['CMS_XS_qq_scale'].append(scale_Zprime)
              
 for l in range(len(fWW)):
  if "CMS_xww_XS_Zprime_WW_13TeV" in fWW[l]: continue
  line=fWW[l]
  if ("jmax" in line) and ("processes" in line): line="jmax 5 number of processes minus 1\n"
  if "kmax" in line: line="kmax 94 number of nuisance parameters\n"
  if "shapes ZprimeWW_xww  ch" in line: line+=line.replace("ZprimeWW","WprimeWZ").replace("Zprime_WW","Wprime_WZ")
  if "bin" in line:
   for i in range(1,9): line=line.replace("ch%i           ch%i           ch%i           ch%i           ch%i"%(i,i,i,i,i),"ch%i           ch%i           ch%i           ch%i           ch%i           ch%i"%(i,i,i,i,i,i))
  if ("process" in fWW[l]) and ("ZprimeWW" in fWW[l]): line=line.replace("ZprimeWW_xww","WprimeWZ_xww  ZprimeWW_xww")
  if ("process" in fWW[l]) and not ("ZprimeWW" in fWW[l]): line=line.replace("0             1","-1            0             1")
  if "rate" in fWW[l]:
   line="rate                                             "
   fWWsplit=fWW[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
   bin = -1
   for s in range(len(fWWsplit)):
    try:
      float(fWWsplit[s])
    except: continue
    signal=(s in [1,6,11,16,21,26,31,36]) # only change signal
    numberWW=float(fWWsplit[s])
    if signal:
     numberWW=numberWW*ZprimeWW[mass]*100. # cards from Jennnifer are in units of 0.01 pb
     bin+=1
     line+="%.5e   %.5e   " %(yieldsWprime[bin],numberWW)
    else: line+="%.5e   " % numberWW  
   line+="\n"      
  if (("CMS_" in fWW[l]) and ("lnN" in fWW[l])) or ("lumi_13TeV" in fWW[l]):
   fWWsplit=fWW[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
   line=fWWsplit[0]+" lnN "
   for v in range(len(sysZprime[fWWsplit[0]])):
    line+=(sysWprime[fWWsplit[0]][v]+" "+sysZprime[fWWsplit[0]][v]+" "+sysWJets[fWWsplit[0]][v]+" "+sysSTop[fWWsplit[0]][v]+" "+sysVV[fWWsplit[0]][v]+" "+sysTTbar[fWWsplit[0]][v]+" ")
   line+="\n"
  f.write(line)
    
 newline1 = 'CMS_XS_qq_PDF lnN '
 newline2 = 'CMS_XS_qq_scale lnN '    
 for v in range(len(sysZprime['CMS_XS_qq_PDF'])):
  newline1+=("%.3f"%sysWprime['CMS_XS_qq_PDF'][v]+" "+"%.3f"%sysZprime['CMS_XS_qq_PDF'][v]+" "+"-"+" "+"-"+" "+"-"+" "+"-"+" ")  
  newline2+=("%.3f"%sysWprime['CMS_XS_qq_scale'][v]+" "+"%.3f"%sysZprime['CMS_XS_qq_scale'][v]+" "+"-"+" "+"-"+" "+"-"+" "+"-"+" ")  
   
 f.write(newline1)
 f.write('\n')
 f.write(newline2)
 f.close()  
   
