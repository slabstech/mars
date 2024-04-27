import os

from flask import Flask, request
from mars import get_mars_photo_url
app = Flask(__name__)

@app.route("/")
def hello():
  #message_body = request.form['Body']
  #photo_url = get_mars_photo_url(2)
  #print(photo_url)
  urls = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY' 
  print(urls)
  return "Hello World!"

if __name__ == "__main__":
  app.run()