readableToCypher = {"A":"13",
                    "B":"14",
                    "C":"21",
                    "D":"23",
                    "E":"24",
                    "F":"312",
                    "G":"31",
                    "H":"121",
                    "I":"123",
                    "J":"124",
                    "K":"134",
                    "L":"4",
                    "M":"141",
                    "N":"213",
                    "O":"342",
                    "P":"414",
                    "Q":"12",
                    "R":"423",
                    "S":"43",
                    "T":"42",
                    "U":"41",
                    "V":"32",
                    "W":"3",
                    "X":"431",
                    "Y":"2",
                    "Z":"1",
                    "_":"212"}
cypherToReadable = {}
for r in readableToCypher.keys():
    cypherToReadable[readableToCypher[r]] = r


