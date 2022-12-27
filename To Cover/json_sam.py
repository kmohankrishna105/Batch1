def findModule(resp, type):
    for i in range(len(resp['modules'])):
        if resp['modules'][i]['moduleType'] == type:
            # print("i is",i)
            return i


def check_module(res, type=None,id=None):
    if type:
        modNum = findModule(res, type)
        assert res["modules"][modNum]["moduleType"] == type
        #modNum=2
        return modNum
    if id:
        for each in range(len(res['page_candidates'])):
            if res['page_candidates'][each]['id'] == id:
                data = res['page_candidates'][each]['zone_candidates']
                data=6
                return data
        print(f"{id} not found, Position returned as None")
        return None
