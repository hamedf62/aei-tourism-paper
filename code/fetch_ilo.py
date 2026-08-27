"""Fetch the ILOSTAT plumber CSV via headless Chrome, waiting out the Cloudflare check."""
import json, time, urllib.request, sys
import websocket

TARGET = sys.argv[1] if len(sys.argv) > 1 else "https://rplumber.ilo.org/data/indicator/?id=EMP_TEMP_SEX_ECO_RT_A&format=.csv&ref_area=USA"

with urllib.request.urlopen('http://localhost:9223/json', timeout=10) as r:
    tabs = json.loads(r.read())
page = [t for t in tabs if t['type'] == 'page'][0]
ws = websocket.create_connection(page['webSocketDebuggerUrl'], timeout=180)

_id = [0]
def send(method, params=None):
    _id[0] += 1
    ws.send(json.dumps({'id': _id[0], 'method': method, 'params': params or {}}))
    while True:
        msg = json.loads(ws.recv())
        if msg.get('id') == _id[0]:
            return msg

send('Page.enable')
send('Page.navigate', {'url': TARGET})
# poll until body contains CSV content, up to 90s (Cloudflare interstitial)
body = ''
for _ in range(45):
    time.sleep(2)
    r = send('Runtime.evaluate', {'expression': "document.body ? document.body.innerText.slice(0,200) : ''", 'returnByValue': True})
    body = r['result']['result'].get('value') or ''
    if body and 'security verification' not in body and 'Cloudflare' not in body and 'Just a moment' not in body:
        break
print("PREVIEW:", body[:200])
r = send('Runtime.evaluate', {'expression': "document.body ? document.body.innerText.length : 0", 'returnByValue': True})
total = r['result']['result'].get('value') or 0
out = []
CH = 200000
for off in range(0, min(total, 20000000), CH):
    r = send('Runtime.evaluate', {'expression': f"document.body.innerText.slice({off},{off+CH})", 'returnByValue': True})
    out.append(r['result']['result'].get('value') or '')
text = ''.join(out)
open('/root/aei-tourism-paper/data/raw/ilo_eco_share.csv', 'w').write(text)
print("LEN:", total, "saved:", len(text))
