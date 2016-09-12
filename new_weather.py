#weather.py
# -*- coding: utf-8 -*-

import forecastio
import os
from geopy.geocoders import Nominatim

#from dotenv import load_dotenv, find_dotenv

#load_dotenv(find_dotenv())





def get_weather(address):
	api_key = os.environ['API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	summary = forecast.summary
	temperature = forecast.temperature
	return "{} and {}° in {}".format(summary, temperature, address)

#print(get_weather(address, api_key))