import cv2
import numpy as np

def rect_contour(contours):
    rect_contours = []
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        # print("area", area)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            # print("cantos", len(approx))
            if len(approx) == 4:
                rect_contours.append(i)
    rect_contours = sorted(rect_contours, key=cv2.contourArea, reverse=True)

    return rect_contours

def get_corner_points(contour):
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
    return approx

def reorder(points):
    points = points.reshape(4, 2)
    points_new = np.zeros((4, 1, 2), np.int32)
    add = points.sum(1)
    # print(points)
    # print(add)
    # onde começa onde termina n sei n entendi
    points_new[0] = points[np.argmin(add)]  # [0,0]
    points_new[3] = points[np.argmax(add)]  # [w,h]
    diff = np.diff(points, axis=1)
    points_new[1] = points[np.argmin(diff)]  # [w,0]
    points_new[2] = points[np.argmax(diff)]  # [0,h]
    # print(diff)
    return points_new

def split_boxes(img):
    rows = np.vsplit(img, 25)
    boxes = []
    for row in rows:
        cols = np.hsplit(row, 5)
        for box in cols:
            boxes.append(box)
    return boxes
