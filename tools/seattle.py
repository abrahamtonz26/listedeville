# -*- coding: utf-8 -*-
import re
SLUG='seattle'; NAME='Seattle'
MD='/home/claude/out/liste-de-ville-seattle-2026.md'
OUT_HTML='/home/claude/out/liste-de-ville-seattle-2026-magazine.html'
OUT_PDF='/home/claude/out/liste-de-ville-seattle-2026.pdf'
IMG_DIR='/home/claude/img_seattle'; COVERBAND='/home/claude/coverband_seattle.jpg'
H1='Se<i>attle</i>'
TAG='The best of the best in the city — must-visit, unique, a rockstar in its own right. The first edition, and the last of the eight.'
MAST='No. 9 · liste de ville / Seattle · Fall/Winter 2026'
FOOTER='Honestly Speaking  ·  liste de ville / Seattle  ·  Fall/Winter 2026'
TITLE='Honestly Speaking — liste de ville / Seattle, Fall/Winter 2026'
STATS=[('2','James Beard 2026 finalists — Atoma and Surrell',True),('13','James Beard 2026 semifinalists',True),('1950',"Canlis — the room, the valet, the view",False)]
RANK_LEGEND='<span><span class="jbf">JBF 2026</span> James Beard finalist or semifinalist</span><span><span class="note">RoY</span> Seattle Met Restaurant of the Year</span>'
COLOPHON="Compiled by Tony Abraham against Yelp, Google, The Seattle Times, Seattle Met, Eater Seattle, OpenTable, Resy and Tock. Michelin does not cover Seattle; the James Beard Foundation's 2026 awards are the cross-check. Cover: the Space Needle at dusk, via Pexels."
AUTHOR_EXTRA="Based in New York, with field notes from all around. <em>liste de ville / Seattle</em> is the eighth and last city guide of the first series — a city Michelin has never rated, which makes the Beard lists, the oyster farms and the coffee lineage the map."
AUTHOR_SMALL='First edition, Fall/Winter 2026. The eight-city series is complete.'
OCC_LEGEND='occasion (editorial, by category and price)'
SEARCH_HINT='(try “oysters”, “Ballard”, “omakase”)'
DECKS = {
 "Cafés & all-day / chef's neighborhood spots": "Beacon Hill's Beard row, Renee Erickson's rooms, and the Capitol Hill counters that run the city.",
 "Speakeasies & hidden bars — descending order of amazingness": "Through a diner, behind a doorbell, into a tiki submarine. Ranked, loosely, by the drink.",
 "Rooftop bars": "The Needle, the Sound, Lake Union — and the beer gardens and piers that do the same job at water level.",
 "Bars — notable mentions": "A Beard-nominated bar in Belltown, the largest spirits collection in the hemisphere, and the saloons since 1888.",
 "Coffee shops": "Where the American espresso bar was born, from Café Allegro in 1975 to the Roastery.",
 "Restaurants": "No Michelin, so: two Beard finalists, thirteen semifinalists, the oyster counters, the Chinatown–ID institutions, and Canlis since 1950.",
 "Brunch spots": "Portage Bay's toppings bar, Glo's line, dim sum in the ID, and the Ballard croissant.",
 "Off-beat & only-in-Seattle": "Fish throwers, a gum wall, an espresso window since 1980, and Bruce Lee's booth.",
 "Bakeries": "The twice-baked croissant, a Beard-nominated pastry chef, Scandinavian Ballard, and mochi doughnuts in the ID.",
 "Dessert bars & sweets": "For after — or instead of — dinner.",
 "Notable mentions — scene dining, lounges & supper clubs": "Where the room is the point: Canlis, the Nest, the Edgewater, and the tasting counters.",
 "Dance clubs & nightlife": "Capitol Hill's rooms, the Crocodile since 1991, the Showbox since 1939.",
}
ABOUT = {
 "Cafés": ("Seattle's neighborhood rooms are the city's best: Atoma, Little Beast, Musang and Homer — four of the Beard semifinalists — plus Renee Erickson's Walrus, Whale Wins and Bateau, and the Capitol Hill counters.",
           "Picked for the room you'd return to on a weeknight. Nine of Seattle's fifteen 2026 James Beard semifinalists are on this list; Atoma is the finalist and Seattle Met's 2024 Restaurant of the Year."),
 "Speakeasies": ("Seattle hides its bars behind a diner (Roxy's), a doorbell (Knee High), an alley door (Bathtub Gin) and inside a tiki submarine (Inside Passage). Canon has more bottles than any bar in the hemisphere.",
           "Ranked by the drink. Roquette and Rob Roy are the 2026 Beard semifinalists; Zig Zag is where Murray Stenson made the Last Word famous again. The closed ones are listed so you know what the scene lost."),
 "Rooftops": ("A city of water more than roofs: the Nest over Pike Place and the Sound, Mbar's Needle view, Westward's fire pit on Lake Union — and the beer gardens and piers that do the same job.",
           "Chosen for the view first, stretched to include the waterfront decks and the breweries' gardens. Kerry Park with a DeLaurenti picnic is on because it's the view, and it's free."),
 "Bars": ("A serious cocktail city since Zig Zag and Rob Roy — Anu Apte is a Beard semifinalist, Roquette too — with saloons since 1888 and a beer culture that gave the country its IPA lineage.",
           "Ranked and recognized first, then institutions, hotel bars, dives, wine, beer. Jules Maes, Central Saloon and J&M for history; Fremont and Holy Mountain for the beer; Le Caviste for the wine."),
 "Coffee": ("The American espresso bar was born here — Café Allegro in 1975, Starbucks' first store, Vivace's latte art — and the third-wave rooms carry it on. Victrola and Vivace are the pilgrimages; Milstead is the multi-roaster.",
           "Selected for the cup and the room. The bakeries that double as cafés — Bakery Nouveau, Temple, Sea Wolf, Besalu — are the best mornings in the city."),
 "Restaurants": ("Michelin has never rated Seattle, so the map is the James Beard lists — two finalists, thirteen semifinalists — plus the oyster counters, the Chinatown–ID institutions since 1904, and Canlis since 1950.",
           "Grouped by recognition, then the classics and the neighborhoods. The Pham sisters' Pho Bac family is the most-honored restaurant group in the city; Oriental Mart is a James Beard America's Classic in a market stall."),
 "Brunch": ("Portage Bay's toppings bar, the line at Glo's since 1985, Toulouse Petit's Creole, and dim sum at Jade Garden.",
           "Kept to places that consistently top Resy and OpenTable's weekend demand plus the counters you walk into. Temple Pastries is the Beard-nominated pastry stop."),
 "Off-beat": ("The fish throwers and the gum wall, an espresso window since 1980, Bruce Lee's booth at Tai Tung, a sandwich argument in Ballard, and oyster farms an hour south.",
           "Selected for singularity. Oriental Mart is a Beard America's Classic in a Pike Place stall; the Herbfarm is the nine-course pilgrimage; Hama Hama is the oyster saloon on the Hood Canal."),
 "Bakeries": ("Bakery Nouveau's twice-baked croissant, Temple's Beard-nominated pastry, Ballard's Scandinavian kringle, and mochi doughnuts in the ID.",
           "Chosen on the strength of one signature item each. Three Girls has been in the market since 1912; Larsen's since 1974."),
 "Dessert": ("Molly Moon's honey lavender, Fran's salted caramel, Theo's factory, Hood Famous' ube cheesecake, and Canlis's finale.",
           "A mix of the destination and the institution. Fran's at the airport is the last stop for a reason."),
 "Scene": ("Where the room is the point: Canlis and its valet since 1950, the Nest over the market, the Edgewater on the water, and the tasting counters.",
           "Canlis leads; the hotel bars and the water follow. The Herbfarm and Passage on Whidbey are the drive-and-stay rooms."),
 "Nightlife": ("Capitol Hill's rooms — Q, Kremwerk, Neumos — the Crocodile since 1991, the Showbox since 1939, and the jazz at Dimitriou's.",
           "Venues and clubs together. Re-bar, the Baltic Room and R Place are listed closed; Wildrose is on for being one of the last lesbian bars in the country."),
}
R="""Atoma|Little Beast Ballard|The Wayland Mill|Café Suliman|Musang|Homer|Pancita|Ramie|Le Caviste|The Walrus and the Carpenter|The Whale Wins|Bateau|Westward|Spinasse|Artusi|Tavolàta|How to Cook a Wolf|Marmite|L'Oursin|JuneBaby|Off Alley|Lark|Altura|Cafe Juanita|Copine|Barnacle|Rupee Bar|Stoneburner|Sawyer|Bar del Corso|Delancey|Essex|Vif|Manolin|Rock Creek|Eight Row|Nue|Oddfellows Café|Oddfellows|Bar Ferdinand|Taylor Shellfish Oyster Bar|Taylor Shellfish|Damn the Weather|Ben Paris|Le Pichet|Café Campagne|Matt's in the Market|Sushi Kashiba|Roquette|Rob Roy|Canon|Bathtub Gin & Co|Needle & Thread|Tavern Law|Zig Zag Café|Knee High Stocking Co|Foreign National|Deep Dive|Herb & Bitter|The Doctor's Office|Bar Vacilando|ShibShib|Pennyroyal|The Fireside Room|Bookstore Bar|The Nest|Mbar|Frolik|Fog Room|Loupe Lounge|Little Water Cantina|Marination Ma Kai|Salty's on Alki|Ray's Boathouse|Bar Harbor|Daniel's Broiler|Chinook's|Maximilien|The Pink Door|Cutters Crabhouse|Elliott's Oyster House|Six Seven|Aqua by El Gaucho|Anthony's HomePort|Agua Verde|Ivar's Salmon House|Canlis|Betty|Toulouse Petit|The Sexton|Smith Tower Observatory Bar|Liberty|Montana|Tin Lizzie Lounge|The Georgian|Shuckers|Oliver's Lounge|Palisade|Light Sleeper|Bottlehouse|Aerlume|Surrell|Archipelago|Tomo|Taneda Sushi in Kaiseki|Wataru|Kisaku|Maneki|The Harvest Vine|The Herbfarm|Passage|Eden Hill|Mamnoon|Ba Bar|Pho Bac Súp Shop|The Boat|Phocific Standard Time|Communion|Il Nido|Tutta Bella|Dino's Tomato Pie|Serious Pie|Lupo|Moto Pizza|Emmett Watson's Oyster Bar|Il Bistro|Place Pigalle|Chan|Tai Tung|Kedai Makan|Little Uncle|Bai Tong|Kin Len|Monsoon|Tamarind Tree|Cafe Selam|Delish Ethiopian Cuisine|Island Soul|Geo's Cuban & Creole|Mezcaleria Oaxaca|La Carta de Oaxaca|Lowell's|Metropolitan Grill|El Gaucho|Mashiko|Skillet Diner|Tallulah's|Coastal Kitchen|Volunteer Park Cafe|Café Presse|The Fat Hen|Roxy's Diner|Silence-Heart-Nest|Voula's Offshore Cafe|Mr. West Cafe Bar|Lola|Palace Kitchen|Citizen|Geraldine's Counter|Ascend Prime|The Ruins|Washington Athletic Club|Bar House|Radiator Whiskey|Neumos|Barboza|The Crocodile|Showbox|Showbox SoDo|Tractor Tavern|Sunset Tavern|Conor Byrne|The Royal Room|Dimitriou's Jazz Alley|The Triple Door|Musicquarium|Vermillion|Chop Suey|Clock-Out Lounge|Substation|Nectar Lounge|High Dive|The Rabbit Box|Foundation Nightclub|Ora Nightclub|Massive|Queer/Bar""".split("|")
T="""Canlis|Archipelago|Surrell|Taneda Sushi in Kaiseki|Wataru|Sushi Kashiba|The Herbfarm|Passage|Tomo|Off Alley|Homer|Atoma""".split("|")
S="""Q Nightclub|Kremwerk / Timbre Room / Cherry|Supernova|Monkey Loft""".split("|")
W="""Un Bien|Paseo|Frelard Tamales|Pike Place Market|Oriental Mart|Piroshky Piroshky|Beecher's Handmade Cheese|Beecher's|The Crumpet Shop|Ellenos Greek Yogurt|Ellenos|Rachel's Ginger Beer|The Gum Wall|Monorail Espresso|Dick's Drive-In|Ivar's Acres of Clams|Ivar's|Ezell's Famous Chicken|Ezell's|Salumi|Tat's Deli|Tat's|Uwajimaya|Fuji Bakery|Hood Famous Cafe + Bar|Hood Famous|Pho Bac Súp Shop|Jules Maes Saloon|Jules Maes|Georgetown Trailer Park Mall|Fremont Sunday Market|The Fremont Troll|Theo Chocolate factory tour|Theo Chocolate|Ballard Farmers Market|Ballard Locks + Ray's afterward|Fishermen's Terminal + Chinook's|Wild Salmon Seafood Market|Mutual Fish|Seattle Fish Guys|Marination|El Camión|Tacos Chukis|Thai Tom|Café Allegro|Espresso Vivace|Starbucks Reserve Roastery|The original Starbucks|Top Pot Doughnuts|Top Pot|Husky Deli|Molly Moon's|Frankie & Jo's|Salt & Straw Seattle|Salt & Straw|Taylor Shellfish farm|Hama Hama Oyster Saloon|Beth's Café|Jade Garden|Harbor City|Dough Zone|Din Tai Fung|Shanghai Garden|Mike's Noodle House|Szechuan Noodle Bowl|Pike Place Chowder|Red Mill Burgers|Li'l Woody's|Fat's Chicken and Waffles|Portage Bay Cafe|Biscuit Bitch|Glo's|Cafe Besalu|Larsen's|Larsen's Bakery|Hattie's Hat|Sea Wolf|Sea Wolf Bakers|Macrina|Macrina Bakery|5 Point Café|Easy Street Records Café|Bakery Nouveau|Temple Pastries|Coyle's Bakeshop|Crumble & Flake|Byen Bakeri|Le Panier|Three Girls Bakery|Grand Central Bakery|Columbia City Bakery|Tall Grass Bakery|Yummy House Bakery|Mee Sum Pastry|General Porpoise|Mighty-O|Mighty-O Donuts|Daily Dozen Doughnuts|Frost Doughnuts|Salmonberry Goods|Deep Sea Sugar & Salt|Hello Robin|Hot Cakes|Nuflours|Sugar Bakery & Café|North Hill Bakery|Le Rêve|Hiroki|Fresh Flours|Lazy Cow Bakery|Ben's Bread|Raised Doughnuts|Dochi|85°C|Sheng Kee|Regent Bakery|La Parisienne|Belle Epicurean|Hitchcock Deli|Blackbird Bakery|Seattle Bagel Bakery|Rubinstein Bagels|Zylberschtein's|Little Oddfellows|The Flour Box|Victrola|Caffè Vita|Analog Coffee|Anchorhead Coffee|Elm Coffee Roasters|Zeitgeist|Storyville|Ghost Alley Espresso|Milstead & Co|Lighthouse Roasters|Fremont Coffee Company|Herkimer Coffee|Zoka|Ballard Coffee Works|Slate Coffee|Caffè Umbria|Olympia Coffee|Boon Boona|Coffeeholic House|Empire Espresso|Squirrel Chops|Cortona Café|Tougo Coffee|Broadcast Coffee|Union Coffee|Porchlight Coffee & Records|Ada's Technical Books & Café|Full Tilt|Fainting Goat Gelato|Gelatiamo|Bottega Italiana|Shug's Soda Fountain|Sweet Alchemy|Parfait|Fran's Chocolates|Dilettante|Intrigue Chocolate|Indi Chocolate|Oasis Tea Zone|Don't Yell at Me|Sharetea|Yifang|Snowy Village|Meet Fresh|Beard Papa's|Uwajimaya's bakery counter|Fran's at the airport|Sun Liquor|Rumba|Inside Passage|Navy Strength|No Anchor|The Backdoor at Roxy's|Hazlewood|Life on Mars|Vito's|The Pine Box|Good Bar|Central Saloon|J&M Café|Merchant's Café|Linda's Tavern|The Comet|Unicorn / Narwhal|Unicorn|Cha Cha Lounge|Shorty's|The Crocodile's Here-After|King's Hardware|Al's Tavern|Blue Moon Tavern|The Whisky Bar|The Smoke Shop|The Dubliner|Brouwer's Café|Brouwer's|Nickerson Street Saloon|Mecca Café|Ozzie's|Rendezvous|Beveridge Place Pub|West 5|Marco Polo Bar & Grill|Dynasty Room|Tinte Cellars|Eight Bells Winery|Fremont Brewing|Stoup Brewing|Stoup|Reuben's Brews|Lucky Envelope|Obec|Holy Mountain|Cloudburst|Optimism Brewing|Optimism|Chuck's Hop Shop|Machine House Brewery|Machine House|Georgetown Brewing|Rhein Haus|Fair Isle Brewing|Urban Family|Ravenna Brewing|Cactus|Pier 62's Overlook Walk|The Crab Pot|Kerry Park + a picnic from DeLaurenti|Add-a-Ball|Pony|The Cuff Complex|Neighbours|Wildrose|Rock Box|9 Million in Unmarked Bills|Climate Pledge Arena|Paramount Theatre|Moore Theatre|The Vera Project|Tomo's bar""".split("|")
PLAT={}
for lst,tag in ((W,'Walk-in'),(S,'SevenRooms'),(R,'Resy'),(T,'Tock')):
    for n in lst:
        n=n.strip()
        if n: PLAT[n]=tag
