string="signal & mass & JJ (8 TeV) & lvJ (8 TeV) & llJ (8 TeV) & JJ (13 TeV) & lvJ (13 TeV) & llJ (13 TeV) \\\\\n"

masses = [2000]
for mass in masses:
  xsec=open("theory_HVT_WZ_8TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection8=float(split[1])

  xsec=open("../Wprime_EXO-15-002/theory_HVT_WZ_13TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection13=float(split[1])

  yields8=[]
  if mass>=1000 and mass<2500:
   card=open("../Wprime_EXO-15-002/comb_"+str(mass)+"/comb_xjj8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields8+=[((float(split[2]))/crosssection8/19700.,(float(split[6]))/crosssection8/19700.)]
  else:
    yields8+=[(0,0)]

  if mass<2500:
   card=open("../Wprime_EXO-15-002/comb_"+str(mass)+"/comb_xww."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields8+=[((float(split[1])+float(split[6]))/crosssection8/19700.,0)]
  else:
    yields8+=[(0,0)]

  if mass<2500:
   card=open("comb_"+str(mass)+"/comb_lljwz8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields8+=[((float(split[1])+float(split[3]))/crosssection8/19700.,0)]
  else:
    yields8+=[(0,0)]

  yields13=[]
  if mass>=1200:
   card=open("comb_"+str(mass)+"/comb_jjwz13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields13+=[((float(split[2])+float(split[10])+float(split[6]))/crosssection13/2600.,(float(split[18])+float(split[14])+float(split[22]))/crosssection13/2600.)]
  else:
    yields13+=[(0,0)]

  if mass>=1200:
   card=open("comb_"+str(mass)+"/comb_lvjwz13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields13+=[((float(split[1])+float(split[6])+float(split[21])+float(split[26]))/crosssection13/2300.,(float(split[11])+float(split[16])+float(split[31])+float(split[36]))/crosssection13/2300.)]
  else:
    yields13+=[(0,0)]

  yields13+=[(0,0)]

  string+="$W' \\to WZ$ & "+str(int(mass/100)/10.)+" TeV &"
  for y1,y2 in yields8:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  for y1,y2 in yields13:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  string+="\\\\\n"

for mass in masses:
  xsec=open("theory_HVT_WW_8TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection8=float(split[1])

  xsec=open("../Wprime_EXO-15-002/theory_HVT_WW_13TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection13=float(split[1])

  yields8=[]
  if mass>=1000 and mass<2500:
   card=open("../Wprime_EXO-15-002/comb_"+str(mass)+"/comb_xjj8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields8+=[((float(split[2]))/2./crosssection8/19700.,(float(split[6]))/2./crosssection8/19700.)]
  else:
    yields8+=[(0,0)]

  if mass<2500:
   card=open("../Wprime_EXO-15-002/comb_"+str(mass)+"/comb_xww."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields8+=[((float(split[1])+float(split[6]))/crosssection8/19700.,0)]
  else:
    yields8+=[(0,0)]

  yields8+=[(0,0)]

  yields13=[]
  if mass>=1200:
   card=open("comb_"+str(mass)+"/comb_jjww13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields13+=[((float(split[2])+float(split[5])+float(split[8]))/crosssection13/2600.,(float(split[11])+float(split[14])+float(split[17]))/crosssection13/2600.)]
  else:
    yields13+=[(0,0)]

  if mass>=1200:
   card=open("comb_"+str(mass)+"/comb_lvjww13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields13+=[((float(split[1])+float(split[6])+float(split[21])+float(split[26]))/crosssection13/2300.,(float(split[11])+float(split[16])+float(split[31])+float(split[36]))/crosssection13/2300.)]
  else:
    yields13+=[(0,0)]

  yields13+=[(0,0)]

  string+="$Z' \\to WW$ & "+str(int(mass/100)/10.)+" TeV &"
  for y1,y2 in yields8:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  for y1,y2 in yields13:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  string+="\\\\\n"

for mass in masses:
  xsec=open("../BulkG_EXO-15-002/xsect_BulkG_WW_c0p5_xsect_in_pb_factor4wrong.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection8ww=float(split[1])/4.

  xsec=open("../BulkG_EXO-15-002/xsect_BulkG_ZZ_c0p5_xsect_in_pb_factor4wrong.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection8zz=float(split[1])/4.

  xsec=open("../BulkG_EXO-15-002/xsect_BulkG_WW_c0p5_13TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection13ww=float(split[1])
      crosssection13zz=float(split[1])/2.

  yields8=[]
  if mass>=1000 and mass<2500:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xjj8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields8+=[((float(split[1])+float(split[2]))/(crosssection8ww+crosssection8zz)/19700.,(float(split[4])+float(split[5]))/(crosssection8ww+crosssection8zz)/19700.)]
  else:
    yields8+=[(0,0)]

  if mass<2500:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xww."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields8+=[((float(split[1])+float(split[6]))/crosssection8ww/19700.,(float(split[11])+float(split[16]))/crosssection8ww/19700.)]
  else:
    yields8+=[(0,0)]

  if mass<2500:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xzz."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields8+=[((float(split[1])+float(split[3]))/crosssection8zz/19700.,(float(split[5])+float(split[7]))/crosssection8zz/19700.)]
  else:
    yields8+=[(0,0)]

  yields13=[]
  if mass>=1200:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xjj13ww."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields13+=[[(float(split[1])+float(split[4])+float(split[7])),(float(split[10])+float(split[13])+float(split[16]))]]
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xjj13zz."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields13[-1][0]+=(float(split[2])+float(split[5])+float(split[8]))
      yields13[-1][0]*=1./(crosssection13ww+crosssection13zz)/2600.
      yields13[-1][1]+=(float(split[11])+float(split[14])+float(split[17]))
      yields13[-1][1]*=1./(crosssection13ww+crosssection13zz)/2600.
  else:
    yields13+=[(0,0)]

  if mass>=1200:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xww13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields13+=[((float(split[1])+float(split[6])+float(split[21])+float(split[26]))/crosssection13ww/2300.,(float(split[11])+float(split[16])+float(split[31])+float(split[36]))/crosssection13ww/2300.)]
  else:
    yields13+=[(0,0)]

  yields13+=[(0,0)]

  string+="$G_{bulk} \\to WW/ZZ$ & "+str(int(mass/100)/10.)+" TeV &"
  for y1,y2 in yields8:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  for y1,y2 in yields13:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  string+="\\\\\n"
  print string

  matrix=[s.split(" &") for s in string.split("\\\\\n")]
  invertedstring=""
  for j in range(len(matrix[0])):
    for i in range(len(matrix)-1):
       invertedstring+=matrix[i][j]
       if i!=len(matrix)-2: invertedstring+=" & "
    invertedstring+="\\\\\n"
  print invertedstring