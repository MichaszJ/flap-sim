import matplotlib.pyplot as plt
import math
import numpy as np

intervals = 200

dxList = np.linspace(0, 371.22648, intervals)
dyList = np.linspace(0, -74.04244, intervals)
thetaList = np.linspace(0, 35, intervals)

chordLength = 1014.28

quarterChord = chordLength/4
quarterChordRemainder = chordLength - quarterChord

def LEx(dx, theta):
    return dx + quarterChord * math.cos(math.radians(theta))

def LEy(dy, theta):
    return dy + quarterChord * math.sin(math.radians(theta))

def TEx(dx, theta):
    return chordLength + dx - quarterChordRemainder * math.cos(math.radians(theta))

def TEy(dy, theta):
    return dy - quarterChordRemainder * math.sin(math.radians(theta))

fig, ax = plt.subplots(dpi = 260)
for i in range(0, intervals):
    ax.cla()

    dx = dxList[i]
    dy = dyList[i]
    theta = thetaList[i]

    ax.set(xlim = (-10, 2010), ylim=(-600, 100))

    ax.plot([LEx(dx, theta), TEx(dx, theta)], [LEy(dy, theta), TEx(dy, theta)])
    ax.plot([dx + quarterChord], [dy], marker='o')

    ax.text(dx + quarterChord + 50, dy - 15, 'QC: {0} | {1}'.format(int(dx + quarterChord), int(dy)))

    plt.pause(0.001)