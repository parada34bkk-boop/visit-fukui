import json
exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'places.py')).read()); exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'rest.py')).read()); exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'trips.py')).read()); exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'more.py')).read())
P=P+P2; A=A+A2; F=F+F2; E=E+E2
STOPMAP.update(STOPMAP_MORE)
ids={p[0] for p in P}; assert len(ids)==len(P)
places=[dict(id=p[0],tier=p[1],name=p[2],area=p[3],type=p[4],why=p[5],best=p[6],access=p[7],jp=p[8],lat=p[9],lon=p[10]) for p in P]
acts=[dict(tier=a[0],name=a[1],place=a[2],what=a[3],note=a[4]) for a in A]
foods=[dict(tier=f[0],name=f[1],jp=f[2],what=f[3],where=f[4],places=f[5],months=f[6]) for f in F]
events=[dict(tier=e[0],name=e[1],when=e[2],latest=e[3],where=e[4],note=e[5],place=e[6],months=e[7]) for e in E]
for a in acts: assert a['place'] in ids, a
for f in foods: assert all(x in ids for x in f['places']), f
for e in events: assert e['place'] is None or e['place'] in ids, e
trips=[]
for name,length,mode,blurb in TRIPS_META:
  stops=[]
  for line in R.split('\n'):
    t,d,tm,stop,how,tip=line.split('|')
    if t==name:
      (stop in STOPMAP) or print("unmapped:",name,"|",stop)
      sm=STOP_SEASON.get(stop)
      stops.append(dict(day=int(d),time=tm,stop=stop,how=how,tip=tip,place=STOPMAP.get(stop),months=sm[0] if sm else None,warn=sm[1] if sm else None))
  assert stops, name
  trips.append(dict(name=name,length=length,mode=mode,blurb=blurb,start=TRIP_ENDS[name][0],end=TRIP_ENDS[name][1],stops=stops))
js="".join(f"const {k}="+json.dumps(v,ensure_ascii=False)+";\n" for k,v in [("PLACES",places),("ACTIVITIES",acts),("FOODS",foods),("EVENTS",events),("TRIPS",trips)])
open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','data.js'),'w').write("// Visit Fukui content. Generated from the Visit Fukui content sheet. Coordinates are approximate.\n"+js)
print(len(places),len(acts),len(foods),len(events))
