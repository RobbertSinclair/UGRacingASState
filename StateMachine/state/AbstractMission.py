class statecontainer :
	def __init__(self) :
        self.TS = False
		self.R2D = False
		self.SA = "unavailable"
		self.SB = "unavailable"
		#self.EBS = EBS
		self.ASSI = "Off"
		#self.RES = RES
		self.ASMS = False

	def preUpdateState(self, newStage) :
    # make changes
    	if newStage = "asoff":
    	#self.prestages needed

 	def postUpdateState(self, newStage):
    # make changes after transitioned

class AbstractMission :
	def __init__(self):
		self.statecontainer = statecontainer()
		self.stage = "ASOFF"
  	def transition(self) :
   		# all of the ifs and elses
    	self.stateVariables.preUpdateState("newStage")
   		self.state = "newState"
    	self.stateVariables.postUpdateState("newStage")
		"""self.TS = TS
		self.R2D = R2D
		self.SA = SA
		self.SB = SB
		self.EBS = EBS
		self.ASSI = ASSI
		self.RES = RES
		self.ASMS = ASMS
		self.stage = stage"""
	
	def countdown(self, t): 
		while t: 
			mins, secs = divmod(t, 60) 
			timer = '{:02d}:{:02d}'.format(mins, secs) 
			print(timer, end="\r") 
			time.sleep(1) 
			t -= 1
	
	def manualOrAS(self):
		response = input("Manual [M] or Autonomous System [AS]")
		return response

	def run(self):
		if self.stage == "ASOFF":
			print("Bbrrrr stage asoff")
			self.runASOFF()
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
	#self.SA = "unavailable", available DONE
	#self.SB = "unavailable", engaged, available DONE
	#self.EBS = "unavailable", "armed, "activated" DONE
	#self.RES = "Off", ""Go", "RESTrigger"DONE
	#self.ASMS = False or True DONE
	#self.stage = stage DONE
	#self.ASSI = ASOFF  AS Ready            AS Driving       Emergency AS    Finished
	#self.ASSI = off    yellow continuous  yellow flashing   blue flashing   blue continuous DONE

	def runASOFF(self):
		print("Im in runasoff()")
		self.TS = False
		self.R2D = False
		self.SA = "unavailable"
		self.SB = "unavailable"
		#self.EBS = EBS
		self.ASSI = "Off"
		#self.RES = RES
		self.ASMS = False
		print("runASOFF")

		response  = self.manualOrAS()

		if response == "M":
			self.transition("ManualDriving")
		elif response == "AS":
			self.transition("ASReady")
		else:
			print("Wrong input")
			manualOrAS()

	def runManualDriving(self):
		self.TS = True
		self.R2D = True
		self.SA = "unavailable"
		self.SB = "unavailable"
		self.EBS = "unavailable"
		self.ASSI = "Off"
		#self.RES = RES
		self.ASMS = False
		print("runManualDriving")
		self.transition("ASOFF")

	def runASReady(self):
		self.TS = True
		self.R2D = False
		self.SA = "available"
		self.SB = "engaged"
		self.EBS = "armed"
		self.ASSI = "yellowConst"
		#self.RES = RES
		self.ASMS = True
		print("runASReady")
		self.transition("ASOFF")

		if self.EBS == "activated":
			self.transition("ASEmergency")
		
		else:
			self.transition("ASDriving")

	def runASDriving(self):
		self.TS = True
		self.R2D = True
		self.SA = "available"
		self.SB = "available"
		self.EBS = "armed"
		self.ASSI = "yellowFlash"
		#self.RES = RES
		self.ASMS = True

		print("runASDriving")
		if self.EBS == "activated":
			self.transition("ASEmergency")
		else:
			self.transition("ASFinished")

	def runASFinished(self):
		self.TS = False
		self.R2D = False
		self.SA = "unavailable"
		#self.SB = SB
		self.EBS = "activated"
		self.ASSI = "blueConst"
		#self.RES = RES
		self.ASMS = True
		print("runASFinished")
		if self.RES =="RESTrigger":
			self.transition("ASEmergency")
		else:
			self.transition("ASOFF")

	def runASEmergency(self):
		self.TS = False
		self.R2D = False
		#self.SA = SA
		#self.SB = SB
		self.EBS = "activated"
		self.ASSI = "blueFlash"
		#self.RES = RES
		self.ASMS = True
		print("runASEmergency")
		self.transition("ASOFF")

	def transition(self, goToStage):
		if self.stage == "ASReady" or "ASDriving" or "ASFinished":
			if goToStage == "ASEmergency":

				self.state = "ASEmergency"
			
			if self.stage == "ASReady":
				if goToStage == "ASDriving":
					countdown(5)
					#IF GO SIGNAL GIVEN - IMPLEMENT HERE BEFORE TRANSITION
#!!!!					self.stateVariables.preUpdateState(newState)
#!!!!					self.stage = "ASDriving"
#!!!!					self.stateVariables.postUpdateState(newState)
				elif goToStage == "ASOFF":
					self.ASMS = False
					# ADD BRAKES RELEASED IN TRANSITION
					self.stage = "ASOFF"
			elif self.stage == "ASDriving":
				if goToStage == "ASFinished":
					# implement finished mission checker
					missionFinished = True
					if missionFinished == True and vehicleSpeed == 0:
						self.stage = "ASFinished"

			elif self.stage == "ASFinished":
				if goToStage == "ASOFF":
					self.ASMS = False
					# ADD BRAKES RELEASED IN TRANSITION
					self.stage = "ASOFF"

		if self.stage == "ASEmergency":
			if goToStage == "ASOFF":
				self.EBS = "unavailable"#
				self.ASMS = False
				# ADD BRAKES RELEASED IN TRANSITION
				self.state = "ASOFF"

		if self.stage == "ASOFF":
			if goToStage == "ASReady":
				password = input("Please Enter Password to Turn on ASMS: ")
				if password == passwordCorrect:
					self.ASMS = True
					self.EBS = "armed"
					self.TS = True
					self.stage = "ASReady"
				else:
					#else what does it do?
					print("Password Incorrect.")
			
			elif goToStage == "ManualDriving":
				self.stage = "ManualDriving"

		if self.stage == "ManualDriving":
			if goToStage == "ASOFF":
				self.EBS = "unavailable"
				self.ASMS = False
				self.TS = True
				self.stage = "ASOFF"