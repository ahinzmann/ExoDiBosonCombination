import ROOT
import sys
from ROOT import *
import CMS_lumi, tdrstyle
import time
from array import array

##################################################################################
def get_canvas(cname):

  CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
  CMS_lumi.lumi_13TeV = "2.2 fb^{-1}"
  CMS_lumi.writeExtraText = 1
  CMS_lumi.extraText = "Preliminary"

  iPos = 11
  if( iPos==0 ): CMS_lumi.relPosX = 0.12
  iPeriod=4
  
  H_ref = 700; 
  W_ref = 700; 
  W = W_ref
  H  = H_ref

  T = 0.08*H_ref
  B = 0.12*H_ref 
  L = 0.12*W_ref
  R = 0.04*W_ref

  canvas = ROOT.TCanvas(cname,cname,50,50,W,H)
  canvas.SetFillColor(0)
  canvas.SetBorderMode(0)
  canvas.SetFrameFillStyle(0)
  canvas.SetFrameBorderMode(0)
  canvas.SetLeftMargin( L/W )
  canvas.SetRightMargin( R/W )
  canvas.SetTopMargin( T/H )
  canvas.SetBottomMargin( B/H )
  #canvas.SetLeftMargin( 0.18 )
  #canvas.SetRightMargin( 0.06 )
  #canvas.SetTopMargin( 0.05 )
  #canvas.SetBottomMargin( 0.12 )
  canvas.SetTickx()
  canvas.SetTicky()
  canvas.SetGrid()
  
  return canvas

##################################################################################
def fill_histos_for_contour(mass,limit,max_width):
 
  limit = 0.0269150498482
  hname = ['h_M'+str(mass)+'_xsec','h_M'+str(mass)+'_width']
  h_list = []
  #h_list.append(ROOT.TH2F(hname[0], hname[0], 120,  -4., 4., 120,  -2., 2.)) #20,-4.,0.,20,0,2.
  #h_list.append(ROOT.TH2F(hname[1], hname[1], 120,  -4., 4., 120,  -2., 2.))
  h_list.append(ROOT.TH2F(hname[0], hname[0], 60,  0., 4., 60,  0., 2.)) #20,-4.,0.,20,0,2.
  h_list.append(ROOT.TH2F(hname[1], hname[1], 60,  0., 4., 60,  0., 2.))
      
  fname13 = 'scanHVT-M%s.root'%mass
  f13 = TFile.Open(fname13,"READ")
  t13 = f13.Get("hvtM%s"%mass)

  gV = array('f',[0])
  cH = array('f',[0])
  cF = array('f',[0])
  g = array('f',[0])
  br13 = array('f',[0])
  br8 = array('f',[0])
  w = array('f',[0])

  t13.SetBranchAddress('gV', gV)
  t13.SetBranchAddress('cH', cH)
  t13.SetBranchAddress('cF', cF)
  t13.SetBranchAddress('g', g)
  t13.SetBranchAddress('xsecTot_WV_13TeV', br13)
  t13.SetBranchAddress('xsecTot_WV_8TeV', br8)
  t13.SetBranchAddress('width_Wp_13TeV', w)
       
  for e in range(t13.GetEntries()):
   t13.GetEntry(e)
   br = br8[0]+br13[0]
   if br < limit:
     h_list[0].Fill(gV[0]*cH[0],g[0]*g[0]*cF[0]/gV[0])
   if w[0]/float(mass) < max_width:
     h_list[1].Fill(gV[0]*cH[0],g[0]*g[0]*cF[0]/gV[0])
	  
  for h in h_list:
   for bx in xrange(1,h.GetNbinsX()+1):
    for by in xrange(1,h.GetNbinsY()+1):
     ne = h.GetBinContent(bx,by)
     if ne != 0:
        h.SetBinContent(bx,by,1)
  
  return h_list

##################################################################################
def plot_graphs_for_contour(histo,opt):

   c = ROOT.TCanvas()
   c.cd()

   histo.Smooth()
   histo.SetContour(2)
   #histo.Draw("COLZ")
   histo.Draw("CONT Z LIST")
   #time.sleep(1000)

   c.Update()

   curves = []
   
   conts = ROOT.TObjArray(gROOT.GetListOfSpecials().FindObject("contours"))
   
   gs = ROOT.TGraphSmooth("normal")
   gin = ROOT.TGraph(conts.At(0).At(0))
   gout = gs.SmoothSuper(gin,"",3)

   x_m = array('d',[])
   x_p = array('d',[])
   y_m = array('d',[])
   y_p = array('d',[])
   npoints = gout.GetN()
   for p in xrange(0,npoints):
    gr_x = ROOT.Double(0.)
    gr_y = ROOT.Double(0.)
    gout.GetPoint(p,gr_x,gr_y)
    x_m.append(-gr_x)
    y_m.append(-gr_y)
    x_p.append(gr_x)
    y_p.append(gr_y)

   if opt == 'w':
    x_p[0] = 0.
    x_m[0] = 0.
      
   curves.append(ROOT.TGraph(len(x_p),x_p,y_p))
   curves.append(ROOT.TGraph(len(x_m),x_m,y_m))
   curves.append(ROOT.TGraph(len(x_p),x_p,y_m))
   curves.append(ROOT.TGraph(len(x_m),x_m,y_p))

   #ctest = TCanvas()
   #ctest.cd()
   #curves[3].Draw("ALP")
   #curves[3].Print()
   #print x_m
   #print y_p
   #time.sleep(1000)
   
   c.Close()  

   return curves

