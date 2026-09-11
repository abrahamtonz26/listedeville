# -*- coding: utf-8 -*-
import re
SLUG='new-orleans'; NAME='New Orleans'
MD='/home/claude/out/liste-de-ville-new-orleans-2026.md'
OUT_HTML='/home/claude/out/liste-de-ville-new-orleans-2026-magazine.html'
OUT_PDF='/home/claude/out/liste-de-ville-new-orleans-2026.pdf'
IMG_DIR='/home/claude/img_new-orleans'; COVERBAND='/home/claude/coverband_new-orleans.jpg'
H1='New <i>Orleans</i>'
TAG='The best of the best in the city — must-visit, unique, a rockstar in its own right. The first edition, in Michelin\'s first year in the South.'
MAST='No. 10 · listedeville / New Orleans · Fall/Winter 2026'
FOOTER='Honestly Speaking  ·  listedeville / New Orleans  ·  Fall/Winter 2026'
TITLE='Honestly Speaking — listedeville / New Orleans, Fall/Winter 2026'
STATS=[('2','Michelin stars at Emeril\'s — the only two-star kitchen in the South',True),('11','Bib Gourmands in Michelin\'s first Southern selection',True),('1840',"Antoine's — the oldest family-run restaurant in America",False)]
RANK_LEGEND='<span><span class="rank">NA50 <b>№6</b></span> North America\'s 50 Best Restaurants</span><span><span class="jbf">JBF 2026</span> James Beard finalist or semifinalist</span>'
COLOPHON="Compiled by Tony Abraham against Yelp, Google, The Times-Picayune, Eater New Orleans, OpenTable, Resy and Tock. Michelin marks reflect the inaugural 2025 American South selection; James Beard marks the 2026 awards. Cover: Canal Street streetcar at dusk, via Pexels."
AUTHOR_EXTRA="Based in New York, with field notes from all around. <em>listedeville / New Orleans</em> is the ninth city guide and the first of the second series — the one American city where the cheapest and the most expensive food are cooked from the same book."
AUTHOR_SMALL='First edition, Fall/Winter 2026. Houston follows.'
OCC_LEGEND='occasion (editorial, by category and price)'
SEARCH_HINT='(try “po\'boy”, “Bywater”, “oysters”)'
DECKS = {
 "Cafés & all-day / chef's neighborhood spots": "Magazine Street's Bibs, the Bywater's wine yard, and the Uptown bistros that run the city on a Tuesday.",
 "Speakeasies & hidden bars — descending order of amazingness": "Behind a hotel lobby, through a gate, under a levee. Ranked, loosely, by the drink — in the city that invented the cocktail.",
 "Rooftop bars": "Not a rooftop city — a courtyard and porch city. The hotel roofs first, then the yards, the levee and the beer gardens.",
 "Bars — notable mentions": "A 50 Best bar in the Quarter, the bar that started the revival on Freret, the oldest bar in the country, and the brass-band rooms.",
 "Coffee shops": "Chicory and beignets since 1862, and the roasters that came after Katrina.",
 "Restaurants": "Michelin's first Southern guide: one two-star, two stars, eleven Bibs — plus the grand rooms since 1840 and the po'boy counters.",
 "Brunch spots": "Jazz brunch at the old houses, biscuits at Willa Jean, praline bacon in the Bywater.",
 "Off-beat & only-in-New Orleans": "Sno-balls on a 1939 machine, a 24-hour deli, a 25-cent martini, the muffuletta's birthplace, and second lines on Sundays.",
 "Bakeries": "King cake from Twelfth Night to Fat Tuesday, doberge, pralines, and a Beard-nominated bakery in the Bywater.",
 "Dessert bars & sweets": "Bananas Foster where it was invented, sno-balls, spumoni since 1905.",
 "Notable mentions — scene dining, lounges & supper clubs": "Where the room is the point: Commander's, Galatoire's on a Friday, the Roosevelt's bar, the Four Seasons on the river.",
 "Dance clubs & nightlife": "Frenchmen Street, Tipitina's since 1977, Preservation Hall, and the Tuesday-and-Thursday brass-band circuit.",
}
ABOUT = {
 "Cafés": ("The rooms you return to on a weeknight: Alon Shaya's Saba, Mason Hereford's Turkey and the Wolf and Hungry Eyes, Justin Devillier's La Petite Grocery, and the Bywater's Bacchanal, where a wine shop became a backyard.",
           "Picked for consistency and the neighborhood. Five of Michelin's eleven Bibs and six of its recommended rooms are on this list; Acamaya, Saint Claire and Evviva are the 2026 Beard names."),
 "Speakeasies": ("New Orleans invented the cocktail and never stopped drinking it. The hidden rooms are hotel salons (Bar Marilou, the Elysian Bar), courtyards (Peychaud's, Cane & Table) and neighborhood bars behind unmarked doors.",
           "Ranked by the drink. Jewel of the South is on North America's 50 Best; Cure is where the revival started in 2009; the historic bars are listed because they're still good, not because they're old."),
 "Rooftops": ("The city is built at sea level, so the views are hotel pools and porches — Hot Tin over St. Charles, the NOPSI's pool, the Four Seasons' river deck — and the courtyards and yards that do the same job under live oaks.",
           "Chosen for the view and the air. The beer gardens and the levee at the Fly are on because a rooftop list here would be short otherwise."),
 "Bars": ("Cocktail bars with real history (Sazerac Bar, Arnaud's French 75, Napoleon House), a new-guard scene that produced a 50 Best bar, and the music rooms where the drink is beside the point.",
           "Recognized first, then institutions, then the neighborhoods. The brass-band bars — Vaughan's, Bullet's, the Maple Leaf, Le Bon Temps — are bars on the right night and shrines the rest of the week."),
 "Coffee": ("Chicory coffee and beignets at Café du Monde since 1862 is the ritual; the third-wave roasters — Congregation, Mammoth, French Truck, Cherry — arrived after Katrina and stayed.",
           "Selected for the cup and the room. The bakery cafés (Bywater Bakery, Levee, Ayu, La Boulangerie) are the best mornings outside the Quarter."),
 "Restaurants": ("Michelin arrived in November 2025 and found what the city knew: E.J. Lagasse's two stars at Emeril's, Saint-Germain and Zasu with one, eleven Bibs that include po'boy shops and a fried-chicken house, and seventeen recommended rooms. Underneath, the grand houses since 1840 and the counters since 1906.",
           "Grouped by the Guide, then the Beard list, then the classics. Dakar NOLA is on North America's 50 Best; Commander's, Galatoire's, Antoine's and Arnaud's are here because they still cook, not because they're museums."),
 "Brunch": ("Jazz brunch is a local invention — Commander's, Arnaud's, Court of Two Sisters — and the modern version is Molly's Rise and Shine, Willa Jean's biscuits and praline bacon at Elizabeth's.",
           "Kept to places with a real kitchen at 10am. Atchafalaya's Bloody Mary bar is the one to book."),
 "Off-beat": ("A 24-hour deli with a po'boy called All That Jazz, a sno-ball machine from 1939, a 25-cent martini lunch, the muffuletta's birthplace, and second lines every Sunday from September to June.",
           "Selected for singularity. Hansen's, Dooky Chase's and Dong Phuong are Beard America's Classics; Mosca's and Middendorf's are the drives worth making."),
 "Bakeries": ("King cake season runs from Twelfth Night to Mardi Gras and the city takes sides: Dong Phuong, Manny Randazzo's, Haydel's, Bywater Bakery. The rest of the year it's doberge, pralines, French pastry on Ursulines and Link's La Boulangerie.",
           "Chosen on the strength of one item each. Bywater Bakery is a 2026 Beard semifinalist for Outstanding Bakery; Lagniappe Bake House was a 2025 finalist."),
 "Dessert": ("Bananas Foster at the Brennan's table where it was invented, bread pudding soufflé at Commander's, spumoni at Brocato's since 1905, and sno-balls from March to Labor Day.",
           "A mix of the destination and the institution. Hansen's is the pilgrimage; Creole Creamery is the neighborhood."),
 "Scene": ("Where the room is the point: Commander's turquoise house, Galatoire's Friday lunch, the Sazerac Bar's murals, the Four Seasons on the river, and the tasting counters that sell out on Tock.",
           "The grand houses lead; the hotel bars and the new supper clubs follow. Jackets after dark at the old rooms."),
 "Nightlife": ("Frenchmen Street is the music district — the Spotted Cat, d.b.a., Snug Harbor — Tipitina's is the shrine, Preservation Hall is the church, and the brass-band circuit runs Tuesday to Thursday in the neighborhoods.",
           "Venues and clubs together. Bourbon Street's gay bars are on for history; the St. Claude rooms for what's happening now."),
}
R="""Saba|Mister Mao|Acamaya|La Petite Grocery|Patois|Osteria Lupo|Herbsaint|Pêche Seafood Grill|Pêche|Cochon|Coquette|Lilette|N7|Justine|Sylvain|Cane & Table|Bayona|Toups' Meatery|The Elysian Bar|Paladar 511|Palm & Pine|Saffron NOLA|Lengua Madre|Bar Frances|Shaya|Saint Claire|Evviva|Gianna|Jack Rose|Vessel|Bywater American Bistro|Delacroix|Zasu|Jewel of the South|Latitude 29|The Columns|Chemin à la Mer|Miss River|Effervescence|Compère Lapin|Clancy's|Lufu|34 Restaurant & Bar|Addis NOLA|Willa Jean|Country Club|Hotel Peter & Paul courtyard|Jack Rose porch|Sylvain courtyard|Cane & Table courtyard|Sylvain brunch|Justine brunch|Compère Lapin brunch|Bywater American Bistro brunch|Jack Rose brunch|Saba brunch|Mister Mao brunch|The Columns porch|Ice cream at Bywater American Bistro|Toasted pineapple rum cake at Compère Lapin|Lemon icebox pie at Clancy's|Bar Frances""".split("|")
T="""Emeril's|Saint-Germain|Dakar NOLA|Mosquito Supper Club|The Kingsway|Dessert at Saint-Germain|Dessert at Emeril's""".split("|")
S="""Bar Marilou|Bar Marilou terrace?""".split("|")
O="""Commander's Palace|Brennan's|Galatoire's|Antoine's|Arnaud's|Restaurant August|Atchafalaya|Café Degas|Rosedale|Domenica|Pizza Domenica|Copper Vine|Court of Two Sisters|Court of Two Sisters courtyard|Brennan's courtyard|Café Amelie|Tujague's|Tujague's balcony|Pascal's Manale|Mr. B's Bistro|Palace Café|Dickie Brennan's Steakhouse|Muriel's|Drago's|Bon Ton Café|Gautreau's|Upperline|Brigtsen's|Boucherie|Dooky Chase's|Irene's|Maypop|Ralph's on the Park|Palm Court Jazz Café|Bombay Club|The Bombay Club|Marigny Brasserie|Josephine Estelle|Josephine Estelle brunch|Seaworthy|Criollo|Tableau|Broussard's|Doris Metropolitan|Desi Vega's Steakhouse|La Boca|GW Fins|Commander's Palace jazz brunch|Brennan's breakfast|The Court of Two Sisters jazz brunch|Arnaud's Sunday jazz brunch|Antoine's jazz brunch|Muriel's jazz brunch|Commander's 25-cent martini lunch|Galatoire's Friday lunch|Antoine's 14 dining rooms|Bananas Foster at Brennan's|Bread pudding soufflé at Commander's|Baked Alaska at Antoine's|Bread pudding at Bon Ton|Bananas Foster at Arnaud's|White chocolate bread pudding at Palace Café|Dooky Chase's lunch buffet""".split("|")
PLAT={}
for lst,tag in ((S,'SevenRooms'),(O,'OpenTable'),(R,'Resy'),(T,'Tock')):
    for n in lst:
        n=n.strip()
        if n: PLAT[n]=tag
