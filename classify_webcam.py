import sys
import os

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import copy
import cv2

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

def predict(image_data):

    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})


    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    max_score = 0.0
    res = ''
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        if score > max_score:
            max_score = score
            res = human_string
    return res, max_score


label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("logs/trained_labels.txt")]


with tf.gfile.FastGFile("logs/trained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')
with tf.Session() as sess:

    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    c = 0
    cap = cv2.VideoCapture(0)
    res, score = '', 0.0
    i = 0
    mem = ''
    consecutive = 0
    sequence = ''
    var_ban = ''
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        if ret:
            x1, y1, x2, y2 = 100, 100, 300, 300
            img_cropped = img[y1:y2, x1:x2]
            c += 1
            image_data = cv2.imencode('.jpg', img_cropped)[1].tostring()
            a = cv2.waitKey(25)
            if i == 4:
                res_tmp, score = predict(image_data)
                res = res_tmp
                i = 0
                if mem == res:
                    consecutive += 1
                else:
                    consecutive = 0
                if consecutive == 2 and res not in ['nothing']:
                    if res == 'space':
                        var_ban += ' '
                    elif res == 'del':
                        var_ban = var_ban[:-1]
                    elif res == 'ae':
                        var_ban += 'এ'
                    elif res == 'bsro':
                        var_ban += 'ঃ'
                    elif res == 'b':
                        var_ban += 'ব'
                    elif res == 'cha':
                        var_ban += 'চ'
                    elif res == 'chha':
                        var_ban += 'ছ'
                    elif res == 'chndro':
                        var_ban += 'ঁ'
                    elif res == 'da':
                        var_ban += 'ড'
                    elif res == 'dda':
                        var_ban += 'দ'
                    elif res == 'ddha':
                        var_ban += 'ধ'
                    elif res == 'dha':
                        var_ban += 'ঢ'
                    elif res == 'eio':
                        var_ban += 'ঞ'
                    elif res == 'fa':
                        var_ban += 'ফ'
                    elif res == 'ga':
                        var_ban += 'গ'
                    elif res == 'gha':
                        var_ban += 'ঘ'
                    elif res == 'ha':
                        var_ban += 'হ'
                    elif res == 'i':
                        var_ban += 'ই'
                    elif res == 'ja':
                        var_ban += 'জ'
                    elif res == 'jha':
                        var_ban += 'ঝ'
                    elif res == 'k':
                        var_ban += 'ক'
                    elif res == 'kha':
                        var_ban += 'খ'
                    elif res == 'la':
                        var_ban += 'ল'
                    elif res == 'ma':
                        var_ban += 'ম'
                    elif res == 'na':
                        var_ban += 'ন'
                    elif res== 'o':
                        var_ban += 'ও'
                    elif res == 'oi':
                        var_ban += 'ঐ'
                    elif res == 'onsor':
                        var_ban += 'ং'
                    elif res == 'ou':
                        var_ban += 'ঐ'
                    elif res == 'pa':
                        var_ban += 'প'
                    elif res == 'rri':
                        var_ban += 'র'
                    elif res == 'sa':
                        var_ban += 'শ'
                    elif res == 'ta':
                        var_ban += 'ট'
                    elif res == 'tha':
                        var_ban += 'ঠ'
                    elif res == 'ttha':
                        var_ban += 'থ'
                    elif res == 'u':
                        var_ban += 'উ'
                    elif res == 'umo':
                        var_ban += 'ঙ'
                    elif res == 'tta':
                        var_ban += 'ত'
                    elif res == 'ah':
                        var_ban += 'আ'
                    elif res == 'ae':
                        var_ban += 'এ'
                    elif res == 'gha':
                        var_ban += 'ঘ'
                    elif res=='oha':
                        var_ban+='অ'
                    elif res=='aec':
                        var_ban+='ে'
                    elif res=='ahc':
                        var_ban+='া'
                    elif res=='ic':
                        var_ban+='ি'
                    elif res=='oc':
                        var_ban+='ো'
                    elif res=='oic':
                        var_ban+='ৌ'
                    elif res=='ouc':
                        var_ban+='ৈ'
                    elif res=='rric':
                        var_ban+='ৃ'
                    elif res=='uc':
                        var_ban+='ু'
                    else:
                        sequence += res
                        consecutive = 0
            i += 1
            cv2.putText(img, '%s' % (res.upper()), (100,400), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 4)

            mem = res
            cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
            cv2.imshow("D&M to Normal People", img)
            img_sequence = np.zeros((200,1200,3), np.uint8)

            print(var_ban)
        else:
            break
cv2.VideoCapture(0).release()
