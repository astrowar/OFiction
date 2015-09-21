from rtools import rsplit as rp

__author__ = 'astrowar'
from shlex import split as sp
import re
from  Scene import *

s = Scene()



#macro comandos
s << rp("Kind book Thing")
s << rp("Instance diary  book")

s << rp("Kind Animal Thing" )
s << rp("Kind Ox Animal" )
s << rp("Instance jairo Ox" )

s << rp("Set diary rare" )
s << rp("Set diary hidden" )
s << rp("Set [location book] library" )
s << rp("Set [title diary] untitled" )
s << rp("Set book portable" )

s << rp("Kind Color KindValue ")

s << rp("Instance red Color")
s << rp("Instance blue Color")
s << rp("Instance green Color")

s << rp("Property [color book] Color")


print(s.data)
print(s.kinds)



s<< rp("Kind? diary") # return "book"
s << rp("Is? diary book ") # diary is an book ?
s << rp("Is? diary Thing ")  #true
s << rp("Is? diary Place ")  #false

rpp = lambda x:print(rp(x))

rpp("Kind? [noum]  [is kind of [some]] ")
rpp("Is? diary Place ")
xx = s.match(rp("Instance :Noum :kind"), rp("Instance book thing ") )
print(xx)
print("------------")
for x in s.matchs(rp("Instance $Noum $Kind") ):
    print( x)
print("------------")



def func_eval_if( ex ):
    # (If X THEN_ELEM ELSE_ELEM )
    return  True






print("F: ", s.func_is_kind("diary", "Animal"))
print("------------")
print("T: ", s.func_is_kind("jairo", "Animal"))




print("IS------------")
print("T: ", s.func_obj_is("diary", "rare"))


print("IS Portable----------")
print("T: ", s.func_obj_is("diary", "portable"))
print("F: ", s.func_obj_is("jairo", "portable"))
print("T: ", s.func_obj_is("diary", "book"))

print("Property----------")
print("T: ", s.func_eval_named_prop("location","diary"))
print("N: ", s.func_eval_named_prop("color","jairo"))


print("Kind Values ----------")
print("T: ", s.func_is_kind("red", "KindValue"))
print("T: ", s.func_is_kind("green", "Color"))
print("F: ", s.func_is_kind("white", "Color"))

# Brightness is a kind of value. The brightnesses are guttering, weak, radiant and blazing.

s << rp("Kind Brightness KindValue")
s << rp("Instance guttering Brightness")
s << rp("Instance weak Brightness")
s << rp("Instance radiant Brightness")
s << rp("Instance blazing Brightness")

# The lantern has a brightness called the flame strength. The flame strength of the lantern is blazing.

s << rp("Property ['flame strength' lantern] Brightness")
s << rp("Set ['flame strength' lantern] blazing")
print("T: ", s.func_eval_named_prop('flame strength' ,"lantern"), "blazing")
print("F: ", s.func_eval_named_prop('flame strength' , "lantern"), "weak")
print("T: ", s.func_is_kind("blazing",  "Brightness" ))

# CanBe
# A fruit can be unripened, ripe, overripe, or mushy
s << rp("CanBe fruit  [unripened, ripe, overripe, mushy]")
s << rp("Set fruit ripe")
s << rp("Set [ color fruit ] red ")
s << rp("Set [ location fruit ] cozinha ")
s << rp("Set [food  player] fruit ")

s << rp("Set ['favorite food'  Animal] fruit ")

#print("T: ", s.func_eval(rp("[color [key  player]]")))
print("T: ", s.is_named_property("color"))
print("T: ", s.is_named_property("location"))
print("F: ", s.is_named_property("book"))

print("Eval Values ----------")
print("T: ", s.func_eval(rp("color [food  player]"))) #red
print("T: ", s.func_eval(rp("location ['favorite food' jairo]"))) #cozinha
print("T: ", s.func_eval(rp("color [location jairo]"))) #None