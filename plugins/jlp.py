# with thanks to https://github.com/JamesBelchamber/ynab-jlp-csv-converter

import re

from bank2ynab import B2YBank, CrossversionCsvReader


class UKJohnLewisPartnership(B2YBank):
    def read_data(self, file_path):
        data = []
        with CrossversionCsvReader(file_path,
                                   self._is_py2,
                                   delimiter=self.config["input_delimiter"]
                                   ) as reader:
            for row in reader:
                if len(row) == 4 and row[3] == "CR":
                    data.append([row[0], row[1], '', '', '', row[2]])
                elif len(row) == 4 and re.match(
                        '[0-9]{2} [a-zA-Z]{3} [0-9]{4}', row[0]) is not None:
                    data.append([row[0], row[1], '', '', row[2], ''])
        return data


def build_bank(config, is_py2):
    return UKJohnLewisPartnership(config, is_py2)