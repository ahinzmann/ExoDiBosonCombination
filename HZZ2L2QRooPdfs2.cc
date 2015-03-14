#include <iostream>
#include <math.h>
#include "TMath.h"

//#include "../interface/RooDoubleCB.h"
//#include "../interface/RooFermi.h"
//#include "../interface/RooRelBW.h"
#include "../interface/HZZ2L2QRooPdfs2.h"
#include "RooRealVar.h"
#include "RooRealConstant.h"

using namespace RooFit;
using namespace std; 


ClassImp(RooLevelledExp2)

  RooLevelledExp2::RooLevelledExp2(){}

RooLevelledExp2::RooLevelledExp2(const char *name, const char *title,
			       RooAbsReal& _x,
			       RooAbsReal& _sigma, 
			       RooAbsReal& _alpha,
			       RooAbsReal& _beta,
			       RooAbsReal& _m,
			       RooAbsReal& _theta):
  RooAbsPdf(name,title),
  x("x","x",this,_x),
  sigma("sigma","sigma",this,_sigma),
  alpha("alpha","alpha",this,_alpha),
  beta("beta","beta",this,_beta),
  m("m","m",this,_m),
  //  k("k","k",this,_k),
  theta("theta","theta",this,_theta)
{
}

RooLevelledExp2::RooLevelledExp2(const RooLevelledExp2& other, const char* name) :
  RooAbsPdf(other,name),
  x("x",this,other.x),
  sigma("sigma",this,other.sigma),
  alpha("alpha",this,other.alpha),
  beta("beta",this,other.beta),
  m("m",this,other.m),
  theta("theta",this,other.theta)
{
}

double RooLevelledExp2::evaluate() const
{
  double res=0.0;
  double s = cos(theta)*sigma - sin(theta)*alpha;
  double a = sin(theta)*sigma + cos(theta)*alpha;
    
  //original
  double t = fabs(x-m);
  double den = (s + a*t + beta*t*t);
  res=exp(-1.0*t/den);
  

  return res;
}


///////////////////

