# Function constrained by user-defined function
# Derek Fujimoto
# August 2019

import numpy as np
from bfit.global_variables import KEYVARS

# =========================================================================== # 
class ConstrainedFunction(object):
    """
        p1
        p2
        constraints
        defined
        equation
    """
    
    # ======================================================================= # 
    def __init__(self, defined, equation, newpar, oldpar):
        """
            defined:        parameters which the equations define (equation LHS)
                            in old parameter order
            equation:       list of strings corresponding to equation RHS in old 
                            parameter order
            newpar:         list of strings corresponding to new function 
                            parameters in order
            oldpar:         list of strings corresponding to old function 
                            parameters in order
        """
        self.header = 'lambda %s : ' % (', '.join(newpar))
        self.oldpar = oldpar
        
        # sort equations and defined by old par
        self.equation = [equation[defined.index(p)] for p in oldpar]
        
    # ======================================================================= # 
    def __call__(self, data, fn):
        """ 
            Identify variable names, make constraining function
            
            data: bfitdata object to generate the constrained function 
            fn: function handle
        """
        
        # get variables in decreasing order of length (no mistakes in replace)
        varlist = np.array(list(KEYVARS.keys()))
        varlist = varlist[np.argsort(list(map(len, varlist))[::-1])]
    
        eqn = []
        for c in self.equation:
                
            # find constant names in the string, replace with constant
            for var in varlist:
                if var in c:
                    value = self._get_value(data, var)
                    c = c.replace(var, str(value))
            eqn.append(c)
        
        # get constraint functions, sorted 
        constr_fns = [eval(self.header+e) for e in eqn]
        
        # define the new fitting function
        def new_fn(x, *newparam):
            oldparam = [c(*newparam) for c in constr_fns]
            return fn(x, *oldparam)
            
        return (new_fn, constr_fns)
            
    # ======================================================================= # 
    def _get_value(self, data, name):
        """
            Tranlate typed constant to numerical value
        """
        new_name = KEYVARS[name]
        return data.get_values(new_name)[0]
