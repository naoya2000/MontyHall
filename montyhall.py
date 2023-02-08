import random
from bokeh.plotting import figure,show
import numpy as np

def montyHall(n):
  results = []
  count = 0
  for i in range(1,n+1):
    doors = [1,2,3]
    carDoor = random.randint(1,3)
    carDoorL = [carDoor]
    goatDoors = [1,2,3]
    goatDoors.remove(carDoor)
    selectedDoor = random.randint(1,3)
    if selectedDoor in goatDoors:
      openDoor = goatDoors
      openDoor.remove(selectedDoor)
    if selectedDoor not in goatDoors:
      openDoor = [random.choice(goatDoors)]
    
    finalDoor = [1,2,3]
    finalDoor.remove(selectedDoor)
    finalDoor.remove(openDoor[0])
    if finalDoor == carDoorL:
      count += 1
      results.append((count/i))
    else:
      results.append((count/i))
  return results
  
f1 = figure(title = "Monty Hall Simulation")
f1.xaxis.axis_label = "Trials"
f1.yaxis.axis_label = "probability of winning if you switch"

for i in range(101):
  yvals = montyHall(200)
  xvals = range(200)
  cols = ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
  f1.line(xvals,yvals,color = cols, line_width = 2)

show(f1)

data = []
for i in range(101):
  data.append(montyHall(1000)[-1])
  
hist = np.histogram(data, bins = 20, range = (0,1))

yvals = hist[0]
xvals = hist[1]
xvals = xvals[0:-1]+(xvals[0]+xvals[1])/2

f2 = figure(title = "Monty Hall Simulation", x_range = (0.4,0.8))
f2.xaxis.axis_label = "Final Percentage of Wins"
f2.yaxis.axis_label = "Number of Occurences"

for (x,y) in zip(xvals,yvals):
  w = (xvals[0]+xvals[1])/2
  f2.vbar(x,w*.99,y,0)

show(f2)
