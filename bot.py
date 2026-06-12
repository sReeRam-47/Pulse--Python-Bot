import requests
from datetime import date

#weather
def get_weather(city="Thiruvanathapuram"):
  """Fetch today's weather as one-line text summary."""
  url=f"https://wttr.in/{city}?format=3
  try:
      response = requests.get(url, timeout=10)
      response.raise_for_status()
      return response.text.strip()
  except Exception as e:
      return f"Weather unavailable ({e})"

#Quote
def get_quote():
    """Fetch a random motivational quote from Zen quotes."""
    url = "https://zenquotes.io/api/random"
    try:
       response = requests.get(url, timeout=10)
       response.raise_for_status()
       data = response.json()
       quote = data[0]["q"]
       author = data[0]["a"]
       return f'"{quote}" - {author}'
    except Exception as e:
       return f"Quote unavailable ({e})"

#summary
def build_summary():
    """Assemble the full daily summary from all data sources."""
    today = date.today().strftime("%A, %d %B %Y")
    weather=get_weather()
    quote = get_quote()
    
    summary= f"""
=========================
Pulse - Daily Summary 
{today}
=========================

WEATHER 
  {weather}
 TODAY'S QUOTE 
  {quote}

=========================
"""
   return summary 

#Run everything 
def run():
    """Main entry point. Called by GitHub Actions."""
    summary = build_summary()
    
    print(summary)
   
    with open("daily_summary.txt","w", encoding="utf-8") as f:
    f.write(summary)

    print("Pulse ran successfully.")

#Entry point guard
if__name__=="__main__":
   run()