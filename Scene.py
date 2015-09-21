from SVar import Svar

__author__ = 'astrowar'

from unification import *

Thing = "Thing"
Kind = "Kind"
Instance = "Instance"
IProperty = "Property"
KindThing = "KindThing"

print(".....")
from rtools import rsplit as rp

def kadd(x, y):
    r = {}
    for k, v in x.items():
        r[k] = v
    for k, v in y.items():
        if k in r:
            if r[k] is not v:
                print("Conflict Var")
                return False
        r[k] = v
    return r


class Scene:
    def __init__(self):
        self.data = []
        self.kinds = ["Thing"]

        self.noum = {}  # lista de NOUMS e suas definicoes
        Svar.scene = self
        pass

    def __lshift__(self, other):
        print("<< ", other)
        self.data.append(other)
        if other[0] == "Kind":
            self.kinds.append(other[1])

        return other

    @staticmethod
    def query_is(op):
        # IS? what value
        return False

    def query_op(self, op):
        for q in self.data:
            if q[0] == op: yield q

    def query_instance(self, q):
        yield from self.matchs([Instance, q, var()])

        # yield from  filter(lambda x: x is not False, [unify([Meta.Instance, q, var()], acct) for acct in self.data])

    def matchs(self, template):
        #print("Tye: ", template)
        Lm = [self.match(template, acct) for acct in self.data]


        yield from  filter(lambda x: x is not False,  Lm)


    def match(self, template, d, evars=None):
        if not evars:
            evars = {}
        qvars = evars
        if isinstance(template, str):
            if template != d: return False
            return evars

        if isinstance(template, tuple):
            if isinstance(d, tuple) is False:
                return False

        if isinstance(template, list):
            if isinstance(d, list) is False:
                return False

        if isinstance(template, list) or isinstance(template, tuple):
            if len(template) != len(d):
                return False
            for i in range(len(template)):
                tv = template[i]
                dv = d[i]
                qvars = self.match(tv, dv, qvars)
                if qvars is False: return False

            return qvars

        if isinstance(template, Svar):
            r = template.match(d)
            if r is False: return False
            return kadd(qvars, r)

        return qvars




    def upper_kinds(s,obj):
        for x1 in s.matchs(["Instance"] + [obj] +[Svar("Kind")]  ):

          yield  x1["Kind"]
          yield from s.upper_kinds(x1["Kind"])
          return

        for x1 in s.matchs(["Kind"] + [obj] +[Svar("Kind")]  ):
          yield  x1["Kind"]
          yield from s.upper_kinds(x1["Kind"])


    def func_is_kind(s,obj, k ):

        if  obj == k: return True
        for x1 in s.matchs(rp("Instance "+ obj + " :Kind"   )):

          rupper =  s.func_is_kind(x1["Kind"] ,k )
          if rupper is True : return True
        for x1 in s.matchs(rp("Kind "+ obj +" :Kind"   )):

          rupper =  s.func_is_kind(x1["Kind"] ,k )
          if rupper is True : return True
        return False


    def func_is_instance_or_kind(s,what):
        for x1 in s.matchs(["Instance"] + [what] + [Svar()]  ):
            return True
        for x1 in s.matchs(["Kind"] + [what] + [Svar()]  ):
            return True
        return False

    def func_obj_is(s, obj ,value ):
        # [is? X Y ]
        #print("F>" , obj, value )
        if  obj == value: return True
        #print( ["Set"] + [obj] + [value])
        for x1 in s.matchs(["Set"] + [obj] + [value]  ):
          return True
        #for x1 in s.matchs(rp("Set "+ obj + "[ not " + value  +" ]"  )):
        for x1 in s.matchs(["Set"]+ [obj] + ["not" + value ]  ):
          return False
        if s.func_is_instance_or_kind(obj):
            for x2 in s.upper_kinds(obj ):
                rupper =  s.func_obj_is( x2 , value )
                if rupper is True : return True
        return False

    def func_eval_named_prop( s,propname , obj ):
        # [prop propname obj ]
        for x1 in s.matchs(["Set"] +[[propname  , obj ]] + [Svar("Value")]    ):
          #print( x1 )
          return x1["Value"]
        for k in  s.upper_kinds(obj):
            rr = s.func_eval_named_prop(propname, k)
            if rr is not None:
                return rr
        return  None

    def is_named_property( s, nn):
        for x1 in s.matchs(["Set"] +[[nn  , Svar() ]] + [Svar()]  ):
          return True
        for x2 in s.matchs(["Property"] +[[nn  , Svar() ]] + [Svar()]  ):
          return True
        return False

    def func_eval( s,expr ):
        # eval this expression
        cmd = expr[0]

        if cmd =="If" :
            pass
        if cmd =="Not" :
            pass
        if s.is_named_property( cmd ):
           remainder = expr[1:]
           if len(remainder) == 1 and  isinstance(remainder[0],str):
              return s.func_eval_named_prop(cmd,remainder[0])
           else:
              rt =  s.func_eval( remainder[0]  )
              if rt is None : return None
              return s.func_eval( [cmd, rt] )

        return None


# scn = Scene()
# Svar.scene = scn



unify(1, 1)
