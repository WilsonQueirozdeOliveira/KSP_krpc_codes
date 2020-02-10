#!/usr/bin/env python2

import krpc
import time
import os

def main():
    connect_server()
    active_vessel()
    get_flight_info()
    start_clock()
    cycle()

def cycle():
    print("start!")
    
    vessel.auto_pilot.target_pitch_and_heading(90,90)
    vessel.auto_pilot.engage()
    vessel.auto_pilot.disengage()
    vessel.control.sas=True
    #vessel.control.sas_mode = conn.space_center.SASMode.stability_assist
    vessel.control.sas_mode = conn.space_center.SASMode.radial
    time.sleep(1)
    #vessel.control.sas=False
    
    while True:
        def_clock()
        def_screen()
        mission()
        if clock < 35.5 and clock > 35.0:
            vessel.control.throttle=0.0
            break

def mission():
    if clock < 5.5 and clock > 5.0:
        vessel.control.throttle=0.5
        vessel.control.activate_next_stage()
    if clock < 10.5 and clock > 10.0:
        vessel.control.throttle=0.41        

def connect_server():
    global conn
    #localhost
    #conn = krpc.connect(name='main')
    #localhost
    
    #server'192.168.56.1'
    conn = krpc.connect(name= 'main',address='192.168.0.104',
    rpc_port=50000, stream_port=50001)
    #sever

    print(conn.krpc.get_status().version)

def active_vessel():
    global vessel
    vessel = conn.space_center.active_vessel
    print(vessel.name)
    time.sleep(4)

def get_flight_info():
    global flight_info
    flight_info = vessel.flight()

def start_clock():
    global time_0
    time_0 = time.time()

def def_clock():
    global clock
    clock = time.time() - time_0
    global seconds
    seconds = int(clock)

def def_screen():
    if not int((clock-seconds)*10):
        os.system('cls' if os.name == 'nt' else 'clear')#windows linux
        print "clock:",seconds      
        flight_info.mean_altitude
        print "altitude(M):",flight_info.mean_altitude

        thrust = vessel.thrust
        print "thrust(N):",thrust
        max_thrust = vessel.max_thrust
        print "max thrust(N):",max_thrust

        g_force = flight_info.g_force
        print "G_Force(g):",g_force
            

if __name__ == '__main__':
    main()