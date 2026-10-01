"""
Simple web form for Scholar Goals OutreachForge
"""

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI(title="Scholar Goals OutreachForge")

FORM_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Scholar Goals – OutreachForge</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 700px; margin: 40px auto; padding: 20px; background: #0f172a; color: #e2e8f0; }
        h1 { color: #38bdf8; }
        label { display: block; margin-top: 16px; font-weight: 600; }
        input, textarea { width: 100%; padding: 10px; margin-top: 6px; border-radius: 8px; border: 1px solid #334155; background: #1e293b; color: white; box-sizing: border-box; }
        button { margin-top: 20px; padding: 12px 24px; background: #38bdf8; color: #0f172a; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; }
        button:hover { background: #7dd3fc; }
        .result { margin-top: 30px; padding: 16px; background: #1e293b; border-radius: 8px; white-space: pre-wrap; }
        .agents { display: flex; flex-wrap: wrap; gap: 8px; margin: 16px 0; }
        .agent { background: #1e293b; padding: 6px 12px; border-radius: 20px; font-size: 14px; }
    </style>
</head>
<body>
    <h1>Scholar Goals – OutreachForge</h1>
    <p>Multi-agent academic outreach system</p>

    <div class="agents">
        <span class="agent">🕵️ Scout</span>
        <span class="agent">📚 Atlas</span>
        <span class="agent">✍️ Scribe</span>
        <span class="agent">🛡️ Sentinel</span>
        <span class="agent">📧 Courier</span>
        <span class="agent">📊 Oracle</span>
    </div>

    <form method="post" action="/run">
        <label>Universities or Research Topics (one per line)</label>
        <textarea name="seeds" rows="5" placeholder="MIT Computer Science\nStanford Artificial Intelligence\nprotocells">MIT Computer Science\nStanford Artificial Intelligence\nprotocells</textarea>

        <button type="submit">Run Agents</button>
    </form>

    RESULT_PLACEHOLDER
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return FORM_HTML.replace("RESULT_PLACEHOLDER", "")

@app.post("/run", response_class=HTMLResponse)
async def run_agents(seeds: str = Form(...)):
    seed_list = [s.strip() for s in seeds.strip().split("\n") if s.strip()]

    result_text = f"""<div class=\"result\"><strong>Input received:</strong>\n{chr(10).join('- ' + s for s in seed_list)}\n\nAgents that will run:\n1. Scout   → Find professors\n2. Atlas   → Get their recent papers\n3. Scribe  → Write personalized emails\n4. Sentinel→ Check compliance\n5. Courier → Prepare / send emails\n6. Oracle  → Analyze results\n\nStatus: Form is working.\nNext step: Connect real OpenAlex + LLM keys to activate full agents.</div>"""

    return FORM_HTML.replace("RESULT_PLACEHOLDER", result_text)

@app.get("/health")
async def health():
    return {"status": "ok", "agents": ["Scout", "Atlas", "Scribe", "Sentinel", "Courier", "Oracle"]}
