import requests as req
import wget

class pdfParser:

    def __init__(self):
        self.dir="downloads/"



    def PatterCounter(self,iid,pattern):
        nocc = 0
        with pdfplumber.open(iid+".pdf") as pdf:
           for page in pdf.pages:
             text = first_page.extract_text()
             nocc+=text.count(pattern)
        return nocc

    def GetBibNumberRef(self,iid,searchiid):
        inRef = False
        found = False
        refCount = 1
        with pdfplumber.open(iid+".pdf") as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text is None: continue
                for line in text.split('\n'):
                    if line.find("References")>0: 
                        inRef=True
                    if inRef:
                        if line.startswith("["+str(refCount)+"]")>0: 
                            print(line)
                            refCount=refCount+1
                    if line.find(pattern)>0:
                        print(line)
                        print(refCount-1)
                        found = True
                        break
                if found: break
        return (refCount-1)


     def GetNoccCitations(self,iid,bibid):
        Nocc=0
        Text=[]
        with pdfplumber.open(idpdf+".pdf") as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text is None: continue
                for line in text.split('\n'):
                    if line.find("["+str(bibid)+"]")>0 or line.find("["+str(bibid)+",")>0 or line.find(str(bibid)+",]")>0 \
                            or line.find("["+str(bibid)+"–")>0 or line.find("–"+str(bibid)+"]")>0:
                        inRef=True
                        #print("REF:",line)
                        Nocc+=1
                        Text.append(line)
                    if line.find("References")>0:
                        inRef=True
                        break
                if inRef: break
        return Nocc,Text


