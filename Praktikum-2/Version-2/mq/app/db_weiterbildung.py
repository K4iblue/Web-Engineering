# coding: utf-8
import os
import os.path
import codecs
import json
#----------------------------------------------------------
class DB_weiterbildung_cl(object):
#----------------------------------------------------------
	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		self.data_o = None
		self.readData_p()
	
	#-------------------------------------------------------
	def read_px(self, id_spl = None):
	#-------------------------------------------------------
		data_o = None
		if id_spl == None:
			data_o = self.data_o
		else:
			if id_spl in self.data_o:
				data_o = self.data_o[id_spl]
				
		return data_o
	
	#-------------------------------------------------------
	def readData_p(self):
	#-------------------------------------------------------
		try:
			fp_o = codecs.open(os.path.join('data', 'Weiterbildung.json'), 'r', 'utf-8')
		except:
			self.data_o = {}
			for loop_i in range(0,15):
				self.data_o[str(loop_i)] = ['', '', '', '', '', '']
				self.saveData_p()
		else:
			with fp_o:
				self.data_o = json.load(fp_o)
		return
	
	#-------------------------------------------------------
	def saveData_p(self):
	#-------------------------------------------------------
		with codecs.open(os.path.join('data', 'Weiterbildung.json'), 'w', 'utf-8') as fp_o:
			json.dump(self.data_o, fp_o)
			
	#-------------------------------------------------------
	def getDefault6_px(self):
	#-------------------------------------------------------
		return ['', '', '', '', '', '']

	#-------------------------------------------------------
	def update_px(self, id_spl, data_opl):
	#-------------------------------------------------------
		status_b = False
		if id_spl in self.data_o:
			self.data_o[id_spl] = data_opl
			self.saveData_p()
			status_b = True
			
		return status_b
	
	#-------------------------------------------------------
	def create_px(self, data_opl):
	#-------------------------------------------------------
		# 'Freien' Platz suchen,
		# Falls vorhanden: belegen und Nummer des Platzes als Id zurückgeben
		id_s = None
		for loop_i in range(0,15):
			if self.data_o[str(loop_i)][0] == '':
				id_s = str(loop_i)
				self.data_o[id_s] = data_opl
				self.saveData_p()
				break
			
		return id_s
	
	#-------------------------------------------------------
	def delete_px(self, id_spl):
	#-------------------------------------------------------
		status_b = False
		if id_spl in self.data_o:
			default = self.getDefault6_px()
			self.data_o[id_spl] = default
			self.saveData_p()
			status_b = True
			
		return status_b

# EOF