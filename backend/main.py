from util import getDate
from youtubeClass import Youtube
# from preprocessingClass import Preprocess
from mongo import mongoDB
import pandas as pd

from flask import Flask, request, jsonify,send_file
from flask_cors import CORS
import io
import re
def extract(txt):
  hangul = re.compile('[^0-9 ㄱ-ㅣ가-힣]+')
  result = hangul.sub('',txt)
  return result


app = Flask(__name__)

CORS(app)



@app.route('/')
def index():
   print("backend Server on")
   return jsonify({"conn":True})

@app.route('/video_ids', methods=['GET'])
def ttemp():
   t = Youtube()
   t.get_id()
   print(t.video_ids)
   return jsonify({"video_id":t.video_ids})

@app.route('/cron', methods=['GET'])
def cron():
    video_ids = Youtube().get_data()
    for video_id in video_ids:
        bow = Preprocess(video_id).make_bow()
        mongoDB(getDate()).insert(video_id,bow)

    return jsonify("T")

@app.route('/img')
def get_image():
    if request.args.get('code'):
       code = request.args.get('code')
       filename = f'img/{code}.jpg'
    else:
       filename = 'img/error.jpg'
    try:
      return send_file(filename, mimetype='image/jpg')
    except:
      return send_file('error.jpg', mimetype='image/jpg')


@app.route('/wordcloud', methods=['POST'])
def wordcloud():
    text=[]
    try:
        video_code = request.json["video_id"]
        if video_code != "favicon.ico":
            print(video_code)
            csv_file = pd.read_csv("raw_data/210501_m-HStXuBpLw.csv")
            text = list(map(extract,csv_file["text"].head(20)))
    except Exception as e:
        print(e)
    return jsonify(text)
    #send_file
    





# @app.route('/guestbook', methods=['POST'])
# def postMain():
#   try:
#     guest_name,content = request.json.values()
#     if guest_name and content and request.method == 'POST':
#       sqlQuery = "INSERT guest(guest_name,content) VALUES(%s,%s)"
#       bindData = (guest_name,content)
#       conn = mysql.connect()
#       cursor = conn.cursor()
#       cursor.execute(sqlQuery, bindData)
#       conn.commit()
#       respone = jsonify('Employee added successfully!')
#       respone.status_code = 200
#       return response
#   except Exception as e:
#     print(e)
#   finally:
#     cursor.close() 
#     conn.close()

   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)