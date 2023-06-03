import os;
import json;

with open("metadata.json", "w") as txt:
    txt.write(json.dumps(list(set(map(lambda x: x.split(".")[0], os.listdir('data'))))))
