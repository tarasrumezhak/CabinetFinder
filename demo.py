import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt

# template = cv2.imread("data/templates/wall_cabinet/cabinet_1.png")
# template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# scale = 0.5
# template = imutils.resize(template, width=int(template.shape[1] * scale))
# template = cv2.Canny(template, 50, 200)


# cv2.imshow("win", template)
# cv2.waitKey(0)

# print("template: ", template.shape)

query = cv2.imread("data/query/interior.png")
# query = cv2.cvtColor(query, cv2.COLOR_BGR2GRAY)

# custom_template = query[558:611, 425:539] # 0.6  3.3 h
# custom_template = query[1066:1171, 417:522] # 0.735 3.0 square
# custom_template = query[1066:1171,590:704] # 0.65 3.3 square
# custom_template = query[558:664, 801:871]   # 0.65 2.0 v
# custom_template = query[558:664, 871:957] # 0.6 2.3 v
# cv2.imwrite("data/templates/wall_cabinet/cabinet_30_20.png", custom_template)



# scale = 0.5
# query = imutils.resize(query, width=int(query.shape[1] * scale))
query = cv2.Canny(query, 50, 200)



print("query: ", query.shape)

# cv2.imshow("win", query)
# cv2.waitKey(0)

plt.imshow(query)
plt.show()

plt.imshow(custom_template)
plt.show()

# for scale in np.linspace(0.1, 0.5, 5)[::-1]:
if True:

    # resized = imutils.resize(template, width=int(template.shape[1] * scale))
    # r = template.shape[1] / float(resized.shape[1])


    temp = custom_template
    (tH, tW) = temp.shape[:2]
    temp = cv2.Canny(temp, 50, 200)

    result = cv2.matchTemplate(query, temp, cv2.TM_CCOEFF)
    # (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
    result_normalized = cv2.normalize(result, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    plt.imshow(result_normalized)
    plt.show()

    threshold = 0.6
    loc = np.where(result_normalized >= threshold)


    # check to see if the iteration should be visualized
    # if args.get("visualize", False):
        # draw a bounding box around the detected region
    clone = np.dstack([query, query, query])

    for pt in zip(*loc[::-1]):
        cv2.rectangle(clone, pt, (pt[0] + tW, pt[1] + tH), (0, 0, 255), 2)

    # cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
    #     (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
    # cv2.imshow("Visualize", clone)
    # cv2.waitKey(0)

    plt.imshow(clone)
    plt.show()
