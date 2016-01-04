void MakeDatacard_fineBinning(){
  gROOT->Reset();
  gStyle->SetCanvasColor(0);
  gStyle->SetFrameBorderMode(0);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1,0);
  gStyle->SetTitleX(0.5);
  gStyle->SetTitleY(0.96);
  gStyle->SetPaintTextFormat(".2f");
  gStyle->SetEndErrorSize(8);
  RooMsgService::instance().setGlobalKillBelow(RooFit::WARNING) ;
  using namespace TMath;
  
  float XMassWidth=200; float XMassBin=15; float XMassMin=0; float XMassMax=XMassWidth;
  float lep1PtCut=10; float tauPtCut=35; int bTagCut=1; float deltaRCut=1; float MassSvfitCut=10000; float METCutFL = 100; float METCutSL = 50; float MassVisCut=0;
	
  int SignalMass      = 1000;
  float SigYield      = 0;
  float DATYield      = 0;
  float BkgYield      = 0;
  float BkgYieldErr   = 0;
  float Alpha1        = 0;
  float Alpha2        = 0;
  float AlphaERR1     = 0;
  float AlphaERR2     = 0;
  float Nsideband     = 0;
  int WIDTH=150;
  int MIN=850;
  int MAX=1000; 
  char cutMC1[1000]; char cutMC2[1000]; char cutData1[1000]; char cutData2[1000]; char cutSIG[1000];
  float NORM=1; float NORMerr=1; float NORMforALPHA=1;

  for(int i=0; i<18; i++){
    SignalMass=800+i*100;
    if(SignalMass==800){
      WIDTH=125;
      MIN=675;
      MAX=800;
      const int N = 14;
      Double_t xbins[N] = {0,300,550,675,800,925,1150,1300,1500,1700,1900,2200,2500,3000};
    } else if(SignalMass==900){
      WIDTH=150;
      MIN=750;
      MAX=900;
      const int N = 13;
      Double_t xbins[N] = {0,300,500,750,900,1050,1250,1500,1750,2000,2250,2500,3000};
    } else if(SignalMass==1000){
      WIDTH=150;
      MIN=850;
      MAX=1000;
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,1900,2200,2500,3000};
    } else if(SignalMass==1100){
      WIDTH=150;
      MIN=950;
      MAX=1100;
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,950,1100,1150,1300,1500,1700,1900,2200,2500,3000};
    } else if(SignalMass==1200){
      WIDTH=200;
      MIN=1000;
      MAX=1200;
      const int N = 13;
      Double_t xbins[N] = {0,300,500,750,1000,1200,1400,1600,1800,2000,2250,2500,3000};
    } else if(SignalMass==1300){
      WIDTH=200;
      MIN=1100;
      MAX=1300;
      const int N = 13;
      Double_t xbins[N] = {0,300,500,750,900,1100,1300,1600,1800,2000,2250,2500,3000};
    } else if(SignalMass==1400){
      WIDTH=200;
      MIN=1200;
      MAX=1400;
      const int N = 13;
      Double_t xbins[N] = {0,300,500,750,1000,1200,1400,1600,1800,2000,2250,2500,3000};
    } else if(SignalMass==1500){
      WIDTH=250;
      MIN=1250;
      MAX=1500;
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1250,1500,1750,2000,2250,2500,3200};
    } else if(SignalMass==1600){
      WIDTH=250;
      MIN=1350;
      MAX=1600;
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1350,1600,1750,2000,2250,2500,3200};
    } else if(SignalMass==1700){
      WIDTH=250;
      MIN=1450;
      MAX=1700;
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1250,1450,1700,2000,2250,2500,3200};
    } else if(SignalMass==1800){
      WIDTH=250;
      MIN=1550;
      MAX=1800;
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1250,1550,1800,2000,2250,2500,3200};
    } else if(SignalMass==1900){
      WIDTH=250;
      MIN=1650;
      MAX=1900;
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1250,1500,1650,1900,2250,2500,3200};
    } else if(SignalMass==2000){
      WIDTH=300;
      MIN=1700;
      MAX=2000;
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,2000,2300,2500,3000};
    } else if(SignalMass==2100){
      WIDTH=300;
      MIN=1800;
      MAX=2100;
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1800,2100,2300,2500,3000};
    } else if(SignalMass==2200){
      WIDTH=300;
      MIN=1900;
      MAX=2200;
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,1900,2200,2500,3000};
    } else if(SignalMass==2300){
      WIDTH=400;
      MIN=1900;
      MAX=2300;
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,1900,2300,2500,3000};
    } else if(SignalMass==2400){
      WIDTH=400;
      MIN=2000;
      MAX=2400;
      const int N = 13;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,2000,2400,3000};
    } else if(SignalMass==2500){
      WIDTH=450;
      MIN=2050;
      MAX=2500;
      const int N = 13;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1550,1800,2050,2500,2950};
    }
  
    TH1F *histo_PRE1 = new TH1F("histo_PRE1","histo_PRE1",N-1,xbins); 
    TH1F *histo_DAT1 = new TH1F("histo_DAT1","histo_DAT1",N-1,xbins); 
    TH1F *ERR1       = new TH1F("ERR1",      "ERR1",      N-1,xbins); 
    THStack *hs1     = new THStack("hs1","hs1");
    TH1F *histo_PRE2 = new TH1F("histo_PRE2","histo_PRE2",N-1,xbins); 
    TH1F *histo_DAT2 = new TH1F("histo_DAT2","histo_DAT2",N-1,xbins); 
    TH1F *ERR2       = new TH1F("ERR2",      "ERR2",      N-1,xbins); 
    THStack *hs2     = new THStack("hs2","hs2");
    TH1F *histo_PRE3 = new TH1F("histo_PRE3","histo_PRE3",N-1,xbins);
    TH1F *histo_DAT3 = new TH1F("histo_DAT3","histo_DAT3",N-1,xbins); 
    TH1F *ERR3       = new TH1F("ERR3",      "ERR3",      N-1,xbins); 
    THStack *hs3     = new THStack("hs3","hs3");
    TH1F *histo_PRE4 = new TH1F("histo_PRE4","histo_PRE4",N-1,xbins);
    TH1F *histo_DAT4 = new TH1F("histo_DAT4","histo_DAT4",N-1,xbins); 
    TH1F *ERR4       = new TH1F("ERR4",      "ERR4",      N-1,xbins); 
    THStack *hs4     = new THStack("hs4","hs4"); 
    TH1F *histo_PRE5 = new TH1F("histo_PRE5","histo_PRE5",N-1,xbins);
    TH1F *histo_DAT5 = new TH1F("histo_DAT5","histo_DAT5",N-1,xbins); 
    TH1F *ERR5       = new TH1F("ERR5",      "ERR5",      N-1,xbins); 
    THStack *hs5     = new THStack("hs5","hs5");

    TCanvas* c1 = new TCanvas("c1","c1",0,0,900,600); 
    MakeSelection("EleMuo", cutMC1, cutMC2, cutData1, cutData2, cutSIG, lep1PtCut, tauPtCut, bTagCut, METCutFL, deltaRCut, MassSvfitCut, MassVisCut);
    Normalization("EleMuo", NORM, NORMerr, cutMC1, cutMC2, cutData1, cutData2);
    BackgroundEstimation("EleMuo",XMassWidth,XMassBin,XMassMin,XMassMax,histo_PRE2,histo_DAT2,ERR2,hs2,cutMC1, cutMC2, cutData1, cutData2, NORM, NORMerr,NORMforALPHA,SignalMass,DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2);
    SignalYield("EleMuo",WIDTH,MIN,MAX,SignalMass,cutSIG, SigYield);
    SaveDatacard("EleMuo",DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2,NORMforALPHA,SigYield,SignalMass,lep1PtCut,tauPtCut,bTagCut,METCutFL,deltaRCut,MassSvfitCut,MassVisCut);
    
    TCanvas* c2 = new TCanvas("c2","c2",0,0,900,600);
    MakeSelection("MuoMuo", cutMC1, cutMC2, cutData1, cutData2, cutSIG, lep1PtCut, tauPtCut, bTagCut, METCutFL, deltaRCut, MassSvfitCut, MassVisCut);
    Normalization("MuoMuo", NORM, NORMerr, cutMC1, cutMC2, cutData1, cutData2);
    BackgroundEstimation("MuoMuo",XMassWidth,XMassBin,XMassMin,XMassMax,histo_PRE1,histo_DAT1,ERR1,hs1,cutMC1, cutMC2, cutData1, cutData2, NORM, NORMerr,NORMforALPHA,SignalMass,DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2);
    SignalYield("MuoMuo",WIDTH,MIN,MAX,SignalMass,cutSIG,SigYield);
    SaveDatacard("MuoMuo",DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2,NORMforALPHA,SigYield,SignalMass,lep1PtCut,tauPtCut,bTagCut,METCutFL,deltaRCut,MassSvfitCut,MassVisCut);
    
    TCanvas* c3 = new TCanvas("c3","c3",0,0,900,600);
    MakeSelection("EleEle", cutMC1, cutMC2, cutData1, cutData2, cutSIG, lep1PtCut, tauPtCut, bTagCut, METCutFL, deltaRCut, MassSvfitCut, MassVisCut);
    Normalization("EleEle", NORM, NORMerr, cutMC1, cutMC2, cutData1, cutData2);
    BackgroundEstimation("EleEle",XMassWidth,XMassBin,XMassMin,XMassMax,histo_PRE3,histo_DAT3,ERR3,hs3,cutMC1, cutMC2, cutData1, cutData2, NORM, NORMerr,NORMforALPHA,SignalMass,DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2);
    SignalYield("EleEle",WIDTH,MIN,MAX,SignalMass,cutSIG,SigYield);
    SaveDatacard("EleEle",DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2,NORMforALPHA,SigYield,SignalMass,lep1PtCut,tauPtCut,bTagCut,METCutFL,deltaRCut,MassSvfitCut,MassVisCut);
    
    TCanvas* c4 = new TCanvas("c4","c4",0,0,900,600);
    MakeSelection("MuoTau", cutMC1, cutMC2, cutData1, cutData2, cutSIG, lep1PtCut, tauPtCut, bTagCut, METCutSL, deltaRCut, MassSvfitCut, MassVisCut);
    Normalization("MuoTau", NORM, NORMerr, cutMC1, cutMC2, cutData1, cutData2);
    BackgroundEstimation("MuoTau",XMassWidth,XMassBin,XMassMin,XMassMax,histo_PRE5,histo_DAT5,ERR5,hs5,cutMC1, cutMC2, cutData1, cutData2, NORM, NORMerr,NORMforALPHA,SignalMass,DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2);
    SignalYield("MuoTau",WIDTH,MIN,MAX,SignalMass,cutSIG,SigYield);
    SaveDatacard("MuoTau",DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2,NORMforALPHA,SigYield,SignalMass,lep1PtCut,tauPtCut,bTagCut,METCutSL,deltaRCut,MassSvfitCut,MassVisCut);
    
    TCanvas* c5 = new TCanvas("c5","c5",0,0,900,600);
    MakeSelection("EleTau", cutMC1, cutMC2, cutData1, cutData2, cutSIG, lep1PtCut, tauPtCut, bTagCut, METCutSL, deltaRCut, MassSvfitCut, MassVisCut);
    Normalization("EleTau", NORM, NORMerr, cutMC1, cutMC2, cutData1, cutData2);
    BackgroundEstimation("EleTau",XMassWidth,XMassBin,XMassMin,XMassMax,histo_PRE4,histo_DAT4,ERR4,hs4,cutMC1, cutMC2, cutData1, cutData2, NORM, NORMerr,NORMforALPHA,SignalMass,DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2);
    SignalYield("EleTau",WIDTH,MIN,MAX,SignalMass,cutSIG,SigYield);
    SaveDatacard("EleTau",DATYield,BkgYield,BkgYieldErr,Nsideband,Alpha1,Alpha2,AlphaERR1,AlphaERR2,NORMforALPHA,SigYield,SignalMass,lep1PtCut,tauPtCut,bTagCut,METCutSL,deltaRCut,MassSvfitCut,MassVisCut);
  }    
}


void MakeSelection(char *channel, char & *cutMC1, char & *cutMC2, char & *cutData1, char & *cutData2, char & *cutSIG, float lep1PtCut, float tauPtCut, 
		   int bTagCut, float METCut, float deltaRCut, float MassSvfitCut, float MassVisCut){
  TString CHANNEL = channel; 
  char BTAG[1000]; sprintf(BTAG, "");
  if(bTagCut==1) {sprintf(BTAG, " && nbtagsL1<1");}
  if(bTagCut==2) {sprintf(BTAG, " && nbtagsL1<2");}
  if(bTagCut==3) {sprintf(BTAG, " && nbtagsM1<1");}
  if(bTagCut==4) {sprintf(BTAG, " && nbtagsM1<2");}
  if(bTagCut==5) {sprintf(BTAG, " && nbtagsT1<1");}
  if(bTagCut==6) {sprintf(BTAG, " && nbtagsT1<2");}
  char cutPre[1000]; sprintf(cutPre, "PUWeight*SFWeight*(PtSvfit>100 && met>%f && dRLep1Lep2<%f && MassSvfit<%f && MassVis>%f %s",
			     METCut,deltaRCut,MassSvfitCut,MassVisCut,BTAG);
  char cutPreSIG[1000]; sprintf(cutPreSIG, "PUWeight*SFWeight*BTWeight*(PtSvfit>100 && met>%f && dRLep1Lep2<%f && MassSvfit<%f && MassVis>%f %s",
				METCut,deltaRCut,MassSvfitCut,MassVisCut,BTAG);
  char MuoTauVETO[1000]; char EleTauVETO[1000]; 
  sprintf(MuoTauVETO, "(EleMuo==0 || (EleMuo==1 && met<100)) && (MuoMuo==0 || (MuoMuo==1 && met<100)) && (EleEle==0 || (EleEle==1 && met<100))");
  sprintf(EleTauVETO, "(EleMuo==0 || (EleMuo==1 && met<100)) && (MuoMuo==0 || (MuoMuo==1 && met<100)) && (EleEle==0 || (EleEle==1 && met<100)) && MuoTau==0");

  if(CHANNEL=="EleMuo")     sprintf(cutSIG,  "%s",cutPreSIG);
  else if(CHANNEL=="MuoMuo")sprintf(cutSIG,  "%s && EleMuo==0 && lep1Pt>%f",cutPreSIG,lep1PtCut);
  else if(CHANNEL=="EleEle")sprintf(cutSIG,  "%s && EleMuo==0 && MuoMuo==0 && lep1Pt>%f",cutPreSIG,lep1PtCut);
  else if(CHANNEL=="MuoTau")sprintf(cutSIG,  "%s && %s && lep1Pt>%f",cutPreSIG,MuoTauVETO,tauPtCut);
  else if(CHANNEL=="EleTau")sprintf(cutSIG,  "%s && %s && lep1Pt>%f",cutPreSIG,EleTauVETO,tauPtCut);

  if(CHANNEL=="EleMuo")     sprintf(cutMC1,  "%s",cutPre);
  else if(CHANNEL=="MuoMuo")sprintf(cutMC1,  "%s && EleMuo==0 && lep1Pt>%f",cutPre,lep1PtCut);
  else if(CHANNEL=="EleEle")sprintf(cutMC1,  "%s && EleMuo==0 && MuoMuo==0 && lep1Pt>%f",cutPre,lep1PtCut);
  else if(CHANNEL=="MuoTau")sprintf(cutMC1,  "%s && %s && lep1Pt>%f",cutPre,MuoTauVETO,tauPtCut);
  else if(CHANNEL=="EleTau")sprintf(cutMC1,  "%s && %s && lep1Pt>%f",cutPre,EleTauVETO,tauPtCut);

  if(CHANNEL=="EleMuo")     sprintf(cutMC2,  "%s && (jetMass<70 || jetMass>140)",cutPre);
  else if(CHANNEL=="MuoMuo")sprintf(cutMC2,  "%s && (jetMass<70 || jetMass>140) && EleMuo==0 && lep1Pt>%f",cutPre,lep1PtCut);
  else if(CHANNEL=="EleEle")sprintf(cutMC2,  "%s && (jetMass<70 || jetMass>140) && EleMuo==0 && MuoMuo==0 && lep1Pt>%f",cutPre,lep1PtCut);
  else if(CHANNEL=="MuoTau")sprintf(cutMC2,  "%s && (jetMass<70 || jetMass>140) && %s && lep1Pt>%f",cutPre,MuoTauVETO,tauPtCut);
  else if(CHANNEL=="EleTau")sprintf(cutMC2,  "%s && (jetMass<70 || jetMass>140) && %s && lep1Pt>%f",cutPre,EleTauVETO,tauPtCut);

  if(CHANNEL=="EleMuo")     sprintf(cutData1, "%s && trigger==1",cutPre);
  else if(CHANNEL=="MuoMuo")sprintf(cutData1, "%s && trigger==1 && EleMuo==0 && lep1Pt>%f",cutPre,lep1PtCut);
  else if(CHANNEL=="EleEle")sprintf(cutData1, "%s && trigger==1 && EleMuo==0 && MuoMuo==0 && lep1Pt>%f",cutPre,lep1PtCut);
  else if(CHANNEL=="MuoTau")sprintf(cutData1, "%s && trigger==1 && %s && lep1Pt>%f",cutPre,MuoTauVETO,tauPtCut);
  else if(CHANNEL=="EleTau")sprintf(cutData1, "%s && trigger==1 && %s && lep1Pt>%f",cutPre,EleTauVETO,tauPtCut);

  if(CHANNEL=="EleMuo")     sprintf(cutData2, "%s && trigger==1 && (jetMass<70 || jetMass>140)",cutPre);
  else if(CHANNEL=="MuoMuo")sprintf(cutData2, "%s && trigger==1 && (jetMass<70 || jetMass>140) && EleMuo==0 && lep1Pt>%f",cutPre,lep1PtCut);
  else if(CHANNEL=="EleEle")sprintf(cutData2, "%s && trigger==1 && (jetMass<70 || jetMass>140) && EleMuo==0 && MuoMuo==0 && lep1Pt>%f",cutPre,lep1PtCut);
  else if(CHANNEL=="MuoTau")sprintf(cutData2, "%s && trigger==1 && (jetMass<70 || jetMass>140) && %s && lep1Pt>%f",cutPre,MuoTauVETO,tauPtCut);
  else if(CHANNEL=="EleTau")sprintf(cutData2, "%s && trigger==1 && (jetMass<70 || jetMass>140) && %s && lep1Pt>%f",cutPre,EleTauVETO,tauPtCut);
}


