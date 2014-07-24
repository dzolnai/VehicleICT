#!/usr/bin/python

# imports
import random
import math
import json
import argparse
import sys
import httplib
import time

""" generateVehicleICTJson.py: Generates fake, but believable sensor data, for the Vehicle ICT project.
NOTE: Tested on Python 2.7.8 """

__author__ = "Daniel Zolnai"
__version__ = "1.0"

# this value defines the amount of JSON to post for a "trip"
separateBy = 1

# global values, which will be in the output
vehicleSpeed = 0
avgFuelEcoCount = 0.0
barometricPress = 0
commandEqRatio = 0.0
ambientAirTemp = 0
userId = 0
engineRPM = 0
engineRuntime = 0
fuelEco = 0.0
fuelEcoCmdMap = 0.0
fuelEcoMap = 0.0
fuelPress = 0.0
gpsSpeed = 0.0
gpsTime = 0
timingAdvance = 0.0
latitude = 0.0
longitude = 0.0
# NOTE: NOT obs time. Linearity should be the same, but minor (or in extreme cases
# major [e.g. misconfigured GPS date]) offset from obs time is possible
obsTimeOffset = 0
massAirFlow = 0.0
longTermFuelTrim = 0
shortTermFuelTrim = 0
throttlePosition = 0
intakeManifoldPress = 0
airIntakeTemp = 0
engineLoad = 0
coolantTemp = 0
# used to calculate latitude and longitude.
# using random offsets for lat and lon could result 'going around in a circle'
directionAngle = 0.0

def main():
	#declare the available arguments
	print("Script started.")
	parser = argparse.ArgumentParser();
	parser.add_argument("-i", "--ip",
		help="The IP address of the machine where you want to post the JSON files",
		type=str)
	parser.add_argument("-p", "--port",
		help="The port associated to the IP address, defaults to 80.",
		type=int)
	parser.add_argument("-a", "--amount", 
		help="The amount of JSON files to post. Defaults to 1.",
		type=int)
	args = parser.parse_args()
	# --- CHECK THE ARGUMENTS ---
	# check if IP was defined
	if (args.ip == None):
		print("No IP address given. Use the -i parameter to define the IP address of the server.")
		sys.exit(0)
	port = args.port
	# if no port given, default to 80
	if (port == None):
		print("No port defined, using port number 80!")
		port = 80
	amount = args.amount
	# if no amount given, default to 1
	if (amount == None):
		print("No amount defined, only one random JSON will be posted!")
		amount = 1
	defineSeparator(amount)
	postJsons(args.ip, port, amount)


def postJsons(destIp, destPort, amount):
	# create the connection
	httpServ = httplib.HTTPConnection(destIp, port=str(destPort))
	httpServ.connect()
	print("Connection created.")
	currentIndex = 0
	# post the jsons
	while (currentIndex < amount):
		jsonString = generateNextJson(currentIndex)
		# Uncomment the next line if you want to see the generated json
		# print(jsonString)
		httpServ.request('POST', '', body=jsonString,
			headers={'Content-Type': 'application/json; charset=utf-8'})
		response = httpServ.getresponse()
		currentIndex = currentIndex + 1
	# close the connection
	httpServ.close()
	print("Connection closed.")

def generateNextJson(currentIndex):
	if (currentIndex % separateBy == 0):
		startNewTrip()
	else:
		alterValues()
	# generate the JSON
	outputDict = {
		"Trouble Codes": "43000000000000",
		"Vehicle Speed": vehicleSpeed,
		"Avarage Fuel Economy Count": avgFuelEcoCount,
		"Barometric Press": barometricPress,
		"Command Equivalence Ratio": commandEqRatio,
		"Ambient Air Temp": ambientAirTemp,
		"UserID": userId,
		"Engine RPM": engineRPM,
		"Engine Runtime": engineRuntime,
		"Fuel Economy": fuelEco,
		"Fuel Economy Cmd. MAP": fuelEcoCmdMap,
		"Fuel Economy MAP": fuelEcoMap,
		"Fuel Press": fuelPress,
		"GPS Speed": gpsSpeed,
		"GPS Time": gpsTime,
		"Timing Advance": timingAdvance,
		"Latitude": latitude,
		"Longitude": longitude,
		"Obs Time": gpsTime + obsTimeOffset,
		"Mass Air Flow": massAirFlow,
		"Long Term Fuel Trim": longTermFuelTrim,
		"Short Term Fuel Trim": shortTermFuelTrim,
		"Throttle Position": throttlePosition,
		"Intake Manifold Press": intakeManifoldPress,
		"Air Intake Temp": airIntakeTemp,
		"Engine Load": engineLoad,
		"Coolant Temp": coolantTemp
		}
	jsonString = json.dumps(outputDict)
	return jsonString


