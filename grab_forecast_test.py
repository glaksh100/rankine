
import requests

def get_raw_data_from_url()
	site='http://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml'
	page= requests.get(site)
	return page.text
get_raw_data_from_url()

