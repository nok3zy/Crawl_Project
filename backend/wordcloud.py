from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image



stopword = set()
stopword.update(["사람","정말","더","이","때","개","수","번은","좀","그","임","생각","번","것","말","왜","거","저","명","존나","생각","영상","한번","저런","뭔가","보고","진짜","계속","영어","언제","다시","이제","그냥","지금","항상","여기","마지막","응원","구독","머리","나이","우리","정도","역시","다음","하나","최고","시간"])



def make_img(text,video_code):
    wc = WordCloud(background_color="white", max_words=1000,font_path="/src/MaruBuri-Regular.ttf")
    # generate word cloud
    wc.generate_from_frequencies(text)
    f = plt.figure(figsize=(15, 15))
    # plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(f"img/{video_code}.svg")

def make_ImageColoredWordcloud(text,video_code):
    wc = WordCloud(max_font_size=100,background_color="#F2F3F7", max_words=1000,font_path="/content/MaruBuri-Regular.ttf")
    # generate word cloud
    wc.generate_from_frequencies(text)
    f = plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(f"img/{video_code}.svg")

# 
# wordcloud = WordCloud(max_font_size=100,background_color="white",font_path="/content/NanumSquareR.ttf",stopwords=stopword).generate(data_string)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()


# def makeImage(text):
#     wc = WordCloud(background_color="white", max_words=1000,font_path="/content/MaruBuri-Regular.ttf")
#     # generate word cloud
#     wc.generate_from_frequencies(text)

#     # show
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.show()