for n in ("Metropolitan Grill","El Gaucho","Aqua by El Gaucho","Daniel's Broiler","Six Seven","Palisade","Ray's Boathouse","Salty's on Alki","Elliott's Oyster House","Ivar's Salmon House","Anthony's HomePort","Chinook's","Cutters Crabhouse","Maximilien","The Pink Door","Lola","Palace Kitchen","Serious Pie","Toulouse Petit","Ascend Prime","Monsoon","Din Tai Fung Bellevue","Dimitriou's Jazz Alley","The Triple Door","Loupe Lounge","The Georgian","Shuckers","Oliver's Lounge"): PLAT[n]='OpenTable'
def lookup(name):
    if name in PLAT: return PLAT[name]
    base=name.split(' (')[0].strip()
    return PLAT.get(base)
PRICE_OVER={"Canlis":4,"Atoma":3,"Surrell":4,"Archipelago":4,"Musang":3,"Homer":3,"Pancita":3,"Ramie":3,"Little Beast Ballard":2,"The Wayland Mill":3,"Café Suliman":2,"Tomo":4,"Sushi Kashiba":4,"Taneda Sushi in Kaiseki":4,"Wataru":4,"Kisaku":3,"Maneki":2,"Off Alley":4,"The Harvest Vine":3,"Altura":4,"Spinasse":3,"Lark":3,"Bateau":4,"The Walrus and the Carpenter":3,"The Whale Wins":3,"Westward":3,"JuneBaby":3,"Cafe Juanita":4,"The Herbfarm":4,"Passage":4,"Copine":4,"Eden Hill":4,"Mamnoon":3,"Metropolitan Grill":4,"El Gaucho":4,"Aqua by El Gaucho":4,"Daniel's Broiler":4,"Six Seven":4,"Palisade":3,"Ascend Prime":4,"Le Caviste":2,"Roquette":2,"Rob Roy":2,"Canon":3,"Zig Zag Café":2,"Deep Dive":3,"The Nest":3,"Mbar":3,"Loupe Lounge":4,"Dick's Drive-In":1,"Un Bien":1,"Paseo":1,"Ezell's Famous Chicken":1,"Ezell's":1,"Tat's Deli":1,"Salumi":1,"Tai Tung":1,"Piroshky Piroshky":1,"Beecher's":1,"The Crumpet Shop":1,"Pike Place Chowder":1,"Oriental Mart":1,"Thai Tom":1,"Tacos Chukis":1,"Marination":1,"El Camión":1,"Pho Bac Súp Shop":1,"The Boat":1,"Jade Garden":2,"Harbor City":2,"Ivar's Acres of Clams":2,"Ivar's":2,"Central Saloon":1,"J&M Café":1,"Jules Maes Saloon":1,"Jules Maes":1,"Blue Moon Tavern":1,"Linda's Tavern":1,"The Comet":1,"Shorty's":1,"Hattie's Hat":1,"5 Point Café":1,"Mecca Café":1,"Q Nightclub":3,"Kremwerk / Timbre Room / Cherry":2,"Supernova":2,"Monkey Loft":2,"The Crocodile":2,"Showbox":3,"Dimitriou's Jazz Alley":3,"The Triple Door":3,"Bakery Nouveau":1,"Temple Pastries":1,"Molly Moon's":1,"Fran's Chocolates":1,"Top Pot":1,"Espresso Vivace":1,"Café Allegro":1,"Starbucks Reserve Roastery":1,"The original Starbucks":1,"Husky Deli":1,"Beth's Café":1,"The Ruins":4,"Washington Athletic Club":4}
def occasions(name, cat=None, price=0):
    o=[]
    if cat=='Restaurants':
        if price>=4: o=['Romantic','Date night']
        elif price==3: o=['Date night']
        elif price==2: o=['Casual','Date night']
        else: o=['Casual']
        if name in ('The Walrus and the Carpenter','Little Beast Ballard','Tutta Bella','Bar del Corso','Delancey','Serious Pie','Jade Garden','Harbor City','Din Tai Fung','Dough Zone','Toulouse Petit','Ivar\'s Acres of Clams','Elliott\'s Oyster House','Ray\'s Boathouse','Salty\'s on Alki','Marination Ma Kai','Rhein Haus'): o=o+['Group']
    elif cat=='Cafés': o=['Date night','Casual'] if price>=2 else ['Casual']
    elif cat=='Speakeasies': o=['Date night','Late night']
    elif cat=='Bars':
        o=['Late night'] if price<=1 else ['Date night','Late night']
        if 'Brew' in name or name in ('Fremont Brewing','Stoup','Reuben\'s Brews','Holy Mountain','Cloudburst','Optimism','Chuck\'s Hop Shop','Machine House','Georgetown Brewing','Brouwer\'s','The Pine Box','Rhein Haus','Fair Isle Brewing','Urban Family','Ravenna Brewing'): o=['Group','Casual']
        if name in ('Roquette','Rob Roy','Canon','Le Caviste','Zig Zag Café','Deep Dive','The Doctor\'s Office','Pennyroyal','The Fireside Room','Bookstore Bar','The Georgian','Oliver\'s Lounge','L\'Oursin','Vif','Bar Ferdinand','Artusi','Light Sleeper'): o=['Romantic','Date night']
    elif cat=='Rooftops': o=['Date night','Group']
    elif cat=='Coffee': o=['Sweets','Brunch']
    elif cat=='Brunch': o=['Brunch']
    elif cat=='Off-beat': o=['Casual']
    elif cat=='Bakeries': o=['Sweets','Brunch']
    elif cat=='Dessert': o=['Sweets']
    elif cat=='Scene': o=['Group','Date night'] if price<=3 else ['Romantic','Group']
    elif cat=='Nightlife': o=['Late night','Group']
    return o
