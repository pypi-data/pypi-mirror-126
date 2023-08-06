

from lotusops.speedtest.jsonformat import string2datetime,msg2sectorId
# in:  2021-07-26T11:32:54.442
# out: datetime.datetime(2021, 7, 26, 11, 32, 54)
import datetime
def string2datetime(st):
    return datetime.datetime.strptime(st, "%Y-%m-%dT%H:%M:%S.%f")

def analyzeFile(filepath,filters):
    sector,sectors={},{}
    with open(filepath,"r") as f:
        lines=f.readlines()
        for line in lines:
            if any(filter not in line for filter in filters): continue
            # structed=line.strip("\t")
            msg = line.rstrip("\n")
            if not any(mark in msg for mark in ["start","finish"]): continue
            time=string2datetime(msg.split()[0])
            # in cse of precommit2
            if any("commit_phase2" in filter for filter in filters):
                if "start" in msg: sector["start"]=time;continue
                if "finish" in msg: sector["finish"]=time
                if all(key in sector for key in ["start","finish"]): 
                    sector["period"]=sector["finish"]-sector["start"]
                    print("duration:{0}    start:{1} finish:{2}".format(sector["period"],sector["start"],sector["finish"]))
                    sectors[sector["start"]]=sector
                sector={};continue
            # in case of precommit1, commit2
            id = msg2sectorId(msg)
            if id < 0: continue
            if id not in sectors.keys(): sectors[id]={}
            if "start" in msg: sectors[id]["start"]=time;continue
            if "finish" in msg: sectors[id]["finish"]=time
            if all(key in sectors[id] for key in ["start","finish"]): 
                sectors[id]["period"]=sectors[id]["finish"]-sectors[id]["start"]
                print("SectorId({0})- duration:{1}    start:{2} finish:{3}".format(id,sectors[id]["period"],sectors[id]["start"],sectors[id]["finish"]))
        # analyze
        import datetime
         ## max, min, mean
        max_=datetime.timedelta(0)
        min_=datetime.timedelta(days=10)
        mean_=datetime.timedelta(0)
        ## initialize
        sum=datetime.timedelta(0)
        cnt=0
        for k,v in sectors.items():
            if "period" not in v.keys(): continue
            cnt+=1
            if v["period"] < min_: min_= v["period"]
            if v["period"] > max_: max_= v["period"]
            sum+=v["period"]
        mean_=sum/cnt if cnt!=0 else sum
        print("*******************************************")  
        print("MIN:  {0}".format(min_))
        print("MAX:  {0}".format(max_))
        print("MEAN: {0}".format(mean_))
        print("*******************************************")        

