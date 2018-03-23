import cv2

from create_hdf5 import *

# loop over train addresses
for i in range(len(gender_train_data)//50 + 1): # 1000 train data only

    # print how many images are saved every 500 images
    if i % 500 == 0 and i > 1:
        print ('Train data: {}/{}'.format(i, len(gender_train_data)//50))

    train_data_addr = gender_train_data[i]
    img = cv2.imread(train_data_addr)
    img = cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)
    # cv2 load images as BGR, convert it to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # save the image and calculate the mean so far
    hdf5_train_file["train_img"][i, ...] = img[None]

# loop over test addresses
for i in range(len(gender_test_data)//28 + 1): # 500 test data
    # print how many images are saved every 200 images
    if i % 200 == 0 and i > 1:
        print ('Test data: {}/{}'.format(i, len(gender_test_data)//28))

    test_data_addr = gender_test_data[i]
    img = cv2.imread(test_data_addr)
    img = cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)
    # cv2 load images as BGR, convert it to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # save the image
    hdf5_test_file["test_img"][i, ...] = img[None]

# save the mean and close the hdf5 files
hdf5_train_file.close()
hdf5_test_file.close()