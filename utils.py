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

"""
Code Descriptions

33 = Regular insulin dose
34 = NPH insulin dose
35 = UltraLente insulin dose
48 = Unspecified blood glucose measurement
57 = Unspecified blood glucose measurement
58 = Pre-breakfast blood glucose measurement
59 = Post-breakfast blood glucose measurement
60 = Pre-lunch blood glucose measurement
61 = Post-lunch blood glucose measurement
62 = Pre-supper blood glucose measurement
63 = Post-supper blood glucose measurement
64 = Pre-snack blood glucose measurement
65 = Hypoglycemic symptoms
66 = Typical meal ingestion
67 = More-than-usual meal ingestion
68 = Less-than-usual meal ingestion
69 = Typical exercise activity
70 = More-than-usual exercise activity
71 = Less-than-usual exercise activity
72 = Unspecified special event

"""


def treshold_insuline():
    """ Set treshold values for Insuline dose """
    pass


def treshold_glucose():
    """ Set treshold values for glucose measurement """
    pass



def notifications():
    """ Return alerts"""
    pass
