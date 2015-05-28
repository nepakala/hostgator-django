import math
import re
import unirest
import json

class NumpyAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray) and obj.ndim == 1:
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def readlocations(fname):
    print('reading in json')
    f = open(fname,'r')
    locations = json.loads(f.read())
    f.close()
    return locations

def fillLatLon(locations):
    print('getting new locations if necessary')
    for location in locations:
        if 'latlon' in location:
            location['latlon'] = list(location['latlon'])
        else:
            print('getting location data')
            city = location['location']
            response = unirest.get("https://montanaflynn-geocoder.p.mashape.com/address?address="+city,
                                   headers={
                                       "X-Mashape-Key": "KZE1CO4Mn7mshjabQzICrvp0grcSp1P4tgfjsnMW4yBZK1vhU7",
                                       "Accept": "application/json"
                                   }
            )
            latlon = list(map(float,[response.body['latitude'],response.body['longitude']]))
            location['latlon'] = latlon

def writelocations(fname,locations):
    print('writing out json')
    f = open(fname,'w')
    f.write(json.dumps(locations,indent=4, separators=(',', ': ')))
    f.close()

def readmaps(fnameLatLon,fnameRaw):
    print('reading in maps')
    f = open(fnameLatLon,"r")
    rawsvg = f.read()
    f.close()
    
    f = open(fnameRaw,"r")
    rawsvgnocoords = f.read()
    f.close()
    return rawsvg,rawsvgnocoords

def makeMaps(locations,rawsvg,rawsvgnocoords):

    teststring = '    <circle cx="91.27999999999997" cy="75.34222222222223" r="2" class="nodata" />'
    re.findall('c[xy]="([0-9\.]+)"',teststring)
    
    allcoords = []
    for line in rawsvg.split("\n"):
        if "circle" in line:
            # allcoords.append(re.findall('c[xy]="([0-9\.]+)"',line))
            allcoords.append(re.findall('l[aton]+="([-0-9\.]+)"',line))
    
    print(len(allcoords))
    
    allcoordsfloats = list([map(float,x) for x in allcoords])
    
    print(allcoordsfloats[:10])
    
    bestIndexes = []
    
    for i,location in enumerate(locations):
        coords = [location.lat,location.lon]
        print(coords)
        mindis = 100000
        bestcoords = [0,0]
        bestindex = 0
        for j in range(len(allcoordsfloats)):
            mapcoords = allcoordsfloats[j]
            # print(mapcoords)
            dis = math.sqrt((coords[0]-mapcoords[1])**2+(coords[1]-mapcoords[0])**2)
            # print(dis)
            if dis < mindis:
                # print('found better match')
                # print(dis)
                mindis = dis
                bestcoords = mapcoords
                bestindex = j
                # print(bestcoords)
        print(mindis)
        print(bestindex)
        bestIndexes.append(bestindex)
    
    print(bestIndexes)
    
    header = '<svg id="map" width="652" height="470.8888888888889">\n'
    footer = '</svg>\n'
    
    boilerplate = """<img src="{0}" />
    <h2>{1}</h2>
    <p>{2}</p>"""
    
    print('printing out new files')
    

    newmapstring = ''
    newhtmlstring = ''
    newmapstring = newmapstring + header
    first = True
    for i,line in enumerate(rawsvgnocoords.split("\n")[1:-1]):
        if i in bestIndexes:
            # print(i)
            # print(bestIndexes.index(i))
            if first:
                newhtmlstring = newhtmlstring + "<div class=\"item active\" city=\""+locations[bestIndexes.index(i)].location+"\">"
                first=False
            else:
                newhtmlstring = newhtmlstring + "<div class=\"item\" city=\""+locations[bestIndexes.index(i)].location+"\">"
            thisdata = locations[bestIndexes.index(i)]
            newhtmlstring = newhtmlstring + boilerplate.format(thisdata.imagelink,thisdata.name,thisdata.description)
            newhtmlstring = newhtmlstring + "\n</div>\n"
            
            newmapstring = newmapstring + line.replace("nodata","data") + "\n"
        else:
            a = line.replace("nodata","data")
            newmapstring = newmapstring + a.replace("data","nodata") + "\n"
    newmapstring = newmapstring + footer

    return newmapstring,newhtmlstring
    
if __name__ == '__main__':    
    locations = readlocations('locations.json')
    fillLatLon(locations)
    writelocations('locations.json',locations)
    rawsvg,rawsvgnocoords = readmaps("mapdata/rawsvgmaplatlon","mapdata/rawsvgmap")
    
    newmapstring,newhtmlstring = makeMaps(locations,rawsvg,rawsvgnocoords)

    f = open("newmap","w")
    g = open("newhtml","w")
    f.write(newmapstring)
    g.write(newhtmlstring)
    f.close()
    g.close()






