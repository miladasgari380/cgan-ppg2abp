from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def saveDataSets(train_data, train_data_noisy, test_data, test_data_noisy):
    for i,j in enumerate(train_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_v2/trainB/%s.png' %str(i))
        
    for i,j in enumerate(train_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_v2/trainA/%s.png' %str(i))

    for i,j in enumerate(test_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_v2/testB/%s.png' %str(i))

    for i,j in enumerate(test_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_v2/testA/%s.png' %str(i))


def max_min_mapper(test_data, test_data_noisy):
    dic = {}
    itr = 0
    
    # print(test_data_noisy)

    for i, j in enumerate(test_data):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    ppg = pd.DataFrame.from_dict(dic, orient='index')
    ppg.to_csv('noise2ppg_v2/ppg.csv', index=False)
    
    dic = {}
    itr = 0

    for i, j in enumerate(test_data_noisy):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    abp = pd.DataFrame.from_dict(dic, orient='index')
    abp.to_csv('noise2ppg_v2/abp.csv', index=False)


def saveDataSets_mimicIII(train_data, train_data_noisy, test_data, test_data_noisy):
    for i,j in enumerate(train_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII/trainB/%s.png' %str(i))
        
    for i,j in enumerate(train_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII/trainA/%s.png' %str(i))

    for i,j in enumerate(test_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII/testB/%s.png' %str(i))

    for i,j in enumerate(test_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII/testA/%s.png' %str(i))


def max_min_mapper_mimicIII(test_data, test_data_noisy):
    dic = {}
    itr = 0
    
    # print(test_data_noisy)

    for i, j in enumerate(test_data):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    ppg = pd.DataFrame.from_dict(dic, orient='index')
    ppg.to_csv('noise2ppg_mimicIII/ppg.csv', index=False)
    
    dic = {}
    itr = 0

    for i, j in enumerate(test_data_noisy):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    abp = pd.DataFrame.from_dict(dic, orient='index')
    abp.to_csv('noise2ppg_mimicIII/abp.csv', index=False)
    
def saveDataSets_mimicIII_subject(train_data, train_data_noisy, test_data, test_data_noisy, subject_id):
    for i,j in enumerate(train_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_s'+str(subject_id)+'/trainB/%s.png' %str(i))
        
    for i,j in enumerate(train_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_s'+str(subject_id)+'/trainA/%s.png' %str(i))

    for i,j in enumerate(test_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_s'+str(subject_id)+'/testB/%s.png' %str(i))

    for i,j in enumerate(test_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_s'+str(subject_id)+'/testA/%s.png' %str(i))


def max_min_mapper_mimicIII_subject(test_data, test_data_noisy, subject_id):
    dic = {}
    itr = 0
    
    # print(test_data_noisy)

    for i, j in enumerate(test_data):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    ppg = pd.DataFrame.from_dict(dic, orient='index')
    ppg.to_csv('noise2ppg_mimicIII_s'+str(subject_id)+'/ppg.csv', index=False)
    
    dic = {}
    itr = 0

    for i, j in enumerate(test_data_noisy):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    abp = pd.DataFrame.from_dict(dic, orient='index')
    abp.to_csv('noise2ppg_mimicIII_s'+str(subject_id)+'/abp.csv', index=False)

    
def saveDataSets_mimicIII_all(train_data, train_data_noisy, test_data, test_data_noisy):
    for i,j in enumerate(train_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_all/trainB/%s.png' %str(i))
        
    for i,j in enumerate(train_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_all/trainA/%s.png' %str(i))

    for i,j in enumerate(test_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_all/testB/%s.png' %str(i))

    for i,j in enumerate(test_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_all/testA/%s.png' %str(i))


def max_min_mapper_mimicIII_all(test_data, test_data_noisy):
    dic = {}
    itr = 0
    
    # print(test_data_noisy)

    for i, j in enumerate(test_data):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    ppg = pd.DataFrame.from_dict(dic, orient='index')
    ppg.to_csv('noise2ppg_mimicIII_all/ppg.csv', index=False)
    
    dic = {}
    itr = 0

    for i, j in enumerate(test_data_noisy):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    abp = pd.DataFrame.from_dict(dic, orient='index')
    abp.to_csv('noise2ppg_mimicIII_all/abp.csv', index=False)
    
    
def saveDataSets_mimicIII_all_subject(train_data, train_data_noisy, test_data, test_data_noisy, subject_id):
    for i,j in enumerate(train_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_all_s'+str(subject_id)+'/trainB/%s.png' %str(i))
        
    for i,j in enumerate(train_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_all_s'+str(subject_id)+'/trainA/%s.png' %str(i))

    for i,j in enumerate(test_data):
        rescaled = ((255.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_all_s'+str(subject_id)+'/testB/%s.png' %str(i))

    for i,j in enumerate(test_data_noisy):
        rescaled = ((155.0 / (j.max() - j.min())) * (j - j.min())).astype(np.uint8)
        #rescaled = np.array(j).astype(np.uint8)
        im = Image.fromarray(rescaled)
        im.save('noise2ppg_mimicIII_all_s'+str(subject_id)+'/testA/%s.png' %str(i))


def max_min_mapper_mimicIII_all_subject(test_data, test_data_noisy, subject_id):
    dic = {}
    itr = 0
    
    # print(test_data_noisy)

    for i, j in enumerate(test_data):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    ppg = pd.DataFrame.from_dict(dic, orient='index')
    ppg.to_csv('noise2ppg_mimicIII_all_s'+str(subject_id)+'/ppg.csv', index=False)
    
    dic = {}
    itr = 0

    for i, j in enumerate(test_data_noisy):
        dic[itr] = {'min': j.min(), 'max': j.max(), 'key': i}
        itr += 1

    abp = pd.DataFrame.from_dict(dic, orient='index')
    abp.to_csv('noise2ppg_mimicIII_all_s'+str(subject_id)+'/abp.csv', index=False)



