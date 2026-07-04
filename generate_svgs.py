import os

svg_template = """<svg width="800" height="60" viewBox="0 0 800 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D4AF37"/>
      <stop offset="50%" stop-color="#FFF0A8"/>
      <stop offset="100%" stop-color="#D4AF37"/>
    </linearGradient>
  </defs>
  <text x="400" y="40" font-family="'Georgia', serif" font-size="28" font-weight="bold" fill="url(#gold)" text-anchor="middle" letter-spacing="6">
    {text}
  </text>
</svg>"""

hero_template = """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D4AF37"/>
      <stop offset="50%" stop-color="#FFF0A8"/>
      <stop offset="100%" stop-color="#AA7C11"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <text x="400" y="130" font-family="'Georgia', serif" font-size="65" font-weight="bold" fill="url(#gold)" text-anchor="middle" filter="url(#glow)" letter-spacing="6">
    LEELA PRASATH S
  </text>
  <text x="400" y="180" font-family="'Courier New', monospace" font-size="18" font-weight="normal" fill="#F3E5AB" text-anchor="middle" letter-spacing="8">
    AGENTIC AI ENGINEER
  </text>
</svg>"""

footer_template = """<svg width="800" height="150" viewBox="0 0 800 150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D4AF37"/>
      <stop offset="50%" stop-color="#FFF0A8"/>
      <stop offset="100%" stop-color="#AA7C11"/>
    </linearGradient>
  </defs>
  <text x="400" y="80" font-family="'Georgia', serif" font-size="22" font-weight="bold" fill="url(#gold)" text-anchor="middle" letter-spacing="8">
    B U I L D I N G   T H E   F U T U R E
  </text>
</svg>"""

os.makedirs('assets', exist_ok=True)

headers = {
    "intro": "I N T R O D U C T I O N",
    "arsenal": "T H E   A R S E N A L",
    "projects": "C O R E   P R O J E C T S",
    "metrics": "M E T R I C S   &   I M P A C T",
    "trophies": "T R O P H I E S",
    "contributions": "C O N T R I B U T I O N S"
}

for name, text in headers.items():
    with open(f"assets/{name}.svg", "w") as f:
        f.write(svg_template.replace("{text}", text))

with open("assets/hero.svg", "w") as f:
    f.write(hero_template)

with open("assets/footer.svg", "w") as f:
    f.write(footer_template)

print("SVGs generated successfully.")
