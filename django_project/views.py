import requests
from django.shortcuts import render
def home(request):
  return render(request, 'templates/index.html')
  #USING APIS Example1
  response2 = requests.get('https://api.github.com/events')
  data2 = response.json()
  result2 = data2[0]["coord"]
  return render(request, 'index.html', {'result': result, 'result2': result2})
  #USING APIS Example2
  response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Nairobi,Kenya&APPID=7d4945a212e3b7ef21aa0118352fbb34')