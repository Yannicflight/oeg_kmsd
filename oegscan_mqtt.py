#!/usr/bin/python3
#

oeg_dict = {

	38:"",	#T1
	39:"",	#T2
	40:"",	#T3
	58:"",	#Pump modulation 0-100%
	}
	
import minimalmodbus
import serial
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

instrument = minimalmodbus.Instrument('COM3', 128, minimalmodbus.MODE_ASCII) # port name, slave address (in decimal) 
#Change the COM port above to the OEG Usb comport or USB address on Linux.
instrument.serial.baudrate = 9600   # Baud
instrument.serial.parity = serial.PARITY_EVEN
instrument.serial.bytesize = 7
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.05	# seconds

broker = 'BROKER_IP_ADDRESS'						# Fill in your MQTT broker IP-address
state_topic = 'home-assistant/oeg/OegT1'
delay = 5

# Send messages in a loop
client = mqtt.Client("ha-client")
client.username_pw_set("MQTT_USERNAME", "MQTT_PASSWORD") 		# Fill in your MQTT credentials
client.connect(broker)
client.loop_start()

while True:
  state_topic = "home-assistant/oeg/OegT1" + oeg_dict[38]
  client.publish(state_topic, instrument.read_register(38,1,3,signed=True))
  state_topic = "home-assistant/oeg/OegT2" + oeg_dict[39]
  client.publish(state_topic, instrument.read_register(39,1,3,signed=True))
  state_topic = "home-assistant/oeg/OegT3" + oeg_dict[40]
  client.publish(state_topic, instrument.read_register(40,1,3,signed=True))
  state_topic = "home-assistant/oeg/Oegpomp" + oeg_dict[58]
  client.publish(state_topic, instrument.read_register(58,0,3,signed=True))
  time.sleep(delay)
