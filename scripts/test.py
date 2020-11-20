from core.pyInspire import *
import inspect
import matplotlib.pyplot as plt

# Validation of pyInspire class

iid = "1231738"
insp = pyInspire()

print(insp.getNofCitations(iid))


def GetCitationValue(iid,variable="Title",dump=False):
    insp = pyInspire()
    mylist = insp.getCitationList(iid)
    output = []
    for i in mylist:
        out = getattr(insp,"get"+variable)(i)
        output.append(out)
        if dump: print(out)
    return output


#option "single" means looks to all single words individually
#option "" means look to expression
def KeywordsStat(data, option=""):
    # data is a list of list of str
    # merge everything in a single list
    lm = [i for el in data for i in el]
    
    if option=="single":
        lm = [w for el in data for i in el for w in i.replace(":"," ").split()]
    #count occurences
    stat = {el: lm.count(el) for el in lm}
    #sort the results
    for k, v in sorted(stat.items(), key=lambda item: item[1],reverse=True):
        print(k,v)

    #print(stat)


def TrendPlotCitation(data,option="year"):
    #data is a list of dates
    ml=[]
    for el in data:
       ml.append(el.split("-")[0])
    #count occurences
    stat = {el: ml.count(el) for el in ml}
    #sort the results
    years=[]
    nofc=[]
    for k, v in sorted(stat.items(), key=lambda item: item[0]):
        print(k,v)
        year=int(k)
        ncit=int(v)
        if k==0: continue
        if len(years)>0 and year!=(years[-1]+1):
            years.append(years[-1]+1)
            nofc.append(ncit)
        else:
            years.append(year)
            nofc.append(ncit)

    plt.plot(years,nofc)#,xlabel="years",ylabel="#citations/year")
    plt.show()


titles = insp.request("topcite 1000+ t supersymmetry")
#?sort=mostcited&size=25&page=2&q=topcite%20500%2B&subject=Phenomenology-HEP&rpp=Exclude%20Review%20of%20Particle%20Physics&arxiv_categories=hep-ph")
for i in titles:
    print(i)
#out = GetCitationValue(iid,"Date",True)
#TrendPlotCitation(out)
#KeywordsStat()


#iid="1792459"
#out = GetCitationValue(iid,"Keywords",True)
#KeywordsStat(out,"single")


