import http.client

conn = http.client.HTTPSConnection("football98.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "d4426bcb7cmsh05fcca96e5d06f4p1d374fjsnf860e2247359",
    'x-rapidapi-host': "football98.p.rapidapi.com"
}

conn.request("GET", "/premierleague/transfers", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))