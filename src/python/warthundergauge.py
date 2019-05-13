from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://localhost:8111")
time.sleep(1)
while True:
    elements = driver.find_elements_by_id("state")
    for element in elements:
        print(element.id, element.text)
    time.sleep(1)



fields = {
"heading" : "stt-H, m", 
"TAS" : "stt-TAS, km/h",
"IAS" :"stt-IAS, km/h",
"" : "stt-M",
"AoA" : "stt-AoA, deg",
"" : "stt-AoS, deg",
"" : "stt-Ny",
"" : "stt-Vy, m/s",
"" : "stt-Wx, deg/s",
"" : "stt-Mfuel, kg",
"" : "stt-Mfuel0, kg",
"" : "stt-Mfuel 1, kg",
"" : "stt-Mfuel0 1, kg",
"" : "stt-undefined",
"" : "stt-Mfuel 2, kg",
"" : "stt-Mfuel0 2, kg",
"aileron" : "stt-aileron, %",
"elevator" : "stt-elevator, %",
"rudder" : "stt-rudder, %",
"flaps" : "stt-flaps, %",
"gear" : "stt-gear, %",
"airbrake" : "stt-airbrake, %"
}

template_engine_fields = {
"throttle" : "stt-throttle {}, %",
"RPM throttle" : "stt-RPM throttle {}, %",
"mixture" : "stt-mixture {}, %",
"radiator" : "stt-radiator {}, %",
"compressor" : "stt-compressor stage {}",
"magneto" : "stt-magneto {}",
"feathering" : "stt-feathered {}",
"power" : "stt-power {}, hp",
"RPM" : "stt-RPM {}",
"pressure" : "stt-manifold pressure {}, atm",
"water" : "stt-water temp {}, C",
"oil" : "stt-oil temp {}, C",
"prop pitch" : "stt-pitch {}, deg",
"thrust" : "stt-thrust {}, kgs",
"efficiency" : "stt-efficiency {}, %",
}

def get_engine_fields(iteration):
    fields = {}
    for k,v in template_engine_fields:
        fields[k] = v.format(iteration)
    return fields

engine_fields = [ get_engine_fields(i) for i in range(1,6) ]

def get_field(name, engine):
    if not engine:
        return fields[name]
    else
        return engine_fields[engine-1][name]





'''
stt-H, m
stt-TAS, km/h
stt-IAS, km/h
stt-M
stt-AoA, deg
stt-AoS, deg
stt-Ny
stt-Vy, m/s
stt-Wx, deg/s
stt-Mfuel, kg
stt-Mfuel0, kg
stt-Mfuel 1, kg
stt-Mfuel0 1, kg
stt-undefined
stt-Mfuel 2, kg
stt-Mfuel0 2, kg
stt-aileron, %
stt-elevator, %
stt-rudder, %
stt-flaps, %
stt-gear, %
stt-airbrake, %

REPEAT FOR EACH ENGINE, 1-4 (1-6?)
stt-throttle 1, %
stt-RPM throttle 1, %
stt-mixture 1, %
stt-radiator 1, %
stt-compressor stage 1
stt-magneto 1
stt-feathered 1
stt-power 1, hp
stt-RPM 1
stt-manifold pressure 1, atm
stt-water temp 1, C
stt-oil temp 1, C
stt-pitch 1, deg
stt-thrust 1, kgs
stt-efficiency 1, %
stt-throttle 1, %
'''
