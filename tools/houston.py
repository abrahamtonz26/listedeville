# -*- coding: utf-8 -*-
import re
SLUG='houston'; NAME='Houston'
MD='/home/claude/out/liste-de-ville-houston-2026.md'
OUT_HTML='/home/claude/out/liste-de-ville-houston-2026-magazine.html'
OUT_PDF='/home/claude/out/liste-de-ville-houston-2026.pdf'
IMG_DIR='/home/claude/img_houston'; COVERBAND='/home/claude/coverband_houston.jpg'
H1='Hous<i>ton</i>'
TAG='The best of the best in the city — must-visit, unique, a rockstar in its own right. The first edition, in Michelin\'s second year in Texas.'
MAST='No. 11 · listedeville / Houston · Fall/Winter 2026'
FOOTER='Honestly Speaking  ·  listedeville / Houston  ·  Fall/Winter 2026'
TITLE='Honestly Speaking — listedeville / Houston, Fall/Winter 2026'
STATS=[('6','Michelin stars — including the first barbecue joint ever starred',True),('22','Bib Gourmands, the most of any Texas city',True),('1977',"Ninfa's — where the fajita was invented",False)]
RANK_LEGEND='<span><span class="note">TM50</span> Texas Monthly Top 50 BBQ</span><span><span class="jbf">JBF 2026</span> James Beard finalist or semifinalist</span>'
COLOPHON="Compiled by Tony Abraham against Yelp, Google, the Houston Chronicle, Houstonia, Texas Monthly, Eater Houston, OpenTable, Resy and Tock. Michelin marks reflect the 2025 Texas selection; James Beard marks the 2026 awards. Cover: downtown from the freeway at dusk, via Pexels."
AUTHOR_EXTRA="Based in New York, with field notes from all around. <em>listedeville / Houston</em> is the tenth city guide — the most diverse food city in America, and the one the guides have covered least."
AUTHOR_SMALL='First edition, Fall/Winter 2026. Two of the second series done.'
OCC_LEGEND='occasion (editorial, by category and price)'
SEARCH_HINT='(try “brisket”, “Bellaire”, “Viet-Cajun”)'
DECKS = {
 "Cafés & all-day / chef's neighborhood spots": "Montrose's Bibs, the Heights' wine bars, and the EaDo rooms where the city's cooks eat on their nights off.",
 "Speakeasies & hidden bars — descending order of amazingness": "Upstairs from a mezcaleria, behind a blue door since 1976, under a neon sparrow. Ranked, loosely, by the drink.",
 "Rooftop bars": "A flat city with big skies: the hotel roofs, then the ice houses, beer gardens and yards that do the same job at ground level.",
 "Bars — notable mentions": "Anvil's 100 list, Julep's Southern drinks, La Carafe's candles, and the ice houses since 1928.",
 "Coffee shops": "Vietnamese coffee at every bánh mì counter, the Blacksmith breakfast, and the roasters that grew up in the Heights.",
 "Restaurants": "Six stars, twenty-two Bibs, the Beard list, and the Bellaire, Hillcroft and Third Ward kitchens that make Houston the most diverse eating city in America.",
 "Brunch spots": "The Breakfast Klub's line, Hugo's buffet, breakfast tacos on flour, dim sum in Asiatown.",
 "Off-beat & only-in-Houston": "A starred barbecue joint, Viet-Cajun crawfish, the fajita's birthplace, a 24-hour pie house, and a farmers market with a Bib taquería.",
 "Bakeries": "Kolaches, pan dulce, bánh mì loaves, Beard-nominated pastry, and Shipley's since 1936.",
 "Dessert bars & sweets": "The Bayou Goo, pecan pie in a wooden box, bingsu on Bellaire, tres leches everywhere.",
 "Notable mentions — scene dining, lounges & supper clubs": "Where the room is the point: Tony's since 1965, Pappas Bros.' cellar, the River Oaks District, the starred tasting rooms.",
 "Dance clubs & nightlife": "The Continental Club, White Oak's lawn, Numbers since 1978, and a country dancehall in the northwest.",
}
ABOUT = {
 "Cafés": ("The rooms you return to on a weeknight: Nancy's Hustle and Nobie's, Rosie Cannonball's wood oven, Theodore Rex, Squable and Coltivare in the Heights, and the Bibs that arrived in 2025 — Máximo, Annam, ChòpnBlọk, Da Gama.",
           "Picked for consistency and the neighborhood. Ten of Michelin's twenty-two Houston Bibs and most of its recommended rooms are on this list; the Ortega family's rooms are the 2026 Beard names."),
 "Speakeasies": ("Houston hides its best bars upstairs (Tongue-Cut Sparrow, Bad News), behind unmarked doors (Marfreless since 1976) and in old buildings by Market Square (La Carafe, Warren's).",
           "Ranked by the drink. Anvil is the bar that taught the city to drink cocktails; Julep and Better Luck Tomorrow are its descendants. The ice houses are on because they're the real Houston bar."),
 "Rooftops": ("Houston is flat and the roofs are hotel bars — Z on 23, the Post's Skylawn — but the outdoor culture is the ice house and the beer garden: West Alabama since 1928, Saint Arnold's yard, Axelrad's hammocks.",
           "Chosen for the air and the view. The breweries are on because Saint Arnold started Texas craft beer and the gardens are where the city drinks outdoors."),
 "Bars": ("A serious cocktail city since Anvil in 2009 — Bobby Heugel and Alba Huerta are Beard nominees — with ice houses, wine bars, blues rooms and a country dancehall.",
           "Recognized first, then institutions, then the neighborhoods. Montrose's gay bars are on for history; the breweries for Saint Arnold's lineage."),
 "Coffee": ("Vietnamese coffee is the city's native cup — cà phê sữa đá at every Bellaire counter — and the third-wave rooms grew up in the Heights and Montrose: Boomtown, Greenway, Blacksmith, Siphon.",
           "Selected for the cup and the room. Blacksmith's Vietnamese steak and eggs is the breakfast; the bakery cafés — Common Bond, Koffeteria, Morningstar — are the best mornings."),
 "Restaurants": ("Michelin's second Texas guide kept Houston's six stars — including CorkScrew, the first barbecue joint ever starred — and grew the Bibs to twenty-two, the most in the state. Underneath: the Beard list, five smokehouses on Texas Monthly's Top 50, and the Bellaire, Hillcroft and Third Ward kitchens that no guide can keep up with.",
           "Grouped by the Guide, then the Beard list and the classics. Street to Kitchen's Benchawan Painter won Best Chef: Texas; Himalaya and Crawfish & Noodles have been semifinalists for years; Ninfa's invented the fajita."),
 "Brunch": ("The Breakfast Klub's line, Hugo's Sunday buffet, breakfast tacos on flour tortillas, dim sum at Ocean Palace, and Blacksmith's steak and eggs.",
           "Kept to places with a real kitchen at 10am. The taco counters are the local brunch; book the hotel rooms for the weekend."),
 "Off-beat": ("A Michelin star for brisket, Viet-Cajun crawfish invented on Bellaire, the fajita's birthplace on Navigation, barbacoa on Sundays at a drive-in, a 24-hour pie house, and a farmers market with a Bib taquería.",
           "Selected for singularity. The barbecue Top 50 and the Asiatown night are the two things Houston does that no other city on this list can."),
 "Bakeries": ("Kolaches (Czech, by way of the Hill Country), pan dulce at El Bolillo, bánh mì loaves in Bellaire, Beard-nominated pastry at Koffeteria and Fluff, and Shipley's glazed since 1936.",
           "Chosen on the strength of one item each. Common Bond is the all-rounder; Three Brothers has been baking since 1949."),
 "Dessert": ("The Bayou Goo at House of Pies, Goode Co.'s pecan pie, bingsu and boba on Bellaire, tres leches at Ninfa's, and the pastry courses at the starred rooms.",
           "A mix of the destination and the institution. House of Pies at 3am is the pilgrimage."),
 "Scene": ("Where the room is the point: Tony's since 1965, Pappas Bros.' 3,000-bottle cellar, the River Oaks District, Bludorn's dining room, and the starred tasting counters.",
           "The old rooms lead; the hotel bars and the steakhouses follow. The Galleria restaurants are on because that's where Houston celebrates."),
 "Nightlife": ("The Continental Club and the Big Top, White Oak's lawn, the Heights Theater, Numbers since 1978, Rich's, and Neon Boots for the two-step.",
           "Venues and clubs together. Fitzgerald's and Walter's are listed closed so you know what the scene lost."),
}
R="""Nancy's Hustle|Nobie's|Rosie Cannonball|Theodore Rex|Street to Kitchen|Da Gama Canteen|Máximo|Annam|ChòpnBlọk|Belly of the Beast|Bar Bludorn|Agnes and Sherman|Late August|Josephine's|Perseid|Candente|Baso|Squable|Riel|Tiny Champions|The Marigold Club|Bludorn|Navy Blue|Georgia James|Wild Oats|Musaafer|Le Jardinier|BCN Taste & Tradition|Ostia|Indianola|Vibrant|CasaEma|Credence|Squable bar|Bar Bludorn brunch|Squable brunch|Nancy's Hustle brunch?|Riel brunch|Ostia brunch|Bludorn brunch|Josephine's brunch|Late August brunch|Máximo brunch|Da Gama brunch|ChòpnBlọk brunch|Bludorn's Bar|Dessert at Musaafer|Dessert at Le Jardinier""".split("|")
T="""March|Tatemó|Hidden Omakase|Neo|Dessert at March""".split("|")
S="""Bisou|Toca Madera|Clé""".split("|")
O="""Hugo's|Xochi|Urbe|Caracol|Backstreet Café|Ninfa's on Navigation|Lucille's|MAD|Killen's|Pappas Bros. Steakhouse|Molina's Cantina|El Tiempo Cantina|Peli Peli|Brennan's of Houston|Tony's|Da Marco|Dolce Vita|Nino's / Vincent's / Grappino di Nino|Carrabba's original|Rainbow Lodge|Brasserie 19|La Colombe d'Or|State of Grace|Goode Co. Seafood|Cuchara|Sambuca|Hugo's Sunday brunch|Backstreet Café brunch|Brennan's of Houston jazz brunch|Rainbow Lodge brunch|Lucille's brunch|Harold's|Ouzo Bay|Ouzo Bay brunch|Brasserie 19 brunch|La Colombe d'Or brunch|State of Grace brunch|The Original Ninfa's brunch|Ouzo Bay patio|Backstreet Café patio|Hugo's balcony?|Brasserie 19 patio|La Colombe d'Or patio|Discovery Green|Third Coast|Steak 48|Mastro's|The Post Oak Hotel's Bloom & Bee|Toro Toro|Kata Robata|Uchi Houston|Nobu Houston|The Annie Café & Bar|B&B Butchers|Turner's|Killen's Steakhouse|Galveston day|Pappas Bros.|Molina's Cantina|Tres leches at Ninfa's|Flan at Hugo's|Churros at Urbe|Bread pudding at Brennan's of Houston|Baked Alaska at Tony's|Cheesecake at Nino's|Ninfa's on Navigation""".split("|")
PLAT={}
for lst,tag in ((S,'SevenRooms'),(O,'OpenTable'),(R,'Resy'),(T,'Tock')):
    for n in lst:
        n=n.strip()
        if n: PLAT[n]=tag
