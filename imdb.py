from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


def get_review(url):

    reviews = None
    try:

        html = urlopen(url).read()

        bsObj = BeautifulSoup( html , "html.parser")
        download_reviews =  bsObj.select("#tn15content p")

        reviews = [review.text for review in download_reviews if review.text != ""]

    except  HTTPError :
        pass

    return  reviews[:-1]




if  __name__ == "__main__":
    reviews = get_review("http://www.imdb.com/title/tt0944947/reviews?ref_=tt_urv")

    for index , review in enumerate(reviews):
        print(str(index),end= ".")
        print(review)



