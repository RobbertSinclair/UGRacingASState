class AbstractMission :
	def __init__(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS, stage):
		self.TS = TS
		self.R2D = R2D
		self.SA = SA
		self.SB = SB
		self.EBS = EBS
		self.ASSI = ASSI
		self.RES = RES
		self.ASMS = ASMS
		self.stage = stage
	

	def run(self):
		if self.stage == "ASOFF":
			self.runASOFF()
			print(self.stage, "Printing self.stage")
			self.run()

		elif self.stage == "ASReady":
			self.runASReady()
			self.run()

		elif self.stage == "ASDriving":
			self.runASDriving()
			self.run()

		elif self.stage == "ASFinished":
			self.runASFinished()
			self.run()

		elif self.stage == "ASEmergency":
			self.runASEmergency()
			self.run()

		elif self.stage == "ManualDriving":
			self.runManualDriving()
			self.run()
	
	#self.TS = False or TRUE DONE
	#self.R2D = False or TRUE DONE
	#self.SA = "Unavailable", available DONE
	#self.SB = "Unavailable", engaged, available DONE
	#self.EBS = "unavailable", "armed, "activated" DONE
	#self.ASSI = ASOff  AS Ready            AS Driving       Emergency AS    Finished
	#self.ASSI = off    yellow continuous  yellow flashing   blue flashing   blue continuous DONE
	#self.RES = "Off", ""Go", "RESTrigger"DONE
	#self.ASMS = False or True DONE
	#self.stage = stage DONE


	#if self.RES = "Off", ""Go", "RESTrigger":
	#	print("brr)")

	def runASOFF(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS):
		self.TS = False
		self.R2D = False
		self.SA = "unavailable"
		self.SB = "unavailable"
		self.EBS = EBS
		self.ASSI = "Off"
		self.RES = RES
		self.ASMS = ASMS

	def runManualDriving(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS)
		self.TS = True
		self.R2D = True
		self.SA = "unavailable"
		self.SB = "unavailable"
		self.EBS = "unavailable"
		self.ASSI = "Off"
		self.RES = RES
		self.ASMS = False

	def runASReady(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS):
		#todo
		self.TS = True
		self.R2D = False
		self.SA = "available"
		self.SB = "engaged"
		self.EBS = "armed"
		self.ASSI = "yellowConst" # implement self.EBS = armed in TRANSITION as per rules
		self.RES = RES
		self.ASMS = True

	def runASDriving(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS):
		#todo
		self.TS = False
		self.R2D = False
		self.SA = False
		self.SB = False
		self.EBS = EBS
		self.ASSI = False
		self.RES = RES
		self.ASMS = ASMS

	def runASFinished(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS):
		#todo
		self.TS = False
		self.R2D = False
		self.SA = False
		self.SB = False
		self.EBS = EBS
		self.ASSI = False
		self.RES = RES
		self.ASMS = ASMS

	def runASEmergency(self, TS, R2D, SA, SB, EBS, ASSI, RES, ASMS):
		#todo
		self.TS = False
		self.R2D = False
		self.SA = False
		self.SB = False
		self.EBS = EBS
		self.ASSI = False
		self.RES = RES
		self.ASMS = ASMS





	def transition(self, goToState):

		if self.stage == "ASReady" or "ASDriving" or "ASFinished":
			if goToStage == "ASEmergency":
				self.state = "ASEmergency"
			
			if self.stage == "ASReady":
				if goToStage == "ASDriving":
					#IMPLEMENT COUNTDOWN FOR 5 SECONDS AND GO SIGNAL CHECK
					self.stage = "ASDriving"
				elif goToStage == "ASOFF":
					self.stage = "ASOFF"
			
			elif self.stage == "ASDriving":
				if goToStage == "ASFinished":
					self.stage = "ASFinished"

			elif self.stage == "ASFinished":
				if goToStage == "ASOFF":
					self.stage = "ASOFF"

		if self.state == "ASEmergency":
			if goToStage == "ASOFF":
				self.state = "ASOFF"

		if self.stage == "ASOFF":
			if goToStage == "ASReady":
				self.stage = "ASReady"
			elif goToStage == "ManualDriving" and self.isManualAllowed:
				self.stage = "ManualDriving"

		if self.stage == "ManualDriving":
			if goToStage == "ASOFF":
				self.stage = "ASOFF"


