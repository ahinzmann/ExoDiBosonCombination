#ifndef HZZ2L2QROOPDFS2
#define HZZ2L2QROOPDFS2

#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooAbsReal.h"



class RooLevelledExp2 : public RooAbsPdf {
 public:
  RooLevelledExp2();
  RooLevelledExp2(const char *name, const char *title,
		 RooAbsReal& _x,
		 RooAbsReal& _sigma,
		 RooAbsReal& _alpha,
		 RooAbsReal& _beta,
		 RooAbsReal& _m,
		 //RooAbsReal& _k,
		 RooAbsReal& _theta
		);

  RooLevelledExp2(const RooLevelledExp2& other, const char* name=0) ;
  virtual TObject* clone(const char* newname) const { return new RooLevelledExp2(*this,newname); }
  inline virtual ~RooLevelledExp2() { }

 protected:

  RooRealProxy x ;
  RooRealProxy sigma;
  RooRealProxy alpha;
  RooRealProxy beta;
  RooRealProxy m;
  // RooRealProxy k;
  RooRealProxy theta;
  

  Double_t evaluate() const ;

 private:

  ClassDef(RooLevelledExp2,1)
    };




#endif
