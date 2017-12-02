# -*- coding utf-8 -*-
"""
>>>  Tagging 

fügt User-Tags in Zeichenobjekte wie Bindebögen etc. ein

die Idee kam mir, da ich bei meinen Noten -ich spiele selber Cello - immer Tipp-Ex brauche, 
so kann man sehen, oder rausfinden, ob der Bindebogen orginal oder vom Herausgeber (Notensetzer) stammt.
und evtl löschen.

(c) Christoph Schultz <ic-schultz@gmx.de> (CC-BY-SA)
<<<

"""

import tempfile, string, new, os, zipfile
#sys.path.append(r'C:\Program Files\capella-software\capella 7\py-ext')
from xml.dom.minidom import parseString, NodeList, Node, Element
from caplib.rational import Rational
from caplib.capDOM import ScoreChange



def insTags(tag):
    if activeScore():
       note = activeScore().cursorObj()
       for drawObjs in note.getElementByTagName('drawObj'):
          for basic in drawObjs.getElementByTagName('basic'):
            if basic.hasAttributes() and basic.hasAttribute('tag') == None:
                basic.setAtrribute('tag', tag)

def UserInput():
    label1 = 'Einzufügenden Tag'
    edit1 = Edit('12345-4096', width=10)
    hbox = HBox(label1, edit1, width=40)
    vbox = VBox(hbox, padding = 1)
    dlg = Dialog('Tags einfügen',vbox)
   
    if dlg.run():
        tag = edit1.value()
        insTags(tag)

                   
    
class ScoreChange(ScoreChange):
    def changeScore(self, score):
        UserInput()
        
if activeScore():
    activeScore().registerUndo('Tagging')
    tempInput = tempfile.mktemp('.capx')
    tempOutput = tempfile.mktemp('.capx')
    activeScore().write(tempInput)
    ScoreChange(tempInput, tempOutput)
    activeScore().read(tempOutput)
    
    os.remove(tempInput)
    os.remove(tempOutput)