def lookup(name):
    if name in PLAT: return PLAT[name]
    base=name.split(' (')[0].strip()
    return PLAT.get(base, 'Walk-in')
PRICE_OVER={"Emeril's":4,"Saint-Germain":4,"Zasu":4,"Dakar NOLA":4,"Mosquito Supper Club":4,"The Kingsway":4,"Restaurant August":4,"Commander's Palace":4,"Brennan's":4,"Galatoire's":4,"Antoine's":4,"Arnaud's":4,"Chemin à la Mer":4,"Miss River":4,"Gautreau's":4,"Dickie Brennan's Steakhouse":4,"Doris Metropolitan":4,"Desi Vega's Steakhouse":4,"La Boca":4,"GW Fins":4,"Pêche Seafood Grill":3,"Herbsaint":3,"Cochon":3,"Saba":3,"Acamaya":3,"La Petite Grocery":3,"Patois":3,"Osteria Lupo":3,"Compère Lapin":3,"Clancy's":3,"Coquette":3,"Lilette":3,"Shaya":3,"Bayona":3,"Justine":3,"Lengua Madre":3,"Saffron NOLA":3,"34 Restaurant & Bar":3,"Atchafalaya":3,"Saint Claire":3,"Evviva":3,"Delacroix":3,"Gianna":3,"Jack Rose":3,"Bywater American Bistro":3,"N7":3,"Paladar 511":3,"Toups' Meatery":3,"Bar Marilou":3,"Maypop":3,"Pascal's Manale":3,"Jacques-Imo's":3,"Tujague's":3,"Mr. B's Bistro":3,"Palace Café":3,"Muriel's":3,"Court of Two Sisters":3,"Bon Ton Café":3,"Upperline":3,"Brigtsen's":3,"Irene's":3,"Mosca's":3,"Turkey and the Wolf":2,"Hungry Eyes":2,"Mister Mao":2,"Lufu":2,"Cochon Butcher":2,"Addis NOLA":2,"Molly's Rise and Shine":2,"Sylvain":2,"Palm & Pine":2,"Marjie's Grill":2,"Mopho":2,"Vessel":2,"Rosedale":2,"Bar Frances":2,"Domenica":2,"Dooky Chase's":2,"Domilise's Po-Boy & Bar":1,"Parkway Bakery & Tavern":1,"Willie Mae's NOLA":1,"Killer PoBoys":1,"Central Grocery":1,"Mother's":1,"Hansen's Sno-Bliz":1,"Café du Monde":1,"Jewel of the South":2,"Cure":2,"Cane & Table":2,"Latitude 29":2,"Sazerac Bar":2,"Carousel Bar":2,"Napoleon House":2,"Bacchanal":2}
def occasions(name, cat=None, price=0):
    o=[]
    if cat=='Restaurants':
        if price>=4: o=['Romantic','Date night']
        elif price==3: o=['Date night']
        elif price==2: o=['Casual','Date night']
        else: o=['Casual']
        if name in ("Pêche Seafood Grill","Cochon","Acme Oyster House","Felix's","Drago's","Deanie's","Jacques-Imo's","Dooky Chase's","Mandina's","Domenica","Pizza Domenica","Bevi Seafood Co.","Cajun Seafood","Clesi's","Seither's","Mother's","Willie Mae's NOLA","Mosquito Supper Club","Dakar NOLA","Turkey and the Wolf","Hungry Eyes","Saba","Shaya","Addis NOLA","Lufu"): o=o+['Group']
    elif cat=='Cafés': o=['Date night','Casual'] if price>=2 else ['Casual']
    elif cat=='Speakeasies': o=['Date night','Late night']
    elif cat=='Bars':
        o=['Late night'] if price<=1 else ['Date night','Late night']
        if 'Brew' in name or name in ("Parleaux Beer Lab","Urban South Brewery","NOLA Brewing","Zony Mash Beer Project","Second Line Brewing","Wrong Iron on the Greenway","Courtyard Brewery","Bayou Beer Garden","The Bulldog","Avenue Pub","Finn McCool's","Mid-City Yacht Club","Brieux Carré"): o=['Group','Casual']
        if name in ("Jewel of the South","Cure","Cane & Table","Bar Tonique","Manolito","Latitude 29","Sazerac Bar","Carousel Bar","Napoleon House","Arnaud's French 75 Bar","Bar Marilou","The Elysian Bar","Peychaud's","Bacchanal","Bar Pomona","Bar Frances","The Delachaise","The Columns","Effervescence","Loa","Chandelier Bar","Bayou Wine Garden","Oak Wine Bar","Barrel Proof","Cellar Door"): o=['Romantic','Date night']
        if name in ("The Spotted Cat","d.b.a.","Snug Harbor","Blue Nile","Three Muses","Vaughan's Lounge","Bullet's Sports Bar","Kermit's Tremé Mother-in-Law Lounge","Candlelight Lounge","Maple Leaf Bar","Le Bon Temps Roulé","Tipitina's","Preservation Hall","Fritzel's","Palm Court Jazz Café","The Jazz Playhouse","Chickie Wah Wah"): o=['Group','Late night']
    elif cat=='Rooftops': o=['Date night','Group']
    elif cat=='Coffee': o=['Sweets','Brunch']
    elif cat=='Brunch': o=['Brunch']
    elif cat=='Off-beat': o=['Casual']
    elif cat=='Bakeries': o=['Sweets','Brunch']
    elif cat=='Dessert': o=['Sweets']
    elif cat=='Scene': o=['Group','Date night'] if price<=3 else ['Romantic','Group']
    elif cat=='Nightlife': o=['Late night','Group']
    return o
