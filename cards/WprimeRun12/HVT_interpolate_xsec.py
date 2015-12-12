from ROOT import *
import ROOT
import array, math
import os

masses =[m*100 for m in range(6,40+1)]

print "8 TeV"
#xsec_x_VH=[900,1000,1500,2000,2500,3000]
#xsec_y_VH=[log(713.95*0.5223),log(501.244*0.5079),log(76.974*0.4849),log(12.886*0.4791),log(2.242*0.4767),log(0.3804*0.4754)]
#xsec_x_array_VH=array.array('d')
#xsec_y_array_VH=array.array('d')
#for p in xsec_x_VH: xsec_x_array_VH.append(p)
#for p in xsec_y_VH: xsec_y_array_VH.append(p)
#g_VH=TGraph(len(xsec_x_array_VH),xsec_x_array_VH,xsec_y_array_VH)
HVTWprime={}
HVTZprime={}
HVTBRWH={}
HVTBRWW={}
HVTBRZH={}
HVTBRZW={}
for line in open("HVTcrossSection.txt").readlines()[1:]:
   split=line.replace("\n","").split(",")
   HVTWprime[int(float(split[0]))]=float(split[-1])+float(split[-3])
   HVTZprime[int(float(split[0]))]=float(split[-2])
   HVTBRWH[int(float(split[0]))]=float(split[-8])
   HVTBRWW[int(float(split[0]))]=float(split[-19])
   HVTBRZH[int(float(split[0]))]=float(split[-18])
   HVTBRZW[int(float(split[0]))]=float(split[-10])
print HVTWprime[1000],HVTZprime[1000],HVTBRWH[1000],HVTBRWW[1000],HVTBRZH[1000],HVTBRZW[1000]

xsec_x_array_Wprime=array.array('d')
xsec_y_array_Wprime=array.array('d')
for p in sorted(HVTWprime.keys()): xsec_x_array_Wprime.append(p)
for p in sorted(HVTWprime.keys()): xsec_y_array_Wprime.append(log(HVTWprime[p]))
g_Wprime=TGraph(len(xsec_x_array_Wprime),xsec_x_array_Wprime,xsec_y_array_Wprime)

xsec_x_array_Zprime=array.array('d')
xsec_y_array_Zprime=array.array('d')
for p in sorted(HVTZprime.keys()): xsec_x_array_Zprime.append(p)
for p in sorted(HVTZprime.keys()): xsec_y_array_Zprime.append(log(HVTZprime[p]))
g_Zprime=TGraph(len(xsec_x_array_Zprime),xsec_x_array_Zprime,xsec_y_array_Zprime)

xsec_x_array_HVTBRWH=array.array('d')
xsec_y_array_HVTBRWH=array.array('d')
for p in sorted(HVTBRWH.keys()): xsec_x_array_HVTBRWH.append(p)
for p in sorted(HVTBRWH.keys()): xsec_y_array_HVTBRWH.append(log(HVTBRWH[p]))
g_HVTBRWH=TGraph(len(xsec_x_array_HVTBRWH),xsec_x_array_HVTBRWH,xsec_y_array_HVTBRWH)

xsec_x_array_HVTBRWW=array.array('d')
xsec_y_array_HVTBRWW=array.array('d')
for p in sorted(HVTBRWW.keys()): xsec_x_array_HVTBRWW.append(p)
for p in sorted(HVTBRWW.keys()): xsec_y_array_HVTBRWW.append(log(HVTBRWW[p]))
g_HVTBRWW=TGraph(len(xsec_x_array_HVTBRWW),xsec_x_array_HVTBRWW,xsec_y_array_HVTBRWW)

xsec_x_array_HVTBRZH=array.array('d')
xsec_y_array_HVTBRZH=array.array('d')
for p in sorted(HVTBRZH.keys()): xsec_x_array_HVTBRZH.append(p)
for p in sorted(HVTBRZH.keys()): xsec_y_array_HVTBRZH.append(log(HVTBRZH[p]))
g_HVTBRZH=TGraph(len(xsec_x_array_HVTBRZH),xsec_x_array_HVTBRZH,xsec_y_array_HVTBRZH)

