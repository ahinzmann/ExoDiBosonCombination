#!/usr/bin/env python
import array, math
import os
import sys

### Make changes here if it is needed
channels = ["JAM13","xjj13ww","xjj13zz","xww13"]
channels = ["xjj13ww","xjj13zz","xww13"]
channels = ["JAM13"]
m=open("masses.txt")
masses=[int(mm.strip("\n")) for mm in m.readlines()]
if len(sys.argv)>1:
  masses=[int(sys.argv[1])]

for channel in channels:
 for mass in masses:
  print mass,channel

  card="comb_"+str(mass)+"/binaryDatacard"+channel+".root"
  os.system("rm comb_"+str(mass)+"/output_"+str(mass)+"_"+channel+".root")
  os.system("grep -a _channel comb_"+str(mass)+"/cra*/res/*.stdout > qwe.txt")
  f=open("qwe.txt")
  files=[]
  for l in reversed(f.readlines()):
   if channel in l or channel in l:
    crab=l.split("/")[1]
    if not "comb_"+str(mass)+"/"+crab+"/res/output*root" in files:
      print crab
      files+=["comb_"+str(mass)+"/"+crab+"/res/output*root"]
  if len(files)>0:
    os.system("hadd comb_"+str(mass)+"/output_"+str(mass)+"_"+channel+".root "+" ".join(files))
    os.system("combine "+card+" -M HybridNew --freq --grid=comb_"+str(mass)+"/output_"+str(mass)+"_"+channel+".root -m "+str(mass)+" --rMin=0.003 --rMax=6000 --expectedFromGrid 0.025 &> comb_"+str(mass)+"/limitM2_"+str(mass)+"_"+channel+".txt;")
    os.system("combine "+card+" -M HybridNew --freq --grid=comb_"+str(mass)+"/output_"+str(mass)+"_"+channel+".root -m "+str(mass)+" --rMin=0.003 --rMax=6000 --expectedFromGrid 0.16 &> comb_"+str(mass)+"/limitM1_"+str(mass)+"_"+channel+".txt;")
    os.system("combine "+card+" -M HybridNew --freq --grid=comb_"+str(mass)+"/output_"+str(mass)+"_"+channel+".root -m "+str(mass)+" --rMin=0.003 --rMax=6000 --expectedFromGrid 0.5 &> comb_"+str(mass)+"/limitE0_"+str(mass)+"_"+channel+".txt;")
    os.system("combine "+card+" -M HybridNew --freq --grid=comb_"+str(mass)+"/output_"+str(mass)+"_"+channel+".root -m "+str(mass)+" --rMin=0.003 --rMax=6000 --expectedFromGrid 0.84 &> comb_"+str(mass)+"/limitP1_"+str(mass)+"_"+channel+".txt;")
    os.system("combine "+card+" -M HybridNew --freq --grid=comb_"+str(mass)+"/output_"+str(mass)+"_"+channel+".root -m "+str(mass)+" --rMin=0.003 --rMax=6000 --expectedFromGrid 0.975 &> comb_"+str(mass)+"/limitP2_"+str(mass)+"_"+channel+".txt;")
    os.system("combine "+card+" -M HybridNew --freq --grid=comb_"+str(mass)+"/output_"+str(mass)+"_"+channel+".root -m "+str(mass)+" --rMin=0.003 --rMax=6000 &> comb_"+str(mass)+"/limitOb_"+str(mass)+"_"+channel+".txt;")
