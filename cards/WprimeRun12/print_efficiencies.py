masses = [1200,2000,3000,4000]
yields1={}
yields2={}
crosssections={}
for mass in masses:
  xsec=open("theory_HVT_WZ_13TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssections[mass]=float(split[1])

  VWcard=open("comb_"+str(mass)+"/comb_xww13."+str(mass)+".txt")
  for l in VWcard.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields1[mass]=[float(split[1])+float(split[21]), float(split[11])+float(split[31]), float(split[6])+float(split[26]), float(split[16])+float(split[36])]

  VVcard=open("comb_"+str(mass)+"/comb_xjj13."+str(mass)+".txt")
  #VVcard=open("JJ_cards_13TeV/CMS_jj_WZfix_"+str(mass)+"_13TeV_CMS_jj_VVnew.txt")
  for l in VVcard.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields2[mass]=[float(split[2]),float(split[14]), float(split[6]),float(split[18]), float(split[10]),float(split[22])]

  string="HVT $W' \\to WZ$ & "+str(int(mass/100)/10.)+" TeV &"
  for y in yields2[mass]:
    string+=" "+str(int(y/crosssections[mass]/2100.*1000)/10.)+" &"
  for y in yields1[mass]:
    string+=" "+str(int(y/crosssections[mass]/2100.*1000)/10.)+" &"
  for i in range(3):
    string+=" &"
  string+="\\\\"
  print string
