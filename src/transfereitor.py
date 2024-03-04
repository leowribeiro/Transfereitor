
'''
------------------------------------------------------------

Transfereitor v0.16b
Ferramenta para automação da criação do processo de transferencia de carga patrimonial no SEI.
03/01/2024
Leonardo W. Ribeiro

------------------------------------------------------------
'''


import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmb
from cryptography.fernet import Fernet
import configparser as cp


from Bem import *
from FileBuilder import *
from Robot import *

logoInt = [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 32, 0, 156, 7, 0, 0, 22, 0, 0, 0, 137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13, 73, 72, 68, 82, 0, 0, 1, 0, 0, 0, 1, 0, 8, 6, 0, 0, 0, 92, 114, 168, 102, 0, 0, 0, 1, 111, 114, 78, 84, 1, 207, 162, 119, 154, 0, 0, 7, 86, 73, 68, 65, 84, 120, 218, 237, 221, 191, 106, 84, 121, 28, 198, 225, 95, 118, 97, 179, 142, 32, 90, 166, 81, 241, 79, 68, 45, 188, 12, 81, 176, 243, 46, 188, 1, 27, 139, 93, 16, 11, 107, 43, 235, 101, 107, 11, 193, 77, 12, 137, 186, 91, 228, 18, 180, 83, 130, 193, 198, 202, 38, 24, 51, 251, 27, 119, 2, 22, 154, 77, 50, 103, 38, 231, 156, 247, 121, 225, 67, 234, 156, 156, 239, 227, 4, 139, 148, 98, 102, 102, 102, 102, 205, 236, 120, 237, 39, 143, 193, 44, 111, 151, 107, 191, 141, 17, 48, 179, 160, 93, 172, 253, 93, 123, 85, 27, 120, 28, 102, 89, 199, 255, 162, 54, 172, 173, 1, 192, 44, 243, 248, 1, 96, 22, 124, 252, 0, 48, 11, 62, 126, 0, 152, 133, 28, 255, 218, 119, 142, 31, 0, 102, 193, 199, 15, 0, 179, 224, 227, 7, 128, 89, 240, 241, 3, 192, 44, 248, 248, 1, 96, 22, 124, 252, 0, 48, 11, 62, 126, 0, 152, 5, 31, 63, 0, 204, 130, 143, 31, 0, 102, 29, 223, 133, 9, 142, 31, 0, 102, 193, 199, 15, 0, 179, 224, 227, 7, 128, 89, 240, 241, 3, 192, 44, 248, 248, 1, 96, 22, 124, 252, 0, 48, 11, 62, 126, 0, 152, 5, 31, 63, 0, 204, 130, 143, 31, 0, 102, 193, 199, 15, 0, 179, 224, 227, 223, 5, 224, 152, 199, 109, 150, 119, 252, 163, 94, 214, 78, 213, 126, 169, 205, 75, 123, 52, 122, 71, 230, 156, 103, 127, 142, 127, 212, 199, 218, 243, 218, 95, 210, 30, 45, 213, 254, 168, 45, 56, 209, 254, 28, 191, 116, 144, 54, 107, 231, 157, 169, 227, 87, 102, 27, 181, 115, 78, 213, 241, 11, 0, 214, 224, 241, 175, 122, 185, 4, 0, 199, 47, 1, 192, 241, 75, 0, 112, 252, 18, 0, 28, 191, 4, 0, 199, 47, 1, 192, 241, 75, 0, 112, 252, 18, 0, 28, 191, 4, 0, 199, 47, 1, 192, 241, 75, 0, 112, 252, 18, 0, 28, 191, 4, 0, 199, 47, 1, 192, 241, 75, 0, 112, 252, 18, 0, 28, 191, 4, 0, 199, 47, 1, 192, 241, 75, 0, 112, 252, 18, 0, 28, 191, 4, 0, 199, 47, 1, 96, 88, 191, 237, 235, 215, 29, 191, 20, 9, 192, 131, 7, 165, 60, 122, 84, 78, 46, 44, 148, 167, 94, 0, 1, 32, 12, 128, 79, 159, 190, 126, 10, 56, 247, 228, 73, 121, 123, 246, 108, 217, 241, 18, 8, 0, 97, 191, 2, 140, 0, 168, 109, 44, 47, 151, 237, 51, 103, 202, 182, 23, 65, 0, 8, 4, 160, 54, 172, 8, 124, 134, 128, 0, 16, 10, 0, 4, 4, 128, 112, 0, 32, 32, 0, 132, 3, 0, 1, 1, 32, 28, 0, 8, 8, 0, 225, 0, 64, 64, 0, 8, 7, 0, 2, 2, 64, 56, 0, 16, 16, 0, 194, 1, 128, 128, 0, 16, 14, 0, 4, 4, 128, 112, 0, 32, 32, 0, 132, 3, 0, 1, 1, 32, 28, 0, 8, 8, 0, 225, 0, 64, 64, 0, 8, 7, 0, 2, 2, 64, 56, 0, 16, 16, 0, 194, 1, 128, 128, 0, 16, 14, 0, 4, 4, 128, 112, 0, 32, 32, 0, 132, 3, 0, 1, 1, 32, 28, 0, 8, 8, 0, 225, 0, 64, 64, 0, 8, 7, 0, 2, 2, 64, 56, 0, 16, 16, 0, 194, 1, 24, 181, 180, 52, 115, 4, 182, 106, 155, 181, 247, 227, 175, 58, 124, 187, 207, 112, 11, 0, 0, 232, 202, 39, 129, 245, 218, 181, 218, 98, 237, 146, 38, 106, 113, 252, 44, 215, 1, 0, 128, 174, 32, 176, 90, 155, 47, 214, 212, 230, 75, 127, 255, 138, 52, 0, 122, 136, 192, 90, 109, 224, 110, 27, 219, 0, 0, 0, 232, 18, 2, 0, 0, 0, 0, 218, 10, 192, 12, 16, 0, 0, 0, 0, 208, 102, 0, 166, 140, 0, 0, 0, 0, 128, 182, 3, 48, 197, 255, 34, 4, 0, 0, 0, 208, 5, 0, 166, 132, 0, 0, 0, 0, 128, 174, 0, 48, 5, 4, 0, 0, 0, 0, 116, 9, 128, 134, 17, 0, 0, 0, 0, 208, 53, 0, 26, 68, 0, 0, 0, 0, 64, 23, 1, 104, 8, 1, 0, 0, 0, 0, 93, 5, 224, 27, 4, 190, 0, 0, 0, 0, 8, 4, 96, 66, 4, 0, 0, 0, 0, 116, 29, 128, 9, 16, 0, 0, 0, 0, 208, 7, 0, 14, 137, 0, 0, 0, 0, 128, 190, 0, 112, 8, 4, 0, 0, 0, 0, 244, 9, 128, 3, 34, 0, 0, 0, 0, 160, 111, 0, 28, 0, 1, 0, 0, 0, 0, 125, 4, 96, 159, 8, 0, 0, 0, 0, 232, 43, 0, 251, 64, 0, 0, 0, 0, 64, 159, 1, 248, 31, 4, 0, 0, 0, 0, 244, 29, 128, 61, 16, 0, 0, 0, 0, 144, 0, 192, 15, 16, 0, 0, 0, 0, 144, 2, 192, 119, 16, 0, 0, 0, 0, 144, 4, 192, 46, 2, 167, 79, 255, 7, 192, 220, 28, 0, 0, 0, 128, 40, 0, 70, 61, 123, 86, 134, 87, 174, 148, 21, 159, 0, 0, 0, 128, 64, 0, 70, 189, 126, 93, 86, 238, 221, 43, 131, 199, 143, 93, 46, 0, 0, 16, 7, 64, 109, 181, 54, 24, 125, 159, 6, 0, 0, 0, 192, 0, 0, 0, 0, 24, 0, 0, 0, 0, 3, 0, 0, 0, 96, 0, 0, 0, 0, 12, 0, 0, 0, 128, 1, 0, 0, 0, 48, 0, 0, 0, 0, 6, 0, 0, 0, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 204, 118, 119, 238, 148, 242, 240, 97, 25, 92, 189, 90, 86, 0, 0, 0, 0, 132, 109, 252, 174, 12, 222, 188, 41, 43, 183, 110, 1, 0, 0, 0, 136, 123, 87, 118, 118, 190, 62, 203, 181, 141, 141, 50, 188, 121, 179, 124, 6, 0, 0, 0, 16, 246, 9, 96, 4, 192, 232, 217, 86, 4, 190, 244, 12, 1, 0, 0, 192, 246, 11, 64, 15, 17, 0, 0, 0, 236, 32, 0, 244, 12, 1, 0, 0, 192, 14, 10, 64, 143, 16, 0, 0, 0, 236, 48, 0, 244, 4, 1, 0, 0, 192, 14, 11, 64, 15, 16, 0, 0, 0, 108, 18, 0, 58, 142, 0, 0, 0, 96, 147, 2, 208, 97, 4, 0, 0, 0, 107, 2, 128, 142, 34, 0, 0, 0, 88, 83, 0, 116, 16, 1, 0, 0, 192, 154, 4, 160, 99, 8, 0, 0, 0, 214, 52, 0, 29, 66, 0, 0, 0, 176, 105, 0, 208, 17, 4, 0, 0, 0, 155, 22, 0, 29, 64, 0, 0, 0, 176, 105, 2, 208, 114, 4, 0, 0, 0, 155, 54, 0, 45, 70, 0, 0, 0, 176, 89, 0, 208, 82, 4, 0, 0, 0, 155, 21, 0, 45, 68, 0, 0, 0, 176, 89, 2, 48, 70, 96, 187, 37, 8, 0, 0, 0, 54, 107, 0, 90, 132, 0, 0, 0, 96, 71, 1, 64, 75, 16, 0, 0, 0, 236, 168, 0, 104, 1, 2, 0, 0, 128, 29, 37, 0, 71, 140, 0, 0, 122, 10, 192, 252, 248, 251, 212, 228, 205, 143, 159, 233, 176, 135, 8, 0, 160, 135, 173, 215, 174, 213, 22, 107, 151, 52, 81, 139, 227, 103, 185, 62, 139, 159, 221, 17, 32, 0, 128, 30, 182, 85, 219, 172, 189, 31, 127, 213, 225, 219, 125, 134, 91, 179, 250, 249, 205, 24, 1, 0, 72, 109, 107, 134, 8, 0, 64, 10, 70, 0, 0, 82, 48, 2, 0, 144, 130, 17, 0, 128, 20, 140, 0, 0, 164, 174, 32, 112, 227, 70, 227, 8, 0, 64, 10, 70, 0, 0, 82, 48, 2, 0, 144, 130, 17, 0, 128, 20, 140, 0, 0, 164, 96, 4, 0, 32, 5, 35, 0, 0, 41, 24, 1, 0, 72, 193, 8, 0, 64, 10, 70, 0, 0, 82, 48, 2, 0, 144, 130, 17, 0, 128, 20, 140, 0, 0, 164, 96, 4, 0, 32, 5, 35, 0, 0, 41, 24, 1, 0, 72, 193, 8, 0, 64, 10, 70, 0, 0, 82, 48, 2, 0, 144, 66, 17, 216, 6, 128, 151, 65, 161, 189, 123, 87, 118, 110, 223, 46, 111, 71, 0, 156, 56, 1, 0, 41, 174, 15, 31, 202, 211, 187, 119, 203, 201, 251, 247, 1, 32, 165, 181, 90, 187, 176, 188, 92, 138, 95, 1, 164, 192, 227, 31, 126, 243, 103, 208, 1, 32, 101, 180, 22, 123, 252, 0, 144, 227, 15, 62, 126, 0, 200, 241, 7, 31, 63, 0, 228, 248, 131, 143, 31, 0, 114, 252, 37, 123, 0, 144, 227, 7, 0, 0, 228, 248, 1, 224, 69, 145, 227, 7, 128, 228, 248, 1, 32, 57, 126, 0, 72, 142, 31, 0, 146, 227, 7, 128, 228, 248, 1, 32, 57, 126, 0, 72, 142, 31, 0, 146, 227, 7, 128, 228, 248, 1, 32, 57, 126, 0, 72, 142, 31, 0, 146, 227, 7, 128, 228, 248, 1, 32, 57, 126, 0, 72, 142, 191, 69, 0, 156, 175, 109, 122, 201, 212, 226, 227, 191, 232, 248, 167, 7, 192, 66, 237, 207, 218, 243, 218, 178, 180, 71, 43, 181, 143, 142, 191, 95, 0, 204, 213, 230, 107, 191, 142, 191, 74, 63, 234, 84, 237, 165, 227, 239, 23, 0, 210, 126, 59, 54, 62, 76, 199, 111, 22, 248, 143, 197, 96, 6, 0, 56, 126, 179, 80, 0, 28, 191, 89, 40, 0, 142, 223, 44, 20, 0, 199, 111, 22, 10, 128, 227, 55, 11, 5, 192, 241, 155, 133, 2, 224, 248, 205, 66, 1, 112, 252, 102, 161, 0, 56, 126, 179, 80, 0, 28, 191, 89, 40, 0, 47, 28, 191, 89, 38, 0, 142, 223, 44, 20, 0, 199, 111, 22, 10, 128, 227, 55, 11, 5, 192, 241, 155, 133, 2, 224, 248, 205, 66, 1, 112, 252, 102, 161, 0, 56, 126, 179, 80, 0, 28, 191, 89, 40, 0, 142, 223, 44, 20, 0, 199, 111, 22, 10, 128, 227, 55, 11, 5, 192, 241, 155, 5, 2, 240, 170, 246, 143, 227, 55, 203, 3, 224, 120, 237, 247, 218, 101, 199, 111, 150, 7, 192, 207, 99, 4, 28, 191, 89, 32, 0, 197, 241, 155, 153, 53, 188, 127, 1, 56, 163, 226, 181, 211, 25, 77, 43, 0, 0, 0, 0, 73, 69, 78, 68, 174, 66, 96, 130]

