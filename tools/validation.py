from core.pyInspire import *
import inspect

# Validation of pyInspire class

print("## Validation of pyInspire class ##")
iid = "1231738"
print("#   test done on inspire id: ",iid)

insp = pyInspire()
out = inspect.getmembers(pyInspire, predicate=inspect.isfunction)
print("Test all methods starts by get ") 
for f in out:
    if f[0].startswith("get") and f[0]!="getDocType":
        print(f[0])
        getattr(insp,f[0])(iid)

print("## if there was no exception, it is validated")