xsec_x_array_HVTBRZW=array.array('d')
xsec_y_array_HVTBRZW=array.array('d')
for p in sorted(HVTBRZW.keys()): xsec_x_array_HVTBRZW.append(p)
for p in sorted(HVTBRZW.keys()): xsec_y_array_HVTBRZW.append(log(HVTBRZW[p]))
g_HVTBRZW=TGraph(len(xsec_x_array_HVTBRZW),xsec_x_array_HVTBRZW,xsec_y_array_HVTBRZW)

f_out_VH=open("theory_HVT_VH_8TeV.txt","w")
for mass in masses:
        theoryVH=exp(g_Wprime.Eval(mass))*exp(g_HVTBRWH.Eval(mass))+exp(g_Zprime.Eval(mass))*exp(g_HVTBRZH.Eval(mass))
	f_out_VH.write(str(mass)+" "+str(theoryVH)+"\n")
        print "mass = ",mass,"theoryVH = ",theoryVH
f_out_VH.close()

f_out_WH=open("theory_HVT_WH_8TeV.txt","w")
for mass in masses:
        #theoryWH=exp(g_WH.Eval(mass))/1000.
        theoryWH=exp(g_Wprime.Eval(mass))*exp(g_HVTBRWH.Eval(mass))
	f_out_WH.write(str(mass)+" "+str(theoryWH)+"\n")
        print "mass = ",mass,"theoryWH = ",theoryWH
f_out_WH.close()

f_out_ZH=open("theory_HVT_ZH_8TeV.txt","w")
for mass in masses:
        #theoryZH=exp(g_ZH.Eval(mass))/1000.
        theoryZH=exp(g_Zprime.Eval(mass))*exp(g_HVTBRZH.Eval(mass))
	f_out_ZH.write(str(mass)+" "+str(theoryZH)+"\n")
        print "mass = ",mass,"theoryZH = ",theoryZH
f_out_ZH.close()

f_out_VW=open("theory_HVT_VW_8TeV.txt","w")
for mass in masses:
        #theoryVW=exp(g_VW.Eval(mass))/1000.
        theoryVW=exp(g_Wprime.Eval(mass))*exp(g_HVTBRZW.Eval(mass))+exp(g_Zprime.Eval(mass))*exp(g_HVTBRWW.Eval(mass))
	f_out_VW.write(str(mass)+" "+str(theoryVW)+"\n")
        print "mass = ",mass,"theoryVW = ",theoryVW
f_out_VW.close()

f_out_WZ=open("theory_HVT_WZ_8TeV.txt","w")
for mass in masses:
        #theoryWZ=exp(g_WZ.Eval(mass))/1000.
        theoryWZ=exp(g_Wprime.Eval(mass))*exp(g_HVTBRZW.Eval(mass))
	f_out_WZ.write(str(mass)+" "+str(theoryWZ)+"\n")
        print "mass = ",mass,"theoryWZ = ",theoryWZ
f_out_WZ.close()

f_out_WW=open("theory_HVT_WW_8TeV.txt","w")
for mass in masses:
        #theoryWW=exp(g_WW.Eval(mass))/1000.
        theoryWW=exp(g_Zprime.Eval(mass))*exp(g_HVTBRWW.Eval(mass))
	f_out_WW.write(str(mass)+" "+str(theoryWW)+"\n")
        print "mass = ",mass,"theoryWW = ",theoryWW
f_out_WW.close()

f_out_HVT=open("theory_HVT_8TeV.txt","w")
for mass in masses:
        #theoryHVT=exp(g_HVT.Eval(mass))/1000.
        theoryHVT=exp(g_Wprime.Eval(mass))+exp(g_Zprime.Eval(mass))
	f_out_HVT.write(str(mass)+" "+str(theoryHVT)+"\n")
        print "mass = ",mass,"theoryHVT = ",theoryHVT
f_out_HVT.close()

f_out_HVT=open("theory_Wprime_8TeV.txt","w")
for mass in masses:
        #theoryHVT=exp(g_HVT.Eval(mass))/1000.
        theoryHVT=exp(g_Wprime.Eval(mass))
	f_out_HVT.write(str(mass)+" "+str(theoryHVT)+"\n")
        print "mass = ",mass,"theoryHVT = ",theoryHVT
f_out_HVT.close()

