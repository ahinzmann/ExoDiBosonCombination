string="signal & mass & JJ (8 TeV) & lvJ (8 TeV) & llJ (8 TeV) & JJ (13 TeV) & lvJ (13 TeV) & llJ (13 TeV) & bbbb (8 TeV) & lvbb (8 TeV) & qqtautau (8 TeV) \\\\\n"

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

  yields=[]
  if mass>=1000 and mass<2500:
   card=open("../Wprime_EXO-15-002/comb_"+str(mass)+"/comb_xjj8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[2]))/crosssection8/19700.,(float(split[6]))/crosssection8/19700.)]
      jjjjcontamination=(float(split[2])+float(split[6]))/crosssection8/19700.
  else:
    yields+=[(0,0)]

  if mass<2500:
   card=open("../Wprime_EXO-15-002/comb_"+str(mass)+"/comb_xww."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[6]))/crosssection8/19700.,0)]
      lvjjcontamination=(float(split[1])+float(split[6]))/crosssection8/19700.
  else:
    yields+=[(0,0)]

  if mass<2500:
   card=open("comb_"+str(mass)+"/comb_lljwz8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[3]))/crosssection8/19700.,0)]
      lljjcontamination=(float(split[1])+float(split[3]))/crosssection8/19700.
  else:
    yields+=[(0,0)]

  if mass>=1200:
   card=open("comb_"+str(mass)+"/comb_jjwz13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[2])+float(split[10])+float(split[6]))/crosssection13/2600.,(float(split[18])+float(split[14])+float(split[22]))/crosssection13/2600.)]
  else:
    yields+=[(0,0)]

  if mass>=1200:
   card=open("comb_"+str(mass)+"/comb_lvjwz13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[6])+float(split[21])+float(split[26]))/crosssection13/2300.,(float(split[11])+float(split[16])+float(split[31])+float(split[36]))/crosssection13/2300.)]
  else:
    yields+=[(0,0)]

  yields+=[(0,0)]

  yields+=[(jjjjcontamination*0.01,-1)] #jjjj
  yields+=[(lvjjcontamination*0.01,-1)] #lvjj
  yields+=[(lljjcontamination*0.01,-1)] #lljj

  string+="$W' \\to WZ$ & "+str(int(mass/100)/10.)+" TeV &"
  for y1,y2 in yields:
   if y2<0:
    string+=" ("+str(int(y1*1000)/10.)+") &"
   else:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  string+="\\\\\n"

  yields=[]

  yields+=[(jjjjcontamination*0.019,-1)] #jjjj
  yields+=[(lvjjcontamination*0.017,-1)] #lvjj
  yields+=[(lljjcontamination*.27*57.7/69.91,0)] #lljj
  yields+=[(jjjjcontamination*0.019,-1)] #jjjj
  yields+=[(lvjjcontamination*.19*57.7/69.91,-1)] #lvjj
  yields+=[(0,0)] #lljj

  xsec=open("../Wprime_EXO-15-002/theory_HVT_WH_8TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection8=float(split[1])

  if mass>=1000 and mass<2500:
   card=open("comb_"+str(mass)+"/comb_jjwh8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[7])+float(split[10]))/crosssection8/19700.,(float(split[4])+float(split[12])+float(split[15])+float(split[17])+float(split[20]))/crosssection8/19700.)]
  else:
    yields+=[(0,0)]

  if mass<2500:
   card=open("comb_"+str(mass)+"/comb_lvjwh8."+str(mass)+".txt")
   for l in card.readlines():
    print l
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[6]))/crosssection8/19700.,0)]
  else:
    yields+=[(0,0)]

  if mass<2500:
   card=open("comb_"+str(mass)+"/comb_ttjwh8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[3])+float(split[5])+float(split[7])+float(split[9])+float(split[11]))/crosssection8/19700.,0)]
  else:
    yields+=[(0,0)]

  string+="$W' \\to WH$ & "+str(int(mass/100)/10.)+" TeV &"
  for y1,y2 in yields:
   if y2<0:
    string+=" ("+str(int(y1*1000)/10.)+") &"
   else:
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

  yields=[]
  if mass>=1000 and mass<2500:
   card=open("../Wprime_EXO-15-002/comb_"+str(mass)+"/comb_xjj8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[2]))/2./crosssection8/19700.,(float(split[6]))/2./crosssection8/19700.)]
      jjjjcontamination=(float(split[2])+float(split[6]))/crosssection8/19700.
  else:
    yields+=[(0,0)]

  if mass<2500:
   card=open("../Wprime_EXO-15-002/comb_"+str(mass)+"/comb_xww."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[6]))/crosssection8/19700.,0)]
      lvjjcontamination=(float(split[1])+float(split[6]))/crosssection8/19700.
  else:
    yields+=[(0,0)]

  yields+=[(0,0)]

  if mass>=1200:
   card=open("comb_"+str(mass)+"/comb_jjww13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[2])+float(split[5])+float(split[8]))/crosssection13/2600.,(float(split[11])+float(split[14])+float(split[17]))/crosssection13/2600.)]
  else:
    yields+=[(0,0)]

  if mass>=1200:
   card=open("comb_"+str(mass)+"/comb_lvjww13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[6])+float(split[21])+float(split[26]))/crosssection13/2300.,(float(split[11])+float(split[16])+float(split[31])+float(split[36]))/crosssection13/2300.)]
  else:
    yields+=[(0,0)]

  yields+=[(0,0)]

  yields+=[(0,0)]
  yields+=[(0,0)]
  yields+=[(0,0)]

  string+="$Z' \\to WW$ & "+str(int(mass/100)/10.)+" TeV &"
  for y1,y2 in yields:
   if y2<0:
    string+=" ("+str(int(y1*1000)/10.)+") &"
   else:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  string+="\\\\\n"

  yields=[]

  yields+=[(jjjjcontamination*0.019,-1)] #jjjj
  yields+=[(lvjjcontamination*0.017,-1)] #lvjj
  yields+=[(0,0)] #lljj
  yields+=[(jjjjcontamination*0.019,-1)] #jjjj
  yields+=[(lvjjcontamination*.19*57.7/67.60,-1)] #lvjj
  yields+=[(0,0)] #lljj

  xsec=open("../Wprime_EXO-15-002/theory_HVT_ZH_8TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection8=float(split[1])

  if mass>=1000 and mass<2500:
   card=open("comb_"+str(mass)+"/comb_jjzh8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[2])+float(split[8])+float(split[9]))/crosssection8/19700.,(float(split[5])+float(split[13])+float(split[14])+float(split[18])+float(split[19]))/crosssection8/19700.)]
  else:
    yields+=[(0,0)]

  yields+=[(0,0)]

  if mass<2500:
   card=open("comb_"+str(mass)+"/comb_ttjzh8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[3])+float(split[5])+float(split[7])+float(split[9])+float(split[11]))/crosssection8/19700.,0)]
  else:
    yields+=[(0,0)]

  string+="$Z' \\to ZH$ & "+str(int(mass/100)/10.)+" TeV &"
  for y1,y2 in yields:
   if y2<0:
    string+=" ("+str(int(y1*1000)/10.)+") &"
   else:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  string+="\\\\\n"

for mass in masses:
  xsec=open("../BulkG_EXO-15-002/xsect_BulkG_WW_c0p5_xsect_in_pb_factor4wrong.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection8ww=float(split[1])/4.

  xsec=open("../BulkG_EXO-15-002/xsect_BulkG_WW_c0p5_13TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection13ww=float(split[1])

  yields=[]
  if mass>=1000 and mass<2500:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xjj8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1]))/(crosssection8ww)/19700.,(float(split[4]))/(crosssection8ww)/19700.)]
  else:
    yields+=[(0,0)]

  if mass<2500:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xww."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[6]))/crosssection8ww/19700.,(float(split[11])+float(split[16]))/crosssection8ww/19700.)]
  else:
    yields+=[(0,0)]

  yields+=[(0,0)]

  if mass>=1200:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xjj13ww."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[[(float(split[1])+float(split[4])+float(split[7])),(float(split[10])+float(split[13])+float(split[16]))]]
      yields[-1][0]*=1./(crosssection13ww)/2600.
      yields[-1][1]*=1./(crosssection13ww)/2600.
  else:
    yields+=[(0,0)]

  if mass>=1200:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xww13."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[6])+float(split[21])+float(split[26]))/crosssection13ww/2300.,(float(split[11])+float(split[16])+float(split[31])+float(split[36]))/crosssection13ww/2300.)]
  else:
    yields+=[(0,0)]

  yields+=[(0,0)]

  yields+=[(0,0)]

  yields+=[(0,0)]

  yields+=[(0,0)]

  string+="$G_{bulk} \\to WW$ & "+str(int(mass/100)/10.)+" TeV &"
  for y1,y2 in yields:
    string+=" "+str(int(y1*1000)/10.).replace("0.0","-")+"/"+str(int(y2*1000)/10.).replace("0.0","-")+" &"
  string+="\\\\\n"
  print string


for mass in masses:
  xsec=open("../BulkG_EXO-15-002/xsect_BulkG_ZZ_c0p5_xsect_in_pb_factor4wrong.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection8zz=float(split[1])/4.

  xsec=open("../BulkG_EXO-15-002/xsect_BulkG_WW_c0p5_13TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssection13zz=float(split[1])/2.

  yields=[]
  if mass>=1000 and mass<2500:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xjj8."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[2]))/(crosssection8zz)/19700.,(float(split[5]))/(crosssection8zz)/19700.)]
  else:
    yields+=[(0,0)]

  yields+=[(0,0)]

  if mass<2500:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xzz."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[((float(split[1])+float(split[3]))/crosssection8zz/19700.,(float(split[5])+float(split[7]))/crosssection8zz/19700.)]
  else:
    yields+=[(0,0)]

  if mass>=1200:
   card=open("../BulkG_EXO-15-002/comb_"+str(mass)+"/comb_xjj13zz."+str(mass)+".txt")
   for l in card.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields+=[[(float(split[2])+float(split[5])+float(split[8])),(float(split[11])+float(split[14])+float(split[17]))]]
      yields[-1][0]*=1./(crosssection13zz)/2600.
      yields[-1][1]*=1./(crosssection13zz)/2600.
  else:
    yields+=[(0,0)]

  yields+=[(0,0)]

  yields+=[(0,0)]

  yields+=[(0,0)]

  yields+=[(0,0)]

  yields+=[(0,0)]

  string+="$G_{bulk} \\to ZZ$ & "+str(int(mass/100)/10.)+" TeV &"
  for y1,y2 in yields:
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