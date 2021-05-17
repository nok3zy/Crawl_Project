import pandas as pd 
from konlpy.tag import Okt
import re
from util import getDate
from collections import defaultdict


class Preprocess():
  def __init__(self,video_id):
    self.stopword=["사람","정말","더","이","때","개","수","번은","좀","그","임","생각","번","것","말","왜","거","저","명","존나","생각","영상","한번","저런","뭔가","보고","진짜","계속","영어","언제","다시","이제","그냥","지금","항상","여기","마지막","응원","구독","머리","나이","우리","정도","역시","다음","하나","최고","시간"]
    self.document = pd.read_csv(f"./raw_data/{getDate()}_{video_id}")
    self.okt = Okt()
    self.text = self.document["text"]

  def extract(self,txt):# 숫자한글 추출.
    temp = re.compile('[^0-9ㄱ-ㅣ가-힣]+')
    result = temp.sub('',txt)
    return result
  
  def make_bow(self): # bow dict 만들기.
    bow = defaultdict(int)

    for txt in self.text:
      temp=self.okt.nouns(self.extract(txt))
      for tmp in temp:
        if tmp not in this.stopword:
          bow[tmp]+=1
    return bow

  def trim(bow,cnt): # 상위 cnt개 trim
    data = sorted(bow.items(),key=lambda x: (-x[1] ) )[:cnt]
    return data
  


  