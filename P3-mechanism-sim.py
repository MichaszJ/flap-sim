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

def QCx(dx, theta):
    return dx + quarterChord * math.cos(math.radians(theta))

def QCy(dy, theta):
    return dy

def LEx(QCx, theta):
    return QCx - quarterChord * math.cos(math.radians(theta))

def LEy(QCy, theta):
    return QCy + quarterChord * math.sin(math.radians(theta))

def TEx(QCx, theta):
    return QCx + quarterChordRemainder * math.cos(math.radians(theta))

def TEy(QCy, theta):
    return QCy - quarterChordRemainder * math.sin(math.radians(theta))

def animate():
    fig, ax = plt.subplots(dpi=260)

    for i in range(0, intervals):
        ax.cla()
        dx = dxList[i]
        dy = dyList[i]
        theta = thetaList[i]

        qcx = QCx(dx, theta)
        qcy = QCy(dy, theta)

        lex = LEx(qcx, theta)
        tex = TEx(qcx, theta)

        ley = LEy(qcy, theta)
        tey = TEy(qcy, theta)

        ax.set(xlim = (-10, 1550), ylim=(-600, 300))

        ax.plot([lex, tex], [ley, tey], marker='o')
        ax.plot([qcx], [qcy], marker='o')

        ax.text(qcx, qcy, 'QC: {0} | {1}'.format(int(dx + quarterChord), int(dy)))
        ax.text(lex, ley, 'LE: {0} | {1}'.format(int(lex), int(ley)))
        ax.text(tex, tey, 'TE: {0} | {1}'.format(int(tex), int(tey)))
        ax.text(10, 250, r'$\theta$: {0}'.format(theta))

        plt.pause(0.001)

def halfDeployment():
    fig, ax = plt.subplots(dpi=260)

    interval = int(intervals/2)

    dx = dxList[interval]
    dy = dyList[interval]
    theta = thetaList[interval]

    qcx = QCx(dx, theta)
    qcy = QCy(dy, theta)

    lex = LEx(qcx, theta)
    tex = TEx(qcx, theta)

    ley = LEy(qcy, theta)
    tey = TEy(qcy, theta)

    ax.set(xlim = (-10, 1800), ylim=(-600, 300))

    ax.plot([lex, tex], [ley, tey], marker='o')
    ax.plot([qcx], [qcy], marker='o')

    ax.text(qcx, qcy, 'QC: {0} | {1}'.format(int(dx + quarterChord), int(dy)))
    ax.text(lex, ley, 'LE: {0} | {1}'.format(int(lex), int(ley)))
    ax.text(tex, tey, 'TE: {0} | {1}'.format(int(tex), int(tey)))
    ax.text(10, 250, r'$\theta$: {0}'.format(theta))

    plt.show()

def fullDeployment():
    fig, ax = plt.subplots(dpi=260)

    interval = intervals - 1

    dx = dxList[interval]
    dy = dyList[interval]
    theta = thetaList[interval]

    qcx = QCx(dx, theta)
    qcy = QCy(dy, theta)

    lex = LEx(qcx, theta)
    tex = TEx(qcx, theta)

    ley = LEy(qcy, theta)
    tey = TEy(qcy, theta)

    ax.set(xlim = (-10, 1800), ylim=(-600, 300))

    ax.plot([lex, tex], [ley, tey], marker='o')
    ax.plot([qcx], [qcy], marker='o')

    ax.text(qcx, qcy, 'QC: {0} | {1}'.format(int(dx + quarterChord), int(dy)))
    ax.text(lex, ley, 'LE: {0} | {1}'.format(int(lex), int(ley)))
    ax.text(tex, tey, 'TE: {0} | {1}'.format(int(tex), int(tey)))
    ax.text(10, 250, r'$\theta$: {0}'.format(theta))

    plt.show()

def stowed():
    fig, ax = plt.subplots(dpi=260)

    interval = 0

    dx = dxList[interval]
    dy = dyList[interval]
    theta = thetaList[interval]

    qcx = QCx(dx, theta)
    qcy = QCy(dy, theta)

    lex = LEx(qcx, theta)
    tex = TEx(qcx, theta)

    ley = LEy(qcy, theta)
    tey = TEy(qcy, theta)

    ax.set(xlim = (-10, 1800), ylim=(-600, 300))

    ax.plot([lex, tex], [ley, tey], marker='o')
    ax.plot([qcx], [qcy], marker='o')

    ax.text(qcx, qcy, 'QC: {0} | {1}'.format(int(dx + quarterChord), int(dy)))
    ax.text(lex, ley, 'LE: {0} | {1}'.format(int(lex), int(ley)))
    ax.text(tex, tey, 'TE: {0} | {1}'.format(int(tex), int(tey)))
    ax.text(10, 250, r'$\theta$: {0}'.format(theta))

    plt.show()

#stowed()
#halfDeployment()
#fullDeployment()
animate()
