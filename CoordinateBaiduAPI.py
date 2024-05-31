
import pandas as pd
import requests
import json
def excel_one_line_to_list():
    df = pd.read_excel(r"C:\Users\Administrator\Desktop\收费站\2021-8-27-10-13-41-4442610865300-【陕西高速收费站一览表】.xlsx", usecols=[0],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    #print(result)
    return result#return返回结果值
if __name__ == '__main__':
        result = excel_one_line_to_list()#接收结果
def getUrl(*address):
    '''
    调用地图API获取待查询地址专属url
    最高查询次数30w/天，最大并发量160/秒
    '''
    ak = '你的key'
    if len(address) < 1:
        return None
    else:
        for add in address:
            url = 'http://api.map.baidu.com/geocoding/v3/?address={inputAddress}&output=json&ak={myAk}'.format(inputAddress=add,myAk=ak)
            yield url
def getPosition(url):
    '''返回经纬度信息'''
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data['status'] == 0:
        lat = json_data['result']['location']['lat'] #纬度
        lng = json_data['result']['location']['lng'] #经度
    else:
        print("Error output!")
        return json_data['status']
    return lat,lng

if __name__ == "__main__":
    address = result
    for add in address:
        add_url = list(getUrl(add))[0]
        print(add_url)
        try:
            lat,lng = getPosition(add_url)
            print("{0}|经度:{1}|纬度:{2}.".format(add,lng,lat))
        except Error as e:
            print(e)