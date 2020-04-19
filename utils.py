""" Utility functions. """
import os
import pandas as pd


def dict_main():
    """ Collects data for each patient and concat on dict"""
    ddict = {}
    for file in os.listdir('patient-data'):
        if file.startswith('data'):
            name = os.path.splitext(file)[0]
            ddict[name] = pd.read_csv(os.path.join('patient-data', file), sep='\t')
            ddict[name].columns = ['Date', 'Time', 'Code', 'Value']
    return ddict


dict_main = dict_main()
print(dict_main['data-70'])

def treshold_insuline():
    """ Set treshold values for Insuline dose """
    pass


def treshold_glucose():
    """ Set treshold values for glucose measurement """
    pass


def notifications():
    """ Return alerts"""
    pass
