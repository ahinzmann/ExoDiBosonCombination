from ROOT import *
import ROOT
import array, math
import os

masses =[m*100 for m in range(8,30+1)]

print "8 TeV"
xsec_x_VH=[900,1000,1500,2000,2500,3000]
xsec_y_VH=[log(713.95*0.5223),log(501.244*0.5079),log(76.974*0.4849),log(12.886*0.4791),log(2.242*0.4767),log(0.3804*0.4754)]
xsec_x_array_VH=array.array('d')
xsec_y_array_VH=array.array('d')
for p in xsec_x_VH: xsec_x_array_VH.append(p)
for p in xsec_y_VH: xsec_y_array_VH.append(p)
g_VH=TGraph(len(xsec_x_array_VH),xsec_x_array_VH,xsec_y_array_VH)
f_out_VH=open("theory_HVT_VH_8TeV.txt","w")
for mass in masses:
        theoryVH=exp(g_VH.Eval(mass))/1000.
	f_out_VH.write(str(mass)+" "+str(theoryVH)+"\n")
        print "mass = ",mass,"theoryVH = ",theoryVH
f_out_VH.close()
