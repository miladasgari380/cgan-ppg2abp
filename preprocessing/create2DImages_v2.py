from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import heartpy as hp
import numpy as np

def create2DImages_mimicIII_full(): #mimic 2
    ppgs = []
    abps = []

    k = 256
    size_to_read = 37888
    
    
    dataset = pd.DataFrame([])
    for i in range(92):
        dataset_new = pd.read_csv('./mimic_full/'+str(i)+'.csv', header=None )
        dataset = pd.concat([dataset, dataset_new.iloc[:size_to_read, :]])
    
    dataset.columns = ['ppg', 'abp']
    print('size_to_read:', size_to_read) # 37888
    
    pleth = hp.filter_signal(dataset['ppg'], cutoff = [0.1, 8], sample_rate = 125.0, order = 3, filtertype='bandpass')
    abp = hp.filter_signal(dataset['abp'], cutoff = 5, sample_rate = 125.0, order = 3, filtertype='lowpass')
    
    ppg_size = len(pleth) // k

    total_ppgs = []
    total_abps = []

    for i in range(ppg_size):
        pleth_subject = pleth[i*k:(i+1)*k]    
        abp_subject = abp[i*k:(i+1)*k]
        ppgs = []
        abps = []
        for j in range(k):
            ppgs.append(pleth_subject)
            abps.append(abp_subject)

        total_ppgs.append(np.array(ppgs))
        total_abps.append(np.array(abps))

    #print(total_abps[1])
    return total_ppgs, total_abps


def create2DImages_mimicIII_full_subject(i):
    ppgs = []
    abps = []

    k = 256
    size_to_read = 37888
    
    
    dataset = pd.read_csv('./mimic_full/'+str(i)+'.csv', header=None )
    dataset = dataset.iloc[:size_to_read, :].copy()
    
    dataset.columns = ['ppg', 'abp']
    print('size_to_read:', size_to_read) # 37888
    
    pleth = hp.filter_signal(dataset['ppg'], cutoff = [0.1, 8], sample_rate = 125.0, order = 3, filtertype='bandpass')
    abp = hp.filter_signal(dataset['abp'], cutoff = 5, sample_rate = 125.0, order = 3, filtertype='lowpass')
    
    ppg_size = len(pleth) // k

    total_ppgs = []
    total_abps = []

    for i in range(0, size_to_read - k, k//4):
        pleth_subject = pleth[i:i+k]    
        abp_subject = abp[i:i+k]
    #for i in range(ppg_size):
     #   pleth_subject = pleth[i*k:(i+1)*k]    
      #  abp_subject = abp[i*k:(i+1)*k]
        ppgs = []
        abps = []
        for j in range(k):
            ppgs.append(pleth_subject)
            abps.append(abp_subject)

        total_ppgs.append(np.array(ppgs))
        total_abps.append(np.array(abps))

    #print(total_abps[1])
    return total_ppgs, total_abps
    
