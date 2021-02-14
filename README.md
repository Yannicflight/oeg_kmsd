# oeg_kmsd - Home assistant

ced2git, thanks allot for figuring out and publishing the OEG Modbus protocol!

The python script is tested and working with Home-assistant and the standard Mosquitto MQTT broker.

## On the PC or PI connected to KSMd:
- Make sure to fill in your broker IP-address, username and password.
- Make sure to fill in the com port or /dev/ttyusb of your KSMd USB connection.
- Use PIP to install pyserial (NOT SERIAL!):  pip install pyserial
- Use PIP to install Paho MQTT:               pip install paho-mqtt

## Home assistant:
- Copy and add the lines in the configuration.yaml file below the "sensors" part in your home-assistants configuration.yaml file.
- Copy the lines of entities.yaml to a new entity card



Original introduction by ced2git:

The KMS-D+ is  heating "controller" module that allow you to "upgrade" your old heating systems with a regulation based on 
on external temperatures. 

https://www.oeg.net/fr/r-gulation-de-chauffage-kms-d-212000040

The module do provide a mini USB interface exposing a series of sensors and settings that might be of an interest to collect
into a home automation software. 

Interface

The Miniusb interface on the KMS-D is based on the MODBUS ASCII protocol and emulate a serial interface.

The Serial parameters to iniate a connections are 

Baudrate :  9600
Parity : Even
Bytesize: 1

Protocol : MODBUS ASCII
Register address: 128 (hex 0x80)
Holding Register: Type 3

Register 

.... Work in progress .....

While the OEG will answer a series of register from 1 to 1000, intersting values are between 1 and 60. I've not figure out all
of the them but here are the most important ones: 

Please refer to the KMS-D manuel (available on their web sites) to understand the various sensor and limits 

Register:Value

38:T1 Sensor
39:T2 Sensor
40:T3 Sensor
41: T4 Sensor
42: T5 Sensor
47: Planning 
49: T1 Limit
50: T2 limit
51: T3 Limit
52: T4 Limit
53: T5 Limit
58: Planning
59: TD2

Based on the instruction manual and some screenshot of the software sold by OEG, i understnad that there probably ways to 
progrma the KMS-D or at least to overide the current planning. I haven't yet, how it works. 

Small sample

I've done a small sample to extract the Modbus informations and publish them on a MQTT broker. This is enough for me 
to monitor the KMS-D. 


