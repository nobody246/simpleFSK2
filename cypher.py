readableToCypher = {"1":"1",
                    "2":"2",
                    "3":"3",
                    "4":"32",
                    "5":"41",
                    "6":"42",
                    "7":"43",
                    "8":"34",
                    "9":"12",
                    "A":"13",
                    "B":"14",
                    "C":"21",
                    "D":"23",
                    "E":"24",
                    "F":"31"}
cypherToReadable = {}
for r in readableToCypher.keys():
    cypherToReadable[readableToCypher[r]] = r


