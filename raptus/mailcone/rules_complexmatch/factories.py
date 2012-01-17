import json
import grok

from raptus.mailcone.core import utils

from raptus.mailcone.rules import interfaces
from raptus.mailcone.rules.factories import BaseFactory


from raptus.mailcone.rules_complexmatch import _



class ComplexMatchFactory(BaseFactory):
    grok.name('raptus.mailcone.rules.complexmatch')
    grok.implements(interfaces.IConditionItemFactory)
    
    
    title = _('Complex Match')
    description = _('no idee was this thing do ???')

    def box_input(self):
        li = list()
        li.append(dict(title=self._translate(_('input')) ))
        return li
    
    def box_output(self):
        li = list()
        li.append(dict(title=self._translate(_('match')) ))
        li.append(dict(title=self._translate(_('do not match')) ))
        return li