from ROOT import *
import ROOT
import array, math
import os

masses =[m*100 for m in range(8,25+1)]

print "8 TeV"
xsec_x_ZH=[800,900,1000,1200,1500,2000,2500]
xsec_y_ZH=[log(7.9478),log(5.6342),log(3.7837),log(1.6871),log(0.5269),log(0.0854),log(0.0150)]
xsec_x_array_ZH=array.array('d')
xsec_y_array_ZH=array.array('d')
for p in xsec_x_ZH: xsec_x_array_ZH.append(p)
for p in xsec_y_ZH: xsec_y_array_ZH.append(p)
g_ZH=TGraph(len(xsec_x_array_ZH),xsec_x_array_ZH,xsec_y_array_ZH)
f_out_ZH=open("theory_HVT_ZH_qqtautau_8TeV.txt","w")
for mass in masses:
        theoryZH=exp(g_ZH.Eval(mass))
	f_out_ZH.write(str(mass)+" "+str(theoryZH)+"\n")
        print "mass = ",mass,"theoryZHqqtautau = ",theoryZH
f_out_ZH.close()
f_out_ZH=open("theory_HVT_ZH_8TeV.txt","w")
for mass in masses:
        theoryZH=exp(g_ZH.Eval(mass))/6.32E-02/0.6991
	f_out_ZH.write(str(mass)+" "+str(theoryZH)+"\n")
        print "mass = ",mass,"theoryZH = ",theoryZH
f_out_ZH.close()
