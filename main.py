from saveDataSets_v2 import saveDataSets, max_min_mapper, saveDataSets_mimicIII, max_min_mapper_mimicIII, saveDataSets_mimicIII_all, max_min_mapper_mimicIII_all, max_min_mapper_mimicIII_subject, saveDataSets_mimicIII_subject, saveDataSets_mimicIII_all_subject, max_min_mapper_mimicIII_all_subject
import sys

path = '.'
from preprocessing.createDataSet_v2 import createDataSet, createDataSet_mimicIII, createDataSet_mimicIII_full, createDataSet_mimicIII_subject, createDataSet_mimicIII_full_subject
from preprocessing.create2DImages_v2 import create2DImages, create2DImages_mimicIII, create2DImages_mimicIII_full, create2DImages_mimicIII_subject, create2DImages_mimicIII_full_subject

# Creating 2D Images
#ppgs, abps = create2DImages()
#ppgs, abps = create2DImages_mimicIII()
#ppgs, abps = create2DImages_mimicIII_full()


# Creating both datasets
#train_data, train_data_abp, test_data, test_data_abp = createDataSet(ppgs, abps)
#train_data, train_data_abp, test_data, test_data_abp = createDataSet_mimicIII(ppgs, abps)
#train_data, train_data_abp, test_data, test_data_abp = createDataSet_mimicIII_full(ppgs, abps)

# Saving the trainData and the testData to noise2ppg directory
#saveDataSets(train_data, train_data_abp, test_data, test_data_abp)
#saveDataSets_mimicIII(train_data, train_data_abp, test_data, test_data_abp)
#saveDataSets_mimicIII_all(train_data, train_data_abp, test_data, test_data_abp)

# create mapping
#max_min_mapper(test_data, test_data_abp)
#max_min_mapper_mimicIII(test_data, test_data_abp)
#max_min_mapper_mimicIII_all(test_data, test_data_abp)


# subject specific train
#for i in range(16, 30):
#    ppgs, abps = create2DImages_mimicIII_full_subject(i)
#    train_data, train_data_abp, test_data, test_data_abp = createDataSet_mimicIII_full_subject(ppgs, abps)
#    saveDataSets_mimicIII_all_subject(train_data, train_data_abp, test_data, test_data_abp, i)
#    max_min_mapper_mimicIII_all_subject(test_data, test_data_abp, i)