def lookup(name):
    if name in PLAT: return PLAT[name]
    base=name.split(' (')[0].strip()
    return PLAT.get(base, 'Walk-in')
PRICE_OVER={"March":4,"Tatemó":4,"Le Jardinier":4,"Musaafer":4,"BCN Taste & Tradition":4,"Hidden Omakase":4,"Neo":4,"Credence":4,"Bludorn":4,"Navy Blue":4,"Georgia James":4,"Pappas Bros. Steakhouse":4,"Tony's":4,"Brennan's of Houston":4,"Da Marco":4,"La Colombe d'Or":4,"Bisou":4,"Toca Madera":4,"Steak 48":4,"Mastro's":4,"Uchi Houston":4,"Nobu Houston":4,"The Annie Café & Bar":4,"B&B Butchers":4,"Turner's":4,"CorkScrew BBQ":2,"Truth BBQ":2,"The Pit Room":2,"Pinkerton's BBQ":2,"Blood Bros. BBQ":2,"Killen's BBQ":2,"Killen's":3,"Rosie Cannonball":3,"Theodore Rex":3,"Belly of the Beast":3,"Máximo":3,"Bar Bludorn":3,"Agnes and Sherman":3,"Late August":3,"Josephine's":3,"Perseid":3,"Baso":3,"Squable":3,"Coltivare":3,"Riel":3,"The Marigold Club":3,"Hugo's":3,"Xochi":3,"Caracol":3,"Backstreet Café":3,"Lucille's":3,"Ostia":3,"MAD":3,"Rainbow Lodge":3,"Brasserie 19":3,"State of Grace":3,"Nancy's Hustle":2,"Nobie's":2,"Street to Kitchen":2,"Da Gama Canteen":2,"Annam":2,"ChòpnBlọk":2,"Candente":2,"Mala Sichuan Bistro":2,"Crawfish & Noodles":2,"Himalaya":2,"Wild Oats":2,"Better Luck Tomorrow":2,"Tiny Champions":2,"Indianola":2,"Ninfa's on Navigation":2,"Nam Giao":1,"Papalo Taqueria":1,"Brisket & Rice":1,"Villa Arcos":1,"Laredo Taqueria":1,"Anvil Bar & Refuge":2,"Julep":2,"Tongue-Cut Sparrow":2,"House of Pies":1}
def occasions(name, cat=None, price=0):
    o=[]
    if cat=='Restaurants':
        if price>=4: o=['Romantic','Date night']
        elif price==3: o=['Date night']
        elif price==2: o=['Casual','Date night']
        else: o=['Casual']
        if name in ("Truth BBQ","The Pit Room","Pinkerton's BBQ","Blood Bros. BBQ","Killen's BBQ","CorkScrew BBQ","Tejas Chocolate & Barbecue","Crawfish & Noodles","Cajun Kitchen","Saigon House","Ninfa's on Navigation","Ocean Palace","Fung's Kitchen","Kim Son","Mala Sichuan Bistro","Hugo's","Xochi","Pappadeaux","Pappasito's","Georgia James","Pappas Bros. Steakhouse","Goode Co. Barbeque","Lucille's"): o=o+['Group']
    elif cat=='Cafés': o=['Date night','Casual'] if price>=2 else ['Casual']
    elif cat=='Speakeasies': o=['Date night','Late night']
    elif cat=='Bars':
        o=['Late night'] if price<=1 else ['Date night','Late night']
        if 'Brew' in name or 'Ice House' in name or name in ("Saint Arnold Beer Garden","Truck Yard","Pitch 25","Kirby Ice House","Axelrad","The Ginger Man","Little Woodrow's","Hans' Bier Haus","Valhalla","Big Star Bar","Cottonwood","Petrol Station","Onion Creek","Bobcat Teddy's Ice House","Alice's Tall Texan","D&T Drive Inn","Wooster's Garden","Moon Tower Inn"): o=['Group','Casual']
        if name in ("Anvil Bar & Refuge","Julep","Tongue-Cut Sparrow","The Pastry War","Better Luck Tomorrow","Squable","Bar Bludorn","Bad News Bar","Lei Low","Present Company","Nightingale Room","Marfreless","Camerata","13 Celsius","Vinology","Cuchara","Reserve 101","La Carafe","Z on 23"): o=['Romantic','Date night']
        if name in ("The Continental Club","Shoeshine Charley's Big Top Lounge","Goode's Armadillo Palace","McGonigel's Mucky Duck","The Big Easy Social & Pleasure Club","Sambuca","Cezanne","Neon Boots","Rebels Honky Tonk","Howl at the Moon","Numbers","Rich's","Barbarella"): o=['Group','Late night']
    elif cat=='Rooftops': o=['Date night','Group']
    elif cat=='Coffee': o=['Sweets','Brunch']
    elif cat=='Brunch': o=['Brunch']
    elif cat=='Off-beat': o=['Casual']
    elif cat=='Bakeries': o=['Sweets','Brunch']
    elif cat=='Dessert': o=['Sweets']
    elif cat=='Scene': o=['Group','Date night'] if price<=3 else ['Romantic','Group']
    elif cat=='Nightlife': o=['Late night','Group']
    return o