from cities.new_orleans_itin import ITINS, GOTCHAS
NOTES_HTML='''<p>Michelin: the inaugural American South selection, announced November 3, 2025 in Greenville, S.C. — Emeril's with two stars (E.J. Lagasse, the youngest chef ever to hold them, and the region's Young Chef award), one star each for Saint-Germain and Zasu, eleven Bib Gourmands (Acamaya, Cochon, Cochon Butcher, Domilise's, Hungry Eyes, Lufu, Mister Mao, Parkway, Saba, Turkey and the Wolf, Willie Mae's) and seventeen recommended rooms, marked MR because a first-year guide's recommended list is worth keeping.</p><p>James Beard 2026: four New Orleans finalists — Donald Link and Stephen Stryjewski (Outstanding Restaurateur), E.J. Lagasse (Emerging Chef), and Ana Castro of Acamaya and Serigne Mbaye of Dakar NOLA (Best Chef: South). Semifinalists included Saint Claire and Evviva (Best New Restaurant) and Bywater Bakery (Outstanding Bakery). Dooky Chase's, Hansen's, Dong Phuong and Willie Mae's hold America's Classics. Dakar NOLA placed №6 on North America's 50 Best Restaurants 2025; Jewel of the South is a North America's 50 Best bar — 2026 placings weren't confirmed for this edition.</p><p>Occasion chips for New Orleans are editorial assignments, by category and price. Booking platforms are listed as best known at time of printing; the Resy app is the source of truth for the Amex credit. Seasonal closures (Casamento's in summer, the sno-ball stands in winter, king cake outside Carnival) are noted where they matter.</p><p>Photography via Pexels (royalty-free): three photographs — the Canal Street streetcar, the City of New Orleans paddlewheel, Bourbon Street — cropped and reused across the twelve sections.</p>'''
from cities.new_orleans_honor import HONOR, HONOR_DECK, HONOR_WHY
