#from iteration_utilities import first
import pandas as pd


class Rawdlc:
    def __init__(self, filepath):
        with open(filepath, 'rb') as f:
            data = pd.read_hdf(filepath)
        network = data.columns[0][0]
        bodyparts = set()
        for col in data.columns:
            bodypart = col[1]
            bodyparts.add(bodypart)

        self.filepath = filepath
        self.network = network
        self.bodyparts = bodyparts
        self.data = data[network]

    def get_loc(self, bodypart):
        return self.data[bodypart]

    def get_low_p_frames(self, bodypart, thresh=0.95):
        data = self.data[bodypart]
        low_p = data.loc[data['likelihood'] < thresh]
        return low_p.index.values
        