void BackgroundEstimation(char *channel, float XMassWidth, float XMassBin, float XMassMin, float XMassMax, TH1F *histo_PRE, TH1F *histo_DAT, TH1F *ERR, 
			  THStack *hs, char *cutMC1, char *cutMC2, char *cutData1, char *cutData2, float NORM, float NORMerr, float & NORMforALPHA,
			  int SignalMass, float & DATYield, float & BkgYield, float & BkgYieldErr, float & Nsideband, float & Alpha1, float & Alpha2, 
			  float & AlphaERR1, float & AlphaERR2){

  Nsideband=0; DATYield=0; BkgYield=0; BkgYieldErr=0; Alpha1=0; Alpha2=0; AlphaERR1=0; AlphaERR2=0;
  float Nsideband1=0; float Nsideband2=0;
  TCanvas* canvasAlpha = new TCanvas("canvasAlpha","canvasAlpha",0,0,900,600);
  canvasAlpha->cd();

  float MAX = XMassWidth*XMassBin;
  char *plot = "met";
  int bin=1; 
  float min=0; 
  float max=50000; 
  char demoSB1    [1000]; sprintf(demoSB1,    "demo/TreeSB1"); 
  char openTreeSB1[1000]; sprintf(openTreeSB1,"%s%s",demoSB1,channel);
  char demoSB2    [1000]; sprintf(demoSB2,    "demo/TreeSB2"); 
  char openTreeSB2[1000]; sprintf(openTreeSB2,"%s%s",demoSB2,channel);
  char demoSB3    [1000]; sprintf(demoSB3,    "demo/TreeSB3"); 
  char openTreeSB3[1000]; sprintf(openTreeSB3,"%s%s",demoSB3,channel);
  char demo       [1000]; sprintf(demo,       "demo/Tree"); 
  char openTree   [1000]; sprintf(openTree,   "%s%s",demo,channel); 
  TString CHANNEL = channel;  

    if(SignalMass==800){
      const int N = 14;
      Double_t xbins[N] = {0,300,550,675,800,925,1150,1300,1500,1700,1900,2200,2500,3000};
    } else if(SignalMass==900){
      const int N = 13;
      Double_t xbins[N] = {0,300,500,750,900,1050,1250,1500,1750,2000,2250,2500,3000};
    } else if(SignalMass==1000){
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,1900,2200,2500,3000};
    } else if(SignalMass==1100){
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,950,1100,1150,1300,1500,1700,1900,2200,2500,3000};
    } else if(SignalMass==1200){
      const int N = 13;
      Double_t xbins[N] = {0,300,500,750,1000,1200,1400,1600,1800,2000,2250,2500,3000};
    } else if(SignalMass==1300){
      const int N = 13;
      Double_t xbins[N] = {0,300,500,750,900,1100,1300,1600,1800,2000,2250,2500,3000};
    } else if(SignalMass==1400){
      const int N = 13;
      Double_t xbins[N] = {0,300,500,750,1000,1200,1400,1600,1800,2000,2250,2500,3000};
    } else if(SignalMass==1500){
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1250,1500,1750,2000,2250,2500,3200};
    } else if(SignalMass==1600){
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1350,1600,1750,2000,2250,2500,3200};
    } else if(SignalMass==1700){
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1250,1450,1700,2000,2250,2500,3200};
    } else if(SignalMass==1800){
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1250,1550,1800,2000,2250,2500,3200};
    } else if(SignalMass==1900){
      const int N = 12;
      Double_t xbins[N] = {0,300,500,750,1000,1250,1500,1650,1900,2250,2500,3200};
    } else if(SignalMass==2000){
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,2000,2300,2500,3000};
    } else if(SignalMass==2100){
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1800,2100,2300,2500,3000};
    } else if(SignalMass==2200){
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,1900,2200,2500,3000};
    } else if(SignalMass==2300){
      const int N = 14;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,1900,2300,2500,3000};
    } else if(SignalMass==2400){
      const int N = 13;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1500,1700,2000,2400,3000};
    } else if(SignalMass==2500){
      const int N = 13;
      Double_t xbins[N] = {0,300,550,700,850,1000,1150,1300,1550,1800,2050,2500,2950};
    }

  TH1F *DY        = new TH1F("DY",       "DY",       N-1,xbins);
  TH1F *TTbar     = new TH1F("TTbar",    "TTbar",    N-1,xbins);
  TH1F *DIBOSON   = new TH1F("DIBOSON",  "DIBOSON",  N-1,xbins); 
  TH1F *WJETS     = new TH1F("WJETS",    "WJETS",    N-1,xbins); 
  TH1F *QCD       = new TH1F("QCD",      "QCD",      N-1,xbins); 
  TH1F *SINGLETOP = new TH1F("SINGLETOP","SINGLETOP",N-1,xbins); 
  TH1F *Nsb       = new TH1F("Nsb",   "Nsb",         N-1,xbins);
  TH1F *Alpha     = new TH1F("Alpha", "Alpha",       N-1,xbins);
	
  TFile *file01 = TFile::Open("data.root");      
  TFile *file02 = TFile::Open("DY100.root");     
  TFile *file03 = TFile::Open("DY70.root");      
  TFile *file04 = TFile::Open("DYM50_100.root"); 
  TFile *file05 = TFile::Open("DYM50_70.root");  
  TFile *file06 = TFile::Open("QCD1000.root");   
  TFile *file07 = TFile::Open("QCD250.root");    
  TFile *file08 = TFile::Open("QCD500.root");    
  TFile *file09 = TFile::Open("TT.root");        
  TFile *file10 = TFile::Open("WJetsHT.root");  
  TFile *file11 = TFile::Open("WW.root");         
  TFile *file12 = TFile::Open("WZ.root");         
  TFile *file13 = TFile::Open("ZZ.root");        
  TFile *file14 = TFile::Open("SingleTop1.root");
  TFile *file15 = TFile::Open("SingleTop2.root");
  TFile *file16 = TFile::Open("SingleTop3.root");
  TFile *file17 = TFile::Open("SingleTop4.root");
  TFile *file18 = TFile::Open("SingleTop5.root");
  TFile *file19 = TFile::Open("SingleTop6.root");

  TTree *Tree01=(TTree*)file01->Get(openTreeSB1);  TTree *Tree20=(TTree*)file01->Get(openTree); 
  TTree *Tree02=(TTree*)file02->Get(openTreeSB1);  TTree *Tree21=(TTree*)file02->Get(openTree); 
  TTree *Tree03=(TTree*)file03->Get(openTreeSB1);  TTree *Tree22=(TTree*)file03->Get(openTree); 
  TTree *Tree04=(TTree*)file04->Get(openTreeSB1);  TTree *Tree23=(TTree*)file04->Get(openTree); 
  TTree *Tree05=(TTree*)file05->Get(openTreeSB1);  TTree *Tree24=(TTree*)file05->Get(openTree); 
  TTree *Tree06=(TTree*)file06->Get(openTreeSB1);  TTree *Tree25=(TTree*)file06->Get(openTree); 
  TTree *Tree07=(TTree*)file07->Get(openTreeSB1);  TTree *Tree26=(TTree*)file07->Get(openTree); 
  TTree *Tree08=(TTree*)file08->Get(openTreeSB1);  TTree *Tree27=(TTree*)file08->Get(openTree); 
  TTree *Tree09=(TTree*)file09->Get(openTreeSB1);  TTree *Tree28=(TTree*)file09->Get(openTree); 
  TTree *Tree10=(TTree*)file10->Get(openTreeSB1);  TTree *Tree29=(TTree*)file10->Get(openTree); 
  TTree *Tree11=(TTree*)file11->Get(openTreeSB1);  TTree *Tree30=(TTree*)file11->Get(openTree); 
  TTree *Tree12=(TTree*)file12->Get(openTreeSB1);  TTree *Tree31=(TTree*)file12->Get(openTree); 
  TTree *Tree13=(TTree*)file13->Get(openTreeSB1);  TTree *Tree32=(TTree*)file13->Get(openTree); 
  TTree *Tree14=(TTree*)file14->Get(openTreeSB1);  TTree *Tree33=(TTree*)file14->Get(openTree); 
  TTree *Tree15=(TTree*)file15->Get(openTreeSB1);  TTree *Tree34=(TTree*)file15->Get(openTree); 
  TTree *Tree16=(TTree*)file16->Get(openTreeSB1);  TTree *Tree35=(TTree*)file16->Get(openTree); 
  TTree *Tree17=(TTree*)file17->Get(openTreeSB1);  TTree *Tree36=(TTree*)file17->Get(openTree); 
  TTree *Tree18=(TTree*)file18->Get(openTreeSB1);  TTree *Tree37=(TTree*)file18->Get(openTree); 
  TTree *Tree19=(TTree*)file19->Get(openTreeSB1);  TTree *Tree38=(TTree*)file19->Get(openTree); 

  TTree *Tree39=(TTree*)file01->Get(openTreeSB2);  TTree *Tree58=(TTree*)file01->Get(openTreeSB3); 
  TTree *Tree40=(TTree*)file02->Get(openTreeSB2);  TTree *Tree59=(TTree*)file02->Get(openTreeSB3); 
  TTree *Tree41=(TTree*)file03->Get(openTreeSB2);  TTree *Tree60=(TTree*)file03->Get(openTreeSB3); 
  TTree *Tree42=(TTree*)file04->Get(openTreeSB2);  TTree *Tree61=(TTree*)file04->Get(openTreeSB3); 
  TTree *Tree43=(TTree*)file05->Get(openTreeSB2);  TTree *Tree62=(TTree*)file05->Get(openTreeSB3); 
  TTree *Tree44=(TTree*)file06->Get(openTreeSB2);  TTree *Tree63=(TTree*)file06->Get(openTreeSB3); 
  TTree *Tree45=(TTree*)file07->Get(openTreeSB2);  TTree *Tree64=(TTree*)file07->Get(openTreeSB3); 
  TTree *Tree46=(TTree*)file08->Get(openTreeSB2);  TTree *Tree65=(TTree*)file08->Get(openTreeSB3); 
  TTree *Tree47=(TTree*)file09->Get(openTreeSB2);  TTree *Tree66=(TTree*)file09->Get(openTreeSB3); 
  TTree *Tree48=(TTree*)file10->Get(openTreeSB2);  TTree *Tree67=(TTree*)file10->Get(openTreeSB3); 
  TTree *Tree49=(TTree*)file11->Get(openTreeSB2);  TTree *Tree68=(TTree*)file11->Get(openTreeSB3); 
  TTree *Tree50=(TTree*)file12->Get(openTreeSB2);  TTree *Tree69=(TTree*)file12->Get(openTreeSB3); 
  TTree *Tree51=(TTree*)file13->Get(openTreeSB2);  TTree *Tree70=(TTree*)file13->Get(openTreeSB3); 
  TTree *Tree52=(TTree*)file14->Get(openTreeSB2);  TTree *Tree71=(TTree*)file14->Get(openTreeSB3); 
  TTree *Tree53=(TTree*)file15->Get(openTreeSB2);  TTree *Tree72=(TTree*)file15->Get(openTreeSB3); 
  TTree *Tree54=(TTree*)file16->Get(openTreeSB2);  TTree *Tree73=(TTree*)file16->Get(openTreeSB3); 
  TTree *Tree55=(TTree*)file17->Get(openTreeSB2);  TTree *Tree74=(TTree*)file17->Get(openTreeSB3); 
  TTree *Tree56=(TTree*)file18->Get(openTreeSB2);  TTree *Tree75=(TTree*)file18->Get(openTreeSB3); 
  TTree *Tree57=(TTree*)file19->Get(openTreeSB2);  TTree *Tree76=(TTree*)file19->Get(openTreeSB3); 

  int AAA1=-1; int AAA2=0;
  for(int i=0; i<N-1; i++){
    AAA1=AAA1+1;
    AAA2=AAA2+1;
    TH1F *data       = new TH1F("","",bin,min,max);      TH1F *data_SR       = new TH1F("","",bin,min,max);
    TH1F *DY100      = new TH1F("","",bin,min,max);	 TH1F *DY100_SR      = new TH1F("","",bin,min,max);
    TH1F *DY70       = new TH1F("","",bin,min,max);	 TH1F *DY70_SR       = new TH1F("","",bin,min,max);
    TH1F *DYM50_100  = new TH1F("","",bin,min,max);	 TH1F *DYM50_100_SR  = new TH1F("","",bin,min,max);
    TH1F *DYM50_70   = new TH1F("","",bin,min,max);	 TH1F *DYM50_70_SR   = new TH1F("","",bin,min,max);
    TH1F *QCD1000    = new TH1F("","",bin,min,max);	 TH1F *TT_SR         = new TH1F("","",bin,min,max);
    TH1F *QCD250     = new TH1F("","",bin,min,max);	 TH1F *QCD1000_SR    = new TH1F("","",bin,min,max);
    TH1F *QCD500     = new TH1F("","",bin,min,max);	 TH1F *QCD250_SR     = new TH1F("","",bin,min,max);
    TH1F *TT         = new TH1F("","",bin,min,max);	 TH1F *QCD500_SR     = new TH1F("","",bin,min,max);
    TH1F *WJetsHT    = new TH1F("","",bin,min,max);	 TH1F *WJetsHT_SR    = new TH1F("","",bin,min,max);
    TH1F *WW         = new TH1F("","",bin,min,max);	 TH1F *WW_SR         = new TH1F("","",bin,min,max);
    TH1F *WZ         = new TH1F("","",bin,min,max);	 TH1F *WZ_SR         = new TH1F("","",bin,min,max);
    TH1F *ZZ         = new TH1F("","",bin,min,max);	 TH1F *ZZ_SR         = new TH1F("","",bin,min,max);
    TH1F *SingleTop1 = new TH1F("","",bin,min,max);      TH1F *SingleTop1_SR = new TH1F("","",bin,min,max);
    TH1F *SingleTop2 = new TH1F("","",bin,min,max);	 TH1F *SingleTop2_SR = new TH1F("","",bin,min,max);
    TH1F *SingleTop3 = new TH1F("","",bin,min,max);	 TH1F *SingleTop3_SR = new TH1F("","",bin,min,max);
    TH1F *SingleTop4 = new TH1F("","",bin,min,max);	 TH1F *SingleTop4_SR = new TH1F("","",bin,min,max);
    TH1F *SingleTop5 = new TH1F("","",bin,min,max);	 TH1F *SingleTop5_SR = new TH1F("","",bin,min,max);
    TH1F *SingleTop6 = new TH1F("","",bin,min,max);	 TH1F *SingleTop6_SR = new TH1F("","",bin,min,max);
	
    char CUTMC1[1000]; char CUTMC2[1000]; char CUTData1[1000]; char CUTData2[1000];
    sprintf(CUTMC1,   "%s && XMassSVFit>%f && XMassSVFit<%f)", cutMC1,   xbins[AAA1], xbins[AAA2]);
    sprintf(CUTMC2,   "%s && XMassSVFit>%f && XMassSVFit<%f)", cutMC2,   xbins[AAA1], xbins[AAA2]);
    sprintf(CUTData1, "%s && XMassSVFit>%f && XMassSVFit<%f)", cutData1, xbins[AAA1], xbins[AAA2]);
    sprintf(CUTData2, "%s && XMassSVFit>%f && XMassSVFit<%f)", cutData2, xbins[AAA1], xbins[AAA2]);

    char input01[50];sprintf(input01,"%s>>h01(%i,%f,%f)",plot,bin,min,max);Tree01->Draw(input01,CUTData1,"E");if(Tree01->Draw(input01,CUTData1,"E")){data          = h01; }
    char input02[50];sprintf(input02,"%s>>h02(%i,%f,%f)",plot,bin,min,max);Tree02->Draw(input02,CUTMC1);      if(Tree02->Draw(input02,CUTMC1))      {DY100         = h02; }
    char input03[50];sprintf(input03,"%s>>h03(%i,%f,%f)",plot,bin,min,max);Tree03->Draw(input03,CUTMC1);      if(Tree03->Draw(input03,CUTMC1))      {DY70          = h03; }
    char input04[50];sprintf(input04,"%s>>h04(%i,%f,%f)",plot,bin,min,max);Tree04->Draw(input04,CUTMC1);      if(Tree04->Draw(input04,CUTMC1))      {DYM50_100     = h04; }
    char input05[50];sprintf(input05,"%s>>h05(%i,%f,%f)",plot,bin,min,max);Tree05->Draw(input05,CUTMC1);      if(Tree05->Draw(input05,CUTMC1))      {DYM50_70      = h05; }
    char input06[50];sprintf(input06,"%s>>h06(%i,%f,%f)",plot,bin,min,max);Tree06->Draw(input06,CUTMC1);      if(Tree06->Draw(input06,CUTMC1))      {QCD1000       = h06; }
    char input07[50];sprintf(input07,"%s>>h07(%i,%f,%f)",plot,bin,min,max);Tree07->Draw(input07,CUTMC1);      if(Tree07->Draw(input07,CUTMC1))      {QCD250        = h07; }
    char input08[50];sprintf(input08,"%s>>h08(%i,%f,%f)",plot,bin,min,max);Tree08->Draw(input08,CUTMC1);      if(Tree08->Draw(input08,CUTMC1))      {QCD500        = h08; }
    char input09[50];sprintf(input09,"%s>>h09(%i,%f,%f)",plot,bin,min,max);Tree09->Draw(input09,CUTMC1);      if(Tree09->Draw(input09,CUTMC1))      {TT            = h09; }
    char input10[50];sprintf(input10,"%s>>h10(%i,%f,%f)",plot,bin,min,max);Tree10->Draw(input10,CUTMC1);      if(Tree10->Draw(input10,CUTMC1))      {WJetsHT       = h10; }
    char input11[50];sprintf(input11,"%s>>h11(%i,%f,%f)",plot,bin,min,max);Tree11->Draw(input11,CUTMC1);      if(Tree11->Draw(input11,CUTMC1))      {WW            = h11; }
    char input12[50];sprintf(input12,"%s>>h12(%i,%f,%f)",plot,bin,min,max);Tree12->Draw(input12,CUTMC1);      if(Tree12->Draw(input12,CUTMC1))      {WZ            = h12; }
    char input13[50];sprintf(input13,"%s>>h13(%i,%f,%f)",plot,bin,min,max);Tree13->Draw(input13,CUTMC1);      if(Tree13->Draw(input13,CUTMC1))      {ZZ            = h13; }
    char input14[50];sprintf(input14,"%s>>h14(%i,%f,%f)",plot,bin,min,max);Tree14->Draw(input14,CUTMC1);      if(Tree14->Draw(input14,CUTMC1))      {SingleTop1    = h14; }
    char input15[50];sprintf(input15,"%s>>h15(%i,%f,%f)",plot,bin,min,max);Tree15->Draw(input15,CUTMC1);      if(Tree15->Draw(input15,CUTMC1))      {SingleTop2    = h15; }
    char input16[50];sprintf(input16,"%s>>h16(%i,%f,%f)",plot,bin,min,max);Tree16->Draw(input16,CUTMC1);      if(Tree16->Draw(input16,CUTMC1))      {SingleTop3    = h16; }
    char input17[50];sprintf(input17,"%s>>h17(%i,%f,%f)",plot,bin,min,max);Tree17->Draw(input17,CUTMC1);      if(Tree17->Draw(input17,CUTMC1))      {SingleTop4    = h17; }
    char input18[50];sprintf(input18,"%s>>h18(%i,%f,%f)",plot,bin,min,max);Tree18->Draw(input18,CUTMC1);      if(Tree18->Draw(input18,CUTMC1))      {SingleTop5    = h18; }
    char input19[50];sprintf(input19,"%s>>h19(%i,%f,%f)",plot,bin,min,max);Tree19->Draw(input19,CUTMC1);      if(Tree19->Draw(input19,CUTMC1))      {SingleTop6    = h19; }
    char input20[50];sprintf(input20,"%s>>h20(%i,%f,%f)",plot,bin,min,max);Tree20->Draw(input20,CUTData1,"E");if(Tree20->Draw(input20,CUTData1,"E")){data_SR       = h20; }
    char input21[50];sprintf(input21,"%s>>h21(%i,%f,%f)",plot,bin,min,max);Tree21->Draw(input21,CUTMC1);      if(Tree21->Draw(input21,CUTMC1))      {DY100_SR      = h21; }
    char input22[50];sprintf(input22,"%s>>h22(%i,%f,%f)",plot,bin,min,max);Tree22->Draw(input22,CUTMC1);      if(Tree22->Draw(input22,CUTMC1))      {DY70_SR       = h22; }
    char input23[50];sprintf(input23,"%s>>h23(%i,%f,%f)",plot,bin,min,max);Tree23->Draw(input23,CUTMC1);      if(Tree23->Draw(input23,CUTMC1))      {DYM50_100_SR  = h23; }
    char input24[50];sprintf(input24,"%s>>h24(%i,%f,%f)",plot,bin,min,max);Tree24->Draw(input24,CUTMC1);      if(Tree24->Draw(input24,CUTMC1))      {DYM50_70_SR   = h24; }
    char input25[50];sprintf(input25,"%s>>h25(%i,%f,%f)",plot,bin,min,max);Tree25->Draw(input25,CUTMC1);      if(Tree25->Draw(input25,CUTMC1))      {QCD1000_SR    = h25; }
    char input26[50];sprintf(input26,"%s>>h26(%i,%f,%f)",plot,bin,min,max);Tree26->Draw(input26,CUTMC1);      if(Tree26->Draw(input26,CUTMC1))      {QCD250_SR     = h26; }
    char input27[50];sprintf(input27,"%s>>h27(%i,%f,%f)",plot,bin,min,max);Tree27->Draw(input27,CUTMC1);      if(Tree27->Draw(input27,CUTMC1))      {QCD500_SR     = h27; }
    char input28[50];sprintf(input28,"%s>>h28(%i,%f,%f)",plot,bin,min,max);Tree28->Draw(input28,CUTMC1);      if(Tree28->Draw(input28,CUTMC1))      {TT_SR         = h28; }
    char input29[50];sprintf(input29,"%s>>h29(%i,%f,%f)",plot,bin,min,max);Tree29->Draw(input29,CUTMC1);      if(Tree29->Draw(input29,CUTMC1))      {WJetsHT_SR    = h29; }
    char input30[50];sprintf(input30,"%s>>h30(%i,%f,%f)",plot,bin,min,max);Tree30->Draw(input30,CUTMC1);      if(Tree30->Draw(input30,CUTMC1))      {WW_SR         = h30; }
    char input31[50];sprintf(input31,"%s>>h31(%i,%f,%f)",plot,bin,min,max);Tree31->Draw(input31,CUTMC1);      if(Tree31->Draw(input31,CUTMC1))      {WZ_SR         = h31; }
    char input32[50];sprintf(input32,"%s>>h32(%i,%f,%f)",plot,bin,min,max);Tree32->Draw(input32,CUTMC1);      if(Tree32->Draw(input32,CUTMC1))      {ZZ_SR         = h32; }
    char input33[50];sprintf(input33,"%s>>h33(%i,%f,%f)",plot,bin,min,max);Tree33->Draw(input33,CUTMC1);      if(Tree33->Draw(input33,CUTMC1))      {SingleTop1_SR = h33; }
    char input34[50];sprintf(input34,"%s>>h34(%i,%f,%f)",plot,bin,min,max);Tree34->Draw(input34,CUTMC1);      if(Tree34->Draw(input34,CUTMC1))      {SingleTop2_SR = h34; }
    char input35[50];sprintf(input35,"%s>>h35(%i,%f,%f)",plot,bin,min,max);Tree35->Draw(input35,CUTMC1);      if(Tree35->Draw(input35,CUTMC1))      {SingleTop3_SR = h35; }
    char input36[50];sprintf(input36,"%s>>h36(%i,%f,%f)",plot,bin,min,max);Tree36->Draw(input36,CUTMC1);      if(Tree36->Draw(input36,CUTMC1))      {SingleTop4_SR = h36; }
    char input37[50];sprintf(input37,"%s>>h37(%i,%f,%f)",plot,bin,min,max);Tree37->Draw(input37,CUTMC1);      if(Tree37->Draw(input37,CUTMC1))      {SingleTop5_SR = h37; }
    char input38[50];sprintf(input38,"%s>>h38(%i,%f,%f)",plot,bin,min,max);Tree38->Draw(input38,CUTMC1);      if(Tree38->Draw(input38,CUTMC1))      {SingleTop6_SR = h38; }
    char input39[50];sprintf(input39,"%s>>h39(%i,%f,%f)",plot,bin,min,max);Tree39->Draw(input39,CUTData2,"E");if(Tree39->Draw(input39,CUTData2,"E")){data      ->Add(h39);}
    char input40[50];sprintf(input40,"%s>>h40(%i,%f,%f)",plot,bin,min,max);Tree40->Draw(input40,CUTMC2);      if(Tree40->Draw(input40,CUTMC2))      {DY100     ->Add(h40);}
    char input41[50];sprintf(input41,"%s>>h41(%i,%f,%f)",plot,bin,min,max);Tree41->Draw(input41,CUTMC2);      if(Tree41->Draw(input41,CUTMC2))      {DY70      ->Add(h41);}
    char input42[50];sprintf(input42,"%s>>h42(%i,%f,%f)",plot,bin,min,max);Tree42->Draw(input42,CUTMC2);      if(Tree42->Draw(input42,CUTMC2))      {DYM50_100 ->Add(h42);}
    char input43[50];sprintf(input43,"%s>>h43(%i,%f,%f)",plot,bin,min,max);Tree43->Draw(input43,CUTMC2);      if(Tree43->Draw(input43,CUTMC2))      {DYM50_70  ->Add(h43);}
    char input44[50];sprintf(input44,"%s>>h44(%i,%f,%f)",plot,bin,min,max);Tree44->Draw(input44,CUTMC2);      if(Tree44->Draw(input44,CUTMC2))      {QCD1000   ->Add(h44);}
    char input45[50];sprintf(input45,"%s>>h45(%i,%f,%f)",plot,bin,min,max);Tree45->Draw(input45,CUTMC2);      if(Tree45->Draw(input45,CUTMC2))      {QCD250    ->Add(h45);}
    char input46[50];sprintf(input46,"%s>>h46(%i,%f,%f)",plot,bin,min,max);Tree46->Draw(input46,CUTMC2);      if(Tree46->Draw(input46,CUTMC2))      {QCD500    ->Add(h46);}
    char input47[50];sprintf(input47,"%s>>h47(%i,%f,%f)",plot,bin,min,max);Tree47->Draw(input47,CUTMC2);      if(Tree47->Draw(input47,CUTMC2))      {TT        ->Add(h47);}
    char input48[50];sprintf(input48,"%s>>h48(%i,%f,%f)",plot,bin,min,max);Tree48->Draw(input48,CUTMC2);      if(Tree48->Draw(input48,CUTMC2))      {WJetsHT   ->Add(h48);}
    char input49[50];sprintf(input49,"%s>>h49(%i,%f,%f)",plot,bin,min,max);Tree49->Draw(input49,CUTMC2);      if(Tree49->Draw(input49,CUTMC2))      {WW        ->Add(h49);}
    char input50[50];sprintf(input50,"%s>>h50(%i,%f,%f)",plot,bin,min,max);Tree50->Draw(input50,CUTMC2);      if(Tree50->Draw(input50,CUTMC2))      {WZ        ->Add(h50);}
    char input51[50];sprintf(input51,"%s>>h51(%i,%f,%f)",plot,bin,min,max);Tree51->Draw(input51,CUTMC2);      if(Tree51->Draw(input51,CUTMC2))      {ZZ        ->Add(h51);}
    char input52[50];sprintf(input52,"%s>>h52(%i,%f,%f)",plot,bin,min,max);Tree52->Draw(input52,CUTMC2);      if(Tree52->Draw(input52,CUTMC2))      {SingleTop1->Add(h52);}
    char input53[50];sprintf(input53,"%s>>h53(%i,%f,%f)",plot,bin,min,max);Tree53->Draw(input53,CUTMC2);      if(Tree53->Draw(input53,CUTMC2))      {SingleTop2->Add(h53);}
    char input54[50];sprintf(input54,"%s>>h54(%i,%f,%f)",plot,bin,min,max);Tree54->Draw(input54,CUTMC2);      if(Tree54->Draw(input54,CUTMC2))      {SingleTop3->Add(h54);}
    char input55[50];sprintf(input55,"%s>>h55(%i,%f,%f)",plot,bin,min,max);Tree55->Draw(input55,CUTMC2);      if(Tree55->Draw(input55,CUTMC2))      {SingleTop4->Add(h55);}
    char input56[50];sprintf(input56,"%s>>h56(%i,%f,%f)",plot,bin,min,max);Tree56->Draw(input56,CUTMC2);      if(Tree56->Draw(input56,CUTMC2))      {SingleTop5->Add(h56);}
    char input57[50];sprintf(input57,"%s>>h57(%i,%f,%f)",plot,bin,min,max);Tree57->Draw(input57,CUTMC2);      if(Tree57->Draw(input57,CUTMC2))      {SingleTop6->Add(h57);}
    char input58[50];sprintf(input58,"%s>>h58(%i,%f,%f)",plot,bin,min,max);Tree58->Draw(input58,CUTData1,"E");if(Tree58->Draw(input58,CUTData1,"E")){data      ->Add(h58);}
    char input59[50];sprintf(input59,"%s>>h59(%i,%f,%f)",plot,bin,min,max);Tree59->Draw(input59,CUTMC1);      if(Tree59->Draw(input59,CUTMC1))      {DY100     ->Add(h59);}
    char input60[50];sprintf(input60,"%s>>h60(%i,%f,%f)",plot,bin,min,max);Tree60->Draw(input60,CUTMC1);      if(Tree60->Draw(input60,CUTMC1))      {DY70      ->Add(h60);}
    char input61[50];sprintf(input61,"%s>>h61(%i,%f,%f)",plot,bin,min,max);Tree61->Draw(input61,CUTMC1);      if(Tree61->Draw(input61,CUTMC1))      {DYM50_100 ->Add(h61);}
    char input62[50];sprintf(input62,"%s>>h62(%i,%f,%f)",plot,bin,min,max);Tree62->Draw(input62,CUTMC1);      if(Tree62->Draw(input62,CUTMC1))      {DYM50_70  ->Add(h62);}
    char input63[50];sprintf(input63,"%s>>h63(%i,%f,%f)",plot,bin,min,max);Tree63->Draw(input63,CUTMC1);      if(Tree63->Draw(input63,CUTMC1))      {QCD1000   ->Add(h63);}
    char input64[50];sprintf(input64,"%s>>h64(%i,%f,%f)",plot,bin,min,max);Tree64->Draw(input64,CUTMC1);      if(Tree64->Draw(input64,CUTMC1))      {QCD250    ->Add(h64);}
    char input65[50];sprintf(input65,"%s>>h65(%i,%f,%f)",plot,bin,min,max);Tree65->Draw(input65,CUTMC1);      if(Tree65->Draw(input65,CUTMC1))      {QCD500    ->Add(h65);}
    char input66[50];sprintf(input66,"%s>>h66(%i,%f,%f)",plot,bin,min,max);Tree66->Draw(input66,CUTMC1);      if(Tree66->Draw(input66,CUTMC1))      {TT        ->Add(h66);}
    char input67[50];sprintf(input67,"%s>>h67(%i,%f,%f)",plot,bin,min,max);Tree67->Draw(input67,CUTMC1);      if(Tree67->Draw(input67,CUTMC1))      {WJetsHT   ->Add(h67);}
    char input68[50];sprintf(input68,"%s>>h68(%i,%f,%f)",plot,bin,min,max);Tree68->Draw(input68,CUTMC1);      if(Tree68->Draw(input68,CUTMC1))      {WW        ->Add(h68);}
    char input69[50];sprintf(input69,"%s>>h69(%i,%f,%f)",plot,bin,min,max);Tree69->Draw(input69,CUTMC1);      if(Tree69->Draw(input69,CUTMC1))      {WZ        ->Add(h69);}
    char input70[50];sprintf(input70,"%s>>h70(%i,%f,%f)",plot,bin,min,max);Tree70->Draw(input70,CUTMC1);      if(Tree70->Draw(input70,CUTMC1))      {ZZ        ->Add(h70);}
    char input71[50];sprintf(input71,"%s>>h71(%i,%f,%f)",plot,bin,min,max);Tree71->Draw(input71,CUTMC1);      if(Tree71->Draw(input71,CUTMC1))      {SingleTop1->Add(h71);}
    char input72[50];sprintf(input72,"%s>>h72(%i,%f,%f)",plot,bin,min,max);Tree72->Draw(input72,CUTMC1);      if(Tree72->Draw(input72,CUTMC1))      {SingleTop2->Add(h72);}
    char input73[50];sprintf(input73,"%s>>h73(%i,%f,%f)",plot,bin,min,max);Tree73->Draw(input73,CUTMC1);      if(Tree73->Draw(input73,CUTMC1))      {SingleTop3->Add(h73);}
    char input74[50];sprintf(input74,"%s>>h74(%i,%f,%f)",plot,bin,min,max);Tree74->Draw(input74,CUTMC1);      if(Tree74->Draw(input74,CUTMC1))      {SingleTop4->Add(h74);}
    char input75[50];sprintf(input75,"%s>>h75(%i,%f,%f)",plot,bin,min,max);Tree75->Draw(input75,CUTMC1);      if(Tree75->Draw(input75,CUTMC1))      {SingleTop5->Add(h75);}
    char input76[50];sprintf(input76,"%s>>h76(%i,%f,%f)",plot,bin,min,max);Tree76->Draw(input76,CUTMC1);      if(Tree76->Draw(input76,CUTMC1))      {SingleTop6->Add(h76);}
    
    float w_DY100     = ( 39.100*19702./12511326.);
    float w_DY70      = ( 62.900*19702./11764538.);
    float w_DYM50_100 = (  4.220*19702./4146124.0);
    float w_DYM50_70  = ( 11.050*19702./5389313.0);
    float w_TT        = (225.197*19702./21675970.);
    float w_QCD1000   = (204.000*19702./13843863.);
    float w_QCD500    = (8426.00*19702./30599292.);
    float w_QCD250    = (276000.*19702./27062078.);
    float w_WW        = (57.1097*19702./10000431.);
    float w_WZ        = ( 33.210*19702./10000283.);
    float w_ZZ        = (  8.059*19702./9799908.0);
    float w_WJetsHT   = ( 25.220*19702./4971847.0);
    float w_SingleTop1 = ( 56.400*19702./3758227.);
    float w_SingleTop2 = ( 3.7900*19702./259961.0);
    float w_SingleTop3 = ( 11.100*19702./497658.0);
    float w_SingleTop4 = ( 30.700*19702./1935072.);
    float w_SingleTop5 = ( 1.7600*19702./139974.0);
    float w_SingleTop6 = ( 11.100*19702./493460.0);

    double N_sb     = data->Integral();
    double N_sb_err = sqrt(data->Integral());
    double f_sb_err = 0;  
    double f_sb = 0; 
    double alpha = 0; 
    double alpha_err = 0;

    double N_QCD_SR      = w_QCD1000*QCD1000_SR->Integral() + w_QCD250*QCD250_SR->Integral() + w_QCD500*QCD500_SR->Integral();
    double N_QCD_SR_err  = sqrt(w_QCD1000*w_QCD1000*QCD1000_SR->Integral()+w_QCD250*w_QCD250*QCD250_SR->Integral()+w_QCD500*w_QCD500*QCD500_SR->Integral());
    double N_QCD_SB      = w_QCD1000*QCD1000->Integral()  +  w_QCD250*QCD250->Integral()  +  w_QCD500*QCD500->Integral();
    double N_QCD_SB_err  = sqrt(w_QCD1000*w_QCD1000*QCD1000->Integral()  +  w_QCD250*w_QCD250*QCD250->Integral()  +  w_QCD500*w_QCD500*QCD500->Integral());

    double N_DY_SR      = w_DY100*DY100_SR->Integral() + w_DY70*DY70_SR->Integral() + w_DYM50_100*DYM50_100_SR->Integral() + w_DYM50_70*DYM50_70_SR->Integral();
    double N_DY_SR_err  = sqrt(w_DY100*w_DY100*DY100_SR->Integral()+w_DY70*w_DY70*DY70_SR->Integral()+w_DYM50_100*w_DYM50_100*DYM50_100_SR->Integral()
			       +w_DYM50_70*w_DYM50_70*DYM50_70_SR->Integral());
    double N_DY_SB      = w_DY100*DY100->Integral() + w_DY70*DY70->Integral() + w_DYM50_100*DYM50_100->Integral() + w_DYM50_70*DYM50_70->Integral();
    double N_DY_SB_err  = sqrt(w_DY100*w_DY100*DY100->Integral()+w_DY70*w_DY70*DY70->Integral()+w_DYM50_100*w_DYM50_100*DYM50_100->Integral()
			       +w_DYM50_70*w_DYM50_70*DYM50_70->Integral());

    double N_VV_SR      = w_WZ*WZ_SR->Integral() + w_WW*WW_SR->Integral() + w_ZZ*ZZ_SR->Integral();
    double N_VV_SR_err  = sqrt(w_WZ*w_WZ*WZ_SR->Integral() + w_WW*w_WW*WW_SR->Integral() + w_ZZ*w_ZZ*ZZ_SR->Integral());
    double N_VV_SB      = w_WZ*WZ->Integral() + w_WW*WW->Integral() + w_ZZ*ZZ->Integral();
    double N_VV_SB_err  = sqrt(w_WZ*w_WZ*WZ->Integral() + w_WW*w_WW*WW->Integral() + w_ZZ*w_ZZ*ZZ->Integral());

    double N_TT_SR      = w_TT*TT_SR->Integral();
    double N_TT_SR_err  = sqrt(w_TT*w_TT*TT_SR->Integral());
    double N_TT_SB      = w_TT*TT->Integral();
    double N_TT_SB_err  = sqrt(w_TT*w_TT*TT->Integral());

    double N_Wjets_SR      = w_WJetsHT*WJetsHT_SR->Integral();
    double N_Wjets_SR_err  = sqrt(w_WJetsHT*w_WJetsHT*WJetsHT_SR->Integral());
    double N_Wjets_SB      = w_WJetsHT*WJetsHT->Integral();
    double N_Wjets_SB_err  = sqrt(w_WJetsHT*w_WJetsHT*WJetsHT->Integral());

    double N_SingleTop_SR      = (w_SingleTop1*SingleTop1_SR->Integral()+w_SingleTop2*SingleTop2_SR->Integral()+w_SingleTop3*SingleTop3_SR->Integral()+
				  w_SingleTop4*SingleTop4_SR->Integral()+w_SingleTop5*SingleTop5_SR->Integral()+w_SingleTop6*SingleTop6_SR->Integral());
    double N_SingleTop_SR_err  = sqrt(w_SingleTop1*w_SingleTop1*SingleTop1_SR->Integral()+w_SingleTop2*w_SingleTop2*SingleTop2_SR->Integral()+
				      w_SingleTop3*w_SingleTop3*SingleTop3_SR->Integral()+w_SingleTop4*w_SingleTop4*SingleTop4_SR->Integral()+
				      w_SingleTop5*w_SingleTop5*SingleTop5_SR->Integral()+w_SingleTop6*w_SingleTop6*SingleTop6_SR->Integral());
    double N_SingleTop_SB      = (w_SingleTop1*SingleTop1->Integral()+w_SingleTop2*SingleTop2->Integral()+w_SingleTop3*SingleTop3->Integral()+
				  w_SingleTop4*SingleTop4->Integral()+w_SingleTop5*SingleTop5->Integral()+w_SingleTop6*SingleTop6->Integral());
    double N_SingleTop_SB_err  = sqrt(w_SingleTop1*w_SingleTop1*SingleTop1->Integral()+w_SingleTop2*w_SingleTop2*SingleTop2->Integral()+
				      w_SingleTop3*w_SingleTop3*SingleTop3->Integral()+w_SingleTop4*w_SingleTop4*SingleTop4->Integral()+
				      w_SingleTop5*w_SingleTop5*SingleTop5->Integral()+w_SingleTop6*w_SingleTop6*SingleTop6->Integral());
		
    double alpha_num     = N_QCD_SR + N_DY_SR + N_VV_SR + N_TT_SR + N_SingleTop_SR + N_Wjets_SR;
    double alpha_num_err = sqrt(N_QCD_SR_err*N_QCD_SR_err + N_DY_SR_err*N_DY_SR_err + N_VV_SR_err*N_VV_SR_err + N_TT_SR_err*N_TT_SR_err + 
				N_SingleTop_SR_err*N_SingleTop_SR_err + N_Wjets_SR_err*N_Wjets_SR_err);
    double alpha_den     = N_QCD_SB + N_DY_SB + N_VV_SB + N_TT_SB + N_SingleTop_SB + N_Wjets_SB;
    double alpha_den_err = sqrt(N_QCD_SB_err*N_QCD_SB_err + N_DY_SB_err*N_DY_SB_err + N_VV_SB_err*N_VV_SB_err + N_TT_SB_err*N_TT_SB_err + 
				N_SingleTop_SB_err*N_SingleTop_SB_err + N_Wjets_SB_err*N_Wjets_SB_err);
		
    if(alpha_den!=0) {
      alpha = alpha_num/alpha_den;
      alpha_err = sqrt(alpha_den*alpha_den*alpha_num_err*alpha_num_err + alpha_num*alpha_num*alpha_den_err*alpha_den_err)/(alpha_den*alpha_den);
    }
		
	
    Nsb->SetBinContent(i+1,N_sb);
    Nsb->SetBinError(i+1,N_sb_err);
    Alpha->SetBinContent(i+1,alpha);
    Alpha->SetBinError(i+1,alpha_err);
    double N_PRE = N_sb * alpha;
    double N_PRE_err = sqrt(N_sb_err*N_sb_err*alpha*alpha + alpha_err*alpha_err*N_sb*N_sb);
    if((xbins[AAA2]>= SignalMass && xbins[AAA1]<= SignalMass))
    {
       Nsideband=Nsideband+N_sb;
       DATYield=DATYield+data_SR->Integral();
       BkgYield=BkgYield+N_PRE;
       BkgYieldErr=BkgYieldErr*BkgYieldErr+N_PRE_err*N_PRE_err;
    }
    if((xbins[AAA2]>= SignalMass && xbins[AAA1]< SignalMass))
    {
       Alpha1=alpha;
       Alpha2=alpha;
       AlphaERR1=alpha_err;
       AlphaERR2=alpha_err;
       Nsideband1=N_sb;
       Nsideband2=N_sb;
    }

    histo_PRE->SetBinContent( i+1, N_PRE);
    histo_PRE->SetBinError(   i+1, N_PRE_err);
    histo_DAT->SetBinContent( i+1, data_SR->Integral());
    DY->SetBinContent(        i+1, N_DY_SR);
    SINGLETOP->SetBinContent( i+1, N_SingleTop_SR);
    TTbar->SetBinContent(     i+1, N_TT_SR);
    DIBOSON->SetBinContent(   i+1, N_VV_SR);
    WJETS->SetBinContent(     i+1, N_Wjets_SR);
    QCD->SetBinContent(       i+1, N_QCD_SR);
    ERR->SetBinContent(       i+1, alpha_num);
    ERR->SetBinError(         i+1, alpha_num_err);
    
    XMassMin=XMassMin+XMassWidth;
    XMassMax=XMassMax+XMassWidth;
  }

  double N1_err = 0.; double N1    = histo_PRE->IntegralAndError(1,MAX-1,N1_err); 
  double N2_err = 0.; double N2    = ERR->IntegralAndError(1,MAX-1,N2_err);
  double N3_err = 0.; double N3    = histo_DAT->IntegralAndError(1,MAX-1,N3_err);
  NORMforALPHA=(NORM/N1);
  histo_PRE->Scale(NORM/N1); 
  BkgYieldErr=sqrt(BkgYield*BkgYield*NORMerr*NORMerr/(N1*N1) + NORM*NORM*BkgYieldErr/(N1*N1) + NORM*NORM*BkgYield*BkgYield/(N1*N1*N1*N1));
  BkgYield=BkgYield*NORM/N1; 
  N1=NORM; N1_err = NORMerr;

  if(Nsideband!=0){
    Alpha1=Alpha1*Nsideband1/Nsideband;
    Alpha2=Alpha2*Nsideband2/Nsideband;
    AlphaERR1=AlphaERR1*Nsideband1/Nsideband;
    AlphaERR2=AlphaERR2*Nsideband2/Nsideband;
  }

  cout<<"RESULTS - "<<CHANNEL<<endl;
  cout<<"RESULTS - Number of predicted BKG events = "<<N1<<"+/-"<<N1_err<<endl;
  cout<<"RESULTS - Number of BKG events from MC   = "<<N2<<"+/-"<<N2_err<<endl;
  cout<<"RESULTS - Number of DATA events          = "<<N3<<"+/-"<<N3_err<<endl;
  cout<<endl;
 
  delete file01;
  delete file02;
  delete file03;
  delete file04;
  delete file05;
  delete file06;
  delete file07;
  delete file08;
  delete file09;
  delete file10;
  delete file11;
  delete file12;
  delete file13;
  delete file14;
  delete file15;
  delete file16;
  delete file17;
  delete file18;
  delete file19;
}

