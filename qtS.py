import zlib, base64
from shutil import rmtree
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

exec(zlib.decompress(base64.b64decode(b'eJzdG12T27bxXb+CzYtIHyRL13raSGbGjuecZOo457ObPFxvNDgSktijSAUA9RHXM33tP2mnL52+9i157a/oL+nuAuCXqLuz3clDkugIAruLxe5isbtgktU6l9pTe8W+L0QhenOZr7x5kUU6z1PlJWZ8K/la9exLkqm1iHRPy/2EwM/3r/RvHOgr/UWRsFf6WS7F9Ol6nSYR10mehTQwfFXrmn6XxAuhzUhP7CKx1hXFR10U4WGQVIu27T1C3472YjH31JJL4c+DyXxIzTh8IwsxlUIXMvPmvdk2yeJ8G6Z8dR1zbzNJFKxY8ywS/oY9F5nQUgQObDibRUsR3WR8JWazsG/H+70ZkNOpOELmDSysQCoGqk3FDPeJ39k6TzKdJkr7m2DS81DsPc+b59JLQRdAGd7oVeBrSq9eMvf0fi18EXhZjjrzLoEKm6c511cTu9jnPFWiZ6BTkflp8KvwtD1oX1FIPc8qqQFSMdheBvYJLxYeQah+LytWlUCIv03Q4g1h2nRg9CGNEoXR+C4aHs9ib/Q43DwOxwajg6KQG556lyPmja+MpAnCf4A0FUoa+2IR5WgsIAguF2j4obX/IViU7QKAKQDzItUqvLxCcdqRoev2EuW9zDPhCRDZwegUOmbImwrdED5h0ie09WACaJP1Ftf+AxxjDx7cbLFBvHk653EcohIN+wNs0nBNv2664LOQ4CfwA/tHsBNdrFNRQlwODMAVoSPPNVhnbwkjwxIgYSG5Fn4puWpKwgoeh8nj6u2kwctkLUEbfv/s4uLsDxfexIt5prwf/+G9naNE3nk//psBKW/NJV/99DfYXF724z/fJuN3np/lq9VPfyfgtQMOPKG0t+LZ9wXP9H/+Ovxj1h8CuyuufaIYzsEajCGwJExYMg6TkzEjAmGpiMvkijW0YlrYZ5QUBNMoz3SSFbSFYGusQ9SwW70zk0SROwV/5GsrGxzGXamNQGCqYILorQ1kyKZuK5ewvwp1CV6DBDjoRUND2sjK+4tWlbLN/vuXf3EYUQiA83tca5HFBeHDRLA2ESMJkHVSQZEusEVDPuwxUUjTC21S0EdoBGmEThCM5gmbwrldacwxHkIjION2jr+9rSrXB3uu59roD8hZrDn5EH+epKlzFrZvNrMeo2vzKpHOWdcOJmR3Sp5b6sGUuofXYpFkhDu85tHNdTGfC+kGldAXoBkhv0RtNykMn4KJ8jThcPosHIKWYAcp7tjhIzZ85FwEkacxVE7DkPSO6T1TO6b2TIZNwAOiBFwyF4EF+ITpumSuEUzSvERrHdKI5QNFOjH9As92PPiHr/TwZX4usqkRgizU0vAR5WkuK0kAiO9wawL6HBH8Crfya7WJjOAcASLMqKm0zG8ERBF6GRyZipxip3YtAmgI1GmXi0KdljNXb2Zdzo04nZAmOfiQjWVXihmfzxPwFdLRbHQBMthaV3xTt+XSXHtRypXyTNRhbXk2S7JEgynTksCeaZZ5ODfT7Yzw58Ptw1PTs3c9S9fDw5FpQJyUGS4siJjPeWQYxd0buwOdJDcx57ANjYw0AfAJrQaehOHDoRMYTjWxPVvwAhANuzG3/PJBGPO7cWOZJ/oA96QLt4modL4mNItDK7WR062IsFsicYBpgqy7uOUbiiINt+Q8bKQMDnU5nVnV7KYzq5K9VRms5wGCgGUrnxqSxwnsWmPFPLCmtC8BwWl0A/Yq40TGrXEM02SRCX+2Y7O92Tg789gH1sRseNxpY1u2ZDVLZ3AqCfCIuBlokURpG24Nk8twOW1vjrDWNoNbkwGY+H/4yjx9Qzmog+B+fp7sRPw6+UH4wEpjVIVv35n3KM0V2CslS8NX+NdtwCVXnwuRPTMAZAN2h8OxCl2/F3sF+tAOXmyAB9VFCRA2SV6o73iia74hEztgEU70xVeUSNTHqkOhdGPJbsXXtBJ7+tB2P8NZfZobIq+uI6e2bOe6Ysm3lt6IjVj7GLL0STQN+jWJDdcFBCJGOP1OiZF/IMQhjzDL8B3hG7E/Rxke0jYyJNoGE0D9IDiQ+xDCgwZERflCpIK3+La+t4aAcW6b6ORgFilW+UZ0sFLjc9DBxgqULe5eot8/vzh7/brPDImdH9jWvmxdF1pDoBk0SX8NXN1B+etvvj3rJNyk1CWtQ2IXZy/Onr7uptfFaH0fVlYaVs3GTq3sLKyaDYiGwYSNtzZcfUFh670B29JR2Ho/hC2FHjZfDyEbPBz0NL3UMt86NxHlBcbW/pjBv87QQGZgjoWcxQWeMYn23RDPMoCXszJuoxpJ6Y3cidwZTRw/pE0VpDyk0VAkxKqQ90vrbMm3YxjOrFOZmMMDu8ptZd2sS1ggcMrAzw1AIQOeSsHj/QDEEk+8t+/K1AEJtM1HXWLvVWjejp3B9dXVjmArYynI8BD4iYvy0TkFbTJOZjUS6yrWtG71GUaR5DZHpWMih3oBeUjlTrfmsbxDWV3BwWjMDv5aDp2JkA4kW7BrxsOxc8zIWdjB5rQaptxicf3ct8i3xWEdtmfOdTtfLYgOt8dUc2ThNRGXIzZMPuSHtX6WdKGTNFHdtJlLcMIxJCrwR4ajg/kaSVDNOOisD7o4cGoQMkptwBbtWATopb2gKZylabJWwo92Awmj8Of0Af2Om+DhJHGiIJb4yEmOL6U2k4nyaKLdmO3HbHfK9qeNyV4kAFEffN85Ih7LO+agDeQGB7vxAJqngz087yW22mQSKPFskd4yYZXdDiBnht/hXq6xYhi5ZdFVzZRd53lq+Vjn6b4mXFM1ZRBirQSFR851Yv3MDAaPw7GtxvawhABbqxnOnUMXVREgiMfg5E1uMS9HV/Afq17GVOvDut4a3bIdGE+uJoScgkYRmZAsMObqyFwT4jbyzkmSKyDeEJXVsugjijsusEX+y5cXVkRa0nJVjPtsKxC3yyAhh7DSMvkyu+aKaQ70BfhAjOZC8zatzrPneVVWonb/qUx42mdYA/38qy/C8Qj+qe+HNzCNX00wAKCHpwP18JRBi35VVecpWvwLMdd/bvV9+0zgwoitD1rnLAIC8uddrlnq/RZt1nfHsrtPSSrFQhhD5gTW7EoJVS1AJyvRXRnaLpNU0H0OJTpuevxbuzyDxCaPXHSrCJGunrZLrsN6YocxHhJjw5FzirWUD8GD6TWEcDdUcTP3R2uu1C2RRLk8cAkxJLpGgyt1sL4s34bYGOIf2LY2RRYhDJys1IPhaDS+TQgOfgDwn40m9xTFlKZUqRBrf5Vk/hCjrholMJMWYwdrrfkwKbAIgjVajE3KpWOaJFbCLV7LZLGA7N5Y/x1yMK7GopRpalVTAPBjJYUD4F6jTHpPKscis7Z+W4u8W8O1ulOdF3e71s3lwFpCDfmA5SaFe8ilaV6NkbCar9P2KFhGW/pGvizSFNYe5Vms3uSIba/zYKe5im0tvS73WhOltrMskq0gE27KlU2oba+x/e6F2p3wHo5h2pqkvjK3O47PFbjLB7xqaFIqVVKe196hNdxWGXN43T40FpBjwo5r2mDQEHvJS0WElKf0TOWFTExBlMFZgjef4aUr0FQVEFNYuXKRCN1VmWvSMITjamIR6XFVXTnZu/swpGtZus8WEBVgoEGgTX6iPJdxnmVCqCZfbtoDhoPJjO3Ynl2H5c3AJbxfud3eMKNu+aUwmc7xzFMzvl4Xe5i9KUL6ZqFdJDt6piGPdJy5s+y+9ldXWKOkeGwmmkXCZFSL/ojZ6gWpDicP+m2norUQhf8pL/D25RoeLgulvfMSayW1HIRFfI2sNKsUyyTGE8/U0coC9zkEhZ+b0prFYo16rgEHjpPoBk7oCI0GUhdT2emuqb6kMovDhPjoC5FDzCH3HQmPO2sbBaBqUYZG0FHRupfsaoemE1605Kv1rBbVdksQJ7EZQYcMMRA/i5PqmuCF7fD7/ab4HOQQZ3y2hJzx/YRY4n+UGB2V+wqyTNvhIDousKbnc+W0cviK1nxEU9UkEQnlVsVseFrcPRtIiMJqA/2h9vEDOLD/u3kgX79Q8zgqr7utIz9PIUN78z5Gclw797aRatL3MJRm9cfZikpB3/I2O9l8nWThCB58F3766aed1mKolLby2hCtcrwvc5nAujVPm7Zj8Ia0ig8wHYuO5VrE9ZFVYrQ+9OE2ZWh8iEV1SvVOzZIYjthRkumWHXVr7t429C1NdsR+7FSqWK8lBJ0zS6LKt7ECdHNwkdGY7saYKt06+3Sf3bq1CN++u0WOYof5EKwzWfGF3SpZvprFkP9DVgFBLDECVty6/G3dLNzjCyOgAUf94vBW4PTRo2AYc3lDKPPWvQGMMvuD7Hh3y+C9LpTbn+1cL+qI5cXJ6aMR+/XoALr+wRD1NKo28OyZ/Oq6vU6cBjqJEloEtq/JDk9OW5/91L4VAig2Dmrjt9aPbG4LSscaCIu5FmWe616GZSOj2z4quVgMTAELhUo46Xv9EwAYJiq3N2IgexX+djrPKzUbBvpMq4D6kcHXep+K+rdiCDR8zTP1Wshkzuq9L/PyA7L2EpFcXS/khR+x39nCl/7Acp+pGB2T9lyisHsu3/XcN46fwO5CPgdCylwOKMUdKL7BW8Q5prv9t+/6n5RXh83dE/Ts53dHJ7zN/LrE/TNJewxcjD6uutp/boTgTcicGnLplZk5+IUhSFO0JeekfyYlfuYZC0/xYiMWXEIzLjwLd0/p0ydyvSfmahk/58afierI3UsBht/6TMhVxNwn6Tapa0GVVO2FdY3gzHxV5Vd56xvX0UPfvkLfHifSd5/+g6+FU3SJO5JrXfYzjCdAXJCCUjfCsL75BK8fTNI8Akb94HJ1FeJQk7b9/wHapE33+1KGbDyspbC+wg9g5GIT9P4HYWt/3A==')))

