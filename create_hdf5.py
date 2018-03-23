'''Create the actual Hierarchical Data File'''
import numpy as np
import h5py
from list_and_label_images import *

# Order image data in 'tf' tensorlow order, color indicator (3 for RGB, 1/gray scale in zis case) comes at the end.
train_data_shape = (len(gender_train_data), 64, 64, 3)
test_data_shape = (len(gender_test_data), 64, 64, 3)
print(train_data_shape)

# open a hdf5 file and create earrays
hdf5_train_file = h5py.File(hdf5_train_data_path, mode='w')
hdf5_test_file = h5py.File(hdf5_test_data_path, mode='w')

hdf5_train_file.create_dataset("train_img", train_data_shape, np.int8)
hdf5_train_file.create_dataset("train_labels", (len(gender_train_data),), np.int8)
hdf5_train_file["train_labels"][...] = train_labels

hdf5_test_file.create_dataset("test_img", test_data_shape, np.int8)
hdf5_test_file.create_dataset("test_labels", (len(gender_test_data),), np.int8)
hdf5_test_file["test_labels"][...] = test_labels

hdf5_test_file.create_dataset("list_classes", (2,), dtype=h5py.special_dtype(vlen=str))
hdf5_test_file["list_classes"][...] = classes

# hdf5_file.create_dataset("train_mean", train_data_shape[1:], np.float32)