from cities.houston_itin import ITINS, GOTCHAS
NOTES_HTML='''<p>Michelin: the second Texas selection, announced October 28, 2025 at the Wortham Theater Center. Houston kept its six one-stars — BCN Taste &amp; Tradition, CorkScrew BBQ (the first barbecue restaurant ever starred, in 2024), Le Jardinier, March, Musaafer and Tatemó — and grew to twenty-two Bib Gourmands with Annam, ChòpnBlọk, Da Gama Canteen, Máximo and Papalo Taqueria; sixteen rooms are recommended (MR). Elliot Wood of Credence took the Service Award; Pappas Bros.' Steven McDonald the 2024 Sommelier Award.</p><p>James Beard 2026: Hugo Ortega and Tracy Vaught's H Town Restaurant Group (Hugo's, Xochi, Urbe, Caracol, Backstreet Café) were semifinalists for Outstanding Restaurateur. Past honors marked JBF: Benchawan Painter of Street to Kitchen won Best Chef: Texas in 2023; Himalaya's Kaiser Lashkari, Crawfish &amp; Noodles' Trong Nguyen, Anvil's Bobby Heugel and Julep's Alba Huerta are repeat nominees; Hugo Ortega won Best Chef: Southwest in 2017. TM50 marks Texas Monthly's Top 50 BBQ list.</p><p>Occasion chips for Houston are editorial assignments, by category and price. Booking platforms are listed as best known at time of printing; the Resy app is the source of truth for the Amex credit. Crawfish season (February–June) and barbecue sell-out times are noted where they matter.</p><p>Photography via Pexels (royalty-free): three photographs — downtown from the freeway, the love-lock fence over the skyline, a barbecue awning — cropped and reused across the twelve sections.</p>'''
from cities.houston_honor import HONOR, HONOR_DECK, HONOR_WHY