void Normalization(char *channel, float & NORM, float & NORMerr, char *cutMC1, char *cutMC2,  char *cutData1,  char *cutData2){
  
  char CUTMC1[1000]; char CUTMC2[1000]; char CUTData1[1000]; char CUTData2[1000];
  sprintf(CUTMC1,   "%s && XMassSVFit<3000)", cutMC1  );
  sprintf(CUTMC2,   "%s && XMassSVFit<3000)", cutMC2  );
  sprintf(CUTData1, "%s && XMassSVFit<3000)", cutData1);
  sprintf(CUTData2, "%s && XMassSVFit<3000)", cutData2);
  
  TString CHANNEL = channel; 
  char demo0     [500]; sprintf(demo0,     "demo/Tree"); 
  char demo1     [500]; sprintf(demo1,     "demo/TreeSB1"); 
  char demo2     [500]; sprintf(demo2,     "demo/TreeSB2"); 
  char openTree0 [500]; sprintf(openTree0, "%s%s",demo0,channel); 
  char openTree1 [500]; sprintf(openTree1, "%s%s",demo1,channel); 
  char openTree2 [500]; sprintf(openTree2, "%s%s",demo2,channel); 
  
  char *plot = "jetMass";
  TString name = "jetMass";
  int bin=18;
  float min=20;
  float max=200;
  float maxy=500;
  TString axis = "jet mass [GeV]";
  
  TH1F *MC         = new TH1F("","",bin,min,max);
  TH1F *data       = new TH1F("","",bin,min,max);
  TH1F *data2      = new TH1F("","",bin,min,max);
  TH1F *DY100      = new TH1F("","",bin,min,max);
  TH1F *DY70       = new TH1F("","",bin,min,max);
  TH1F *DYM50_100  = new TH1F("","",bin,min,max);
  TH1F *DYM50_70   = new TH1F("","",bin,min,max);											     
  TH1F *QCD1000    = new TH1F("","",bin,min,max);
  TH1F *QCD250     = new TH1F("","",bin,min,max);
  TH1F *QCD500     = new TH1F("","",bin,min,max);
  TH1F *TT         = new TH1F("","",bin,min,max);
  TH1F *WJetsHT    = new TH1F("","",bin,min,max);
  TH1F *WW         = new TH1F("","",bin,min,max);
  TH1F *WZ         = new TH1F("","",bin,min,max);
  TH1F *ZZ         = new TH1F("","",bin,min,max);
  TH1F *SingleTop1 = new TH1F("","",bin,min,max);
  TH1F *SingleTop2 = new TH1F("","",bin,min,max);
  TH1F *SingleTop3 = new TH1F("","",bin,min,max);
  TH1F *SingleTop4 = new TH1F("","",bin,min,max);
  TH1F *SingleTop5 = new TH1F("","",bin,min,max);
  TH1F *SingleTop6 = new TH1F("","",bin,min,max);
  
  TFile *file01=TFile::Open("data.root");      
  TFile *file02=TFile::Open("DY100.root");      
  TFile *file03=TFile::Open("DY70.root");       
  TFile *file04=TFile::Open("DYM50_100.root");  
  TFile *file05=TFile::Open("DYM50_70.root");   
  TFile *file06=TFile::Open("QCD1000.root");    
  TFile *file07=TFile::Open("QCD250.root");     
  TFile *file08=TFile::Open("QCD500.root");     
  TFile *file09=TFile::Open("TT.root");        
  TFile *file10=TFile::Open("WJetsHT.root");   
  TFile *file11=TFile::Open("WW.root");          
  TFile *file12=TFile::Open("WZ.root");          
  TFile *file13=TFile::Open("ZZ.root");
  TFile *file14=TFile::Open("SingleTop1.root"); 
  TFile *file15=TFile::Open("SingleTop2.root"); 
  TFile *file16=TFile::Open("SingleTop3.root"); 
  TFile *file17=TFile::Open("SingleTop4.root"); 
  TFile *file18=TFile::Open("SingleTop5.root"); 
  TFile *file19=TFile::Open("SingleTop6.root"); 
  
  TTree *Tree01=(TTree*)file01->Get(openTree0); TTree *Tree20=(TTree*)file01->Get(openTree1); TTree *Tree39=(TTree*)file01->Get(openTree2); 
  TTree *Tree02=(TTree*)file02->Get(openTree0); TTree *Tree21=(TTree*)file02->Get(openTree1); TTree *Tree40=(TTree*)file02->Get(openTree2);  
  TTree *Tree03=(TTree*)file03->Get(openTree0); TTree *Tree22=(TTree*)file03->Get(openTree1); TTree *Tree41=(TTree*)file03->Get(openTree2);  
  TTree *Tree04=(TTree*)file04->Get(openTree0); TTree *Tree23=(TTree*)file04->Get(openTree1); TTree *Tree42=(TTree*)file04->Get(openTree2);  
  TTree *Tree05=(TTree*)file05->Get(openTree0); TTree *Tree24=(TTree*)file05->Get(openTree1); TTree *Tree43=(TTree*)file05->Get(openTree2);  
  TTree *Tree06=(TTree*)file06->Get(openTree0); TTree *Tree25=(TTree*)file06->Get(openTree1); TTree *Tree44=(TTree*)file06->Get(openTree2);  
  TTree *Tree07=(TTree*)file07->Get(openTree0); TTree *Tree26=(TTree*)file07->Get(openTree1); TTree *Tree45=(TTree*)file07->Get(openTree2);  
  TTree *Tree08=(TTree*)file08->Get(openTree0); TTree *Tree27=(TTree*)file08->Get(openTree1); TTree *Tree46=(TTree*)file08->Get(openTree2);  
  TTree *Tree09=(TTree*)file09->Get(openTree0); TTree *Tree28=(TTree*)file09->Get(openTree1); TTree *Tree47=(TTree*)file09->Get(openTree2);  
  TTree *Tree10=(TTree*)file10->Get(openTree0); TTree *Tree29=(TTree*)file10->Get(openTree1); TTree *Tree48=(TTree*)file10->Get(openTree2);  
  TTree *Tree11=(TTree*)file11->Get(openTree0); TTree *Tree30=(TTree*)file11->Get(openTree1); TTree *Tree49=(TTree*)file11->Get(openTree2);  
  TTree *Tree12=(TTree*)file12->Get(openTree0); TTree *Tree31=(TTree*)file12->Get(openTree1); TTree *Tree50=(TTree*)file12->Get(openTree2);  
  TTree *Tree13=(TTree*)file13->Get(openTree0); TTree *Tree32=(TTree*)file13->Get(openTree1); TTree *Tree51=(TTree*)file13->Get(openTree2);
  TTree *Tree14=(TTree*)file14->Get(openTree0); TTree *Tree33=(TTree*)file14->Get(openTree1); TTree *Tree52=(TTree*)file14->Get(openTree2);
  TTree *Tree15=(TTree*)file15->Get(openTree0);	TTree *Tree34=(TTree*)file15->Get(openTree1); TTree *Tree53=(TTree*)file15->Get(openTree2);
  TTree *Tree16=(TTree*)file16->Get(openTree0);	TTree *Tree35=(TTree*)file16->Get(openTree1); TTree *Tree54=(TTree*)file16->Get(openTree2);
  TTree *Tree17=(TTree*)file17->Get(openTree0);	TTree *Tree36=(TTree*)file17->Get(openTree1); TTree *Tree55=(TTree*)file17->Get(openTree2);
  TTree *Tree18=(TTree*)file18->Get(openTree0);	TTree *Tree37=(TTree*)file18->Get(openTree1); TTree *Tree56=(TTree*)file18->Get(openTree2);
  TTree *Tree19=(TTree*)file19->Get(openTree0);	TTree *Tree38=(TTree*)file19->Get(openTree1); TTree *Tree57=(TTree*)file19->Get(openTree2);

  char input01 [50]; sprintf(input01, "%s>>h01(%i,%f,%f)",plot,bin,min,max);
  char input02 [50]; sprintf(input02, "%s>>h02(%i,%f,%f)",plot,bin,min,max);
  char input03 [50]; sprintf(input03, "%s>>h03(%i,%f,%f)",plot,bin,min,max);
  char input04 [50]; sprintf(input04, "%s>>h04(%i,%f,%f)",plot,bin,min,max);
  char input05 [50]; sprintf(input05, "%s>>h05(%i,%f,%f)",plot,bin,min,max);
  char input06 [50]; sprintf(input06, "%s>>h06(%i,%f,%f)",plot,bin,min,max);
  char input07 [50]; sprintf(input07, "%s>>h07(%i,%f,%f)",plot,bin,min,max);
  char input08 [50]; sprintf(input08, "%s>>h08(%i,%f,%f)",plot,bin,min,max);
  char input09 [50]; sprintf(input09, "%s>>h09(%i,%f,%f)",plot,bin,min,max);
  char input10 [50]; sprintf(input10, "%s>>h10(%i,%f,%f)",plot,bin,min,max);
  char input11 [50]; sprintf(input11, "%s>>h11(%i,%f,%f)",plot,bin,min,max);
  char input12 [50]; sprintf(input12, "%s>>h12(%i,%f,%f)",plot,bin,min,max);
  char input13 [50]; sprintf(input13, "%s>>h13(%i,%f,%f)",plot,bin,min,max);
  char input14 [50]; sprintf(input14, "%s>>h14(%i,%f,%f)",plot,bin,min,max);
  char input15 [50]; sprintf(input15, "%s>>h15(%i,%f,%f)",plot,bin,min,max);
  char input16 [50]; sprintf(input16, "%s>>h16(%i,%f,%f)",plot,bin,min,max);
  char input17 [50]; sprintf(input17, "%s>>h17(%i,%f,%f)",plot,bin,min,max);
  char input18 [50]; sprintf(input18, "%s>>h18(%i,%f,%f)",plot,bin,min,max);
  char input19 [50]; sprintf(input19, "%s>>h19(%i,%f,%f)",plot,bin,min,max);
  char input20 [50]; sprintf(input20, "%s>>h20(%i,%f,%f)",plot,bin,min,max);
  char input21 [50]; sprintf(input21, "%s>>h21(%i,%f,%f)",plot,bin,min,max);
  char input22 [50]; sprintf(input22, "%s>>h22(%i,%f,%f)",plot,bin,min,max);
  char input23 [50]; sprintf(input23, "%s>>h23(%i,%f,%f)",plot,bin,min,max);
  char input24 [50]; sprintf(input24, "%s>>h24(%i,%f,%f)",plot,bin,min,max);
  char input25 [50]; sprintf(input25, "%s>>h25(%i,%f,%f)",plot,bin,min,max);
  char input26 [50]; sprintf(input26, "%s>>h26(%i,%f,%f)",plot,bin,min,max);
  char input27 [50]; sprintf(input27, "%s>>h27(%i,%f,%f)",plot,bin,min,max);
  char input28 [50]; sprintf(input28, "%s>>h28(%i,%f,%f)",plot,bin,min,max);
  char input29 [50]; sprintf(input29, "%s>>h29(%i,%f,%f)",plot,bin,min,max);
  char input30 [50]; sprintf(input30, "%s>>h30(%i,%f,%f)",plot,bin,min,max);
  char input31 [50]; sprintf(input31, "%s>>h31(%i,%f,%f)",plot,bin,min,max);
  char input32 [50]; sprintf(input32, "%s>>h32(%i,%f,%f)",plot,bin,min,max);
  char input33 [50]; sprintf(input33, "%s>>h33(%i,%f,%f)",plot,bin,min,max);
  char input34 [50]; sprintf(input34, "%s>>h34(%i,%f,%f)",plot,bin,min,max);
  char input35 [50]; sprintf(input35, "%s>>h35(%i,%f,%f)",plot,bin,min,max);
  char input36 [50]; sprintf(input36, "%s>>h36(%i,%f,%f)",plot,bin,min,max);
  char input37 [50]; sprintf(input37, "%s>>h37(%i,%f,%f)",plot,bin,min,max);
  char input38 [50]; sprintf(input38, "%s>>h38(%i,%f,%f)",plot,bin,min,max);
  char input39 [50]; sprintf(input39, "%s>>h39(%i,%f,%f)",plot,bin,min,max);
  char input40 [50]; sprintf(input40, "%s>>h40(%i,%f,%f)",plot,bin,min,max);
  char input41 [50]; sprintf(input41, "%s>>h41(%i,%f,%f)",plot,bin,min,max);
  char input42 [50]; sprintf(input42, "%s>>h42(%i,%f,%f)",plot,bin,min,max);
  char input43 [50]; sprintf(input43, "%s>>h43(%i,%f,%f)",plot,bin,min,max);
  char input44 [50]; sprintf(input44, "%s>>h44(%i,%f,%f)",plot,bin,min,max);
  char input45 [50]; sprintf(input45, "%s>>h45(%i,%f,%f)",plot,bin,min,max);
  char input46 [50]; sprintf(input46, "%s>>h46(%i,%f,%f)",plot,bin,min,max);
  char input47 [50]; sprintf(input47, "%s>>h47(%i,%f,%f)",plot,bin,min,max);
  char input48 [50]; sprintf(input48, "%s>>h48(%i,%f,%f)",plot,bin,min,max);
  char input49 [50]; sprintf(input49, "%s>>h49(%i,%f,%f)",plot,bin,min,max);
  char input50 [50]; sprintf(input50, "%s>>h50(%i,%f,%f)",plot,bin,min,max);
  char input51 [50]; sprintf(input51, "%s>>h51(%i,%f,%f)",plot,bin,min,max);
  char input52 [50]; sprintf(input52, "%s>>h52(%i,%f,%f)",plot,bin,min,max);
  char input53 [50]; sprintf(input53, "%s>>h53(%i,%f,%f)",plot,bin,min,max);
  char input54 [50]; sprintf(input54, "%s>>h54(%i,%f,%f)",plot,bin,min,max);
  char input55 [50]; sprintf(input55, "%s>>h55(%i,%f,%f)",plot,bin,min,max);
  char input56 [50]; sprintf(input56, "%s>>h56(%i,%f,%f)",plot,bin,min,max);
  char input57 [50]; sprintf(input57, "%s>>h57(%i,%f,%f)",plot,bin,min,max);
  char input58 [50]; sprintf(input58, "%s>>h58(%i,%f,%f)",plot,bin,min,max);//data2
  char input59 [50]; sprintf(input59, "%s>>h59(%i,%f,%f)",plot,bin,min,max);//data2
  char input60 [50]; sprintf(input60, "%s>>h60(%i,%f,%f)",plot,bin,min,max);//data2
  
  Tree01->Draw(input01,CUTData2,"E");   if(Tree01->Draw(input01,CUTData2,"E"))   {data       =    h01;  }
  Tree02->Draw(input02,CUTMC1);         if(Tree02->Draw(input02,CUTMC1))         {DY100      =    h02;  }
  Tree03->Draw(input03,CUTMC1);         if(Tree03->Draw(input03,CUTMC1))         {DY70       =    h03;  }
  Tree04->Draw(input04,CUTMC1);         if(Tree04->Draw(input04,CUTMC1))         {DYM50_100  =    h04;  }
  Tree05->Draw(input05,CUTMC1);         if(Tree05->Draw(input05,CUTMC1))         {DYM50_70   =    h05;  }
  Tree06->Draw(input06,CUTMC1);         if(Tree06->Draw(input06,CUTMC1))         {QCD1000    =    h06;  }
  Tree07->Draw(input07,CUTMC1);         if(Tree07->Draw(input07,CUTMC1))         {QCD250     =    h07;  }
  Tree08->Draw(input08,CUTMC1);         if(Tree08->Draw(input08,CUTMC1))         {QCD500     =    h08;  }
  Tree09->Draw(input09,CUTMC1);         if(Tree09->Draw(input09,CUTMC1))         {TT         =    h09;  }
  Tree10->Draw(input10,CUTMC1);         if(Tree10->Draw(input10,CUTMC1))         {WJetsHT    =    h10;  }
  Tree11->Draw(input11,CUTMC1);         if(Tree11->Draw(input11,CUTMC1))         {WW         =    h11;  }
  Tree12->Draw(input12,CUTMC1);         if(Tree12->Draw(input12,CUTMC1))         {WZ         =    h12;  }
  Tree13->Draw(input13,CUTMC1);         if(Tree13->Draw(input13,CUTMC1))         {ZZ         =    h13;  }
  Tree14->Draw(input14,CUTMC1);         if(Tree14->Draw(input14,CUTMC1))         {SingleTop1 =    h14;  }
  Tree15->Draw(input15,CUTMC1);         if(Tree15->Draw(input15,CUTMC1))         {SingleTop2 =    h15;  }
  Tree16->Draw(input16,CUTMC1);         if(Tree16->Draw(input16,CUTMC1))         {SingleTop3 =    h16;  }
  Tree17->Draw(input17,CUTMC1);         if(Tree17->Draw(input17,CUTMC1))         {SingleTop4 =    h17;  }
  Tree18->Draw(input18,CUTMC1);         if(Tree18->Draw(input18,CUTMC1))         {SingleTop5 =    h18;  }
  Tree19->Draw(input19,CUTMC1);         if(Tree19->Draw(input19,CUTMC1))         {SingleTop6 =    h19;  }
  Tree20->Draw(input20,CUTData2,"E");   if(Tree20->Draw(input20,CUTData2,"E"))   {data      ->Add(h20); }
  Tree21->Draw(input21,CUTMC1);         if(Tree21->Draw(input21,CUTMC1))         {DY100     ->Add(h21); }
  Tree22->Draw(input22,CUTMC1);         if(Tree22->Draw(input22,CUTMC1))         {DY70      ->Add(h22); }
  Tree23->Draw(input23,CUTMC1);         if(Tree23->Draw(input23,CUTMC1))         {DYM50_100 ->Add(h23); }
  Tree24->Draw(input24,CUTMC1);         if(Tree24->Draw(input24,CUTMC1))         {DYM50_70  ->Add(h24); }
  Tree25->Draw(input25,CUTMC1);         if(Tree25->Draw(input25,CUTMC1))         {QCD1000   ->Add(h25); }
  Tree26->Draw(input26,CUTMC1);         if(Tree26->Draw(input26,CUTMC1))         {QCD250    ->Add(h26); }
  Tree27->Draw(input27,CUTMC1);         if(Tree27->Draw(input27,CUTMC1))         {QCD500    ->Add(h27); }
  Tree28->Draw(input28,CUTMC1);         if(Tree28->Draw(input28,CUTMC1))         {TT        ->Add(h28); }
  Tree29->Draw(input29,CUTMC1);         if(Tree29->Draw(input29,CUTMC1))         {WJetsHT   ->Add(h29); }
  Tree30->Draw(input30,CUTMC1);         if(Tree30->Draw(input30,CUTMC1))         {WW        ->Add(h30); }
  Tree31->Draw(input31,CUTMC1);         if(Tree31->Draw(input31,CUTMC1))         {WZ        ->Add(h31); }
  Tree32->Draw(input32,CUTMC1);         if(Tree32->Draw(input32,CUTMC1))         {ZZ        ->Add(h32); }
  Tree33->Draw(input33,CUTMC1);         if(Tree33->Draw(input33,CUTMC1))         {SingleTop1->Add(h33); }
  Tree34->Draw(input34,CUTMC1);         if(Tree34->Draw(input34,CUTMC1))         {SingleTop2->Add(h34); }
  Tree35->Draw(input35,CUTMC1);         if(Tree35->Draw(input35,CUTMC1))         {SingleTop3->Add(h35); }
  Tree36->Draw(input36,CUTMC1);         if(Tree36->Draw(input36,CUTMC1))         {SingleTop4->Add(h36); }
  Tree37->Draw(input37,CUTMC1);         if(Tree37->Draw(input37,CUTMC1))         {SingleTop5->Add(h37); }
  Tree38->Draw(input38,CUTMC1);         if(Tree38->Draw(input38,CUTMC1))         {SingleTop6->Add(h38); }
  Tree39->Draw(input39,CUTData2,"E");   if(Tree39->Draw(input39,CUTData2,"E"))   {data      ->Add(h39); }
  Tree40->Draw(input40,CUTMC1);         if(Tree40->Draw(input40,CUTMC1))         {DY100     ->Add(h40); }
  Tree41->Draw(input41,CUTMC1);         if(Tree41->Draw(input41,CUTMC1))         {DY70      ->Add(h41); }
  Tree42->Draw(input42,CUTMC1);         if(Tree42->Draw(input42,CUTMC1))         {DYM50_100 ->Add(h42); }
  Tree43->Draw(input43,CUTMC1);         if(Tree43->Draw(input43,CUTMC1))         {DYM50_70  ->Add(h43); }
  Tree44->Draw(input44,CUTMC1);         if(Tree44->Draw(input44,CUTMC1))         {QCD1000   ->Add(h44); }
  Tree45->Draw(input45,CUTMC1);         if(Tree45->Draw(input45,CUTMC1))         {QCD250    ->Add(h45); }
  Tree46->Draw(input46,CUTMC1);         if(Tree46->Draw(input46,CUTMC1))         {QCD500    ->Add(h46); }
  Tree47->Draw(input47,CUTMC1);         if(Tree47->Draw(input47,CUTMC1))         {TT        ->Add(h47); }
  Tree48->Draw(input48,CUTMC1);         if(Tree48->Draw(input48,CUTMC1))         {WJetsHT   ->Add(h48); }
  Tree49->Draw(input49,CUTMC1);         if(Tree49->Draw(input49,CUTMC1))         {WW        ->Add(h49); }
  Tree50->Draw(input50,CUTMC1);         if(Tree50->Draw(input50,CUTMC1))         {WZ        ->Add(h50); }
  Tree51->Draw(input51,CUTMC1);         if(Tree51->Draw(input51,CUTMC1))         {ZZ        ->Add(h51); }
  Tree52->Draw(input52,CUTMC1);         if(Tree52->Draw(input52,CUTMC1))         {SingleTop1->Add(h52); }
  Tree53->Draw(input53,CUTMC1);         if(Tree53->Draw(input53,CUTMC1))         {SingleTop2->Add(h53); }
  Tree54->Draw(input54,CUTMC1);         if(Tree54->Draw(input54,CUTMC1))         {SingleTop3->Add(h54); }
  Tree55->Draw(input55,CUTMC1);         if(Tree55->Draw(input55,CUTMC1))         {SingleTop4->Add(h55); }
  Tree56->Draw(input56,CUTMC1);         if(Tree56->Draw(input56,CUTMC1))         {SingleTop5->Add(h56); }
  Tree57->Draw(input57,CUTMC1);         if(Tree57->Draw(input57,CUTMC1))         {SingleTop6->Add(h57); }
  Tree01->Draw(input58,CUTData1,"E");if(Tree01->Draw(input58,CUTData1,"E"))      {data2      =    h58;  }
  Tree20->Draw(input59,CUTData1,"E");if(Tree20->Draw(input59,CUTData1,"E"))      {data2     ->Add(h59); }
  Tree39->Draw(input60,CUTData1,"E");if(Tree39->Draw(input60,CUTData1,"E"))      {data2     ->Add(h60); }
  
  float w_DY100      = ( 39.100*19702./12511326.);
  float w_DY70       = ( 62.900*19702./11764538.);
  float w_DYM50_100  = (  4.220*19702./4146124.0);
  float w_DYM50_70   = ( 11.050*19702./5389313.0);
  float w_QCD1000    = (204.000*19702./13843863.);
  float w_QCD500     = (8426.00*19702./30599292.);
  float w_QCD250     = (276000.*19702./27062078.);
  float w_TT         = (225.197*19702./21675970.);
  float w_WW         = (57.1097*19702./10000431.);
  float w_WZ         = ( 33.210*19702./10000283.);
  float w_ZZ         = (  8.059*19702./9799908.0);
  float w_WJetsHT    = ( 25.220*19702./4971847.0);
  float w_SingleTop1 = ( 56.400*19702./3758227.0);
  float w_SingleTop2 = ( 3.7900*19702./259961.00);
  float w_SingleTop3 = ( 11.100*19702./497658.00);
  float w_SingleTop4 = ( 30.700*19702./1935072.0);
  float w_SingleTop5 = ( 1.7600*19702./139974.00);
  float w_SingleTop6 = ( 11.100*19702./493460.00);
  
  TH1F *ERR = new TH1F("","",data->GetNbinsX(),data->GetXaxis()->GetXmin(),data->GetXaxis()->GetXmax());
  for(int m=1; m<ERR->GetNbinsX()+1; m++){
    ERR->SetBinContent(m,w_DY100     *  DY100->GetBinContent(m)+
		       w_DY70      *  DY70->GetBinContent(m)+
		       w_DYM50_100 *  DYM50_100->GetBinContent(m)+
		       w_DYM50_70  *  DYM50_70->GetBinContent(m)+
		       w_QCD1000   *  QCD1000->GetBinContent(m)+
		       w_QCD500    *  QCD500->GetBinContent(m)+
		       w_QCD250    *  QCD250->GetBinContent(m)+
		       w_TT        *  TT->GetBinContent(m)+
		       w_WW        *  WW->GetBinContent(m)+
		       w_WZ        *  WZ->GetBinContent(m)+
		       w_ZZ        *  ZZ->GetBinContent(m)+
		       w_WJetsHT   *  WJetsHT->GetBinContent(m)+
		       w_SingleTop1*  SingleTop1->GetBinContent(m)+
		       w_SingleTop2*  SingleTop2->GetBinContent(m)+
		       w_SingleTop3*  SingleTop3->GetBinContent(m)+
		       w_SingleTop4*  SingleTop4->GetBinContent(m)+
		       w_SingleTop5*  SingleTop5->GetBinContent(m)+
		       w_SingleTop6*  SingleTop6->GetBinContent(m)
		       ); 
    ERR->SetBinError(m,sqrt(
			    w_DY100     *  w_DY100     *  DY100->GetBinContent(m)+
			    w_DY70      *  w_DY70      *  DY70->GetBinContent(m)+
			    w_DYM50_100 *  w_DYM50_100 *  DYM50_100->GetBinContent(m)+
			    w_DYM50_70  *  w_DYM50_70  *  DYM50_70->GetBinContent(m)+
			    w_QCD1000   *  w_QCD1000   *  QCD1000->GetBinContent(m)+
			    w_QCD500    *  w_QCD500    *  QCD500->GetBinContent(m)+
			    w_QCD250    *  w_QCD250    *  QCD250->GetBinContent(m)+
			    w_TT        *  w_TT        *  TT->GetBinContent(m)+
			    w_WW        *  w_WW        *  WW->GetBinContent(m)+
			    w_WZ        *  w_WZ        *  WZ->GetBinContent(m)+
			    w_ZZ        *  w_ZZ        *  ZZ->GetBinContent(m)+
			    w_WJetsHT   *  w_WJetsHT   *  WJetsHT->GetBinContent(m)+
			    w_SingleTop1*  w_SingleTop1*  SingleTop1->GetBinContent(m)+
			    w_SingleTop2*  w_SingleTop2*  SingleTop2->GetBinContent(m)+
			    w_SingleTop3*  w_SingleTop3*  SingleTop3->GetBinContent(m)+
			    w_SingleTop4*  w_SingleTop4*  SingleTop4->GetBinContent(m)+
			    w_SingleTop5*  w_SingleTop5*  SingleTop5->GetBinContent(m)+
			    w_SingleTop6*  w_SingleTop6*  SingleTop6->GetBinContent(m)
			    )); 
  }
  
  TH1F *ERR2 = new TH1F("","",data->GetNbinsX(),data->GetXaxis()->GetXmin(),data->GetXaxis()->GetXmax());
  for(int m=1; m<ERR2->GetNbinsX()+1; m++){
    ERR2->SetBinContent(m,w_TT      *  TT->GetBinContent(m)+
			w_SingleTop1*  SingleTop1->GetBinContent(m)+
			w_SingleTop2*  SingleTop2->GetBinContent(m)+
			w_SingleTop3*  SingleTop3->GetBinContent(m)+
			w_SingleTop4*  SingleTop4->GetBinContent(m)+
			w_SingleTop5*  SingleTop5->GetBinContent(m)+
			w_SingleTop6*  SingleTop6->GetBinContent(m)
		       ); 
    ERR2->SetBinError(m,sqrt(
			    w_TT        *  w_TT        *  TT->GetBinContent(m)+
			    w_SingleTop1*  w_SingleTop1*  SingleTop1->GetBinContent(m)+
			    w_SingleTop2*  w_SingleTop2*  SingleTop2->GetBinContent(m)+
			    w_SingleTop3*  w_SingleTop3*  SingleTop3->GetBinContent(m)+
			    w_SingleTop4*  w_SingleTop4*  SingleTop4->GetBinContent(m)+
			    w_SingleTop5*  w_SingleTop5*  SingleTop5->GetBinContent(m)+
			    w_SingleTop6*  w_SingleTop6*  SingleTop6->GetBinContent(m)
			    )); 
  }
  
  TH1F *ERR3 = new TH1F("","",data->GetNbinsX(),data->GetXaxis()->GetXmin(),data->GetXaxis()->GetXmax());
  for(int m=1; m<ERR3->GetNbinsX()+1; m++){
    ERR3->SetBinContent(m,w_DY100     *  DY100->GetBinContent(m)+
		       w_DY70      *  DY70->GetBinContent(m)+
		       w_DYM50_100 *  DYM50_100->GetBinContent(m)+
		       w_DYM50_70  *  DYM50_70->GetBinContent(m)+
		       w_QCD1000   *  QCD1000->GetBinContent(m)+
		       w_QCD500    *  QCD500->GetBinContent(m)+
		       w_QCD250    *  QCD250->GetBinContent(m)+
		       w_WW        *  WW->GetBinContent(m)+
		       w_WZ        *  WZ->GetBinContent(m)+
		       w_ZZ        *  ZZ->GetBinContent(m)+
		       w_WJetsHT   *  WJetsHT->GetBinContent(m)
		       ); 
    ERR3->SetBinError(m,sqrt(
			    w_DY100     *  w_DY100     *  DY100->GetBinContent(m)+
			    w_DY70      *  w_DY70      *  DY70->GetBinContent(m)+
			    w_DYM50_100 *  w_DYM50_100 *  DYM50_100->GetBinContent(m)+
			    w_DYM50_70  *  w_DYM50_70  *  DYM50_70->GetBinContent(m)+
			    w_QCD1000   *  w_QCD1000   *  QCD1000->GetBinContent(m)+
			    w_QCD500    *  w_QCD500    *  QCD500->GetBinContent(m)+
			    w_QCD250    *  w_QCD250    *  QCD250->GetBinContent(m)+
			    w_WW        *  w_WW        *  WW->GetBinContent(m)+
			    w_WZ        *  w_WZ        *  WZ->GetBinContent(m)+
			    w_ZZ        *  w_ZZ        *  ZZ->GetBinContent(m)+
			    w_WJetsHT   *  w_WJetsHT   *  WJetsHT->GetBinContent(m)
			    )); 
  }

  DY100->Scale(w_DY100);
  DY70->Scale(w_DY70);
  DYM50_100->Scale(w_DYM50_100);
  DYM50_70->Scale(w_DYM50_70);
  QCD1000->Scale(w_QCD1000);
  QCD500->Scale(w_QCD500);
  QCD250->Scale(w_QCD250);
  TT->Scale(w_TT);
  WW->Scale(w_WW);
  WZ->Scale(w_WZ);
  ZZ->Scale(w_ZZ);
  WJetsHT->Scale(w_WJetsHT);
  SingleTop1->Scale(w_SingleTop1);
  SingleTop2->Scale(w_SingleTop2);
  SingleTop3->Scale(w_SingleTop3);
  SingleTop4->Scale(w_SingleTop4);
  SingleTop5->Scale(w_SingleTop5);
  SingleTop6->Scale(w_SingleTop6);

  DY100->Add(DY70);
  DY100->Add(DYM50_70);
  DY100->Add(DYM50_100);
  QCD1000->Add(QCD250);
  QCD1000->Add(QCD500);
  WW->Add(WZ);
  WW->Add(ZZ);
  SingleTop1->Add(SingleTop2);
  SingleTop1->Add(SingleTop3);
  SingleTop1->Add(SingleTop4);
  SingleTop1->Add(SingleTop5);
  SingleTop1->Add(SingleTop6);
  TT->Add(SingleTop1);

  TH1D *RATIO = new TH1D("","",ERR->GetNbinsX(),ERR->GetXaxis()->GetXmin(),ERR->GetXaxis()->GetXmax());
  for(int m=1; m<ERR->GetNbinsX()+1; m++){ 
    if(ERR->GetBinContent(m)!=0 && data2->GetBinContent(m)!=0) {
      RATIO->SetBinContent(m,data2->GetBinContent(m)/ERR->GetBinContent(m));
      RATIO->SetBinError(m,sqrt(ERR->GetBinContent(m)*ERR->GetBinContent(m)*data2->GetBinError(m)*data2->GetBinError(m)
				+data2->GetBinContent(m)*data2->GetBinContent(m)*ERR->GetBinError(m)*ERR->GetBinError(m))/(ERR->GetBinContent(m)*ERR->GetBinContent(m)));
    }
  }

  //PARAMETERS
  float norm1=1.0; float norm2=1.0;
  float SYST1=0.0; float SYST2=0.0;
  float a0=-0.01;  float a0down=-0.90;  float a0up=-0.001;
  float b0=150.1;  float b0down=100.2;  float b0up=200.3;
  float c0=150.1;  float c0down=100.2;  float c0up=200.3;
  float g0=150.1;  float g0down=100.2;  float g0up=200.3;
  float h0=150.1;  float h0down=100.2;  float h0up=200.3;
  if(CHANNEL=="EleMuo"){
    b0=179.1; b0down=100.2; b0up=200.3;
    c0=269.1; c0down=200.2; c0up=300.3;
  }
  if(CHANNEL=="MuoMuo"){
    b0=179.1; b0down=100.2; b0up=200.3;
    c0=269.1; c0down=200.2; c0up=300.3;
  }
  if(CHANNEL=="EleEle"){
    b0=179.1; b0down=100.2; b0up=200.3;
    c0=269.1; c0down=200.2; c0up=300.3;
  }
  if(CHANNEL=="MuoTau"){
    norm1=1.78148+SYST1*1.25076;
    norm2=0.91313+SYST2*0.106924;
    b0=150.1; b0down=100.2; b0up=400.3;
    c0=150.1; c0down=10.2; c0up=200.3;
    g0=150.1; g0down=100.2; g0up=200.3;
    h0=150.1; h0down=100.2; h0up=200.3;
  }
  if(CHANNEL=="EleTau"){
    norm1=1.67067+SYST1*2.14245;
    norm2=0.87991+SYST2*0.116598;
    b0=150.1; b0down=100.2; b0up=300.3;
    c0=150.1; c0down=100.2; c0up=300.3;
    g0=150.1; g0down=100.2; g0up=200.3;
    h0=150.1; h0down=100.2; h0up=200.3;
  }


  //STEP 2 - MAKE FIT
  RooRealVar jetMass("jetMass","jetMass",20,200);
  RooPlot* frame  = jetMass.frame();
  jetMass.setRange("fullRange", 20, 200);
  RooDataHist dataset01("dataset01","dataset01",jetMass,ERR2);
  RooRealVar A0("A0","A0",  a0, a0down, a0up);
  RooRealVar B0("B0","B0",  b0, b0down, b0up);
  RooRealVar C0("C0","C0",  c0, c0down, c0up);
  RooRealVar D0("D0","D0", 82.9, 82.9-0.3, 82.9+0.3);
  RooRealVar E0("E0","E0",  7.1,  7.1-0.4,  7.1+0.4); 
  D0.setConstant(kTRUE);
  E0.setConstant(kTRUE);
  RooRealVar Npeak0("Npeak0",    "Npeak0",  50,0.,10000); 
  RooRealVar NnoPeak0("NnoPeak0","NnoPeak0",50,0.,10000); 
  RooGenericPdf nonPeaking0("nonPeaking0","nonPeaking0","TMath::Exp(A0*jetMass)*0.5*(1+(TMath::Erf((jetMass-B0)/C0)))",RooArgList(jetMass,A0,B0,C0));
  RooGaussian Peaking0("Peaking0","Peaking0",jetMass,D0,E0);
  RooAddPdf model01("model01","model01",RooArgList(Peaking0,nonPeaking0),RooArgList(Npeak0, NnoPeak0));
  RooFitResult* r01 = model01.fitTo(dataset01,RooFit::Range("fullRange"), RooFit::Extended(kTRUE), RooFit::Save());
  RooArgSet* params01 = model01.getVariables();
  RooDataHist dataset02("dataset02","dataset02",jetMass,ERR3);
  RooRealVar F0("F0","F0", -0.01, -0.900, -0.001);
  RooRealVar G0("G0","G0", g0, g0down, g0up);
  RooRealVar H0("H0","H0", h0, h0down, h0up);
  RooRealVar Nother0("Nother0",    "Nother0",  50,0.,10000); 
  RooGenericPdf Other0("Other0","Other0","TMath::Exp(F0*jetMass)*0.5*(1+(TMath::Erf((jetMass-G0)/H0)))",RooArgList(jetMass,F0,G0,H0));
  RooExtendPdf model02("model02","model02",Other0,Nother0,"fullRange");
  RooFitResult* r02 = model02.fitTo(dataset02,RooFit::Range("fullRange"), RooFit::Extended(kTRUE), RooFit::Save());
  RooArgSet* params02 = model02.getVariables();

  RooDataHist dataset1("dataset1","dataset1",jetMass,ERR);
  RooRealVar nsig1("nsig1","nsig1",50,0.,10000); 
  RooRealVar A1("A1","A1", params01->getRealValue("A0"), params01->getRealValue("A0")-A0.getError(), params01->getRealValue("A0")+A0.getError());
  RooRealVar B1("B1","B1", params01->getRealValue("B0"), params01->getRealValue("B0")-B0.getError(), params01->getRealValue("B0")+B0.getError());
  RooRealVar C1("C1","C1", params01->getRealValue("C0"), params01->getRealValue("C0")-C0.getError(), params01->getRealValue("C0")+C0.getError());
  RooRealVar D1("D1","D1", 83.4, 83.4-0.3, 83.4+0.3);
  RooRealVar E1("E1","E1",  7.2,  7.2-0.4,  7.2+0.4); 
  RooRealVar F1("F1","F1", params02->getRealValue("F0"), params02->getRealValue("F0")-F0.getError(), params02->getRealValue("F0")+F0.getError());
  RooRealVar G1("G1","G1", params02->getRealValue("G0"), params02->getRealValue("G0")-G0.getError(), params02->getRealValue("G0")+G0.getError());
  RooRealVar H1("H1","H1", params02->getRealValue("H0"), params02->getRealValue("H0")-H0.getError(), params02->getRealValue("H0")+H0.getError());
  RooRealVar Npeak1("Npeak1",    "Npeak1",   params01->getRealValue("Npeak0")  , 0, 10000); 
  RooRealVar NnoPeak1("NnoPeak1","NnoPeak1", params01->getRealValue("NnoPeak0"), 0, 10000); 
  RooRealVar Nother1("Nother1","Nother1",    params02->getRealValue("Nother0") , 0, 10000); 
  if(CHANNEL=="MuoTau" || CHANNEL=="EleTau") {
    A1.setConstant(kTRUE);
    B1.setConstant(kTRUE);
    C1.setConstant(kTRUE);
    D1.setConstant(kTRUE);
    E1.setConstant(kTRUE);
    F1.setConstant(kTRUE);
    G1.setConstant(kTRUE);
    H1.setConstant(kTRUE);
    Npeak1.setConstant(kTRUE);
    NnoPeak1.setConstant(kTRUE);
    Nother1.setConstant(kTRUE);
  }
  RooGaussian      Peaking1("Peaking1",   "Peaking1",   jetMass,D1,E1);
  RooGenericPdf nonPeaking1("nonPeaking1","nonPeaking1","TMath::Exp(A1*jetMass)*0.5*(1+(TMath::Erf((jetMass-B1)/C1)))",RooArgList(jetMass,A1,B1,C1));
  RooGenericPdf      Other1("Other1",     "Other1",     "TMath::Exp(F1*jetMass)*0.5*(1+(TMath::Erf((jetMass-G1)/H1)))",RooArgList(jetMass,F1,G1,H1));
  if(CHANNEL=="MuoTau" || CHANNEL=="EleTau") RooAddPdf model1("model1","model1",RooArgList(Peaking1,nonPeaking1,Other1),RooArgList(Npeak1, NnoPeak1, Nother1));
  else RooAddPdf model1("model1","model1",RooArgList(nonPeaking1),RooArgList(NnoPeak1));
  RooFitResult* r1 = model1.fitTo(dataset1,RooFit::Range("fullRange"), RooFit::Extended(kTRUE), RooFit::Save());
  dataset1.plotOn(frame,RooFit::Name("dataset1"),RooFit::Binning(bin),RooFit::LineColor(2),RooFit::MarkerColor(2),RooFit::LineWidth(2),RooFit::DrawOption("EX"));  
  model1.plotOn(frame,RooFit::LineColor(2),RooFit::Name("model1"));
  RooArgSet* params1 = model1.getVariables();

  jetMass.setRange("Range1", 20, 70); 
  jetMass.setRange("Range2", 140,200);  
  RooDataHist dataset2("dataset2","dataset2",jetMass,data);
  if(CHANNEL=="MuoTau" || CHANNEL=="EleTau") {
    RooRealVar A2("A2","A2", params01->getRealValue("A0"), params01->getRealValue("A0")-A0.getError(), params01->getRealValue("A0")+A0.getError());
    RooRealVar B2("B2","B2", params01->getRealValue("B0"), params01->getRealValue("B0")-B0.getError(), params01->getRealValue("B0")+B0.getError());
    RooRealVar C2("C2","C2", params01->getRealValue("C0"), params01->getRealValue("C0")-C0.getError(), params01->getRealValue("C0")+C0.getError());
  } else {
    RooRealVar A2("A2","A2", params1->getRealValue("A1"), params1->getRealValue("A1")-A1.getError(), params1->getRealValue("A1")+A1.getError());
    RooRealVar B2("B2","B2", params1->getRealValue("B1"), params1->getRealValue("B1")-B1.getError(), params1->getRealValue("B1")+B1.getError());
    RooRealVar C2("C2","C2", params1->getRealValue("C1"), params1->getRealValue("C1")-C1.getError(), params1->getRealValue("C1")+C1.getError());
  }
  RooRealVar D2("D2","D2", 84.7, 84.7-0.4, 84.7+0.4);
  RooRealVar E2("E2","E2",  7.9,  7.9-0.6,  7.9+0.6);
  RooRealVar F2("F2","F2", params02->getRealValue("F0"), params02->getRealValue("F0")-F0.getError(), params02->getRealValue("F0")+F0.getError());
  RooRealVar G2("G2","G2", params02->getRealValue("G0"), params02->getRealValue("G0")-G0.getError(), params02->getRealValue("G0")+G0.getError());
  RooRealVar H2("H2","H2", params02->getRealValue("H0"), params02->getRealValue("H0")-H0.getError(), params02->getRealValue("H0")+H0.getError());
  RooRealVar Npeak2(  "Npeak2",    "Npeak2",  norm1*params1->getRealValue("Npeak1")  , 0, 10000); 
  RooRealVar NnoPeak2("NnoPeak2","NnoPeak2",  norm2*params1->getRealValue("NnoPeak1"), 0, 10000); 
  RooRealVar Nother2( "Nother2","Nother2",          params1->getRealValue("Nother1"),  0, 10000); 
  A2.setConstant(kTRUE);
  B2.setConstant(kTRUE);
  C2.setConstant(kTRUE);
  D2.setConstant(kTRUE);
  E2.setConstant(kTRUE);
  F2.setConstant(kTRUE);
  G2.setConstant(kTRUE);
  H2.setConstant(kTRUE);
  Npeak2.setConstant(kTRUE);
  NnoPeak2.setConstant(kTRUE);
  RooGaussian      Peaking2("Peaking2",   "Peaking2",   jetMass,D2,E2);
  RooGenericPdf nonPeaking2("nonPeaking2","nonPeaking2","TMath::Exp(A2*jetMass)*0.5*(1+(TMath::Erf((jetMass-B2)/C2)))",RooArgList(jetMass,A2,B2,C2));
  RooGenericPdf      Other2("Other2",     "Other2",     "TMath::Exp(F2*jetMass)*0.5*(1+(TMath::Erf((jetMass-G2)/H2)))",RooArgList(jetMass,F2,G2,H2));
  if(CHANNEL=="MuoTau" || CHANNEL=="EleTau") RooAddPdf model2("model2","model2",RooArgList(Peaking2,nonPeaking2,Other2),RooArgList(Npeak2, NnoPeak2, Nother2));
  else  RooAddPdf model2("model2","model2",RooArgList(nonPeaking2),RooArgList(NnoPeak2));
  RooFitResult* r2 = model2.fitTo(dataset2,RooFit::Range("Range1,Range2"), RooFit::Extended(kTRUE), RooFit::Save());
  dataset2.plotOn(frame,RooFit::Name("dataset2"),RooFit::Binning(bin),RooFit::LineColor(1),RooFit::MarkerColor(1),RooFit::LineWidth(2),RooFit::DrawOption("EX"));  
  model2.plotOn(frame,RooFit::LineColor(1),RooFit::Name("model2"),RooFit::Range("fullRange"));
  RooArgSet* params2 = model2.getVariables();
  
  jetMass.setRange("cut1",  20, 70);
  jetMass.setRange("cut2",  70,110);
  jetMass.setRange("cut3", 110,140);
  jetMass.setRange("cut4", 140,200);
  RooAbsReal* MC1   = model1.createIntegral(jetMass, RooFit::NormSet(jetMass), RooFit::Range("cut1"));
  RooAbsReal* MC2   = model1.createIntegral(jetMass, RooFit::NormSet(jetMass), RooFit::Range("cut2"));
  RooAbsReal* MC3   = model1.createIntegral(jetMass, RooFit::NormSet(jetMass), RooFit::Range("cut3"));
  RooAbsReal* MC4   = model1.createIntegral(jetMass, RooFit::NormSet(jetMass), RooFit::Range("cut4"));
  RooAbsReal* DATA1 = model2.createIntegral(jetMass, RooFit::NormSet(jetMass), RooFit::Range("cut1"));
  RooAbsReal* DATA2 = model2.createIntegral(jetMass, RooFit::NormSet(jetMass), RooFit::Range("cut2"));
  RooAbsReal* DATA3 = model2.createIntegral(jetMass, RooFit::NormSet(jetMass), RooFit::Range("cut3"));
  RooAbsReal* DATA4 = model2.createIntegral(jetMass, RooFit::NormSet(jetMass), RooFit::Range("cut4"));
  float fraction1_MC = MC1->getVal();  float fraction1_DATA = DATA1->getVal();
  float fraction2_MC = MC2->getVal();  float fraction2_DATA = DATA2->getVal();
  float fraction3_MC = MC3->getVal();  float fraction3_DATA = DATA3->getVal();
  float fraction4_MC = MC4->getVal();  float fraction4_DATA = DATA4->getVal();
  float inDATA = fraction2_DATA/(fraction1_DATA+fraction4_DATA);
  NORM=inDATA*dataset2.sumEntries();
  NORMerr=inDATA*sqrt(dataset2.sumEntries());
  
  delete file01;
  delete file02;
  delete file03;
  delete file04;
  delete file05;
  delete file06;
  delete file07;
  delete file08;
  delete file09;
  delete file10;
  delete file11;
  delete file12;
  delete file13;
  delete file14;
  delete file15;
  delete file16;
  delete file17;
  delete file18;
  delete file19;
}


