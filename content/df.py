# Discover Fukui page for each place (path after https://www.fuku-e.com/en/)
_A = "attractions/detail_%s.html"
DF = {k: _A % v for k, v in {
"eiheiji":1089,"heisenji":1105,"dino":1193,"tojinbo":1476,"maruoka":1018,"ichijodani":1002,"mikata":1330,"ono":1004,
"daibutsu":1041,"awara":1580,"yokokan":1153,"eshikoto":5975,"megane":1585,"hokojima":1480,"okamoto":1048,"benkei":4985,
"heko":1544,"city":1016,"ichimuseum":5625,"aquarium":1459,"crabmuseum":1220,"pottery":1315,"skijam":1275,"shibamasa":1319,
"myotsuji":1118,"sancho":1137,"wharf":5204,"kumagawa":1135,"kehi":1062,"humanity":1183,"brick":1124,"kanegasaki":1006,
"shiroyama":1434,"kanazu":1228,"asuwayama":1515,"nishiyama":1462,"yurinosato":1553,"cosmos":1528,"knife":2031,"washi":1131,
"sobavillage":2028,"kawada":6158,"kehimatsu":1471,"matsushima":1466,"suisen":1521,"horossa":1621,
"dinopark":1594,"stndino":1669,"curuf":6449,"yatai":6450,"oshima":1468,"mikuniminato":1146,"daianzenji":1087,"wadabeach":1395,
"foodculture":1209,"chopstick":2006,"varve":1625,"sakanamachi":1408,"eki_echizen":5267,"echizencoast":1624,"mizushima":1391,
"mermaid":1032,"angelland":1238,"kitanosho":1057,"fieldstation":2086,"katsucastle":1169,"yumeole":1192,"gotanjoji":1631,
"saikoji":1645,"ichijotaki":1484,"ranch":1460,"wakasahime":1569,"uriwari":1511,"kuzuryu":1273,"obamacastle":1567,
"takidanji":1090,"yoshizaki":1170,"toriage":5296,"akausagi":5295,"suishohama":1359,"kinoko":1426,"raigoji":1652,
"citymuseum":1204,"prefmuseum":1200,"sankairi":5245}.items()}
DF.update({"umenosato":"shop/detail_7068.html","jinguji":"events/detail_5816.html","uchiyama":"events/detail_5112.html"})
# photos we have permission to use: place id -> (image url, credit). Empty until permission or our own photos.
PHOTOS = {}
