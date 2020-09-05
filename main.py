import requests
from time import sleep

apiKey = input("Api key: ")
print("")

itemsList = [
    "NETHER_STALK",
    "NETHERRACK",
    "FEATHER",
    "COAL",
    "INK_SACK:4",
    "OBSIDIAN",
    "FLINT",
    "SLIME_BALL",
    "RAW_FISH:1",
    "RABBIT_FOOT",
    "SPIDER_EYE",
    "MAGMA_CREAM",
    "RABBIT",
    "ENCHANTED_RABBIT_FOOT",
    "RAW_FISH:3",
    "ENCHANTED_PUFFERFISH",
    "GOLD_INGOT",
    "ENCHANTED_GOLD",
    "ENCHANTED_GOLD_BLOCK",
    "SUGAR_CANE",
    "ENCHANTED_SUGAR",
    "ENCHANTED_SUGAR_CANE",
    "MELON",
    "ENCHANTED_MELON",
    "ENCHANTED_GLISTERING_MELON",
    "BLAZE_ROD",
    "ENCHANTED_BLAZE_POWDER",
    "ENCHANTED_BLAZE_ROD",
    "GHAST_TEAR",
    "ENCHANTED_GHAST_TEAR"
]
xpAmount = {
    "NETHER_STALK":5,
    "NETHERRACK":5,
    "FEATHER":10,
    "COAL":5,
    "INK_SACK:4":5,
    "OBSIDIAN":15,
    "FLINT":10,
    "SLIME_BALL":10,
    "RAW_FISH:1":20,
    "RABBIT_FOOT":12,
    "SPIDER_EYE":10,
    "MAGMA_CREAM":10,
    "RABBIT":10,
    "ENCHANTED_RABBIT_FOOT":-1,
    "RAW_FISH:3":12,
    "ENCHANTED_PUFFERFISH":600,
    "GOLD_INGOT":5,
    "ENCHANTED_GOLD":300,
    "ENCHANTED_GOLD_BLOCK":15000,
    "SUGAR_CANE":5,
    "ENCHANTED_SUGAR":300,
    "ENCHANTED_SUGAR_CANE":15000,
    "MELON":10,
    "ENCHANTED_MELON":250,
    "ENCHANTED_GLISTERING_MELON":500,
    "BLAZE_ROD":20,
    "ENCHANTED_BLAZE_POWDER":500,
    "ENCHANTED_BLAZE_ROD":23000,
    "GHAST_TEAR":30,
    "ENCHANTED_GHAST_TEAR":100
}

print("Getting data...")
data = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + apiKey).json()['products']
print("Done.")

print("")
print("Please read notes.txt")
print("")
sleep(1)

prices = {}
for item in itemsList:
    buyPrice = data[item]["buy_summary"][0]["pricePerUnit"]
    print(item + " " + str(buyPrice))
    pricePerXp = round(buyPrice / xpAmount[item], 1)
    print("  > Price per alch xp: " + str(pricePerXp))
    prices[item] = str(pricePerXp)

print("")
print("In order of cheapest to most expensive:")
for i in sorted(prices.items(), key=lambda x: x[1], reverse=True):
    print(i)

end = input("")
