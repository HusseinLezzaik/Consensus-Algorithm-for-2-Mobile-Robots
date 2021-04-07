"""
Control Initial Position of two robots using Python Remote API 

@author: hussein
"""

import sim
import time 
import math
import numpy as np
print("Program Started")

" Control to V-Rep "

sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19997,True,True,-500000,5) # Connect to CoppeliaSim

iter = 1
x_disp = np.array([[0], [1]])
y_disp = np.array([[0], [1]])
z_rot =  np.array([[0], [90]])

if clientID!=-1:
    print ('Connected to remote API server')
    for z in z_rot:
        for x in x_disp:
            for y in y_disp:
                print(" Simulation ", iter)
                
                # Start the simulation:
                sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot_wait)
                
                
                # Retrieve some handles:
                
                ErrLocM1,LocM1 =sim.simxGetObjectHandle(clientID, 'CoppeliaSim_Two_Robots_Scenes', sim.simx_opmode_oneshot_wait)
                ErrLocM2,LocM2 =sim.simxGetObjectHandle(clientID, 'CoppeliaSim_Two_Robots_Scenes', sim.simx_opmode_oneshot_wait)
                
                
                ErrLoc1,Loc1 =sim.simxGetObjectPosition(clientID, LocM1, -1, sim.simx_opmode_oneshot_wait)
                ErrLoc2,Loc2 =sim.simxGetObjectPosition(clientID, LocM2, -1, sim.simx_opmode_oneshot_wait)
                
                
                ErrLocO1,OriRobo1 =sim.simxGetObjectOrientation(clientID,LocM1, -1, sim.simx_opmode_oneshot_wait)
                ErrLocO2,OriRobo2 =sim.simxGetObjectOrientation(clientID,LocM2, -1, sim.simx_opmode_oneshot_wait)
                
                
                OriRobo1[0] = ((z*math.pi)/180)
                OriRobo2[0] = ((z*math.pi)/180)
                
                
                # Set Robot Orientation
                
                sim.simxSetObjectOrientation(clientID, LocM1, -1, OriRobo1, sim.simx_opmode_oneshot_wait) 
                sim.simxSetObjectOrientation(clientID, LocM2, -1, OriRobo2, sim.simx_opmode_oneshot_wait)
                
                
                Loc1[0] = x
                Loc2[0] = x
                
                
                Loc1[1] = y
                Loc2[1] = y
                
                # Set Robot Position
                
                sim.simxSetObjectPosition(clientID, LocM1, -1, Loc1, sim.simx_opmode_oneshot)
                sim.simxSetObjectPosition(clientID, LocM2, -1, Loc2, sim.simx_opmode_oneshot)
                
                # Start the Simulation
                
                print("Robot1 Position:", Loc1)
                print("Robot2 Position:", Loc2)
                
                print("Robot1 Orientation:", OriRobo1)
                print("Robot2 Orientation:", OriRobo2)
                
                
                
                print("Simulation Running ...")
                sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot_wait)
                time.sleep(5)
                sim.simxStopSimulation(clientID, sim.simx_opmode_oneshot_wait)
                iter += 1
                
                # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
                sim.simxGetPingTime(clientID)

                # End Connection to V-Rep
                sim.simxFinish(clientID)


else:
    print("Failed connecting to remote API server") 
print("Program Ended")
