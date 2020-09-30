import io
import json
from os import path

import arrow
import requests

from commons.provider import get_logger, Provider, Status, ProviderException

logger = get_logger('meteoswiss')


class MeteoSwiss(Provider):
    provider_code = 'meteoswiss'
    provider_name = 'meteoswiss.ch'
    provider_url = 'https://www.meteoswiss.ch'

    def process_data(self):
        try:
            self.log.info('Processing MeteoSwiss data...')

            with open(path.join(path.dirname(__file__), 'meteoswiss/vqha69.json')) as in_file:
                descriptions = json.load(in_file)

            data_file = io.StringIO(requests.get('http://data.geo.admin.ch/ch.meteoschweiz.swissmetnet/VQHA69.csv',
                                                 headers={'Accept': '*/*', 'User-Agent': 'winds.mobi'},
                                                 timeout=(self.connect_timeout, self.read_timeout)).text)
            lines = data_file.readlines()
            keys = lines[2].strip().split('|')

            for line in lines[3:]:
                station_id = None
                try:
                    data = {}
                    for i, key in enumerate(keys):
                        values = line.strip().split('|')
                        if values[i] != '-':
                            data[key] = values[i]
                        else:
                            data[key] = None

                    description = descriptions[data['stn']]
                    station = self.save_station(
                        data['stn'],
                        description['name'],
                        description['name'],
                        description['location']['lat'],
                        description['location']['lon'],
                        Status.GREEN,
                        altitude=description['altitude'],
                        tz='Europe/Zurich')
                    station_id = station['_id']

                    key = arrow.get(data['time'], 'YYYYMMDDHHmm').timestamp

                    measures_collection = self.measures_collection(station_id)
                    new_measures = []

                    if not self.has_measure(measures_collection, key):
                        measure = self.create_measure(
                            key,
                            data['dkl010z0'],
                            data['fu3010z0'],
                            data['fu3010z1'],
                            temperature=data['tre200s0'],
                            humidity=data['ure200s0'],
                            pressure=data['prestas0'],
                            rain=data['rre150z0'],
                        )
                        new_measures.append(measure)

                    self.insert_new_measures(measures_collection, station, new_measures)

                except ProviderException as e:
                    self.log.warn(f"Error while processing station '{station_id}': {e}")
                except Exception as e:
                    self.log.exception(f"Error while processing station '{station_id}': {e}")

        except Exception as e:
            self.log.exception(f'Error while processing MeteoSwiss: {e}')

        self.log.info('...Done!')


MeteoSwiss().process_data()
