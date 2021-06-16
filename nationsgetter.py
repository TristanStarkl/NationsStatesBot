import requests

def get_all_nations():
	NATION_STATE_API = "https://www.nationstates.net/cgi-bin/api.cgi?nation="
	user_agent = {'User-agent': 'email=thomas.rety57@gmail.com'}

	list_of_nations = [
		"avarsan",
		"allortators",
		"balante",
		"khuravia",
		"progravie",
		"eoliria",
		"khalikistan",
		"villeplanche",
		"TRISIKISTAN"
	]
	castor = ""
	for nation in list_of_nations:
		text = requests.get(NATION_STATE_API + nation + "&q=gdp+richest+poorest+income+majorindustry+population", headers=user_agent)
		castor += text.text 
		castor += "\n"
	return castor