# -*- coding: utf-8 -*-
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

doc = parseString('<score/>')

def gotoChild(self, name, new=False):
    newEl = None
    if new:
        pass
    else:
        for child in self.childNodes:
            if child.nodeType == child.ELEMENT_NODE and child.tagName == name:
                newEl = child
                break
    if newEl == None:
        newEl = doc.createElement(name)
        self.appendChild(newEl)
    return newEl
Node.gotoChild = new.instancemethod(gotoChild,None,Node)

def gotoChildN( el, name, new=False):
    newEl = None
    if new:
        pass
    else:
        for child in el.childNodes:
            if child.NodeType == child.ELEMENT_NODE and child.tagName == name:
                newEl = child
                break
    if newEl == None:
        newEl = doc.createElement(name)
        el.appendChild(newEl)
    return newEl



def insTags(tag, score):
   
  note = cursorObj()
 
  #voice = activeScore().system(0).staff(0).voice(0)
  #chord = voice.noteObj(0)
  
  for ch in score.getElementsByTagName('chord'):
     for dObjs in ch.getElementsByTagName('drawObjects'):
        for dObj in dObjs.getElementsByTagName('drawObj'):
            #messageBox('','%s' % dObj)
            basic = dObj.gotoChild('basic')
           # messageBox('','%s' % basic)
            bl = basic.hasAttributes()
            if bl : b = 'True'
            else: b = 'False'
           # messageBox('', '%s' % b)
            if basic.hasAttributes():
                #messageBox('Eingabe:', 'tag: %s' % tag)
                basic.setAttribute('tag', tag)
    
        
            
     #if chrd == chord:
     #messageBox('', 'note: %s chord %s chrd: %s' % ( note, chord, chrd))
     #break
      
    
    
def UserInput():
    label1 = Label('Einzufügenden Tag')
    edit1 = Edit('12345-4096', width=9)
    vbox = VBox([label1, edit1], padding = 8)
    dlg = Dialog('Tags einfügen', vbox, help= 'fügt den User-Tag in Grafikobjekt ein')
   
    if dlg.run():
        tag = edit1.value()
    return tag

                   
  
class ScoreChange(ScoreChange):
    def changeScore(self, score):
        tag = UserInput()
        messageBox( 'Eingabe:', 'tag: %s' % tag)
        insTags(tag, score)
        
if activeScore():
    activeScore().registerUndo('Tagging')
    tempInput = tempfile.mktemp('.capx')
    tempOutput = tempfile.mktemp('.capx')
    activeScore().write(tempInput)
    ScoreChange(tempInput, tempOutput)
    activeScore().read(tempOutput)
    
    os.remove(tempInput)
    os.remove(tempOutput)

