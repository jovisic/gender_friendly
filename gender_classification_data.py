import os
import shutil
import cv2

import face_recognition
from PIL import Image, ImageDraw
from face_recognition import face_landmarks
import tensorflow as tf
import numpy as np




# def data_array(batch_size = 32, color_depth = 3, height = 200, width = 180):
#     return np.empty((batch_size, color_depth, height, width), dtype=np.uint8)


def image_path(root, path):
    return "{}/{}".format(root, path)


def traversePath(dataset_path, label):
    cnt = 0
    temp_data = []
    for root, dirs, files in os.walk(dataset_path):
        for idx, file_path in enumerate(files):
            if cnt < 400:
                path = image_path(root, file_path)
                image = cv2.imread(path, cv2.IMREAD_COLOR)
                temp_data.append((image, label))
                cnt += 1
            else:
                break
    return temp_data
    #print(label, cnt)
    #
    #     dataList = filename[2].copy()
    #     print(dataList)
    # return dataList

def shuffle_data(data):
    pass

def create_dataset():
    male_data = traversePath("DatasetFaces/male", "male")
    female_data = traversePath("DatasetFaces/female", "female")

    merged_data = male_data + female_data
    # print(merged_data)
    return merged_data

if __name__ == '__main__':
    create_dataset()