"""Idempotent Prove2Me submission helper. Credentials stay in memory."""
import json,pathlib,sys,urllib.request,urllib.error,time,uuid
ROOT=pathlib.Path(__file__).parent
STATE=ROOT/'Verification/platform_actions.json'
BASE='https://prove2.me/api/v1'
opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
creds=json.loads(pathlib.Path(r'D:\users\self_projects\prove2me_workspace\credentials.json').read_text(encoding='utf8'))
def req(method,path,data=None,raw=None,ctype='application/json',auth=True):
    body=raw if raw is not None else json.dumps(data).encode() if data is not None else None
    headers={'Content-Type':ctype}
    if auth:headers['Authorization']='Bearer '+token
    r=urllib.request.Request(BASE+path,data=body,headers=headers,method=method)
    with opener.open(r,timeout=120) as response:return json.load(response)
token=creds.get('access_token')
if not token or creds.get('expires_at',0)<time.time()+120:
    fresh=req('POST','/agent/refresh',{'api_key':creds['api_key']},auth=False)
    token=fresh.get('access_token') or fresh.get('token')
    print('Server version',fresh.get('version'),flush=True)
state=json.loads(STATE.read_text(encoding='utf8')) if STATE.exists() else {}
def save():STATE.write_text(json.dumps(state,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
action=sys.argv[1]
if action=='get':
    obj=req('GET',sys.argv[2]);dest=ROOT/'Verification'/sys.argv[3];dest.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf8');print(json.dumps(obj,ensure_ascii=True)[:2000]);sys.exit()
key=sys.argv[2]
if key in state:
    print(json.dumps(state[key],ensure_ascii=True)[:2000]);sys.exit()
if action=='json':
    path=sys.argv[3];data=json.loads((ROOT/sys.argv[4]).read_text(encoding='utf8'))
    state[key]={'started_at':time.time(),'endpoint':path};save()
    result=req('POST',path,data)
elif action=='verify':
    tid=sys.argv[3];name=sys.argv[4]
    boundary='----ProofBoundary'+uuid.uuid4().hex
    fields={'theorem_id':tid,'proof_type':'prove','explanation':(ROOT/'Platform'/f'{name}_explanation.txt').read_text(encoding='utf8')}
    parts=[]
    for k,v in fields.items():parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="solution.lean"\r\nContent-Type: text/plain\r\n\r\n'.encode())
    parts.append((ROOT/'Platform'/f'{name}_solution.lean').read_bytes());parts.append(f'\r\n--{boundary}--\r\n'.encode())
    state[key]={'started_at':time.time(),'endpoint':'/verify','theorem_id':tid};save()
    result=req('POST','/verify',raw=b''.join(parts),ctype='multipart/form-data; boundary='+boundary)
else:raise SystemExit('Unknown action')
state[key]['response']=result;state[key]['finished_at']=time.time();save()
print(json.dumps(result,ensure_ascii=True)[:2500])
