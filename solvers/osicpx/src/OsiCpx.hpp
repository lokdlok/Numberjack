#include "Osi.hpp"
#include <OsiCpxSolverInterface.hpp>

class OsiCpxSolver: public OsiSolver {
private:
	OsiCpxSolverInterface* clpSi;
public:
	OsiCpxSolver();
	virtual ~OsiCpxSolver();
};
