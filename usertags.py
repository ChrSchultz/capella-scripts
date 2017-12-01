"""
Capella Script das in Grafik-Objekte Benutzer(Herausgeber-)Tags einfügt, um diese evtl. ausblenden zu können.

>>> (c) by Christoph Schultz <ic-schultz@gmx.de>

Die Idee ist entstanden, da ich selber Cello spiele, und viele Noten habe, bei denen ich erstmal
sämtliche  nicht originale Bindungen und Dynamiken mit TippEx o.ä. entfernen muss um einigermaßen übersichtliche
Noten zu erhalten, und sie mir auf meine Bedürfnisse einzurichten.

Man kann im erscheinenden Dialog dann einen Tag, bestehend aus seiner 5-Stelligen KundenNr: 12345 einem Minuszeichen und einer 
Zahl zwichen 1 und 4096 als Kennung für verschiedene Objekte z.B 12345-10 für f(orte) 12345-20 für piano etc.
Mit dem Suchen Knopf, wird das nächste GrafikObjekt gesucht und man kann entscheiden ob man weiter Sucht oder einen Tag 
einfügen möchte.
<<<
""""







from xml.dom.minidom import parseString, NodeList, Node, Element
from caplib.rational import Rational
from caplib.capDOM import ScoreChange
import tempfile, string, new

def
