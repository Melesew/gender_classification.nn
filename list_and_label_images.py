from random import shuffle
import glob

shuffle_data = True  # shuffle the addresses before saving
hdf5_train_data_path =  'gender/train_dataset.h5'  # address to where you want to save the hdf5 file
hdf5_test_data_path = 'gender/test_dataset.h5'

female_train_path = 'gender/train/f/*.jpg'
male_train_path = 'gender/train/m/*.jpg'

female_test_path = 'gender/test/f/*.jpg'
male_test_path = 'gender/test/m/*.jpg'

# read actual data and label addresses from the 'train' folder
male_train_data = glob.glob(male_train_path)
female_train_data = glob.glob(female_train_path)

male_test_data = glob.glob(male_test_path)
female_test_data = glob.glob(female_test_path)
gender_train_data = male_train_data + female_train_data # mix the the addresses
# print(len(gender_train_data))

gender_test_data = male_test_data + female_test_data # mix the the addresses
# print(len(gender_test_data))

train_labels = [0 if '/f/' in address else 1 for address in gender_train_data]  # 0 = female, 1 = male
# print(len(train_labels))
test_labels = [0 if '/f/' in address else 1 for address in gender_test_data]  # 0 = female, 1 = male
# print(len(test_labels))

classes = ['female', 'male']

# to shuffle data
if shuffle_data:
    mixed_train_data = list(zip(gender_train_data, train_labels))
    mixed_test_data = list(zip(gender_test_data, test_labels))
    shuffle(mixed_train_data)
    shuffle(mixed_test_data)
    gender_train_data, train_labels = list(zip(*mixed_train_data))
    gender_test_data, test_labels = list(zip(*mixed_test_data))

# print(len(gender_train_data))
# print(len(gender_test_data))

