import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler
from urllib.parse import quote

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # YOUR REAL AMAZON TAG
        AMAZON_TAG = "timevalue0e2-20"
        
        hour = datetime.now().hour
        
        # Real products with REAL Amazon search terms
        if hour < 12:
            phase = "PRE-MATCH"
            product = "FIFA World Cup Official Ball"
            search_term = "FIFA+World+Cup+Official+Match+Ball"
            message = "Match starting soon! Get the official ball now."
            color = "#ff4757"
        elif hour < 18:
            phase = "LIVE NOW"
            product = "Samsung 75-Inch 4K Smart TV"
            search_term = "Samsung+75+Inch+Class+QLED+4K+Smart+TV"
            message = "Live match! Upgrade to crystal clear 4K viewing."
            color = "#2ed573"
        else:
            phase = "POST-MATCH"
            product = "Official FIFA Jersey"
            search_term = "Official+FIFA+World+Cup+Jersey+2026"
            message = "Match ended! Celebrate with official merchandise."
            color = "#ffa502"
        
        # REAL AMAZON AFFILIATE LINK WITH YOUR TAG
        amazon_url = f"https://www.amazon.com/s?k={search_term}&tag={AMAZON_TAG}"
        
        # Check if API request
        if 'api' in self.path or self.path == '/api':
            response_data = {
                "status": "REAL_DATA",
                "phase": phase,
                "product": product,
                "message": message,
                "amazon_link": amazon_url,
                "your_affiliate_tag": AMAZON_TAG,
                "verification": "This is a REAL Amazon affiliate link with your tag"
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response_data, indent=2).encode('utf-8'))
        else:
            # HTML Page
            html = f'''<!DOCTYPE html>
<html>
<head>
    <title>FIFA Live Deals - {phase}</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            background: #0f0f0f; 
            color: white; 
            margin: 0; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            min-height: 100vh; 
        }}
        .card {{ 
            background: #1a1a1a; 
            padding: 50px; 
            border-radius: 20px; 
            text-align: center; 
            max-width: 600px; 
            border: 3px solid {color};
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        }}
        .badge {{ 
            background: {color}; 
            color: black; 
            padding: 12px 30px; 
            border-radius: 25px; 
            font-weight: bold; 
            display: inline-block; 
            margin-bottom: 25px;
            font-size: 16px;
        }}
        h1 {{ margin: 15px 0; font-size: 32px; }}
        p {{ color: #ccc; margin: 20px 0; font-size: 18px; line-height: 1.5; }}
        .btn {{ 
            display: inline-block; 
            background: #ff9900; 
            color: black; 
            padding: 20px 40px; 
            text-decoration: none; 
            border-radius: 10px; 
            font-weight: bold; 
            margin-top: 30px;
            font-size: 20px;
            transition: transform 0.2s;
        }}
        .btn:hover {{ transform: scale(1.05); }}
        .tag-info {{
            margin-top: 30px;
            padding: 15px;
            background: #2a2a2a;
            border-radius: 8px;
            font-size: 14px;
            color: #888;
        }}
        .tag-info code {{
            background: #333;
            padding: 3px 8px;
            border-radius: 4px;
            color: #2ed573;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">{phase}</div>
        <h1>{product}</h1>
        <p>{message}</p>
        <a href="{amazon_url}" class="btn" target="_blank">Buy on Amazon</a>
        
        <div class="tag-info">
            <strong>Affiliate Tag:</strong> <code>{AMAZON_TAG}</code><br>
            <small>Every purchase through this link earns you commission</small>
        </div>
    </div>
</body>
</html>'''
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass
