#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.models import load_model
import os


# In[2]:


print(tf.__version__)
print(tf.keras.__version__)


# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


# In[5]:


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# In[6]:


train_images.shape


# In[7]:


train_labels.shape


# In[8]:


test_images.shape


# In[9]:


test_labels.shape


# In[10]:


plt.figure()
plt.imshow(np.squeeze(train_images[220]))


# In[11]:


train_labels[220]


# In[12]:


# Let us plot some training images to see how they look
plt.figure(figsize=(10,10))
for i in range(15):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()


# In[13]:


train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))


# In[14]:


train_images_norm = train_images / 255.0


# In[15]:


test_images_norm = test_images / 255.0


# In[16]:



model = models.Sequential()




model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1) ))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.Conv2D(128, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, 'softmax'))


# In[17]:



# In[18]:


model.summary()


# In[19]:


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# In[20]:


fit_model = model.fit(train_images_norm, train_labels, epochs=2, batch_size=512, shuffle=True, validation_split=0.1)


# In[21]:


test_loss, test_accuracy = model.evaluate(test_images_norm, test_labels)


# In[22]:


print(test_accuracy)


# In[23]:


text = fit_model.history
accuracy = text['accuracy'][1] * 100
accuracy = int(accuracy)
f= open("accuracy.txt","w+")
f.write(str(accuracy))
f.close()

print("Accuracy for the model is : " , accuracy ,"%")


# In[ ]:




