import requests
from time import sleep

apiKey = input("Api key: ")
print("")

print("Getting data...")
data = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey).json()['products']
print("Done.")

print("")
print("Please read notes.txt")
print("")
sleep(1)

buyPrices = {}
buyOrderAmounts = {}
sellPrices = {}
sellOrderAmounts = {}
for item in data:
    buyPrices[item] = round(data[item]["quick_status"]["buyPrice"],1)
    buyOrderAmounts[item] = data[item]["quick_status"]["buyOrders"]
    sellPrices[item] = round(data[item]["quick_status"]["sellPrice"], 1)
    sellOrderAmounts[item] = data[item]["quick_status"]["sellOrders"]

difs = {}
for item in buyPrices.keys():
    difs[item] = buyPrices[item] - sellPrices[item]

print("")
print("In order of most to least price gap:")
sleep(0.5)
for i in sorted(difs.items(), key=lambda x: x[1], reverse=True):
    print(i)

end = input("")
