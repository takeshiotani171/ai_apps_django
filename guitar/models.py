from django.db import models

import numpy as np
#import tensorflow as tf
import base64
import requests
import json

# graph = tf.get_default_graph()

# class Photo(models.Model):
#     image = models.ImageField(upload_to='photos')

  
#     def predict(self):
#         global graph
#         with graph.as_default():
            
#             img_data = self.image.read()
#             object_categories =['ギターの写真', 'ギター以外の写真']
#             list = base64.b64encode(img_data).decode('utf-8')

#             url = 'https://y0stvmi0ij.execute-api.us-east-1.amazonaws.com/mlmodel/'
#             body = {"data": list}
#             res = requests.post(url, json.dumps(body))
  
#             predicted = np.argmax(res.json())
#             percentage = int(res.json()[predicted] * 100)
#             predicted_label = object_categories[predicted]
            
#             return predicted_label, percentage

#     def image_src(self):
#         with self.image.open() as img:
#             base64_img = base64.b64encode(img.read()).decode()

#             return 'data:' + img.file.content_type + ';base64,' + base64_img



class Photo(models.Model):
    
    image = models.ImageField(upload_to='photos')

  
    def predict(self):

        img_data = self.image.read()
        object_categories =['ギターの写真', 'ギター以外の写真']
        list = base64.b64encode(img_data).decode('utf-8')

        url = 'https://y0stvmi0ij.execute-api.us-east-1.amazonaws.com/mlmodel/'
        body = {"data": list}
        res = requests.post(url, json.dumps(body))
  
        predicted = np.argmax(res.json())
        percentage = int(res.json()[predicted] * 100)
        predicted_label = object_categories[predicted]
            
        return predicted_label, percentage

    def image_src(self):
        with self.image.open() as img:
            base64_img = base64.b64encode(img.read()).decode()

            return 'data:' + img.file.content_type + ';base64,' + base64_img