void SignalYield(char *channel, float XMassWidth, float XMassMin, float XMassMax, int SignalMass, char *cutMC1, float & SigYield){ 
  char demo       [500]; sprintf(demo,       "demo/Tree"); 
  char openTree   [500]; sprintf(openTree,   "%s%s",demo,channel);  
  TTree *TreeSig;
  double WeightSig = 1;
  if(SignalMass==800)      {
    TFile *fileSig = TFile::Open("ZH800.root");  
    TreeSig=(TTree*)fileSig->Get(openTree); 
    WeightSig = 19.700/19864;
  } else if(SignalMass==900) {
    TFile *fileSig = TFile::Open("ZH900.root");  
    TreeSig=(TTree*)fileSig->Get(openTree); 
    WeightSig = 19.700/19834;
  } else if(SignalMass<=1100) {
    TFile *fileSig = TFile::Open("ZH1000.root");  
    TreeSig=(TTree*)fileSig->Get(openTree); 
    WeightSig = 19.700/17958;
  } else if(SignalMass<=1400) {
    TFile *fileSig = TFile::Open("ZH1200.root");  
    TreeSig=(TTree*)fileSig->Get(openTree); 
    WeightSig = 19.700/19790;
  } else if(SignalMass<=1900) {
    TFile *fileSig = TFile::Open("ZH1500.root");  
    TreeSig=(TTree*)fileSig->Get(openTree); 
    WeightSig = 19.700/14099;
  } else if(SignalMass<=2400) {
    TFile *fileSig = TFile::Open("ZH2000.root");  
    TreeSig=(TTree*)fileSig->Get(openTree); 
    WeightSig = 19.700/13080;
  } else if(SignalMass==2500) {
    TFile *fileSig = TFile::Open("ZH2500.root");  
    TreeSig=(TTree*)fileSig->Get(openTree); 
    WeightSig = 19.700/13091;
  }  
  
  TString CHANNEL = channel; 
	
  char CUTMC1[1000];
  sprintf(CUTMC1,   "%s)", cutMC1  );
  char CUT1[500]; sprintf(CUT1,  "XMassSVFit>>data_sig(2,%f,%f)",XMassMin,XMassMax+XMassWidth);
  TreeSig->SetWeight(WeightSig);
  TreeSig->Draw(CUT1,CUTMC1);  
  SigYield = data_sig->Integral(); 
}


