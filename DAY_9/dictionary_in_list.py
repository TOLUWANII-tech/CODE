travel_log = [
    {
        'country': 'France',
        'visits': 12,
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
    }
]


def add_new_country(name, number_of_visits, cities_visited):
    travel_log.append(
        {
            'country': name,
            'visits': number_of_visits,
            'cities_visited': cities_visited,
        }
    )



add_new_country('Russia', 2, ['Moscow', 'Saint Petersburg'])
print(travel_log)