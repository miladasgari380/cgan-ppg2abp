from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def createDataSet(ppgs, abps):
#	train_data = ppgs[0:7] # Clean PPG signal for training
#	train_data_noisy = abps[0:7] # Noisy PPG signal for training
#	test_data = ppgs[7:] # Clean PPG signal for testing
#	test_data_noisy = abps[7:] # Noisy PPG signal for testing

    ppg_size = len(ppgs)
    train_size = int(0.8*ppg_size)
    print('train size', train_size)
    return ppgs[0:train_size], abps[0:train_size], ppgs[train_size:], abps[train_size:]
    
def createDataSet_mimicIII(ppgs, abps): #cv
    #train_size = 8*998400
    train_size = int(8 * 528) # 5fold
    test_size = len(ppgs) - train_size
    
    k = 4
    mask = np.ones(len(ppgs), bool)
    mask[k*test_size:(k+1)*test_size] = False
    
    #print(len(abps[k*test_size:(k+1)*test_size]))
    print("len of all data:", len(ppgs), len(abps), train_size, test_size)
    #return ppgs[:train_size], abps[:train_size], ppgs[train_size:], abps[train_size:]
    #return np.delete(ppgs, exclude), np.delete(ppgs, exclude), ppgs[k*test_size:(k+1)*test_size], abps[k*test_size:(k+1)*test_size]
    return np.array(ppgs)[mask], np.array(abps)[mask], ppgs[k*test_size:(k+1)*test_size], abps[k*test_size:(k+1)*test_size]


def createDataSet_mimicIII_subject(ppgs, abps, subject_id):
    #train_size = 8*998400
    train_size = int(0.8*len(ppgs))
    print("len of all data:", len(ppgs), len(abps), train_size, subject_id)
    return ppgs[0:train_size], abps[0:train_size], ppgs[train_size:], abps[train_size:]


def createDataSet_mimicIII_full(ppgs, abps):
    #train_size = 70 * 9728000
    train_size = int(70 * 148)
    print("len of all data:", len(ppgs), len(abps), train_size) # 13616
    return ppgs[:train_size], abps[:train_size], ppgs[train_size:], abps[train_size:]


def createDataSet_mimicIII_full_subject(ppgs, abps):
    #train_size = 70 * 9728000
    train_size = int(0.8*len(ppgs))
    print("len of all data:", len(ppgs), len(abps), train_size)
    return ppgs[0:train_size], abps[0:train_size], ppgs[train_size:], abps[train_size:]
