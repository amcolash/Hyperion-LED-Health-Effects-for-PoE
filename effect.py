import hyperion
import time
import colorsys
import PIL.ImageGrab

""" Define some variables """
sleepTime = 0.1

x = 143
yStart = 1173
yHeight = 233

testX = 20
testY = 1176

threshold = 15
testR = 186
testG = 103
testB = 27

ambient = 90
last = -255

""" The effect loop """
while not hyperion.abort():

	# Get all pixels on screen
	px = PIL.ImageGrab.grab().load()
	red = ambient

	# Test that we have a health bar, if so set the rgb
	testColor = px[testX, testY]

	matchR = abs(testColor[0] - testR) < threshold
	matchG = abs(testColor[1] - testG) < threshold
	matchB = abs(testColor[2] - testB) < threshold

	if matchR and matchG and matchB:
		for y in range(yStart, yStart + yHeight):
			red += px[x, y][0]

		avg = red / yHeight
		norm = 1 - (avg / 255.)

		red = (1.9 * norm - 0.6) * 255

		# clamp from 80 - 255, so there is always some light but not too much
		red = max(ambient, min(red, 255))

	if abs(last - red) > 5:
		# Only update when red changes enough, otherwise loop
		last = red

		#print (norm, avg, red)

		""" The algorithm to calculate the change in color """
		led_data = bytearray()

		for i in range(hyperion.ledCount):
			led_data += bytearray((int(red), 0, 0))

		""" send the data to hyperion or clear the effect """
		if red == ambient:
			hyperion.clear()
		else:
			hyperion.setColor(led_data)

		# wait a moment before updating again
		time.sleep(sleepTime)
	else:
		# wait a frame before checking again
		time.sleep(0.015)
