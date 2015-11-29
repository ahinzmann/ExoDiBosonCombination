masses = [1000,2000,3000,4000]
yields={}
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
      yields[mass]=[float(split[1])+float(split[21]), float(split[11])+float(split[31]), float(split[6])+float(split[26]), float(split[16])+float(split[36])]

  string="HVT $W' \\to WZ$ & "+str(mass/1000)+" TeV &"
  for i in range(6):
    string+=" &"
  for y in yields[mass]:
    string+=" "+str(int(y/crosssections[mass]/2100.*1000)/10.)+" &"
  for i in range(3):
    string+=" &"
  string+="\\\\"
  print string
