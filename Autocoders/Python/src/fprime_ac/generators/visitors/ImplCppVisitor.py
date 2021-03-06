# ===============================================================================
# NAME: ImplCppVisitor.py
#
# DESCRIPTION: A visitor class for generating component implementation cpp files.
#
# AUTHOR: bocchino
# EMAIL:  bocchino@jpl.nasa.gov
# DATE CREATED: October 12, 2015
#
# Copyright 2015, California Institute of Technology.
# ALL RIGHTS RESERVED. U.S. Government Sponsorship acknowledged.
# ===============================================================================
import sys

from fprime_ac.generators.visitors import ImplVisitorBase
from fprime_ac.utils import ConfigManager

try:
    from fprime_ac.generators.templates.impl import cpp
except ImportError:
    print("ERROR: must generate python templates first.")
    sys.exit(-1)


class ImplCppVisitor(ImplVisitorBase.ImplVisitorBase):
    """
    A visitor class for generating component implementation cpp files.
    """

    __config = None

    def __init__(self):
        super().__init__()
        self.__config = ConfigManager.ConfigManager.getInstance()
        self.initBase("ImplCpp")

    def buildFileName(self, obj):
        return obj.get_name() + self.__config.get("component", "ImplCpp")

    def emitPortParams(self, params):
        return self.emitPortParamsCpp(8, params)

    def emitNonPortParams(self, params):
        return self.emitNonPortParamsCpp(8, params)

    def startSourceFilesVisit(self, obj):
        c = cpp.cpp()
        self.init(obj, c)
        self.initImpl(obj, c)
        c.emit_port_params = self.emitPortParams
        c.emit_non_port_params = self.emitNonPortParams
        self._writeTmpl(c, "startSourceFilesVisit")
