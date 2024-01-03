

class Bem:
	
	def __init__(self):
		self.tombo 				= ""
		self.tomboAntigo		= False
		self.respAtual		 	= ""
		self.descricao			= ""
		self.novoSetor			= ""
		self.novoResp		 	= ""
		
	def __str__(self):
		
		string = ""
		string = string + "tombo: ".ljust(18) + str(self.tombo) + "\n"
		string = string + "tombo antigo: ".ljust(18) + str(self.tomboAntigo) + "\n"
		string = string + "responsável atual: ".ljust(18) + str(self.respAtual) + "\n"
		string = string + "descrição: ".ljust(18) + str(self.descricao) + "\n"
		string = string + "novo setor: ".ljust(18) + str(self.novoSetor) + "\n"
		string = string + "novo responsável: ".ljust(18) + str(self.novoResp) + "\n"
		
		return string
	