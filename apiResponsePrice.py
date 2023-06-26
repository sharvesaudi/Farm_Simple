import requests

base_currency = 'INR'
# symbol = 'COCOA,'+'CORN,'+'COTTON' 
symbol = 'CORN'
endpoint = 'latest'
access_key = 'dwaf0qy9eves78kp1o7qj4j5f9fv25zw3cn7rhdbl2pn88t0rqsiaple5670'
link = 'https://commodities-api.com/api/open-high-low-close/2023-02-20'+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol
# link = 'https://commodities-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol


resp = requests.get(link)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /'+endpoint+'/ {}'.format(resp.status_code))
print(resp.json())
