from urllib.parse import unquote_plus as decodeUrl

def decodeData(dataString):
    dataLines = dataString.split('&')
    data = {}

    for dataLine in dataLines:
        dataKey, dataValue = dataLine.split('=')
        dataKey = decodeUrl(dataKey)
        dataValue = decodeUrl(dataValue)
        
        data[dataKey] = dataValue

    return data
