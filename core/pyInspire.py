import requests as req
import wget


class pyInspire:

    def __init__(self):
       self.urlapi = "https://inspirehep.net/api/literature"
       self.json = None 
       #dictionnary of the current inspire id
       self.ciid = None 
       #current inspire id

    #retrieve an Inspire id from a arxiv number
    def getIdFromArxivId(self,axid):
        url=self.urlapi+"?q="+axid
        json = req.get(url).json()
        if len(json['hits']['hits'])>0:
           return json['hits']['hits'][0]['id']
        return None
   
    def getTitle(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        return self.json['metadata']['titles'][-1]['title'] 
   
    #from inspire id
    def LoadJson(self,iid):
        url=self.urlapi+"/"+iid
        self.ciid = iid
        self.json = req.get(url).json()
        return self.json

    #check if iiid is the current one
    def check(self, iid):
        if iid!=self.ciid: return False
        if self.json is None: return False
        if self.json["id"] !=iid: return False
        return True

    def getArxivId(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        if len(self.json["metadata"]["arxiv_eprints"])>0:
          return self.json["metadata"]["arxiv_eprints"][0]['value']


    def getAbstract(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        if len(self.json["metadata"]['abstracts'])>0:
           return(self.json["metadata"]['abstracts'][0]['value'])
  
    def getCollab(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        return self.json["metadata"]["collaborations"][0]["value"]

    def getCategory(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        return self.json["metadata"]["inspire_categories"][0]["term"]


    def getKeywords(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        if "keywords" not in self.json["metadata"].keys(): return []
        klist = self.json["metadata"]["keywords"]
        keywords=[]
        for el in klist:
            keywords.append(el['value'])
        return keywords

    def getNofCitations(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        return self.json["metadata"]["citation_count"]


    def getCitationList(self,iid):
        liids = []
        url=self.urlapi+"?sort=mostcited&size=1000&page=1&q=refersto%3Arecid%3A"+iid
        json = req.get(url).json()
        for el in json["hits"]["hits"]:
            liids.append(el["id"])
        return liids

    def request(self,command, output="cit+date+title", sort="mostrecent", size=1000, **args):
        out = []
        newcommand = "?sort="+sort+"&size="+str(size)
        if "subject" in args.keys():
            newcommand+="&subject="+args["subject"]
        if "arxiv_categories" in args.keys():
            newcommand+="&arxiv_categories="+args["arxiv_categories"]
        if "arxiv_categories" in args.keys():
            newcommand+="&arxiv_categories="+args["arxiv_categories"]
        #replace spaces and +
        command = command.replace(" ","%20")
        command = command.replace("+","%2B")
        newcommand+="&q="+command
        url=self.urlapi+newcommand
        print(url)
        json = req.get(url).json()
        print("Number of references found:",len(json["hits"]["hits"]))
        for el in json["hits"]["hits"]:
            data=[]
            if output.find("cit")>=0:
                data.append(el["metadata"]["citation_count"])
            if output.find("date")>=0:
                if "preprint_date" in el["metadata"]: data.append(el["metadata"]["preprint_date"])
                elif "publication_info" in el["metadata"] and len(el["metadata"]["publication_info"])>0:  data.append(el["metadata"]["publication_info"][0].get("year","0"))
                elif "legacy_creation_date" in el["metadata"]:  data.append(el["metadata"]["legacy_creation_date"])
            if output.find("id")>=0:
                data.append(el["id"])
            if output.find("title")>=0:
                data.append(el["metadata"]["titles"][0]["title"])
            out.append(data)
        return out


    def getDocType(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        return self.json["metadata"]["documentation_type"]
   
    def getDate(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        return self.json["metadata"].get("preprint_date","0-0-0")


    def getReferences(self,iid):
        if not self.check(iid):
           self.LoadJson(iid)
        ref = []
        for el in self.json['metadata']['references']:
            if 'record' not in el.keys(): continue
            ref.append(el['record']["$ref"].split("/")[-1])
        return ref



