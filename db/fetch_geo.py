#!/usr/bin/python3
"""Fetch African countries and cities data by web scrapping"""
from db import storage
from db.models.country import Country
from db.models.city import City
from requests import get

if __name__ == '__main__':
    #  Retrieve countries

    url = 'http://api.geonames.org/countryInfoJSON?'
    url += 'formatted=true&lang=en&username=youssef070222&style=full'
    response = get(url)
    countries = response.json()['geonames']
    african_countries = list(filter(lambda c: c['continent'] == 'AF',
                                    countries))

    african_countries_names = []
    for african_country in african_countries:
        name = african_country['countryName']
        if name.startswith('The '):
            name = name[4:]
        if name == 'Western Sahara':
            continue
        african_countries_names.append(name)

    african_countries_names.sort()

    for name in african_countries_names:
        country = Country(name=name)
        storage.add(country)

    storage.commit()

    #  Retrieve cities

    response = get('https://countriesnow.space/api/v0.1/countries')
    countries_and_cities = response.json()['data']
    for ctr in countries_and_cities:
        if ctr['country'] in african_countries_names:
            country = list(filter(lambda c: c.name == ctr['country'],
                                  storage.all('Country')))[0]
            for city_name in list(set(ctr['cities'])):
                if len(city_name) > 49:
                    continue
                city = City(name=city_name, country_id=country.id)
                storage.add(city)

    storage.commit()

#    countries = storage.all('Country')
#
#    for ctr in countries:
#        print('Country :', ctr.name, '->')
#        for city in ctr.cities:
#            print('\t', city.name)
#        print()
