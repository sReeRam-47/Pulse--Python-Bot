import requests
from datetime import date

#weather
def get_weather(city="Thiruvanathapuram"):
  """Fetch today's weather as one-line text summary."""
  url=f"https://wttr.in/{city}?format=3
  try:
      response = requests.get(url, timeout=10)
      response.raise_for_status()
      
