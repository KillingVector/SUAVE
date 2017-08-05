## @ingroup Attributes-Constants
# Constant.py

# Created:  Mar, 2014, SUAVE Team
# Modified: Jan, 2016, M. Vegh

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data
from SUAVE.Core import Container as ContainerBase

# ----------------------------------------------------------------------
#  Constant Data Class
# ----------------------------------------------------------------------
## @ingroup Attributes-Constants
class Constant(Data):
    """A container for constant values.
    
    Assumptions:
    None
    
    Source:
    None
    """
    def __defaults__(self):
        """This sets the default values (just a pass here).

        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        None
        """          
        pass

class Container(ContainerBase):
    """A subcontainer for constant values.
    
    Assumptions:
    None
    
    Source:
    None
    """    
    pass

# ----------------------------------------------------------------------
#  Handle Linking
# ----------------------------------------------------------------------

Constant.Container = Container    
    
    