image = "https://onboard.qualcomm.com/img/spotlight/alfonso-castellanos.jpg";

########### Python 2.7 #############
import http.client, urllib, base64,os

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': os.environ['APIKEY'],
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    # print("[Errno {0}] {1}".format(e.strerror))
    print ('The server couldn\'t fulfill the request.')
    if hasattr(e, 'reason'):   
    	print ('Reason: ', e.reason)
    if hasattr(e, 'code'):
    	print ('Reason: ', e.code)
    if hasattr(e, 'strerror'):    
    	print ('Reason: ', e.strerror)
    if hasattr(e, 'errno'):
        print ('Error code: ', e.errno)

####################################

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': '{string}',
})

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################