import requests as req
import wget

class pyArxiv:

    def __init__(self):
        self.url="https://arxiv.org/pdf/"
        self.url="downloads"

    def download(iid):
        wget.download(self.url+str(iid),"downloads/"+str(iid)+".pdf")


