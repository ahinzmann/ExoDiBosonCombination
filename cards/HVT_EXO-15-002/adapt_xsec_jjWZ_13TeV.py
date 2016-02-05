from array import array
import sys

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

WprimeWZ={}
for mass in masses:

 m = int((mass-800)/100)
 #print "mass = ",mass
 
 try:
   fWZ=open("JJ_cards_13TeV/CMS_jj_WZ_"+str(mass)+"_13TeV_CMS_jj_VVnew.txt").readlines()
 except:
   print "could not open"
   continue
   
 outfile="JJ_cards_13TeV/CMS_jj_WZfix_"+str(mass)+"_13TeV_CMS_jj_VVnew.txt"
 print outfile
 f=open(outfile,"w")

 WprimeWZ[mass]=(xsecMap['CX-(pb)'][m]+xsecMap['CX+(pb)'][m])*xsecMap['BRZW'][m]*(0.6991*0.6760)*(0.6991*0.6760)
 for l in range(len(fWZ)):
   if "rate" in fWZ[l]:
     line="rate 				    "
     fWZsplit=fWZ[l].replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
     for s in range(len(fWZsplit)):
       try:
 	 float(fWZsplit[s])
       except: continue
       signal=(s in [2,6,10,14,18,22]) 
       numberWZ=float(fWZsplit[s])
       if signal:
 	 numberWZ=numberWZ*WprimeWZ[mass]*100. # cards from Jennnifer are in units of 0.01 pb
       line+="%.5e  " % numberWZ
     line+="\n"
     f.write(line)
   else:
     f.write(fWZ[l])