def defineSeparator(amount):
	# request access to global variable
	global separateBy

	if (amount < 50):
		separateBy = 1
	elif (amount < 200):
		separateBy = 10
	elif (amount < 2000):
		separateBy = 100
	elif (amount < 20000):
		separateBy = 1000
	elif (amount < 200000):
		separateBy = 10000
	else:
		separateBy = 50000

def startNewTrip():
	# request global access to the variables
	global vehicleSpeed
	global avgFuelEcoCount
	global barometricPress
	global commandEqRatio
	global ambientAirTemp
	global userId
	global engineRPM
	global engineRuntime
	global fuelEco
	global fuelEcoCmdMap
	global fuelEcoMap
	global fuelPress
	global gpsSpeed
	global gpsTime
	global timingAdvance
	global latitude
	global longitude
	# NOTE: NOT obs time. Linearity should be the same, but minor (or in extreme cases
	# major [e.g. misconfigured GPS date]) offset from obs time is possible
	global obsTimeOffset
	global massAirFlow
	global longTermFuelTrim
	global shortTermFuelTrim
	global throttlePosition
	global intakeManifoldPress
	global airIntakeTemp
	global engineLoad
	global coolantTemp
	global directionAngle

	# randomize the values real-looking data
	vehicleSpeed = random.randint(0,120)
	avgFuelEcoCount = random.uniform(0.0, 150.0)
	barometricPress = random.randint(130, 300)
	commandEqRatio = random.uniform(0.9, 1.0)
	ambientAirTemp = random.randint(-10, 36)
	userId = random.randint(0, 20)
	engineRPM = random.randint(0, 5500)
	engineRuntime = random.randint(0, 5000)
	fuelEco = random.uniform(4.0, 12.0)
	fuelEcoCmdMap = fuelEco + random.uniform(-1.0, 1.0)
	fuelEcoMap = fuelEco + random.uniform(-1.0, 1.0)
	fuelPress = random.uniform(380.0,410.0)
	gpsSpeed = vehicleSpeed / 3.6 + random.uniform(-2.0, 2.0)
	# make sure it doesn't go below 0
	if (gpsSpeed < 0):
		gpsSpeed = 0.0
	gpsTime = time.time() * 1000 + random.randint(-10000,10000)
	timingAdvance = random.uniform(-10, 10)
	latitude = random.uniform(47.912552, 46.697480)
	longitude = random.uniform(17.055730, 21.610620)
	obsTimeOffset = random.randint(-500,500)
	massAirFlow = 2.0 + engineRPM / 600.0
	longTermFuelTrim = random.randint(0,40)
	shortTermFuelTrim = random.randint(0,40)
	throttlePosition = random.randint(0,100)
	intakeManifoldPress = random.randint(20,150)
	airIntakeTemp = ambientAirTemp + random.randint(15,30)
	engineLoad = random.randint(0,30) + engineRPM / 100
	coolantTemp = airIntakeTemp + engineLoad / 3
	directionAngle = random.randint(0,360)

