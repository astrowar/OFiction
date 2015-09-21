__author__ = 'astrowar'
from shlex import split as sp

from  Scene import *

s = Scene()

#macro comandos
s << sp("Kind book Thing")
s << sp("Instance diary  book")
s << sp("Property color  diary red")

print(s.data)
print(s.kinds)
sq = (var("n") , "is an" , var("value") )

for g in   s.matchs( sq  ):
  print(g)

print( s.match( "x" , "x" , {})  )
print( s.match( "x" , "y" , {})  )

print( s.match( ((Svar("Noum") , "is")   ,Svar("Z") ), (("this" , "is") ,"y") )  )
print( s.match( [Svar("Noum") , Svar("Noum2")]   ,["x","y"] , {})  ) # pass
print( s.match( (Svar("Noum") , Svar("Noum"))   ,("x","y") , {})  ) #cannot pass
print( s.match( (Svar("Noum") , Svar("Noum"))   ,("x","x") , {})  ) # pass
