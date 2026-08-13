from pathlib import Path

OUTPUT = Path("info-card.svg")

svg = """<svg xmlns="http://www.w3.org/2000/svg"
width="490" height="360" viewBox="0 0 490 360">

<rect x="5" y="5" width="480" height="350"
      rx="12" fill="#0d1117"
      stroke="#30363d" stroke-width="2"/>

<rect x="5" y="5" width="480" height="35"
      rx="12" fill="#161b22"/>

<circle cx="25" cy="22" r="6" fill="#ff5f56"/>
<circle cx="45" cy="22" r="6" fill="#ffbd2e"/>
<circle cx="65" cy="22" r="6" fill="#27c93f"/>

<g font-family="Courier New, monospace">

<text x="90" y="27" font-size="12" fill="#8b949e">
tushar@github ~
</text>

<text x="25" y="70" font-size="18"
      font-weight="bold" fill="#58a6ff">
$ whoami
</text>

<text x="25" y="105" font-size="18"
      font-weight="bold" fill="#f0f6fc">
TUSHAR WAGADRE
</text>

<text x="25" y="135" font-size="14"
      font-weight="bold" fill="#8b949e">
ROLE
</text>

<text x="135" y="135" font-size="14" fill="#f0f6fc">
CSE • Data Science
</text>

<text x="25" y="165" font-size="14"
      font-weight="bold" fill="#8b949e">
LANGUAGES
</text>

<text x="135" y="165" font-size="14" fill="#f0f6fc">
Python • SQL • C++
</text>

<text x="25" y="195" font-size="14"
      font-weight="bold" fill="#8b949e">
DATA
</text>

<text x="135" y="195" font-size="14" fill="#f0f6fc">
Pandas • NumPy • Power BI
</text>

<text x="25" y="225" font-size="14"
      font-weight="bold" fill="#8b949e">
ML
</text>

<text x="135" y="225" font-size="14" fill="#f0f6fc">
Scikit-learn • TensorFlow
</text>

<text x="25" y="255" font-size="14"
      font-weight="bold" fill="#8b949e">
DATABASE
</text>

<text x="135" y="255" font-size="14" fill="#f0f6fc">
MySQL • PostgreSQL
</text>

<text x="25" y="285" font-size="14"
      font-weight="bold" fill="#8b949e">
CLOUD
</text>

<text x="135" y="285" font-size="14" fill="#f0f6fc">
AWS
</text>

<text x="25" y="315" font-size="14"
      font-weight="bold" fill="#8b949e">
FOCUS
</text>

<text x="135" y="315" font-size="14" fill="#f0f6fc">
ML • Cloud • Open Source
</text>

<text x="25" y="340" font-size="14" fill="#58a6ff">
█
</text>

</g>
</svg>
"""

OUTPUT.write_text(svg, encoding="utf-8")

print("Created info-card.svg")