def alterValues():
	# request global access to the variables
	global vehicleSpeed
	global avgFuelEcoCount
	global barometricPress
	global commandEqRatio
	global ambientAirTemp
	global userId
	global engineRPM
	global engineRuntime
	global fuelEco
	global fuelEcoCmdMap
	global fuelEcoMap
	global fuelPress
	global gpsSpeed
	global gpsTime
	global timingAdvance
	global latitude
	global longitude
	# NOTE: NOT obs time. Linearity should be the same, but minor (or in extreme cases
	# major [e.g. misconfigured GPS date]) offset from obs time is possible
	global obsTimeOffset
	global massAirFlow
	global longTermFuelTrim
	global shortTermFuelTrim
	global throttlePosition
	global intakeManifoldPress
	global airIntakeTemp
	global engineLoad
	global coolantTemp
	global directionAngle

	# Vehicle speed does not always change, and it stays between 0 and 160
	if (bool(random.getrandbits(1))):
		vehicleSpeed = vehicleSpeed + random.randint(-2, 2)
		if (vehicleSpeed < 0):
			vehicleSpeed = 0
		elif (vehicleSpeed > 160):
			vehicleSpeed = 160
	# Average fuel economy count does rarely change, and stays between 0 and 150 [5% chance to change]
	if (random.randint(0, 99) < 5):
		avgFuelEcoCount = avgFuelEcoCount + random.randint(-2, 2)
		if (avgFuelEcoCount < 0):
			avgFuelEcoCount = 0
		elif (avgFuelEcoCount > 150):
			avgFuelEcoCount = 150
	# Barometric press stays above 40, and can only decrease [1% chance to decrease]
	if (random.randint(0, 99) < 1):
		barometricPress = barometricPress - 1
		if (barometricPress < 40):
			barometricPress = 40
	# Commanded Equivalence Ratio just changes randomly between 0.8 and 1.0 [5% chance to change]
	if (random.randint(0, 99) < 5):
		commandEqRatio = commandEqRatio + random.uniform(0.03, -0.03)
		if (commandEqRatio < 0.8):
			commandEqRatio = 0.8
		elif (commandEqRatio > 1.0):
			commandEqRatio = 1.0
	# Ambient air temp stays between -20 and +40 [2% chance to change]
	if (random.randint(0,99) < 2):
		ambientAirTemp = ambientAirTemp + random.randint(-1,1)
		if (ambientAirTemp < -20):
			ambientAirTemp = -20
		elif (ambientAirTemp > 40):
			ambientAirTemp = 40
	# User ID does not change!
	# EngineRPM can decrease or increase. When below 1000, it jumps to 2600. When above 4500, it jumps to 2200.
	engineRPM = engineRPM + random.randint(-100,100)
	if (engineRPM < 1000):
		engineRPM = 2600
	elif (engineRPM > 4500):
		engineRPM = 2200
	# Engine runtime increases by 1
	engineRuntime = engineRuntime + 1
	# Fuel economy stays between 3.0 and 18.0.
	fuelEco = fuelEco + random.uniform(-0.1, 0.1)
	if (fuelEco < 3.0):
		fuelEco = 3.0
	elif (fuelEco > 18.0):
		fuelEco = 18.0
	# Fuel economoy CMD MAP stays close to fuel economy
	fuelEcoCmdMap = fuelEco + random.uniform(-0.5, 0.5)
	# Same with Fuel economy MAP
	fuelEcoMap = fuelEco + random.uniform(-0.5, 0.5)
	# Fuel press stays between 350 and 450 [2% chance to change]
	if (random.randint(0,99) < 2):
		fuelPress = fuelPress + random.uniform(-1.0, 1.0)
		if (fuelPress < 350):
			fuelPress = 350
		if (fuelPress > 450):
			fuelPress = 450
	# GPS speed shows almost the same as Vehicle speed
	gpsSpeed = vehicleSpeed / 3.6 + random.uniform(-3.0, 3.0)
	if (gpsSpeed < 0.0):
		gpsSpeed = 0.0
	# GPS time increases by 1000 ms
	gpsTime = gpsTime + 1000
	# Timing advance doesn't change
	# Direction angle sometimes changes [10% chance to change]
	if (random.randint(0,99) < 10):
		directionAngle = (directionAngle + random.randint(-20,20)) % 360
	oneMeterInDegrees = 1 / 111111
	latitude = latitude + sin(directionAngle) * oneMeterInDegrees * gpsSpeed
	longitude = longitude + cos(directionAngle) * oneMeterInDegrees * gpsSpeed
	# Observed time offset doesn't change
	# Mass air flow canges depending on engine RPM
	massAirFlow =  2.0 + engineRPM / 600.0
	# Long term fuel trim stays between 0 and 100. [1% chance to change]
	if (random.randint(0,99) < 1):
		longTermFuelTrim = longTermFuelTrim + random.randint(-2, 2)
		if (longTermFuelTrim < 0):
			longTermFuelTrim = 0
		elif (longTermFuelTrim > 100):
			longTermFuelTrim = 100
	# Short term fuel trim stays between 0 and 100 [3% chance to change]
	if (random.randint(0,99) < 3):
		shortTermFuelTrim = shortTermFuelTrim + random.randint(-2, 2)
		if (shortTermFuelTrim < 0):
			shortTermFuelTrim = 0
		elif (shortTermFuelTrim > 100):
			shortTermFuelTrim = 100
	# Throttle position randomly changes between 0 and 100
	throttlePosition = throttlePosition + random.randint(-10,10)
	if (throttlePosition < 0):
		throttlePosition = 0
	if (throttlePosition > 100):
		throttlePosition = 100
	# Intake manifold press changes between 20 and 180 [10% chance to change]
	if (random.randint(0,99) < 10):
		intakeManifoldPress = intakeManifoldPress + random.randint(-2, 2)
		if (intakeManifoldPress < 20):
			intakeManifoldPress = 20
		elif (intakeManifoldPress > 180):
			intakeManifoldPress = 180
	# Air intake temp should be higher than the ambient air temp
	if (random.randint(0,99) < 2):
		airIntakeTemp = airIntakeTemp + random.randint(-1,1)
		if (airIntakeTemp < ambientAirTemp):
			airIntakeTemp = ambientAirTemp
		if (airIntakeTemp > 50):
			airIntakeTemp = 50
	# Engine load is calculated from the RPM
	engineLoad = random.randint(0,30) + engineRPM / 100
	# Coolant temperature is calculated from the engine load
	coolantTemp = airIntakeTemp + engineLoad / 3

# Start main function
if (__name__ == "__main__"):
	main()
