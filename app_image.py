#!/usr/bin/env python
# coding: utf-8

# In[5]:

import streamlit as st
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax
from tensorflow.keras.preprocessing import image as IMG
import os
import h5py

st.header("News Image Class Predictor - Frankfurter Allgemeine vs. Spiegel")

def main():
	file_uploaded = st.file_uploader("Choose the file", type = ['jpg', 'png', 'jpeg'])
	if file_uploaded is not None:
		image = Image.open(file_uploaded)
		figure = plt.figure()
		plt.imshow(image)
		plt.axis('off')
		result = predict_class(image)
		st.write(result)
		st.pyplot(figure)
		img = IMG.load_img(file_uploaded,target_size=[150,150])

def predict_class(image):
	classifier = tf.keras.models.load_model(r'vgg16_model_array_fazsp.h5')
	x = IMG.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	class_names = ['FAZ', 'Spiegel']
	pred = classification.predict(x)
	scores = tf.nn.softmax(pred[0])
	scores = scores.numpy()
	image_class = class_names[np.argmax(scores)]
	result = "The image uploaded is: {}".format(image_class)
	return result
	
if __name__ == "__main__":
	main()