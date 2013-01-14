#include "OsiCpx.hpp"

/**************************************************************
 ********************     Solver        ***********************
 **************************************************************/
OsiCpxSolver::OsiCpxSolver() : OsiSolver() {
	clpSi = new OsiCpxSolverInterface;
	OsiSolver::setSolver(clpSi);
}

OsiCpxSolver::~OsiCpxSolver() {
}

