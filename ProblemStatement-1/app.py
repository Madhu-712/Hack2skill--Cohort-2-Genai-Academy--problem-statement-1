from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Agent URL
AGENT_URL = "https://lookerstudio.google.com/conversation?agent=projects/notebooklm-491108/locations/us/dataAgents/agent_3ef6798f-065b-41d4-99c9-1a984d8d2076"

@app.get("/")
async def get_dashboard(request: Request, persona: str = "Traveler"):
    # You can pass different URLs or configurations based on the persona
    return templates.TemplateResponse(
    request=request, 
    name="dashboard.html", 
    context={
        "persona": persona, 
        "agent_url": AGENT_URL
    }
)
