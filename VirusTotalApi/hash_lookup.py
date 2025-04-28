import requests
import time

headers = {"accept":"application/json", "x-apikey":"7973af30c9f785c0f3b28cfc5b5fd401ba5a384dbd361909c82ff7aec868a572"}

line = ""

with open("list.txt","r") as file:
    with open("output.txt","w") as y:
        for x in file:
            hash = x.replace("\n","")
            url = "https://www.virustotal.com/api/v3/files/" + hash

            response = requests.get(url, headers = headers)

            output = response.json()
            
            try:
                line = hash + ":" + str(output['data']['attributes']['last_analysis_stats']['malicious']) + ":" + str(output['data']['attributes']['last_analysis_stats']['undetected']) + "\n"
                print(output['data']['attributes']['last_analysis_stats']['malicious'])
            except:
                line = hash + ":0\n"
            
            y.writelines([line])
            time.sleep(16)
            

