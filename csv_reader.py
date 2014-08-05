import csv
import json

HEADER = ["name", "hrs", "cost"]


class InvalidFileFormat(Exception):
    pass


class FileReader(object):
    """
    Take as input a csv file and output json data
    """
    def __init__(self, file_name, *args, **kwargs):
        self.file_name = file_name
        self.file_extn = file_name.split('.')[-1]
        if self.file_extn == 'csv':
            self.converter = self.csv_converter
        else:
            raise InvalidFileFormat("Invalid file format.")

    def csv_converter(self):
        """
        csv to json converter
        """
        try:
            f = open(self.file_name, 'rb')
        except IOError:
            raise IOError("invalid file path, please check")
        reader = csv.reader(f)
        reader.next()
        data = {}
        try:
            for line in reader:
                data[line[0]] = {"hrs": int(line[1]), "cost": int(line[2])}
        except IndexError, e:
            pass
        finally:
            f.close()
        return data
