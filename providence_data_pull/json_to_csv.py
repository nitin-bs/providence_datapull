import json
data=json.load(open('hosts.json',))
outfile=open('hosts.csv','w')
outfile.write('installationId,public_ip,auth_token\n')
for i in data:
    dict_val=json.loads(i["params"])
    auth_token=dict_val["auth_token"]
    public_ip=dict_val["output"]["public_ip"]
    outfile.write(i['installationId']+','+public_ip+','+auth_token+'\n')
outfile.close()    
#print(i['installationId']+','+i['params']['output']['public_ip'])
    #print("\n")
