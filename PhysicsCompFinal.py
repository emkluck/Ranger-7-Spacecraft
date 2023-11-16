Web VPython 3.2
from visual import *
earth = sphere(pos=vector(0,0,0), radius = 6371, color=color.cyan)
moon = sphere(pos=vector(0,38440,0), radius = 1737.4, color=color.white)
rocket = sphere(pos=vector(0,50+6371+500,0), radius = 500, color=color.red)
massEarth = (5.97219 * 10**24) #kg
massRocket = 173 #kg
massMoon = 7.34767309 * 10**22 #kg

forceRocketMoon
forceRocketMoon = ((6.67*10**-11)*(massRocket)*(massMoon))/(31519**2)
vForceRocketMoon = 

forceMoonEarth = ((6.67*10**-11)*(massEarth)*(massMoon))/(38440**2)
vForceMoonEarth = vector(0 ,-forceMoonEarth, 0)
t = 0
delta_t = 0.01

while t >= 0 and t <= 100

forceRocketEarth = ((6.67*10**-11)*(massRocket)*(massEarth))/(pos.x(rocket) - pos.x(earth) **2)
fnetRocket = forceRocketMoon + forceRocketEarth
rocketAcceleration = fnetRocket / massRocket
vRocket = vRocket + 
