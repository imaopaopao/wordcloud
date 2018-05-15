## English wordcloud
import os
currentpath= os.getcwd()
filename= "China.txt"
mytext=open(filename).read()

from wordcloud import WordCloud
wordcloud=WordCloud().generate(mytext)

import matplotlib.pyplot as plt
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis ("off")

#Chinese wordcloud
import os
currentpath= os.getcwd()
filename= "CChina.txt"
mytext=open(filename).read()

import jieba
mytext=" ".join(jieba.cut(mytext))

from wordcloud import WordCloud
wordcloud=WordCloud(font_path ="simsun.ttf").generate(mytext)

import matplotlib.pyplot as plt
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis ("off")


## English wordcloud with mask
import os
import numpy
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

## currentpath= os.getcwd()
filename= "China.txt"
mytext=open(filename).read()
mymask=numpy.array(Image.open('mask.png'))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc=WordCloud(background_color="white", max_words=2000, mask=mymask,stopwords=stopwords)
wc.generate(mytext)

wc.to_file("mask2f.png")

# show
plt.imshow(wc,interpolation='bilinear')
plt.axis ("off")
plt.figure()
plt.imshow(mymask,cmap=plt.cm.gray,interpolation='bilinear')
plt.axis ("off")
plt.show()