progName = "Transfereitor"

# problemas
# testar múltiplas solicitações sem fechar o programa
# impedir de processar quando a treeview estiver vazia
# não usar os 25 primeiros caracteres, procurar pelo 3° espaço e para ali na descrição do bem

class App(tk.Tk):

	def loadData(self):
	
		global progName
	
		config = cp.ConfigParser()
		
		try:
			config.read("config.ini")
			user = config.get("data", "login")
			passwEncrypted = config.get("data", "passw")
			progName = config.get("program", "name")
			licenseMessage = config.get("data", "licenseMessage")
		except:
			tkmb.Message(self, message="Problema com o arquivo INI. Terminando execução.", type=tkmb.OK, icon=tkmb.ERROR, title="ERRO DE CONFIGURAÇÃO").show()		
			quit()
			return None
	
		self.user.set(user)
	
		key = b"70F3T4GCnMSIfkA3aSydw28BIzSDO9YUXs30Wc0-034="
		fernet = Fernet(key)
		passwDecrypted = fernet.decrypt(passwEncrypted).decode("utf-8")
		self.passw.set(passwDecrypted)
		
		if licenseMessage == "1":
			self.licenseMessage = True
		elif licenseMessage == "0":
			self.licenseMessage = False

	def saveData(self):
		
		key = b"70F3T4GCnMSIfkA3aSydw28BIzSDO9YUXs30Wc0-034="
		fernet = Fernet(key)
		passwEncrypted = fernet.encrypt(self.passw.get().encode("utf-8")).decode("utf-8")
		
		config = cp.ConfigParser()
		config.read("config.ini")
		config["program"] = { "name" : progName }
		config["data"] = { "login": self.user.get(), "passw": passwEncrypted, "licenseMessage" : config.get("data", "licenseMessage") }

		file = open("config.ini", "w")
		config.write(file)

	def addTombo(self, event=""):
	
		tombo = self.tomboSV.get()
	
		tomboSplit = tombo.split(" ")
	
		if tombo.isdigit() or (tomboSplit[0] == "CEFET" and tomboSplit[1].isdigit()) :	
			self.treeview.insert('', 'end', values=(tombo, "", "") )
			self.tomboEntry.delete(0, "end")
			self.tomboEntry.focus_set()
			self.treeview.see(self.treeview.get_children("")[-1])
		else:
			tkmb.Message(self, message="Tombo deve seguir uma das seguintes expressões regulares, \"[0-9]+\" ou \"CEFET [0-9]+\". Exemplos válidos: \"053123\" e \"CEFET 13455\".", type=tkmb.OK, icon=tkmb.ERROR, title = "Erro em \"" + tombo + "\"").show()		

	def removeTombo(self, event=""):
		for item in self.treeview.selection():
			self.treeview.delete(item)

	def getTomboFromClipboard(self):
		
		try:
			rawdata = self.clipboard_get()
			data = rawdata.split("\n")
	
			for tombo in data :
			
				tomboSplit = tombo.split(" ")
			
				if tombo.isdigit() or (tomboSplit[0] == "CEFET" and tomboSplit[1].isdigit()) :
					self.treeview.insert('', 'end', values=(tombo, "", "") )
					self.treeview.see(self.treeview.get_children("")[-1])
					
		except:
			print("clipboard failure")

	def updateTitle(self, event):
		title = f"Mouse @ ({event.x},{event.y})"
		self.title(title)

	def getAuth(self):
		
		class AuthData:
			def __init__(self):
				self.username = None
				self.password = None
		
		auth = AuthData()
		auth.username = self.user.get()
		auth.password = self.passw.get()
		return auth

	def process(self):
	
		answer = tkmb.Message(self, message="Tem certeza que deseja iniciar o processo?", type=tkmb.YESNO, icon=tkmb.QUESTION).show()		
		
		
		if answer == tkmb.YES:
			
			self.bot.start()
			self.bot.getAuth = self.getAuth
			
			# passar para o robot a lista de bens colocados no treeview
			self.listaBens.clear()
			
			for child in self.treeview.get_children():
				item = self.treeview.item(child)
			
				splitted = str(item["values"][0]).split(" ")
				bem = Bem()
				
				if len(splitted) > 1 :
					if splitted[0] == "CEFET" and splitted[1].isdigit() :
						bem.tombo = splitted[1]
						bem.tomboAntigo = True
				else:
					bem.tombo = item["values"][0]
				
				bem.novoSetor = item["values"][1]
				bem.novoResp = item["values"][2]
				
				self.listaBens.append(bem)
				
			self.bot.criaProcessoTransf(self.listaBens)
			
			
	def novoSetorChanged(self, thing1, thing2, thing3):
		
		for item in self.treeview.selection():
			self.treeview.set(item, "#2", self.novoSetorSV.get())

	def novoRespChanged(self, thing1, thing2, thing3):
		
		for item in self.treeview.selection():
			self.treeview.set(item, "#3", self.novoRespSV.get())

	def getTomboKeyAlpha(self, item):
		splitted = item[0].split(" ")
		return int(splitted[1])
	
	def getTomboKeyNumeric(self, item):
		return int(item[0])
	
	def getSetorKey(self, item):
		return str(item[1])

	def getRespKey(self,item):
		return str(item[2])

	def orderByTombo(self):
	
		numericList = []
		alphaList = []
	
		for child in self.treeview.get_children("") :
			item = self.treeview.item(child)["values"]
			if str(item[0]).isdigit() :
				numericList.append(item)
			else:
				alphaList.append(item)
	
		alphaList.sort(key=self.getTomboKeyAlpha)
		numericList.sort(key=self.getTomboKeyNumeric)
	
		# delete every line of treeview
		for child in self.treeview.get_children(""):
			self.treeview.delete(child)
	
		# numeric first
		for item in numericList:
			#item[0] = str(item[0]).zfill(6)
			self.treeview.insert('', 'end', values=item )
			
		# alpha last
		for item in alphaList:
			self.treeview.insert('', 'end', values=item )
			
	def orderBySetor(self):
		
		list = []
	
		for child in self.treeview.get_children("") :
			list.append(self.treeview.item(child)["values"])
	
		list.sort(key=self.getSetorKey)
	
		for child in self.treeview.get_children(""):
			self.treeview.delete(child)
	
		for item in list:
			self.treeview.insert('', 'end', values=item )
		
	def orderByResp(self):
		
		list = []
	
		for child in self.treeview.get_children("") :
			list.append(self.treeview.item(child)["values"])
	
		list.sort(key=self.getRespKey)
	
		for child in self.treeview.get_children(""):
			self.treeview.delete(child)
	
		for item in list:
			self.treeview.insert('', 'end', values=item )

	def loadNotes(self):
		
		try:
			file = open("notas.txt", "r")
			notes = file.read()
			file.close()
			
			notes = notes[:-1]
			self.notasText.insert("1.0", notes)
		except:
			pass
		
	def saveNotes(self):
	
		try:
			file = open("notas.txt", "w")
			file.write( self.notasText.get("1.0", "end") )
			file.close()
		except:
			print("falha em salvar notas")

	def search(self, string=""):
		
		if self.stringBusca.get() == "":
			self.buscaIndex = "0.1"
			self.notasText.tag_delete("selecao")
		else:
			count = tk.IntVar()
			noCase = not self.caseSensitiveBV.get()
			busca = self.notasText.search(pattern=self.stringBusca.get(), index=self.buscaIndex, count=count, nocase=noCase)
			self.notasText.tag_delete("selecao")
			
			if busca != "" :
				self.buscaIndex = busca + " + 1 chars"
				self.notasText.tag_add("selecao", busca, busca + " + " + str(count.get()) + " chars")
				self.notasText.tag_config("selecao", background="blue", foreground="white")
				self.notasText.see(busca)
			else:
				tkmb.Message(self, message="Nada foi encontrado.", type=tkmb.OK, icon=tkmb.WARNING).show()		

	def deleteSelecaoTag(self, event=""):
		try:
			self.notasText.tag_delete("selecao")
		except:
			pass

	def addWidgets(self):
		
		notebook = ttk.Notebook(self)
		
		usuarioTab = ttk.Frame(notebook)
		notebook.add(usuarioTab, text="USUÁRIO")
		
		transfTab = ttk.Frame(notebook)
		notebook.add(transfTab, text="TRANSFERÊNCIA")
		
		notasTab = ttk.Frame(notebook)
		notebook.add(notasTab, text="NOTAS")
		
		notebook.place(x=0, y=0, width=600, height=400)
	
		# ORELHA USUÁRIO

		self.user = tk.StringVar()
		self.passw = tk.StringVar()
		
		userEntry = ttk.Entry(usuarioTab, textvariable=self.user)
		userEntry.place(x = 70, y = 20)
		passwEntry = ttk.Entry(usuarioTab, textvariable=self.passw, show="*")
		passwEntry.place(x = 70, y = 45)
		
		ttk.Label(usuarioTab, text="USUÁRIO").place(x=10, y=20)
		ttk.Label(usuarioTab, text="SENHA").place(x=20, y=45)

		# ORELHA TRANSFERENCIA
		
		ttk.Label(transfTab, text="Tombo").place(x=10, y=20)
		
		self.tomboSV = tk.StringVar()
		self.tomboEntry = ttk.Entry(transfTab, textvariable=self.tomboSV)
		self.tomboEntry.place(x=60, y=20, width=100)
		self.tomboEntry.bind("<Return>", self.addTombo)
		
		ttk.Button(transfTab, text="+", command=self.addTombo).place(x=162, y=18, width=25)
		ttk.Button(transfTab, text="-", command=self.removeTombo).place(x=187, y=18, width=25)
		cButton = ttk.Button(transfTab, text="C", command=self.getTomboFromClipboard).place(x=212, y=18, width=25)
		
		
		
		ttk.Label(transfTab, text="Novo Setor").place(x=250, y=20)
		self.novoSetorSV = tk.StringVar()
		setorEntry = ttk.Entry(transfTab, textvariable=self.novoSetorSV)
		setorEntry.place(x=320, y=20, width=100)
		#setorEntry.bind("<Return>", self.addTombo)
		
		ttk.Label(transfTab, text="Novo Responsável").place(x=212, y=50)
		self.novoRespSV = tk.StringVar()
		respEntry = ttk.Entry(transfTab, textvariable=self.novoRespSV)
		respEntry.place(x=320, y=50, width=180)
		#respEntry.bind("<Return>", self.addTombo)
		
		ttk.Button(transfTab, text="PROCESSAR", command=self.process).place(x=507, y=18, height=54, width=82)
		
		self.treeview = ttk.Treeview(transfTab)
		self.treeview.place(x=10, y=80, width=578, height=287)
		
		self.treeview["columns"] = ("", "", "")
		
		self.treeview.heading("#1", text="Tombo", command=self.orderByTombo)
		self.treeview.heading("#2", text="Novo Setor", command=self.orderBySetor)
		self.treeview.heading("#3", text="Novo Responsável", command=self.orderByResp)
		
		self.treeview.column("#0", minwidth=0, width=0, anchor="center")
		self.treeview.column("#1", width=130, anchor="center")
		self.treeview.column("#2", width=130, anchor="center")
		self.treeview.column("#3", width=316, anchor="center")
		self.treeview.bind("<Motion>", "break")
		self.treeview.bind("<Delete>", self.removeTombo)
		
		self.scroll = ttk.Scrollbar(transfTab, orient=tk.VERTICAL, command=self.treeview.yview)
		self.treeview["yscrollcommand"] = self.scroll.set
		self.scroll.place(x=570, y=81, height=285)

		self.novoSetorSV.trace_add("write", self.novoSetorChanged)
		self.novoRespSV.trace_add("write", self.novoRespChanged)
		
		# ORELHA NOTAS
		
		scrollbar = ttk.Scrollbar(notasTab, orient="vertical")
		scrollbar.place(x=580, y=0, height=340)
		self.notasText = tk.Text(notasTab, yscrollcommand=scrollbar.set)
		self.notasText.place(x=0, y=0, width=580, height=340)
		scrollbar.config(command=self.notasText.yview)
		ttk.Button(notasTab, text="SALVAR", command=self.saveNotes).place(x = 520, y = 345)
		
		self.buscaIndex = "1.0"
		self.stringBusca = tk.StringVar()
		pesquisaEntry = ttk.Entry(notasTab, textvariable=self.stringBusca)
		pesquisaEntry.place(x=10, y=347, width = 130)

		ttk.Button(notasTab, text=">", command=self.search).place(x = 140, y = 345, width = 40)
		pesquisaEntry.bind("<Return>", self.search)
		
		self.notasText.bind("<Button-1>", self.deleteSelecaoTag)
		
		self.caseSensitiveBV = tk.BooleanVar()
		self.caseCheck = ttk.Checkbutton(notasTab, text="Diferenciar maiúsc. e minúsc.", variable=self.caseSensitiveBV)
		self.caseCheck.place(x=190, y=347)
		
	def avisoLicenca(self):
		s = progName
		s = s + " -- Criador de Processos de Transferência de Carga Patrimonial no SEI.\n\n"
		s = s + "Este programa é software livre; você pode redistribuí-lo e/ou modificá-lo sob "
		s = s + "os termos da Licença Pública Geral GNU, conforme publicada pela Free Software "
		s = s + "Foundation.\n\n"
		s = s + "Este programa é distribuído na expectativa de ser útil, mas SEM QUALQUER "
		s = s + "GARANTIA; incluindo as garantias implícitas de COMERCIALIZAÇÃO ou de ADEQUAÇÃO "
		s = s + "A QUALQUER PROPÓSITO EM PARTICULAR. Consulte a Licença Pública Geral GNU para "
		s = s + "obter mais detalhes.\n\n"
		s = s + "Você deve ter recebido uma cópia da Licença Pública Geral GNU (\""
		s = s + "Licenca Publica Geral GNU.txt\") em conjunto com este programa; "
		s = s + "caso contrário, entre no site:\n https://www.gnu.org/licenses/gpl-2.0.en.html.\n\n"
		s = s + "Leonardo Weiss Ribeiro,\n"
		s = s + "Autor do "
		s = s + progName.split(" ")[0] + "."
		return s

	def run(self):
		if self.licenseMessage :
			tkmb.Message(self, message=self.avisoLicenca(), type=tkmb.OK, icon=tkmb.WARNING, title="AVISO IMPORTANTE").show()		
		self.mainloop()
	
	def onExit(self):
		self.saveNotes()
		self.saveData()
		self.destroy()
	
	def onStartUp(self):
		self.loadData()
		self.loadNotes()
		self.title(progName)
	
	def __init__(self):
		super().__init__()
		width = 600
		height = 400
		centerX = round( (self.winfo_screenwidth() - width) /2.0 )
		centerY = round( (self.winfo_screenheight() - height) /2.0 )
		self.geometry(f"{width}x{height}+{centerX}+{centerY}")
		self.resizable(False, False)
		
		self.bot = Robot()
		self.licenseMessage = True
		self.listaBens = []
		
		try:
			self.iconbitmap("logo.ico")
		except:
			FileBuilder("logo.ico").build(logoInt)
			self.iconbitmap("logo.ico")
	
		self.protocol("WM_DELETE_WINDOW", self.onExit)
		
		self.addWidgets()
		self.onStartUp()
		
app = App()
app.run()





