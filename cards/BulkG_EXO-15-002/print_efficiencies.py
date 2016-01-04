masses = [1200,2000,3000,4000]
yields1={}
yields2={}
yields3={}
crosssections={}
for mass in masses:
  xsec=open("xsect_BulkG_WW_c0p5_13TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssections[mass]=float(split[1])

  VWcard=open("comb_"+str(mass)+"/comb_xww13."+str(mass)+".txt")
  for l in VWcard.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields1[mass]=[float(split[1])+float(split[21]), float(split[11])+float(split[31]), float(split[6])+float(split[26]), float(split[16])+float(split[36])]

  VVcard=open("comb_"+str(mass)+"/comb_xjj13ww."+str(mass)+".txt")
  for l in VVcard.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields2[mass]=[float(split[1]),float(split[10]), float(split[4]),float(split[13]), float(split[7]),float(split[16])]

  string="Bulk $G \\to WW$ & "+str(int(mass/100)/10.)+" TeV &"
  for y in yields2[mass]:
    string+=" "+str(int(y/crosssections[mass]/2100.*1000)/10.)+" &"
  for y in yields1[mass]:
    string+=" "+str(int(y/crosssections[mass]/2100.*1000)/10.)+" &"
  #for i in range(3):
  #  string+=" &"
  string+="\\\\"
  print string
  
for mass in masses:
  xsec=open("xsect_BulkG_WW_c0p5_13TeV.txt")
  for l in xsec.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]==str(mass):
      crosssections[mass]=float(split[1])

  VVcard=open("comb_"+str(mass)+"/comb_xjj13zz."+str(mass)+".txt")
  for l in VVcard.readlines():
    split=l.replace("\n"," ").replace("\t"," ").replace("     "," ").replace("    "," ").replace("   "," ").replace("  "," ").split(" ")
    if split[0]=="rate":
      yields3[mass]=[float(split[2]),float(split[11]), float(split[5]),float(split[14]), float(split[8]),float(split[17])]

  string="Bulk $G \\to ZZ$ & "+str(int(mass/100)/10.)+" TeV &"
  for y in yields3[mass]:
    string+=" "+str(int(y/crosssections[mass]/2100.*1000)/10.)+" &"
  for i in range(4):
    string+="- &"
  string+="\\\\"
  print string
