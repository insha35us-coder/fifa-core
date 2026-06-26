from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Route Logic: Frontend UI vs API vs Cron Tracker
        if self.path.startswith('/api'):
            if 'action=track' in self.path:
                self.handle_tracker()
            else:
                self.handle_api()
        else:
            self.handle_frontend()

    def get_real_context(self):
        tag = "timevalue0e2-20"
        hour = datetime.now().hour
        
        # Real Psychological Triggers based on Match Time
        if hour < 12:
            return {"phase": "PRE-MATCH HYPE", "product": "Official FIFA Match Ball", "query": "fifa+world+cup+official+match+ball", "hook": "⚽ Match Day! Feel the real grass. Get the Official Match Ball delivered before kickoff!", "color": "#ff4757"}
        elif hour < 18:
            return {"phase": "LIVE MATCH ADRENALINE", "product": "Samsung 75-Inch 4K QLED TV", "query": "samsung+75+inch+4k+qled+tv", "hook": "📺 LIVE NOW! Don't watch in blurry HD. Upgrade to 4K QLED and see every sweat drop!", "color": "#2ed573"}
        elif hour < 21:
            return {"phase": "HALFTIME / SOUND CHECK", "product": "Premium Home Theater Soundbar", "query": "premium+home+theater+soundbar+system", "hook": "🔊 Feel the stadium roar! Upgrade your sound system for the second half!", "color": "#1e90ff"}
        else:
            return {"phase": "AFTERPARTY & MERCH", "product": "Official National Team Jersey", "query": "official+fifa+national+team+jersey", "hook": "🏆 Match is over! Rep your team with the Official Authentic Jersey!", "color": "#ffa502"}

    def handle_frontend(self):
        ctx = self.get_real_context()
        link = f"https://www.amazon.com/s?k={ctx['query']}&tag={ctx['tag']}&ref=nb_sb_noss"
        
        # High-Converting Dark Mode UI
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>FIFA Live Hub - {ctx['phase']}</title>
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f0f0f; color: #fff; margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh; text-align: center; }}
                .card {{ background: #1a1a1a; padding: 40px; border-radius: 20px; max-width: 500px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #333; }}
                .badge {{ display: inline-block; padding: 8px 16px; border-radius: 50px; font-size: 14px; font-weight: bold; background: {ctx['color']}; color: #000; margin-bottom: 20px; animation: pulse 2s infinite; }}
                @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.6; }} 100% {{ opacity: 1; }} }}
                h1 {{ font-size: 28px; margin: 10px 0; }}
                p {{ color: #aaa; font-size: 18px; line-height: 1.5; margin-bottom: 30px; }}
                .btn {{ display: inline-block; background: #ff9900; color: #000; padding: 18px 36px; text-decoration: none; border-radius: 10px; font-weight: bold; font-size: 20px; transition: transform 0.2s; }}
                .btn:hover {{ transform: scale(1.05); }}
            </style>
        </head>
        <body>
            <div class="card">
                <span class="badge">{ctx['phase']}</span>
                <h1>{ctx['product']}</h1>
                <p>{ctx['hook']}</p>
                <a href="{link}" class="btn" target="_blank">🛒 Get It Now on Amazon</a>
            </div>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def handle_api(self):
        ctx = self.get_real_context()
        link = f"https://www.amazon.com/s?k={ctx['query']}&tag={ctx['tag']}&ref=nb_sb_noss"
        response = {"status": "LIVE", "phase": ctx['phase'], "hook": ctx['hook'], "product": ctx['product'], "buy_link": link, "tag": ctx['tag']}
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response, indent=2).encode('utf-8'))

    def handle_tracker(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = {"status": "CRON_SUCCESS", "time": timestamp, "tag": "timevalue0e2-20"}
        print(f"[TRACKER] {log}")
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(log).encode('utf-8'))
