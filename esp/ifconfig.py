import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
print('sta_if %s'%str(sta_if.active()))
print('ap_if %s'%str(ap_if.active()))
print('ap ifconfig: %s'%str(ap_if.ifconfig()))
print('sta ifconfig: %s'%str(sta_if.ifconfig()))


