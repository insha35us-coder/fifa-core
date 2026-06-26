import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        tag = "timevalue0e2-20"
        hour = datetime.now().hour
        
        # Dynamic content based on time
        if hour < 12:
            phase = "PRE-MATCH"
            product = "FIFA Official Match Ball"
            query = "fifa+world+cup+official+ball"
            hook = "⚽ Match Day! Get the official ball before kickoff!"
            color = "#ff4757"
        elif hour < 18:
            phase = "LIVE NOW"
            product = "Samsung 75-Inch 4K TV"
            query = "samsung+75+inch+4k+tv"
            hook = "📺 Watch in crystal clear 4K! Upgrade now!"
            color = "#2ed573"
        else:
            phase = "POST-MATCH"
            product = "Official Team Jersey"
            query = "fifa+world+cup+jersey"
            hook = "🏆 Celebrate with official merch!"
            color = "#ffa502"
        
        amazon_link = f"https://www.amazon.com/s?k={query}&tag={tag}"
        
        # Check if API request or browser request
        if 'api' in self.path:
            # Return JSON for API
            response = {
                "status": "active",
                "phase": phase,
                "product": product,
                "hook": hook,
                "buy_link": amazon_link,
                "tag": tag
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            # Return HTML for browser
            html = f"""<!DOCTYPE html>
<html>
<head>
    <title>FIFA Live - {phase}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ font-family: Arial, sans-serif; background: #0f0f0f; color: white; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
        .card {{ background: #1a1a1a; padding: 40px; border-radius: 15px; text-align: center; max-width: 500px; border: 2px solid {color}; }}
        .badge {{ background: {color}; color: black; padding: 10px 20px; border-radius: 20px; font-weight: bold; display: inline-block; margin-bottom: 20px; }}
        h1 {{ margin: 10px 0; }}
        p {{ color: #aaa; margin: 20px 0; }}
        .btn {{ display: inline-block; background: #ff9900; color: black; padding: 15px 30px; text-decoration: none; border-radius: 8px; font-weight: bold; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">{phase}</div>
        <h1>{product}</h1>
        <p>{hook}</p>
        <a href="{amazon_link}" class="btn">🛒 Buy on Amazon</a>
    </div>
</body>
</html>"""
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())