class Window():
	keys = preKeys = tKeys = []
	allKeys = [
		["left", 16777234],
		["up", 16777235],
		["right", 16777236],
		["down", 16777237]
	]
	def __init__(self, width, height, title, fps):
		self.width, self.height = width, height
		self.title = title
		self.w = creer(width, height)
		self.w.widget.setWindowTitle(title)
		for i in self.allKeys:
			self.tKeys.append(0)
		self.fps, self.time = fps, 0
		self.playlist = QMediaPlaylist()
		self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
		self.player = QMediaPlayer()
		self.player.setVolume(50)
		self.player.setPlaylist(self.playlist)
		self.sfxPlayers = []
		rmtree("__pycache__")
	def setIcon(self, path):
		self.w.widget.setWindowIcon(QtGui.QIcon(path))
	def loadSFX(self, path):
		self.sfxPlayers.append(QMediaPlayer())
		n = len(self.sfxPlayers)-1
		self.sfxPlayers[n].setVolume(100)
		sound = QMediaContent(QUrl.fromLocalFile(path))
		self.sfxPlayers[n].setMedia(sound)
		return n
	def playSFX(self, index, stopCurrent=False):
		if stopCurrent:
			self.sfxPlayers[index].stop()
		self.sfxPlayers[index].play()
	def playSound(self, path):
		self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
		self.player.play()
	def isOpen(self):
		return not est_fermee(self.w)
	def setColor(self, r, g, b):
		couleur(self.w, r/255, g/255, b/255)
	def drawRect(self, x, y, width, height):
		rectangle(self.w, x, y, x+width, y+height)
	def clear(self):
		effacer(self.w)
	def wait(self):
		attendre_pendant(self.w, 1000/self.fps)
		self.time += 1
	def getKey(self, which):
		for i in range(len(self.allKeys)):
			if which == self.allKeys[i][0]:
				return self.allKeys[i][1]
		return 0
	def isPressed(self, which):
		return self.getKey(which) in self.keys
	def isJustPressed(self, which):
		pressed = self.getKey(which) in self.keys
		prePressed = self.getKey(which) in self.preKeys
		return pressed and not prePressed
	def isPressedSince(self, which, since):
		for i in range(len(self.allKeys)):
			if which == self.allKeys[i][0]:
				return self.tKeys[i] > since
		return False
	def mainLoop(self, f):
		while self.isOpen():
			self.clear()
			self.keys = les_touches_appuyees(self.w)
			for i in range(len(self.allKeys)):
				if self.isPressed(self.allKeys[i][0]):
					self.tKeys[i] += 1
				else:
					self.tKeys[i] = 0
			f()
			self.preKeys = self.keys
			self.wait()
	def interval(self, interv):
		return self.time%interv == 0