from cities.seattle_itin import ITINS, GOTCHAS
NOTES_HTML='''<p>Michelin does not publish a Seattle guide, so the James Beard Foundation's 2026 awards are the cross-check. Seattle's finalists were Johnny Courtney of Atoma and Aaron Tekulve of Surrell for Best Chef: Northwest and Pacific — neither won (Portland's Nodoguro did), extending a shutout that dates to Brady Williams's 2019 win at Canlis. The semifinalists were Archipelago (Outstanding Chef), Café Suliman (Emerging Chef), Little Beast Ballard and the Wayland Mill (Best New Restaurant), Temple Pastries (Outstanding Pastry Chef), Le Caviste (Wine), Roquette (Outstanding Bar), Anu Apte of Rob Roy (Cocktail Service), and Musang, Homer, Pancita and Ramie (Best Chef). The Pham sisters of Pho Bac were Outstanding Restaurateur finalists in 2024 and 2025. Seattle Met's Restaurants of the Year — Atoma (2024), Little Beast (2025) — are marked RoY; Oriental Mart holds a James Beard America's Classic.</p><p>Occasion chips for Seattle are editorial assignments, by category and price. Tock runs the tasting counters (Canlis, Archipelago, Surrell, the Herbfarm); Resy the neighborhood rooms; the Amex credit works at both.</p><p>Photography via Pexels (royalty-free): three photographs, cropped and reused across the twelve sections.</p>'''
