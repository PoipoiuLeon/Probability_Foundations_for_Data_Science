#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

flights = pd.read_csv('flights.csv', index_col=False).dropna()

"""
# p(flight started in California)
num_flights_in_CA = (flights['ORIGIN_STATE_NM'] == 'California').sum()
total_flights = len(flights)
#print('p(flight started in California) = {}'.format(num_flights_in_CA / total_flights))

# p(flight started in X) for all states X
flight_states = flights.groupby('ORIGIN_STATE_NM')
num_flights_per_state = flight_states.size()
flight_state_prob = num_flights_per_state.apply(lambda num_flights: num_flights / total_flights)
#print(flight_state_prob)

#print(flight_state_prob.max())
#print(flight_state_prob.idxmax())
"""

# p(flight ended in New York | flight started in CA)
ca_start_ny_end = ((flights['ORIGIN_STATE_NM'] == 'California') & (flights['DEST_STATE_NM'] == 'New York')).sum()
ca_start = (flights['ORIGIN_STATE_NM'] == 'California').sum()
#print('p(flight ended in New York | flight started in CA) = {}'.format(ca_start_ny_end / ca_start))

# p(flight ended in Y | flight started in X) for all states X, Y
flight_states = flights.groupby('ORIGIN_STATE_NM')

# p(flight ended in Y and started in X)
num_flights_per_state = flight_states['DEST_STATE_NM'].value_counts()
state_counts = flight_states['DEST_STATE_NM'].count()

flight_dist = num_flights_per_state / state_counts

print(flight_dist['California']['New York'])
