import h5py
import numpy as np

hdf5_path = 'dataset.hdf5'
subtract_mean = False

# open the hdf5 file
hdf5_file = h5py.File(hdf5_path, "r")

# subtract the training mean
if subtract_mean:
    mm = hdf5_file["train_mean"][0, ...]
    mm = mm[np.newaxis, ...]

# Total number of samples
data_num = hdf5_file["train_img"].shape[0]
print(data_num)
print(data_num)