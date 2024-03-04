
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service as ChromeService 
from subprocess import CREATE_NO_WINDOW

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmb

from PIL import Image 
import time
import winsound
import keyboard
import shutil
import os

from Bem import *


class Robot(webdriver.Chrome) :

	started = False

	def __init__(self):
		pass

	def start(self):
	
		if not Robot.started:
	
			chrome_service = ChromeService()
			#chrome_service.creation_flags = CREATE_NO_WINDOW

			super().__init__(service=chrome_service)
			self.getAuth = None
			self.maximize_window()
			self.implicitly_wait(0.3)
			
			self.windowHandle = self.current_window_handle
			
			Robot.started = True
			self.loggedInSEI = False
			self.loggedInSC = False
	
	def logInSistemasCorporativos(self) :

		self.unminimize()
		self.get("http://sistemas2.utfpr.edu.br")
		
		if not self.loggedInSC:
			userbox = self.find_element(By.XPATH, "//input[@placeholder='Login']")
			passbox = self.find_element(By.XPATH, "//input[@placeholder='Senha']")
			button = self.find_element(By.XPATH, "//p-button")

			auth = self.getAuth()
			userbox.send_keys(auth.username)
			passbox.send_keys(auth.password)
			button.click()
			
			loop = True
			while loop:
				try:
					self.find_element(By.XPATH, "//span[contains(.,'Curitiba')]").click()
					loop = False
				except:
					pass
			
			self.loggedInSC = True
		
	def logInSEI(self):

		self.unminimize()
		self.get("http://sei.utfpr.edu.br")
	
		if not self.loggedInSEI:
		
			userbox = self.find_element(By.XPATH, "//input[@id='txtUsuario']")
			passbox = self.find_element(By.XPATH, "//input[@id='pwdSenha']")
			button = self.find_element(By.XPATH, "//button[@id='sbmAcessar']")
			
			auth = self.getAuth()			
			userbox.send_keys(auth.username)
			passbox.send_keys(auth.password)
			button.click()	
			
			self.loggedInSEI = True

	def iniciarProcessoSEI(self, tipo):
	
		self.find_element(By.XPATH, "//span[contains(.,'Iniciar Processo')]").click()
		self.find_element(By.LINK_TEXT, tipo).click()
	
		if tipo == "Patrimônio: Solicitação de Transferência de Bens" :
			self.find_element(By.ID, "btnSalvar").click()
		
	def incluirDocumento(self, tipo, numero=""):
		
		butt = None
		
		loop = True
		while loop:
			try:
				butt = self.find_element(By.XPATH, "//img[@alt='Incluir Documento']")
				loop = False
			except:
				print("I'm stuck!")
				continue
		
		butt.click()
		self.find_element(By.LINK_TEXT, tipo).click()
		
		if tipo == "Patrimônio: Solicitação de Transferência de Bem":
			self.find_element(By.ID, "btnSalvar").click()
		elif tipo == "Cadastro Aluno UTFPR como usuário externo no SEI":
			self.find_element(By.ID, "txtNumero").send_keys(numero)
			self.find_element(By.ID, "btnSalvar").click()

	def liberarAssinaturaExterna(self, nome, senha):
	
		self.find_element(By.XPATH, "//img[@alt='Gerenciar Liberações para Assinatura Externa']").click()
		selectEmailElement = self.find_element(By.ID, "selEmailUnidade")
		selectEmail = Select(selectEmailElement)
		selectEmail.select_by_index(1)
		
		self.find_element(By.ID, "txtUsuario").send_keys(nome)
		time.sleep(2)
		
		AC = ActionChains(self)
		AC.send_keys(Keys.DOWN)
		AC.send_keys(Keys.ENTER)
		AC.perform()
		
		self.find_element(By.ID, "txtDias").send_keys("30")
		self.find_element(By.ID, "pwdSenha").send_keys(senha)
		self.find_element(By.ID, "btnLiberar").click()

	def beep(self, freq=500, duration=100):
		winsound.Beep(freq, duration)
		
	def waitKey(self, key="esc"):
		print("waiting for " + key + "...")
		keyboard.wait(key)

	def wait(self, totalTime):
		time.sleep(totalTime)

	def kill(self):
		self.quit()

	def changeUnidadeToF_DIRGRAD(self):
				
		unidades = self.find_elements(By.XPATH, "//a[@id='lnkInfraUnidade']")		
		
		if unidades[1].text != "F_DIRGRAD-CT":
			unidades[1].click()
		
			tds = self.find_elements(By.XPATH, "//td")
			for td in tds :
				if td.text == "F_DIRGRAD-CT":
					td.click()
					break

	def unminimize(self):
		self.switch_to.window(self.windowHandle)
		self.maximize_window()
		
	def minimize(self):
		self.minimize_window()

	def criaProcessoTransf(self, listaBens):
				
		self.logInSistemasCorporativos()
		
		for bem in listaBens:
		
			if bem.tomboAntigo :
				self.get("https://sistemas2.utfpr.edu.br/dpls/sistema/corp01/mpIncorporarBem.pcpesquisa?p_bempattombonr=" + str(bem.tombo) + "&p_tomboant=1&p_matdescrvc=&p_partestr=I&p_matcomplvc=&p_bempatmarcamodvc=&p_gestaocodnr=1&p_altdeprnr=0&p_incorpconsulta=1")
			else: 
				self.get("https://sistemas2.utfpr.edu.br/dpls/sistema/corp01/mpIncorporarBem.pcpesquisa?p_bempattombonr=" + str(bem.tombo) + "&p_tomboant=0&p_matdescrvc=&p_partestr=I&p_matcomplvc=&p_bempatmarcamodvc=&p_gestaocodnr=1&p_altdeprnr=0&p_incorpconsulta=1")
	
			tds = self.find_elements(By.XPATH, "//td")
				
			if len(tds) > 12 and tds[12].text == "Bens encontrados: 1" :
				bem.respAtual = tds[11].text.replace("\n", "").upper()
				bem.descricao = tds[7].text.replace("\n", "")
				
				if tds[9].text == "BAIXADO":
					bem.respAtual = "BAIXADO"
					bem.novoResp = "BAIXADO"
					bem.novoSetor = "BAIXADO"
			else:
				bem.respAtual = "NÃO ENCONTRADO"
				bem.novoResp = "NÃO ENCONTRADO"
				bem.novoSetor = "NÃO ENCONTRADO"
		
		self.logInSEI()
		self.iniciarProcessoSEI("Patrimônio: Solicitação de Transferência de Bens")
		self.switch_to.frame(1)
		self.incluirDocumento("Patrimônio: Solicitação de Transferência de Bem")
		
		#espera janela abrir
		timer = 0
		while (len(self.window_handles) < 2) and (timer < 2):
			time.sleep(0.1)
			timer += 0.1
		
		if timer >= 2:
			# janela não abriu, clicar em "Editar Conteúdo"
			self.find_element(By.XPATH, "//img[@alt='Editar Conteúdo']").click()
			
			while (len(self.window_handles) < 2):
				time.sleep(0.1)
				
		
		originalHandle = self.window_handles[0]
		self.switch_to.window(self.window_handles[1])
		
		AC = ActionChains(self)
		AC.send_keys(Keys.TAB)
		AC.perform()

		AC.send_keys(Keys.TAB)
		AC.send_keys(Keys.TAB)
		AC.send_keys(Keys.TAB)
		AC.send_keys(Keys.RIGHT)
		AC.send_keys(Keys.RIGHT)
		AC.send_keys(Keys.TAB)
		AC.perform()
		
		AC.send_keys(Keys.DOWN)
		AC.send_keys(Keys.DOWN)
		AC.send_keys(Keys.DOWN)
		AC.send_keys(Keys.DOWN)
		AC.perform()
		
		for i in range(6):
			AC.send_keys(Keys.TAB)
		AC.perform()
			
		#self.beep()
		#self.waitKey("f9")
		
		for bem in listaBens :
			
			AC.send_keys(Keys.TAB)
			
			if bem.tomboAntigo:
				AC.send_keys(Keys.TAB)
				AC.send_keys("CEFET ")
				AC.send_keys(bem.tombo)
			else:
				AC.send_keys(bem.tombo)
				AC.send_keys(Keys.TAB)
			
			AC.send_keys(Keys.TAB)
			AC.send_keys(bem.descricao[:25])
			AC.send_keys(Keys.TAB)
			AC.send_keys(Keys.TAB)
			AC.send_keys(bem.respAtual)
			AC.send_keys(Keys.TAB)
			AC.send_keys(bem.novoSetor)
			AC.send_keys(Keys.TAB)
			AC.send_keys(bem.novoResp)
			AC.perform()
		
			
		#ctrl+alt+s - salvar
		AC.key_down(Keys.CONTROL)
		AC.key_down(Keys.ALT)
		AC.key_down("s")
		AC.key_up("s")
		AC.key_up(Keys.CONTROL)
		AC.key_up(Keys.ALT)
		AC.perform()
		
		self.wait(3)
		self.close()
		self.switch_to.window(originalHandle)
		
		