void SaveDatacard(char *channel, float DATYield, float BkgYield, float BkgYieldErr, float NSideband, float Alpha1, float Alpha2, float AlphaErr1, float AlphaErr2,float NORMforALPHA, float SigYield, int SignalMass, float lep1PtCut, float tauPtCut, int bTagCut, float METCut, float deltaRCut, float MassSvfitCut, float MassVisCut){
  SigYield=SigYield*0.935797; // V-TAG SCALE FACTOR
  char saveName [500]; sprintf(saveName, "datacard_%s_%i.txt",channel,SignalMass);
  
  //SYSTEMATICS HERE
  float TauIDStandard = 1;
  if(channel=="MuoTau" && SignalMass== 800) TauIDStandard = 1 + 0.089;
  if(channel=="EleTau" && SignalMass== 800) TauIDStandard = 1 + 0.085;
  if(channel=="MuoTau" && SignalMass== 900) TauIDStandard = 1 + 0.089;
  if(channel=="EleTau" && SignalMass== 900) TauIDStandard = 1 + 0.085;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) TauIDStandard = 1 + 0.089;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) TauIDStandard = 1 + 0.085;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) TauIDStandard = 1 + 0.089;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) TauIDStandard = 1 + 0.085;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) TauIDStandard = 1 + 0.099;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) TauIDStandard = 1 + 0.097;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) TauIDStandard = 1 + 0.111;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) TauIDStandard = 1 + 0.108;
  if(channel=="MuoTau" && SignalMass==2500) TauIDStandard = 1 + 0.124;
  if(channel=="EleTau" && SignalMass==2500) TauIDStandard = 1 + 0.119;
  float TauCleaning   = 1;
  if(channel=="MuoTau" && SignalMass== 800) TauCleaning = 1 + 0.004;
  if(channel=="EleTau" && SignalMass== 800) TauCleaning = 1 + 0.005;
  if(channel=="MuoTau" && SignalMass== 900) TauCleaning = 1 + 0.004;
  if(channel=="EleTau" && SignalMass== 900) TauCleaning = 1 + 0.005;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) TauCleaning = 1 + 0.004;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) TauCleaning = 1 + 0.005;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) TauCleaning = 1 + 0.004;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) TauCleaning = 1 + 0.005;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) TauCleaning = 1 + 0.035;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) TauCleaning = 1 + 0.031;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) TauCleaning = 1 + 0.060;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) TauCleaning = 1 + 0.068;
  if(channel=="MuoTau" && SignalMass==2500) TauCleaning = 1 + 0.070;
  if(channel=="EleTau" && SignalMass==2500) TauCleaning = 1 + 0.157;
  float MuonCleaning   = 1;
  if(channel=="MuoTau" && SignalMass== 800) MuonCleaning = 1 + 0.007;
  if(channel=="MuoTau" && SignalMass== 900) MuonCleaning = 1 + 0.007;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) MuonCleaning = 1 + 0.007;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) MuonCleaning = 1 + 0.007;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) MuonCleaning = 1 + 0.017;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) MuonCleaning = 1 + 0.016;
  if(channel=="MuoTau" && SignalMass==2500) MuonCleaning = 1 + 0.010;
  float ModifiedPFIso   = 0;
  if(channel=="MuoTau" && SignalMass== 800) ModifiedPFIso = 1 + 0.012;
  if(channel=="EleTau" && SignalMass== 800) ModifiedPFIso = 1 + 0.035;
  if(channel=="MuoTau" && SignalMass== 900) ModifiedPFIso = 1 + 0.012;
  if(channel=="EleTau" && SignalMass== 900) ModifiedPFIso = 1 + 0.035;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) ModifiedPFIso = 1 + 0.012;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) ModifiedPFIso = 1 + 0.035;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) ModifiedPFIso = 1 + 0.012;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) ModifiedPFIso = 1 + 0.035;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) ModifiedPFIso = 1 + 0.061;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) ModifiedPFIso = 1 + 0.035;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) ModifiedPFIso = 1 + 0.095;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) ModifiedPFIso = 1 + 0.098;
  if(channel=="MuoTau" && SignalMass==2500) ModifiedPFIso = 1 + 0.143;
  if(channel=="EleTau" && SignalMass==2500) ModifiedPFIso = 1 + 0.208;
  float PUReweighting = 1;
  if(channel=="EleMuo" && SignalMass== 800) PUReweighting = 1 + 0.006;
  if(channel=="MuoMuo" && SignalMass== 800) PUReweighting = 1 + 0.013;
  if(channel=="EleEle" && SignalMass== 800) PUReweighting = 1 + 0.004;
  if(channel=="MuoTau" && SignalMass== 800) PUReweighting = 1 + 0.011;
  if(channel=="EleTau" && SignalMass== 800) PUReweighting = 1 + 0.012;
  if(channel=="EleMuo" && SignalMass== 900) PUReweighting = 1 + 0.006;
  if(channel=="MuoMuo" && SignalMass== 900) PUReweighting = 1 + 0.013;
  if(channel=="EleEle" && SignalMass== 900) PUReweighting = 1 + 0.004;
  if(channel=="MuoTau" && SignalMass== 900) PUReweighting = 1 + 0.011;
  if(channel=="EleTau" && SignalMass== 900) PUReweighting = 1 + 0.012;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) PUReweighting = 1 + 0.006;
  if(channel=="MuoMuo" && SignalMass>=1000 && SignalMass<1200) PUReweighting = 1 + 0.013;
  if(channel=="EleEle" && SignalMass>=1000 && SignalMass<1200) PUReweighting = 1 + 0.004;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) PUReweighting = 1 + 0.011;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) PUReweighting = 1 + 0.012;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) PUReweighting = 1 + 0.006;
  if(channel=="MuoMuo" && SignalMass>=1200 && SignalMass<1500) PUReweighting = 1 + 0.013;
  if(channel=="EleEle" && SignalMass>=1200 && SignalMass<1500) PUReweighting = 1 + 0.004;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) PUReweighting = 1 + 0.011;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) PUReweighting = 1 + 0.012;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) PUReweighting = 1 + 0.018;
  if(channel=="MuoMuo" && SignalMass>=1500 && SignalMass<2000) PUReweighting = 1 + 0.015;
  if(channel=="EleEle" && SignalMass>=1500 && SignalMass<2000) PUReweighting = 1 + 0.011;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) PUReweighting = 1 + 0.014;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) PUReweighting = 1 + 0.007;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) PUReweighting = 1 + 0.002;
  if(channel=="MuoMuo" && SignalMass>=2000 && SignalMass<2500) PUReweighting = 1 + 0.010;
  if(channel=="EleEle" && SignalMass>=2000 && SignalMass<2500) PUReweighting = 1 + 0.004;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) PUReweighting = 1 + 0.004;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) PUReweighting = 1 + 0.012;
  if(channel=="EleMuo" && SignalMass==2500) PUReweighting = 1 + 0.022;
  if(channel=="MuoMuo" && SignalMass==2500) PUReweighting = 1 + 0.019;
  if(channel=="EleEle" && SignalMass==2500) PUReweighting = 1 + 0.015;
  if(channel=="MuoTau" && SignalMass==2500) PUReweighting = 1 + 0.002;
  if(channel=="EleTau" && SignalMass==2500) PUReweighting = 1 + 0.012;
  float BTagSyst = 1;
  if(channel=="EleMuo" && SignalMass== 800) BTagSyst = 1 + 0.018;
  if(channel=="MuoMuo" && SignalMass== 800) BTagSyst = 1 + 0.024;
  if(channel=="EleEle" && SignalMass== 800) BTagSyst = 1 + 0.040;
  if(channel=="MuoTau" && SignalMass== 800) BTagSyst = 1 + 0.023;
  if(channel=="EleTau" && SignalMass== 800) BTagSyst = 1 + 0.024;
  if(channel=="EleMuo" && SignalMass== 900) BTagSyst = 1 + 0.018;
  if(channel=="MuoMuo" && SignalMass== 900) BTagSyst = 1 + 0.024;
  if(channel=="EleEle" && SignalMass== 900) BTagSyst = 1 + 0.040;
  if(channel=="MuoTau" && SignalMass== 900) BTagSyst = 1 + 0.023;
  if(channel=="EleTau" && SignalMass== 900) BTagSyst = 1 + 0.024;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) BTagSyst = 1 + 0.018;
  if(channel=="MuoMuo" && SignalMass>=1000 && SignalMass<1200) BTagSyst = 1 + 0.024;
  if(channel=="EleEle" && SignalMass>=1000 && SignalMass<1200) BTagSyst = 1 + 0.040;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) BTagSyst = 1 + 0.023;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) BTagSyst = 1 + 0.024;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) BTagSyst = 1 + 0.018;
  if(channel=="MuoMuo" && SignalMass>=1200 && SignalMass<1500) BTagSyst = 1 + 0.024;
  if(channel=="EleEle" && SignalMass>=1200 && SignalMass<1500) BTagSyst = 1 + 0.040;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) BTagSyst = 1 + 0.023;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) BTagSyst = 1 + 0.024;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) BTagSyst = 1 + 0.027;
  if(channel=="MuoMuo" && SignalMass>=1500 && SignalMass<2000) BTagSyst = 1 + 0.023;
  if(channel=="EleEle" && SignalMass>=1500 && SignalMass<2000) BTagSyst = 1 + 0.056;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) BTagSyst = 1 + 0.026;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) BTagSyst = 1 + 0.026;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) BTagSyst = 1 + 0.031;
  if(channel=="MuoMuo" && SignalMass>=2000 && SignalMass<2500) BTagSyst = 1 + 0.023;
  if(channel=="EleEle" && SignalMass>=2000 && SignalMass<2500) BTagSyst = 1 + 0.030;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) BTagSyst = 1 + 0.025;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) BTagSyst = 1 + 0.025;
  if(channel=="EleMuo" && SignalMass==2500) BTagSyst = 1 + 0.021;
  if(channel=="MuoMuo" && SignalMass==2500) BTagSyst = 1 + 0.025;
  if(channel=="EleEle" && SignalMass==2500) BTagSyst = 1 + 0.019;
  if(channel=="MuoTau" && SignalMass==2500) BTagSyst = 1 + 0.027;
  if(channel=="EleTau" && SignalMass==2500) BTagSyst = 1 + 0.024;
  float SYSTNormalization = 1;
  if(channel=="EleMuo") SYSTNormalization = 1 + 0.357;
  if(channel=="MuoMuo") SYSTNormalization = 1 + 0.254;
  if(channel=="EleEle") SYSTNormalization = 1 + 0.467;
  if(channel=="MuoTau") SYSTNormalization = 1 + 0.177;
  if(channel=="EleTau") SYSTNormalization = 1 + 0.291;
  float EleID = 1;
  if(channel=="EleMuo" && SignalMass== 800) EleID = 1 + 0.011;
  if(channel=="EleEle" && SignalMass== 800) EleID = 1 + 0.026;
  if(channel=="EleTau" && SignalMass== 800) EleID = 1 + 0.013;
  if(channel=="EleMuo" && SignalMass== 900) EleID = 1 + 0.011;
  if(channel=="EleEle" && SignalMass== 900) EleID = 1 + 0.026;
  if(channel=="EleTau" && SignalMass== 900) EleID = 1 + 0.013;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) EleID = 1 + 0.011;
  if(channel=="EleEle" && SignalMass>=1000 && SignalMass<1200) EleID = 1 + 0.026;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) EleID = 1 + 0.013;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) EleID = 1 + 0.011;
  if(channel=="EleEle" && SignalMass>=1200 && SignalMass<1500) EleID = 1 + 0.026;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) EleID = 1 + 0.013;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) EleID = 1 + 0.015;
  if(channel=="EleEle" && SignalMass>=1500 && SignalMass<2000) EleID = 1 + 0.025;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) EleID = 1 + 0.013;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) EleID = 1 + 0.016;
  if(channel=="EleEle" && SignalMass>=2000 && SignalMass<2500) EleID = 1 + 0.030;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) EleID = 1 + 0.016;
  if(channel=="EleMuo" && SignalMass==2500) EleID = 1 + 0.014;
  if(channel=="EleEle" && SignalMass==2500) EleID = 1 + 0.035;
  if(channel=="EleTau" && SignalMass==2500) EleID = 1 + 0.018;
  float EleScale = 1;
  if(channel=="EleMuo" && SignalMass== 800) EleScale = 1 + 0.000;
  if(channel=="EleEle" && SignalMass== 800) EleScale = 1 + 0.000;
  if(channel=="EleTau" && SignalMass== 800) EleScale = 1 + 0.004;
  if(channel=="EleMuo" && SignalMass== 900) EleScale = 1 + 0.000;
  if(channel=="EleEle" && SignalMass== 900) EleScale = 1 + 0.000;
  if(channel=="EleTau" && SignalMass== 900) EleScale = 1 + 0.004;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) EleScale = 1 + 0.000;
  if(channel=="EleEle" && SignalMass>=1000 && SignalMass<1200) EleScale = 1 + 0.000;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) EleScale = 1 + 0.004;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) EleScale = 1 + 0.000;
  if(channel=="EleEle" && SignalMass>=1200 && SignalMass<1500) EleScale = 1 + 0.000;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) EleScale = 1 + 0.004;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) EleScale = 1 + 0.004;
  if(channel=="EleEle" && SignalMass>=1500 && SignalMass<2000) EleScale = 1 + 0.001;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) EleScale = 1 + 0.001;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) EleScale = 1 + 0.000;
  if(channel=="EleEle" && SignalMass>=2000 && SignalMass<2500) EleScale = 1 + 0.009;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) EleScale = 1 + 0.001;
  if(channel=="EleMuo" && SignalMass==2500) EleScale = 1 + 0.000;
  if(channel=="EleEle" && SignalMass==2500) EleScale = 1 + 0.000;
  if(channel=="EleTau" && SignalMass==2500) EleScale = 1 + 0.000;
  float EleResol = 1;
  if(channel=="EleMuo" && SignalMass== 800) EleResol = 1 + 0.000;
  if(channel=="EleEle" && SignalMass== 800) EleResol = 1 + 0.001;
  if(channel=="EleTau" && SignalMass== 800) EleResol = 1 + 0.005;
  if(channel=="EleMuo" && SignalMass== 900) EleResol = 1 + 0.000;
  if(channel=="EleEle" && SignalMass== 900) EleResol = 1 + 0.001;
  if(channel=="EleTau" && SignalMass== 900) EleResol = 1 + 0.005;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) EleResol = 1 + 0.000;
  if(channel=="EleEle" && SignalMass>=1000 && SignalMass<1200) EleResol = 1 + 0.001;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) EleResol = 1 + 0.005;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) EleResol = 1 + 0.000;
  if(channel=="EleEle" && SignalMass>=1200 && SignalMass<1500) EleResol = 1 + 0.001;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) EleResol = 1 + 0.005;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) EleResol = 1 + 0.006;
  if(channel=="EleEle" && SignalMass>=1500 && SignalMass<2000) EleResol = 1 + 0.024;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) EleResol = 1 + 0.002;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) EleResol = 1 + 0.000;
  if(channel=="EleEle" && SignalMass>=2000 && SignalMass<2500) EleResol = 1 + 0.003;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) EleResol = 1 + 0.000;
  if(channel=="EleMuo" && SignalMass==2500) EleResol = 1 + 0.001;
  if(channel=="EleEle" && SignalMass==2500) EleResol = 1 + 0.019;
  if(channel=="EleTau" && SignalMass==2500) EleResol = 1 + 0.007;
  float MuoID = 1;
  if(channel=="EleMuo" && SignalMass== 800) MuoID = 1 + 0.010;
  if(channel=="MuoMuo" && SignalMass== 800) MuoID = 1 + 0.057;
  if(channel=="MuoTau" && SignalMass== 800) MuoID = 1 + 0.009;
  if(channel=="EleMuo" && SignalMass== 900) MuoID = 1 + 0.010;
  if(channel=="MuoMuo" && SignalMass== 900) MuoID = 1 + 0.057;
  if(channel=="MuoTau" && SignalMass== 900) MuoID = 1 + 0.009;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) MuoID = 1 + 0.010;
  if(channel=="MuoMuo" && SignalMass>=1000 && SignalMass<1200) MuoID = 1 + 0.057;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) MuoID = 1 + 0.009;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) MuoID = 1 + 0.010;
  if(channel=="MuoMuo" && SignalMass>=1200 && SignalMass<1500) MuoID = 1 + 0.057;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) MuoID = 1 + 0.009;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) MuoID = 1 + 0.009;
  if(channel=="MuoMuo" && SignalMass>=1500 && SignalMass<2000) MuoID = 1 + 0.057;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) MuoID = 1 + 0.008;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) MuoID = 1 + 0.009;
  if(channel=="MuoMuo" && SignalMass>=2000 && SignalMass<2500) MuoID = 1 + 0.057;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) MuoID = 1 + 0.008;
  if(channel=="EleMuo" && SignalMass==2500) MuoID = 1 + 0.008;
  if(channel=="MuoMuo" && SignalMass==2500) MuoID = 1 + 0.057;
  if(channel=="MuoTau" && SignalMass==2500) MuoID = 1 + 0.008;
  float MuoScale = 1;
  if(channel=="EleMuo" && SignalMass== 800) MuoScale = 1 + 0.007;
  if(channel=="MuoMuo" && SignalMass== 800) MuoScale = 1 + 0.019;
  if(channel=="MuoTau" && SignalMass== 800) MuoScale = 1 + 0.003;
  if(channel=="EleMuo" && SignalMass== 900) MuoScale = 1 + 0.007;
  if(channel=="MuoMuo" && SignalMass== 900) MuoScale = 1 + 0.019;
  if(channel=="MuoTau" && SignalMass== 900) MuoScale = 1 + 0.003;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) MuoScale = 1 + 0.007;
  if(channel=="MuoMuo" && SignalMass>=1000 && SignalMass<1200) MuoScale = 1 + 0.019;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) MuoScale = 1 + 0.003;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) MuoScale = 1 + 0.007;
  if(channel=="MuoMuo" && SignalMass>=1200 && SignalMass<1500) MuoScale = 1 + 0.019;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) MuoScale = 1 + 0.003;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) MuoScale = 1 + 0.011;
  if(channel=="MuoMuo" && SignalMass>=1500 && SignalMass<2000) MuoScale = 1 + 0.002;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) MuoScale = 1 + 0.008;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) MuoScale = 1 + 0.001;
  if(channel=="MuoMuo" && SignalMass>=2000 && SignalMass<2500) MuoScale = 1 + 0.000;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) MuoScale = 1 + 0.007;
  if(channel=="EleMuo" && SignalMass==2500) MuoScale = 1 + 0.005;
  if(channel=="MuoMuo" && SignalMass==2500) MuoScale = 1 + 0.009;
  if(channel=="MuoTau" && SignalMass==2500) MuoScale = 1 + 0.005;
  float MuoResol = 1;
  if(channel=="EleMuo" && SignalMass== 800) MuoResol = 1 + 0.000;
  if(channel=="MuoMuo" && SignalMass== 800) MuoResol = 1 + 0.019;
  if(channel=="MuoTau" && SignalMass== 800) MuoResol = 1 + 0.001;
  if(channel=="EleMuo" && SignalMass== 900) MuoResol = 1 + 0.000;
  if(channel=="MuoMuo" && SignalMass== 900) MuoResol = 1 + 0.019;
  if(channel=="MuoTau" && SignalMass== 900) MuoResol = 1 + 0.001;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) MuoResol = 1 + 0.000;
  if(channel=="MuoMuo" && SignalMass>=1000 && SignalMass<1200) MuoResol = 1 + 0.019;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) MuoResol = 1 + 0.001;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) MuoResol = 1 + 0.000;
  if(channel=="MuoMuo" && SignalMass>=1200 && SignalMass<1500) MuoResol = 1 + 0.019;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) MuoResol = 1 + 0.001;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) MuoResol = 1 + 0.005;
  if(channel=="MuoMuo" && SignalMass>=1500 && SignalMass<2000) MuoResol = 1 + 0.000;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) MuoResol = 1 + 0.004;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) MuoResol = 1 + 0.001;
  if(channel=="MuoMuo" && SignalMass>=2000 && SignalMass<2500) MuoResol = 1 + 0.000;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) MuoResol = 1 + 0.002;
  if(channel=="EleMuo" && SignalMass==2500) MuoResol = 1 + 0.000;
  if(channel=="MuoMuo" && SignalMass==2500) MuoResol = 1 + 0.000;
  if(channel=="MuoTau" && SignalMass==2500) MuoResol = 1 + 0.001;
  float TauScale = 1;
  if(channel=="MuoTau" && SignalMass== 800) TauScale = 1 + 0.003;
  if(channel=="EleTau" && SignalMass== 800) TauScale = 1 + 0.024;
  if(channel=="MuoTau" && SignalMass== 900) TauScale = 1 + 0.003;
  if(channel=="EleTau" && SignalMass== 900) TauScale = 1 + 0.024;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) TauScale = 1 + 0.003;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) TauScale = 1 + 0.024;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) TauScale = 1 + 0.003;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) TauScale = 1 + 0.024;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) TauScale = 1 + 0.010;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) TauScale = 1 + 0.006;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) TauScale = 1 + 0.004;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) TauScale = 1 + 0.009;
  if(channel=="MuoTau" && SignalMass==2500) TauScale = 1 + 0.002;
  if(channel=="EleTau" && SignalMass==2500) TauScale = 1 + 0.005;
  float JES = 1;
  if(channel=="EleMuo" && SignalMass== 800) JES = 1 + 0.011;
  if(channel=="MuoMuo" && SignalMass== 800) JES = 1 + 0.026;
  if(channel=="EleEle" && SignalMass== 800) JES = 1 + 0.043;
  if(channel=="MuoTau" && SignalMass== 800) JES = 1 + 0.009;
  if(channel=="EleTau" && SignalMass== 800) JES = 1 + 0.014;
  if(channel=="EleMuo" && SignalMass== 900) JES = 1 + 0.011;
  if(channel=="MuoMuo" && SignalMass== 900) JES = 1 + 0.026;
  if(channel=="EleEle" && SignalMass== 900) JES = 1 + 0.043;
  if(channel=="MuoTau" && SignalMass== 900) JES = 1 + 0.009;
  if(channel=="EleTau" && SignalMass== 900) JES = 1 + 0.014;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) JES = 1 + 0.011;
  if(channel=="MuoMuo" && SignalMass>=1000 && SignalMass<1200) JES = 1 + 0.026;
  if(channel=="EleEle" && SignalMass>=1000 && SignalMass<1200) JES = 1 + 0.043;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) JES = 1 + 0.009;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) JES = 1 + 0.014;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) JES = 1 + 0.011;
  if(channel=="MuoMuo" && SignalMass>=1200 && SignalMass<1500) JES = 1 + 0.026;
  if(channel=="EleEle" && SignalMass>=1200 && SignalMass<1500) JES = 1 + 0.043;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) JES = 1 + 0.009;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) JES = 1 + 0.014;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) JES = 1 + 0.005;
  if(channel=="MuoMuo" && SignalMass>=1500 && SignalMass<2000) JES = 1 + 0.012;
  if(channel=="EleEle" && SignalMass>=1500 && SignalMass<2000) JES = 1 + 0.008;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) JES = 1 + 0.007;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) JES = 1 + 0.003;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) JES = 1 + 0.009;
  if(channel=="MuoMuo" && SignalMass>=2000 && SignalMass<2500) JES = 1 + 0.010;
  if(channel=="EleEle" && SignalMass>=2000 && SignalMass<2500) JES = 1 + 0.020;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) JES = 1 + 0.001;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) JES = 1 + 0.005;
  if(channel=="EleMuo" && SignalMass==2500) JES = 1 + 0.016;
  if(channel=="MuoMuo" && SignalMass==2500) JES = 1 + 0.007;
  if(channel=="EleEle" && SignalMass==2500) JES = 1 + 0.001;
  if(channel=="MuoTau" && SignalMass==2500) JES = 1 + 0.015;
  if(channel=="EleTau" && SignalMass==2500) JES = 1 + 0.009;
  float JER = 1;
  if(channel=="EleMuo" && SignalMass== 800) JER = 1 + 0.007;
  if(channel=="MuoMuo" && SignalMass== 800) JER = 1 + 0.000;
  if(channel=="EleEle" && SignalMass== 800) JER = 1 + 0.000;
  if(channel=="MuoTau" && SignalMass== 800) JER = 1 + 0.001;
  if(channel=="EleTau" && SignalMass== 800) JER = 1 + 0.003;
  if(channel=="EleMuo" && SignalMass== 900) JER = 1 + 0.007;
  if(channel=="MuoMuo" && SignalMass== 900) JER = 1 + 0.000;
  if(channel=="EleEle" && SignalMass== 900) JER = 1 + 0.000;
  if(channel=="MuoTau" && SignalMass== 900) JER = 1 + 0.001;
  if(channel=="EleTau" && SignalMass== 900) JER = 1 + 0.003;
  if(channel=="EleMuo" && SignalMass>=1000 && SignalMass<1200) JER = 1 + 0.007;
  if(channel=="MuoMuo" && SignalMass>=1000 && SignalMass<1200) JER = 1 + 0.000;
  if(channel=="EleEle" && SignalMass>=1000 && SignalMass<1200) JER = 1 + 0.000;
  if(channel=="MuoTau" && SignalMass>=1000 && SignalMass<1200) JER = 1 + 0.001;
  if(channel=="EleTau" && SignalMass>=1000 && SignalMass<1200) JER = 1 + 0.003;
  if(channel=="EleMuo" && SignalMass>=1200 && SignalMass<1500) JER = 1 + 0.007;
  if(channel=="MuoMuo" && SignalMass>=1200 && SignalMass<1500) JER = 1 + 0.000;
  if(channel=="EleEle" && SignalMass>=1200 && SignalMass<1500) JER = 1 + 0.000;
  if(channel=="MuoTau" && SignalMass>=1200 && SignalMass<1500) JER = 1 + 0.001;
  if(channel=="EleTau" && SignalMass>=1200 && SignalMass<1500) JER = 1 + 0.003;
  if(channel=="EleMuo" && SignalMass>=1500 && SignalMass<2000) JER = 1 + 0.007;
  if(channel=="MuoMuo" && SignalMass>=1500 && SignalMass<2000) JER = 1 + 0.016;
  if(channel=="EleEle" && SignalMass>=1500 && SignalMass<2000) JER = 1 + 0.022;
  if(channel=="MuoTau" && SignalMass>=1500 && SignalMass<2000) JER = 1 + 0.018;
  if(channel=="EleTau" && SignalMass>=1500 && SignalMass<2000) JER = 1 + 0.012;
  if(channel=="EleMuo" && SignalMass>=2000 && SignalMass<2500) JER = 1 + 0.000;
  if(channel=="MuoMuo" && SignalMass>=2000 && SignalMass<2500) JER = 1 + 0.005;
  if(channel=="EleEle" && SignalMass>=2000 && SignalMass<2500) JER = 1 + 0.017;
  if(channel=="MuoTau" && SignalMass>=2000 && SignalMass<2500) JER = 1 + 0.017;
  if(channel=="EleTau" && SignalMass>=2000 && SignalMass<2500) JER = 1 + 0.015;
  if(channel=="EleMuo" && SignalMass==2500) JER = 1 + 0.009;
  if(channel=="MuoMuo" && SignalMass==2500) JER = 1 + 0.003;
  if(channel=="EleEle" && SignalMass==2500) JER = 1 + 0.000;
  if(channel=="MuoTau" && SignalMass==2500) JER = 1 + 0.003;
  if(channel=="EleTau" && SignalMass==2500) JER = 1 + 0.011;


  //DATACARD
  if(BkgYield==0) BkgYield=0.00001;
  ofstream myfile;
  myfile.open(saveName); 
  myfile<<"imax 1"<<endl;
  myfile<<"jmax 1"<<endl;
  myfile<<"kmax *"<<endl;
  myfile<<"--------------------------------------------------------------------------------------------"<<endl;
  myfile<<"bin                           "<<channel<<endl;
  myfile<<"observation                   "<<DATYield<<endl;
  myfile<<"--------------------------------------------------------------------------------------------"<<endl;
  myfile<<"bin                           "<<channel<<"           "<<channel<<endl;
  myfile<<"process                       signal"<<channel<<"     background"<<channel<<endl;
  myfile<<"process                       0                1"<<endl;
  myfile<<"rate                          "<<SigYield<<"         "<<BkgYield<<endl;
  myfile<<"--------------------------------------------------------------------------------------------"<<endl;
  myfile<<"lumi                lnN       1.026            -"<<endl;
  if(NSideband!=0){
    myfile<<"Bkg"<<channel<<"           gmN "<<NSideband<<"     -                "<<BkgYield/NSideband<<"    #"<<BkgYield<<"+/-"<<BkgYieldErr<<endl;
    myfile<<"Alpha"<<channel<<"         lnN       -                "<<1+sqrt(AlphaErr1*AlphaErr1+AlphaErr2*AlphaErr2)/(BkgYield/(NSideband*NORMforALPHA))<<endl;
    myfile<<"Normalization"<<channel<<" lnN       -                "<<SYSTNormalization<<endl;
  } else {
    myfile<<"Bkg"<<channel<<"           gmN "<<NSideband<<"     -                "<<(Alpha1+Alpha2)*NORMforALPHA<<"    #"<<BkgYield<<"+/-"<<BkgYieldErr<<endl;
    myfile<<"Alpha"<<channel<<"         lnN       -                "<<1+sqrt(AlphaErr1*AlphaErr1+AlphaErr2*AlphaErr2)/((Alpha1+Alpha2)*NORMforALPHA+1e-10)<<endl;
    myfile<<"Normalization"<<channel<<" lnN       -                "<<SYSTNormalization<<endl;
  }
  myfile<<"VTag                lnN       "<<1+0.0643192/0.935797<<"          -"<<endl;
  myfile<<"PUReweighting       lnN       "<<PUReweighting<<"            -"<<endl;
  myfile<<"BTagSyst            lnN       "<<BTagSyst<<"            -"<<endl;
  myfile<<"JES                 lnN       "<<JES<<"            -"<<endl;
  myfile<<"JER                 lnN       "<<JER<<"            -"<<endl;
  if(channel=="MuoTau" || channel=="EleTau") myfile<<"TauIDStandard       lnN       "<<TauIDStandard<<"            -"<<endl;
  if(channel=="MuoTau" || channel=="EleTau") myfile<<"TauCleaning"<<channel<<"   lnN       "<<TauCleaning<<"            -"<<endl;
  if(channel=="MuoTau" || channel=="EleTau") myfile<<"ModifiedPFIso"<<channel<<" lnN       "<<ModifiedPFIso<<"            -"<<endl;
  if(channel=="EleMuo" || channel=="EleEle" || channel=="EleTau") myfile<<"EleID         lnN       "<<EleID<<"            -"<<endl;
  if(channel=="EleMuo" || channel=="EleEle" || channel=="EleTau") myfile<<"EleScale      lnN       "<<EleScale<<"            -"<<endl;
  if(channel=="EleMuo" || channel=="EleEle" || channel=="EleTau") myfile<<"EleResol      lnN       "<<EleResol<<"            -"<<endl;
  if(channel=="EleMuo" || channel=="MuoMuo" || channel=="MuoTau") myfile<<"MuoID         lnN       "<<MuoID<<"            -"<<endl;
  if(channel=="EleMuo" || channel=="MuoMuo" || channel=="MuoTau") myfile<<"MuoScale      lnN       "<<MuoScale<<"            -"<<endl;
  if(channel=="EleMuo" || channel=="MuoMuo" || channel=="MuoTau") myfile<<"MuoResol      lnN       "<<MuoResol<<"            -"<<endl;
  if(channel=="MuoTau" || channel=="EleTau") myfile<<"TauES         lnN       "<<TauScale<<"            -"<<endl;
}
