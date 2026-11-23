TRIPS_META = [
("Dinosaurs & Zen","1 day","Train & bus","Temple morning, dinosaur afternoon"),
("Cliffs, crab & onsen","1 day","Train & bus","Cliffs, seafood lunch, a hot spring footbath"),
("Samurai city walk","1 day","Walk & bus","Gardens, castle ruins and a lost samurai town"),
("Fukui highlights","2 days","Train & bus","Temple and dinosaurs, then the coast"),
("Zen stay & moss","2 days","Train, bus & taxi","A night by Eiheiji and the moss shrine"),
("Craft towns","2 days","Train & bus","Glasses, lacquer, knives and paper"),
("Best of Fukui","3 days","Rental car","Every highlight, with a dawn castle in the sky"),
("Coast & seafood","3 days","Rental car","Northern cliffs, Echizen Coast, Tsuruga"),
("Grand tour, north to south","4 days","Rental car","The whole prefecture, ending in Wakasa"),
("Deep & unseen","4 days","Rental car","Only the hidden places"),
]
R = """Dinosaurs & Zen|1|9:00|Eiheiji Temple|Eiheiji Liner express bus from Fukui Stn East, about 30 min|Go early, before the tour groups
Dinosaurs & Zen|1|11:30|Lunch in Eiheiji temple town|Walk|Oroshi soba and goma tofu
Dinosaurs & Zen|1|12:30|Fukui Prefectural Dinosaur Museum|Bus to Eiheiji-guchi Stn (about 13 min), Echizen Railway to Katsuyama, then bus (check)|Allow 3 hours
Dinosaurs & Zen|1|16:30|Back to Fukui Stn|Bus about 1 h, or bus + Echizen Railway|Photos with the dinosaur statues outside the station
Dinosaurs & Zen|1|18:00|Dinner: sauce katsudon|Walk near Fukui Stn|
Cliffs, crab & onsen|1|9:00|Ride to Mikuni-minato|Echizen Railway Mikuni-Awara Line from Fukui Stn|
Cliffs, crab & onsen|1|10:00|Tojinbo Cliffs|Bus about 10 min from Mikuni-minato Stn|Add the sightseeing boat
Cliffs, crab & onsen|1|11:30|Echizen Matsushima|Short bus or walk from Tojinbo (check)|The bridge to Oshima reopened in spring 2026
Cliffs, crab & onsen|1|13:00|Lunch in Mikuni|Bus back toward Mikuni (check)|Echizen crab from Nov 6 to Mar 20
Cliffs, crab & onsen|1|15:30|Awara Onsen|Bus to Awara-Onsen (check)|Free footbath, day bath and onsen eggs at Sentopia Awara
Cliffs, crab & onsen|1|18:00|Back to Fukui|Shinkansen from Awara-Onsen, one stop|
Samurai city walk|1|9:00|Yokokan Garden|About 15 min walk from Fukui Stn|Closed Mondays and Dec 29 to end of Feb
Samurai city walk|1|10:30|Fukui castle ruins & city centre|Walk|Cherry-lined river walk in spring
Samurai city walk|1|11:30|Lunch: Echizen oroshi soba|Walk|
Samurai city walk|1|12:30|Ichijodani Asakura Ruins + Museum|Direct bus from Fukui Stn|The museum is good if it rains
Samurai city walk|1|16:00|Asuwayama Park|Bus from Fukui Stn (check)|Free mini zoo. Cherry and autumn views
Samurai city walk|1|18:00|Dinner: sauce katsudon|Walk near Fukui Stn|
Fukui highlights|1|9:00|Eiheiji Temple|Eiheiji Liner from Fukui Stn East, about 30 min|
Fukui highlights|1|12:30|Fukui Prefectural Dinosaur Museum|Bus to Eiheiji-guchi, Echizen Railway to Katsuyama, bus (check)|Allow 3 hours
Fukui highlights|1|18:00|Stay near Fukui Stn|Bus back to Fukui Stn|Sauce katsudon for dinner
Fukui highlights|2|9:00|Tojinbo Cliffs|Echizen Railway to Mikuni-minato, bus about 10 min|
Fukui highlights|2|11:30|Echizen Matsushima|Short bus or walk (check)|
Fukui highlights|2|13:00|Lunch in Mikuni|Bus (check)|Crab in season
Fukui highlights|2|15:30|Awara Onsen, then home|Bus to Awara-Onsen, Shinkansen onward|Footbath before the train
Zen stay & moss|1|9:30|Ichijodani Asakura Ruins + Museum|Direct bus from Fukui Stn|
Zen stay & moss|1|13:30|Eiheiji Temple|Bus (check)|
Zen stay & moss|1|16:00|Check in at Hakujukan|5 min walk from the temple|Zazen or sutra tracing with a Zen concierge
Zen stay & moss|2|6:00|Eiheiji morning sutra service|Short walk|Hotel guests are welcome before breakfast
Zen stay & moss|2|9:30|Fukui Prefectural Dinosaur Museum|Bus to Eiheiji-guchi, Echizen Railway to Katsuyama, bus (check)|
Zen stay & moss|2|13:30|Heisenji Hakusan Shrine|Taxi from the museum area|Moss is greenest after rain
Zen stay & moss|2|16:00|Back to Fukui Stn|Echizen Railway from Katsuyama|
Craft towns|1|9:30|Megane Museum|JR to Sabae, walk (check)|Book the make-your-own-glasses workshop
Craft towns|1|13:00|Nishiyama Park & Zoo|5 min walk from Nishiyama-koen Stn|Red pandas. Zoo closed Mondays
Craft towns|1|15:00|Echizen lacquerware with a craftsman|Kawada, Sabae: bus or taxi (check)|Book ahead
Craft towns|1|18:00|Stay in Takefu|JR to Takefu|
Craft towns|2|9:30|Takefu Knife Village|Bus or taxi from Takefu (check)|Customize your knife handle
Craft towns|2|11:30|Lunch: Volga rice or Takefu chuka soba|Takefu|
Craft towns|2|13:30|Echizen Washi Village + Okamoto & Otaki Shrines|Bus from Takefu (check)|Shrine roof repairs until end of 2026
Craft towns|2|16:30|Home|Shinkansen from Echizen-Takefu Stn|
Best of Fukui|1|9:30|Ichijodani Asakura Ruins + Museum|Car from Fukui Stn|
Best of Fukui|1|12:30|ESHIKOTO|Car|Lunch on the river terrace, sake soft-serve
Best of Fukui|1|14:30|Eiheiji Temple|About 15 min by car from ESHIKOTO|
Best of Fukui|2|9:00|Fukui Prefectural Dinosaur Museum|Car|Book a fossil dig nearby
Best of Fukui|2|13:00|Heisenji Hakusan Shrine|Car|
Best of Fukui|2|14:30|Echizen Daibutsu|Car|Few visitors, huge Buddha
Best of Fukui|2|16:00|Ono castle town & Oshozu spring|Car|Shoyu katsudon for dinner. Stay in Ono
Best of Fukui|3|6:00|Castle in the Sky from Mt Inuyama|Car + about 20 min hike|Oct to Apr only, best in Nov
Best of Fukui|3|10:30|Maruoka Castle|Car|
Best of Fukui|3|12:30|Tojinbo Cliffs + lunch in Mikuni|Car|Crab in season
Best of Fukui|3|15:00|Echizen Matsushima|Car|
Best of Fukui|3|17:00|Awara Onsen|Car|Stay, or drop the car and take the Shinkansen
Coast & seafood|1|10:00|Tojinbo Cliffs|Car from Fukui Stn|
Coast & seafood|1|12:00|Lunch in Mikuni|Car|
Coast & seafood|1|13:30|Brilliant Heart Museum|Car|Reservation needed. Apr to Nov, Fri to Sun
Coast & seafood|1|15:30|Echizen Matsushima|Car|
Coast & seafood|1|17:00|Sunset at Mikuni Sunset Beach|Car|Stay in Awara Onsen
Coast & seafood|2|10:00|Hokojima|Car along the Echizen Coast|Climb to the summit view
Coast & seafood|2|11:30|Benkei's Washing Rock|Car|
Coast & seafood|2|13:00|Echizen Crab Museum|Car|Crab lunch nearby
Coast & seafood|2|15:00|Echizen Misaki Suisen Land|Car|Daffodils late Dec to Feb
Coast & seafood|3|10:00|Kehi no Matsubara|Car to Tsuruga|
Coast & seafood|3|11:30|Kehi Jingu Shrine|Car|
Coast & seafood|3|13:30|Tsuruga Red Brick Warehouses|Car|Tsuruga ramen for lunch
Coast & seafood|3|15:00|Port of Humanity Tsuruga Museum|Car|End at Tsuruga Stn (Shinkansen)
Grand tour, north to south|1|9:00|Yokokan Garden|Car from Fukui Stn|
Grand tour, north to south|1|11:00|Ichijodani Asakura Ruins + Museum|Car|
Grand tour, north to south|1|14:30|Eiheiji Temple|Car|
Grand tour, north to south|2|9:00|Fukui Prefectural Dinosaur Museum|Car|
Grand tour, north to south|2|13:00|Heisenji Hakusan Shrine|Car|
Grand tour, north to south|2|15:30|Echizen Ono Castle & castle town|Car|Stay in Ono
Grand tour, north to south|3|9:30|Takefu Knife Village|Car|
Grand tour, north to south|3|11:30|Echizen Washi Village|Car|Volga rice for lunch in Takefu
Grand tour, north to south|3|14:30|Echizen Pottery Village|Car|
Grand tour, north to south|3|16:30|Sunset at Hokojima|Car|Stay on the Echizen Coast (check)
Grand tour, north to south|4|9:30|Rainbow Line Summit Park (Mikata Five Lakes)|Car to Wakasa|
Grand tour, north to south|4|11:30|Kumagawa-juku|Car|Mackerel lunch
Grand tour, north to south|4|14:00|Sotomo cruise from Wakasa Fisherman's Wharf|Car to Obama|About 1 hour
Grand tour, north to south|4|16:00|Myotsuji Temple, then Tsuruga Stn|Car (check drive time)|Shinkansen home from Tsuruga
Deep & unseen|1|10:00|Hokojima|Car from Fukui Stn|
Deep & unseen|1|11:30|Benkei's Washing Rock|Car|
Deep & unseen|1|13:30|Brilliant Heart Museum|Car|Reservation needed. Apr to Nov, Fri to Sun
Deep & unseen|1|15:30|Echizen Matsushima & Oshima bridge|Car|Bridge reopened spring 2026
Deep & unseen|2|9:30|Ryusogataki Falls|About 40 min by car from Fukui IC|
Deep & unseen|2|11:00|Kazura-bashi vine bridge|Car|
Deep & unseen|2|13:30|Tree Picnic Adventure Ikeda|Car|1 km zipline
Deep & unseen|2|16:00|Mt Heko|Car + 20 min walk|Clear days only
Deep & unseen|3|10:00|Okamoto & Otaki Shrines|Car|Roof repairs until end of 2026
Deep & unseen|3|12:00|Jisagawa River baikamo|Car. Narrow road, no roadside parking|Jul to Aug only
Deep & unseen|3|13:30|Lunch: Takefu chuka soba|Car|
Deep & unseen|3|15:00|Murasaki Shikibu Park|Car|Stay in Ono
Deep & unseen|4|6:00|Castle in the Sky from Mt Inuyama|Car + about 20 min hike|Oct to Apr only
Deep & unseen|4|10:00|Yamabushi-iwa (cat rock)|Car, Route 158, no parking|
Deep & unseen|4|11:30|Oshozu spring & Ono castle town|Car|Shoyu katsudon for lunch, then back to Fukui"""
