"""Serve the actual generated static build and record HTTP status evidence."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import time

WORKSPACE=Path(__file__).resolve().parents[1]
PUBLIC=WORKSPACE / 'vercel-deploy/public'
LOG=WORKSPACE / 'tools/web-support/http-requests.jsonl'
LOG.parent.mkdir(parents=True, exist_ok=True)

class Handler(SimpleHTTPRequestHandler):
    extensions_map={**SimpleHTTPRequestHandler.extensions_map,'.wasm':'application/wasm','.data':'application/octet-stream'}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,directory=str(PUBLIC),**kwargs)
    def log_request(self,code='-',size='-'):
        with LOG.open('a',encoding='utf-8') as f:
            f.write(json.dumps(dict(time=time.time(),path=self.path,status=code,size=size))+'\n')
    def end_headers(self):
        self.send_header('Cache-Control','no-cache')
        super().end_headers()

print('Serving real RenPy Web build at http://127.0.0.1:8042',flush=True)
ThreadingHTTPServer(('127.0.0.1',8042),Handler).serve_forever()
