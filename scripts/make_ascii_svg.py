from pathlib import Path

OUTPUT = Path("ascii-portrait.svg")

svg = """<svg xmlns="http://www.w3.org/2000/svg"
width="370" height="360" viewBox="0 0 370 360">

<style>
    .terminal {
        font-family: "Courier New", monospace;
    }

    .line {
        opacity: 0;
        animation: typeIn 0.6s ease forwards;
    }

    @keyframes typeIn {
        from {
            opacity: 0;
            transform: translateX(-12px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    .cursor {
        animation: blink 1s step-end infinite;
    }

    @keyframes blink {
        50% {
            opacity: 0;
        }
    }
</style>

<rect
    x="5"
    y="5"
    width="360"
    height="350"
    rx="12"
    fill="#0d1117"
    stroke="#30363d"
    stroke-width="2"/>

<rect
    x="5"
    y="5"
    width="360"
    height="35"
    rx="12"
    fill="#161b22"/>

<circle cx="25" cy="22" r="6" fill="#ff5f56"/>
<circle cx="45" cy="22" r="6" fill="#ffbd2e"/>
<circle cx="65" cy="22" r="6" fill="#27c93f"/>

<g class="terminal">

<text
    x="25"
    y="70"
    fill="#58a6ff"
    font-size="15"
    class="line"
    style="animation-delay:0.2s">
    TUSHAR@GITHUB
</text>

<text
    x="25"
    y="95"
    fill="#8b949e"
    font-size="12"
    class="line"
    style="animation-delay:0.5s">
    ─────────────────────────────
</text>

<text
    x="45"
    y="130"
    fill="#39d353"
    font-size="16"
    class="line"
    style="animation-delay:0.8s">
    &lt; / &gt;
</text>

<text
    x="25"
    y="165"
    fill="#f0f6fc"
    font-size="15"
    class="line"
    style="animation-delay:1.1s">
    DATA SCIENCE
</text>

<text
    x="25"
    y="195"
    fill="#f0f6fc"
    font-size="15"
    class="line"
    style="animation-delay:1.4s">
    MACHINE LEARNING
</text>

<text
    x="25"
    y="225"
    fill="#f0f6fc"
    font-size="15"
    class="line"
    style="animation-delay:1.7s">
    CLOUD COMPUTING
</text>

<text
    x="25"
    y="265"
    fill="#8b949e"
    font-size="12"
    class="line"
    style="animation-delay:2.0s">
    Python • SQL • C++
</text>

<text
    x="25"
    y="290"
    fill="#8b949e"
    font-size="12"
    class="line"
    style="animation-delay:2.3s">
    AWS • ML • PostgreSQL
</text>

<text
    x="25"
    y="325"
    fill="#58a6ff"
    font-size="13"
    class="line"
    style="animation-delay:2.6s">
    $ keep_building
</text>

<text
    x="150"
    y="325"
    fill="#39d353"
    font-size="13"
    class="cursor"
    style="animation-delay:2.6s">
    █
</text>

</g>

</svg>
"""

OUTPUT.write_text(svg, encoding="utf-8")

print("Created ascii-portrait.svg")