import wiotp.sdk.device
import time
import random
import requests, json
myConfig = { 
    "identity": {
        "orgId": "z33zfc",
        "typeId": "ESP32",
        "deviceId":"81795"
    },
    "auth": {
        "token": "12345678"
    }
}
api_key = "902856e07c32938df0024a47e76f9ae4"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
   if x["cod"] != "404":
  
    # store the value of "main"
    # key in variable y
        y = x["main"]
  
    # store the value corresponding
    # to the "temp" key of y
        current_temperature = y["temp"]
  
    # store the value corresponding
    # to the "pressure" key of y
        current_pressure = y["pressure"]
      
    # store the value corresponding
    # to the "humidity" key of y
        current_humidiy = y["humidity"]
  
    # store the value of "weather"
    # key in variable z
        z = x["weather"]
  
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z
        weather_description = z[0]["description"]
        visibility=x["visibility"]
    # print following values
       
        
    
        myData={'temp':current_temperature, 'humidity':current_humidiy,'pressure':current_pressure,
                'visibility':visibility,'description':weather_description}
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(2)
client.disconnect()
