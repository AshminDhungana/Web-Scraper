"""All CSV oprations classes"""

import csv

class CSV:
    def __init__(self,filename = '') -> None:
        self.filename = filename

    @classmethod
    def csvread(self, filename):
        datas = []
        with open(filename, newline='') as csvfile:
            content = csv.reader(csvfile)
            for row in content:
                datas.append(row)
        return datas

    @classmethod
    def csvwrite(self, filename, datas):
        with open(filename, 'w', newline='') as csvfile:
            content = csv.writer(csvfile, delimiter=' ')
            content.writerows(datas)
        return True