##################################################################################
def write_extra_text(text,textpos,col,opts):

   ptext = ROOT.TPaveText(textpos[0],textpos[1],textpos[2],textpos[3],"NDC")
   ptext.SetTextFont(42)
   ptext.SetTextSize(0.05)
   ptext.SetTextAlign(12)
   ptext.SetFillStyle(0)
   ptext.SetBorderSize(0)
   ptext.SetTextColor(col)
   ptext.AddText(text)
   
   if opts == 'w':
      ptext.SetFillStyle(1001)
      ptext.SetTextSize(0.03)
      ptext.SetFillColor(kWhite)

   return ptext

##################################################################################
gROOT.SetBatch(ROOT.kTRUE)
obs_lim = {'1500':0.0314,'2000': 0.0269,'3000': 0.0177}
max_width = 0.05
model = 'B3'
#model = 'A1'
#model = 'A3'

print ""

histos = {}

for m,l in obs_lim.iteritems():

   print "M %s : preparing 2D histos for width and xsec contours" %(m)
   histos[m] = fill_histos_for_contour(m,l,max_width)

print ""

g_xsec = {}
g_width = {}

for m in histos.keys():

   print "M %s : preparing graphs for width and xsec contours" %(m)
   g_width[m] = plot_graphs_for_contour(histos[m][1],'w')
   g_xsec[m] = plot_graphs_for_contour(histos[m][0],'')

##################################################################################   
colors = {'1000':kAzure+1,'1500':kBlack,'2000':kViolet+7, '3000': kTeal-8}
linestyle = {'1000':1,'1500':1,'2000':7,'3000':1}
lim_text_pos = {'1000':[0.5138191,0.4825175,0.5942211,0.5629371],'1500':[0.591954,0.360119,0.6522989,0.4300595],
                '2000':[0.6508621,0.5967262,0.7255747,0.6666667],'3000':[0.6609195,0.7514881,0.7284483,0.8214286]}
lim_extra_text = {'1000':'1 TeV','1500':'1.5 TeV','2000':'2 TeV','3000':'3 TeV'}
models_text_pos = {'A1':[0.49,0.34,0.55,0.41],'A3':[0.46,0.48,0.52,0.55],'B3':[0.1465517,0.5610119,0.204023,0.6324405]}
models_point = {'A1':[-0.4225,-0.43278],'A3':[-0.1447,-0.1447],'B3':[-2.928729,0.13883712988411501]}
models_extra_text = {'A1':'A(g_{V}=1)','A3':'A(g_{V}=3)','B3':'B(g_{V}=3)'}
width_extra_text = ['#frac{#Gamma_{th}}{M} > 5% #approx #frac{#sigma_{exp}}{M}']
width_text_pos = [0.1465517,0.1428571,0.341954,0.2127976]

tdrstyle.setTDRStyle()

canv = get_canvas("canv")
canv.cd()

mg = ROOT.TMultiGraph()

linewidth = [3502,3502,-3502,-3502]

idx = 0
for g in g_width['3000']:

   g.SetLineColor(kGray)
   g.SetLineStyle(7)
   g.SetFillColor(kGray)
   g.SetFillStyle(1001)
   g.SetLineWidth(linewidth[idx])
   g.RemovePoint(3)
   mg.Add(g)
   idx = idx+1
      
for m in obs_lim.keys():

   for g in g_xsec[m]:
   
     g.SetLineWidth(3)
     g.SetLineColor(colors[m])
     g.SetLineStyle(linestyle[m])
     mg.Add(g)
     
mg.Draw("AL")   
mg.GetXaxis().SetTitle("g_{V}c_{H}") 
mg.GetXaxis().SetRangeUser(-3.,3.)
mg.GetXaxis().SetTitleSize(0.05) 
mg.GetXaxis().SetTitleOffset(1.1)
mg.GetYaxis().SetTitle("g^{2}c_{F}/g_{V}")
mg.GetYaxis().SetTitleSize(0.05)  
mg.GetYaxis().SetTitleOffset(1.1)
mg.GetYaxis().SetRangeUser(-1.,1.)
mg.GetYaxis().SetNdivisions(505)

add_text = []
#for m in lim_text_pos.keys():
for m in obs_lim.keys():
   add_text.append(write_extra_text(lim_extra_text[m],lim_text_pos[m],colors[m],''))

x = array('d',[models_point[model][0]])
y = array('d',[models_point[model][1]])
g_model = ROOT.TGraph(1,x,y)
g_model.SetMarkerStyle(21)
g_model.SetMarkerColor(kMagenta)
g_model.Draw("Psame")
add_text.append(write_extra_text(models_extra_text[model],models_text_pos[model],kMagenta,''))

add_text.append(write_extra_text(width_extra_text[0],width_text_pos,kRed,'w'))

for t in add_text:
   t.Draw()
      
#--------------------------------
canv.Update()
canv.cd()

CMS_lumi.CMS_lumi(canv, 7, 11)
		
canv.cd()
canv.Update()
canv.RedrawAxis()
canv.RedrawAxis("g")
frame = canv.GetFrame()
frame.Draw()   
canv.cd()
canv.Update()

canv.SaveAs("hvt-couplings.pdf")
canv.SaveAs("hvt-couplings.png")
canv.SaveAs("hvt-couplings.eps")
canv.SaveAs("hvt-couplings.C")

