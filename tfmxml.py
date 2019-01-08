import os
import re
import base64
import urllib2

# Caso for coloca-lo em alguma source deixe meus créditos.
# Créditos: Becker

class XML_Parser:
	def __init__(self, code):
		self.keys = "59A[XG^znsqsq8v{`Xhp3P9G"
		self.perms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 18, 19, 20, 21, 22, 24, 32, 41, 44]
		self.getmap(code)

	def get(self, url): # Becker
		req = urllib2.Request(url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'})
		doc = urllib2.urlopen(req).read()
		return doc

	def getmap(self, code):
		doc = self.get("http://api.micetigri.fr/maps/xmlnew/{0}".format(code))
		code = self.getinfo(doc, "CODE")
		perm = self.getinfo(doc, "PERM")
		print("Map perm: {0}".format(perm))
		creator = self.getinfo(doc, "CREATOR")
		print("Map name: {0}".format(creator))
		xml = self.getinfo(doc, "XML")
		xml = self.decrypt(xml, self.keys)
		print("Map Saved.")
		self.save(code, xml)

	def getinfo(self, doc, value):
		xml = doc.split(value + '="')[1]
		xml = xml.split('"')[0]
		return xml

	def save(self, code, xml):
		file = open("./maps/{0}.xml".format(code), "w")
		file.write(xml)
		file.close()

	def decrypt(self, xml, key):
		print("Decrypting XML...")
		c = int()
		xml = base64.b64decode(xml)
		end = ""
		i = 0
		while i < len(xml):
			c = int(ord(xml[i]))
			c = (c - int(ord(key[(i + 1) % len(key)])))
			end += chr(abs(c) & 0xFF)
			i += 1
		return end

if __name__ == "__main__":
	os.system("title Becker XML parser")
	print("Starting...")
	code = raw_input("Map code: ")
	if "@" in code:
		XML_Parser(code.replace("@", ""))
	else:
		print("Invalid map code. Example: @0231")
input("Finished.")