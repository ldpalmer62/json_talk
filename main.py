import network
import urequests
import ujson
import time
import sys

# ==== USER CONFIGURATION ====
WIFI_SSID = "lpnetiot"
WIFI_PASSWORD = "mondomom"
API_URL = "http://192.168.1.41:5000/api/payload"  # Replace with your API endpoint

# ==== CONNECT TO WIFI ====
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF) # Instantiate the network - WLAN class - network.STA_IF connect to upstream WiFi access point
    wlan.active(True) # Activate the network
    wlan.connect(ssid, password) # Connect the interface to the network

    print("Connecting to Wi-Fi...")
    timeout = 10  # seconds
    start_time = time.time()
    # if can't connect within 10 seconds, give up
    while not wlan.isconnected():
        if time.time() - start_time > timeout:
            print("Failed to connect to Wi-Fi.")
            sys.exit()
        time.sleep(0.5)

    print("Connected to Wi-Fi:", wlan.ifconfig())
    return wlan

# ==== SEND JSON PAYLOAD, save response ====
def send_json(url, mydata):
    try:
        headers = {"Content-Type": "application/json"}
        json_data = ujson.dumps(mydata)  # Convert dict to JSON string for microcontrollers
        response = urequests.post(url, data=json_data, headers=headers) 
        print("Status:", response.status_code)
        print("Response:", response.text)
        response.close()
    except Exception as e:
        print("Error sending JSON:", e)


# ==== MAIN PROGRAM ====
if __name__ == "__main__":
    wlan = connect_wifi(WIFI_SSID, WIFI_PASSWORD)
    mytemp = 4
    while mytemp <=10:
        payload = {
            #"device": "Raspberry Pi Pico W",
            "temperature": mytemp,
            #"status": "OK",
            "message": "Pico is OK"
         }
        mytemp += 1
        time.sleep(2)
        send_json(API_URL, payload)
