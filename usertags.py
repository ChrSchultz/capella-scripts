
# -*- coding: utf-8 -*-
"""
Capella Script das in Grfik-Objekte Benutzer(Herausgeber-)Tags einfügt, um diese evtl. ausblenden zu können.

>>> User Tags lesen

(c) by Christoph Schultz <ic-schultz@gmx.de>

Die Idee ist entstanden, da ich selber Cello spiele, und viele Noten habe, bei denen ich erstmal
sämtliche  nicht originale Bindungen und Dynamiken mit TippEx o.ä. entfernen muss um einigermaßen übersichtliche
Noten zu erhalten, und sie mir auf meine Bedürfnisse einzurichten.

Man kann im erscheinenden Dialog dann einen Tag, bestehend aus seiner 5-Stelligen KundenNr: 12345 einem Minuszeichen und einer 
Zahl zwichen 1 und 4096 als Kennung für verschiedene Objekte z.B 12345-10 für f(orte) 12345-20 für piano etc.
Mit dem Suchen Knopf, wird das nächste GrafikObjekt gesucht und man kann entscheiden ob man weiter Sucht oder einen Tag 
einfügen möchte.
<<<
"""






import tempfile, string, new, sys, zipfile
sys.path.append(r'C:\Program Files\capella-software\capella 7\py-ext')
from xml.dom.minidom import parseString, NodeList, Node, Element
from caplib.rational import Rational
from caplib.capDOM import ScoreChange


class ScoreReadTag:
    
    def __init__(self, infile, debug = False):
       zr = zipfile.ZipFile(infile, 'r')
       for name in zr.namelist():
         n =  z.read(name)
         print(name)
         if name == 'score.xml':
           self.score = parseString(n)
           score = self.score
           #print(score)
          
    def getElObjs(objList):
        List = NodeList()
        for n in Range(objList.length()):
           if objList[n].nodeType == objList[n].ELEMENT_NODE:
              List.append(objList[n])
        return List
         
        
    def getTag(self, score):
        
       for drawObjs in score.getElementsByTagName('drawObjects'):
        for drawObj in drawObjs.getElementsByTagName('drawObj'):
           for basic in drawObj.getElementsByTagName('basic'):
             if basic.hasAttributes():
                if basic.hasAttribute('tag'):
                  tag = basic.getAttribute('tag')
                else:
                  tag = "leer"
                if debug:
                print(tag)
               
                
                    
                          
              
               
                  

                
                
            
          
            
            
            
    
    
   
   
   
