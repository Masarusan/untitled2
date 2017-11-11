# -*- coding: utf-8 -*-
import csv


class Csv_Checker:
    def __init__(self, csv_file=['']):
        self.__csv_file = csv_file
        self.csv_encode(self.__csv_file)

    def csv_encode(self,csv_file):
        with open(csv_file, 'r')as f:
            reader = csv.reader(f)
            header = next(reader)
            print(''.join(header))
            for row in reader:
                print(''.join(row))

    def csv_dict(self, csv_file):
        with open(csv_file)as f:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(row.get('English'),row.get('japanese'))

    #使わない
    @staticmethod
    def csv_save(self, csv_file):
        with open(csv_file, 'w', newline='')as f:
            writer = csv_file.writer(f)
            writer.writerow(['rank', 'city', 'population'])
            print(f)
        pass

