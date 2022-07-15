from webserver import keep_alive
import requests

channelID = 924947607879569428
headers = {
    "authorization":
   "OTI1NjQ5Mzk3MTg5MDc5MDcw.GaHIyU.69LZNJrVQXahRZpCu8PKK27oiHT-Y_SsVaiJQ8"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
