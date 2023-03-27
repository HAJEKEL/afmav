import cv2
import numpy as np
import os

def find_color(image, color):
    image = image[:, 80:180]
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    if color == "green":
        lower= np.array([0, 0, 0])
        upper = np.array([255, 115, 145])
    elif color == "white":
        lower= np.array([214, 0, 0])
        upper = np.array([255, 255, 255]) 
    elif color == "black":
        lower= np.array([0, 0, 0])
        upper = np.array([115, 127, 255])
    mask_yuv = cv2.inRange(yuv_image, lower, upper)
    result_yuv = cv2.bitwise_and(image, image, mask=mask_yuv)
    result_yuv = cv2.threshold(result_yuv[:, :, 0], 1, 255, cv2.THRESH_BINARY)[1]
    result_yuv = cv2.cvtColor(result_yuv, cv2.COLOR_GRAY2RGB)
    count = cv2.countNonZero(mask_yuv)
    return result_yuv, count

image_files = os.listdir("black")
count_black = []
for image_file in image_files:
# Load the image
    image_path = os.path.join("black", image_file)
    image = cv2.imread(image_path)
    result_yuv, count = find_color(image,"black")
    count_black.append(count)
    cv2.imshow('Original', image)
    cv2.imshow('Result YUV', result_yuv)
    cv2.waitKey(0)

image_files = os.listdir("green")
count_green = []

for image_file in image_files:
# Load the image
    image_path = os.path.join("green", image_file)
    image = cv2.imread(image_path)
    result_yuv, count = find_color(image,"green")
    count_green.append(count)
    cv2.imshow('Original', image)
    cv2.imshow('Result YUV', result_yuv)
    cv2.waitKey(0)


image_files = os.listdir("white")
count_white = []

for image_file in image_files:
# Load the image
    image_path = os.path.join("white", image_file)
    image = cv2.imread(image_path)
    result_yuv, count = find_color(image,"white")
    count_white.append(count)
    cv2.imshow('Original', image)
    cv2.imshow('Result YUV', result_yuv)
    cv2.waitKey(0)

print("Number of black pixels for the black images",count_black)
print("Number of green pixels for the green images",count_green)
print("Number of white pixels for the white images",count_white)

print("If there are more pixels than the threshold, drone should turn:")
print("black_threshold =",min(count_black))
print("green_threshold =",min(count_green))
print("white_threshold =",min(count_white))