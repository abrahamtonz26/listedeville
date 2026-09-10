# -*- coding: utf-8 -*-
# City config: Boston
import re
SLUG='boston'; NAME='Boston'
MD='/mnt/user-data/outputs/liste-de-ville-boston-2026.md'
OUT_HTML='/mnt/user-data/outputs/liste-de-ville-boston-2026-magazine.html'
OUT_PDF='/mnt/user-data/outputs/liste-de-ville-boston-2026.pdf'
IMG_DIR='/home/claude/img_boston'; COVERBAND='/home/claude/coverband_boston.jpg'
H1='Bos<i>ton</i>'
TAG="The best of the best in the city — must-visit, unique, a rockstar in its own right. The first edition, in Michelin's first year."
MAST='No. 4 · liste de ville / Boston · Fall/Winter 2026'
FOOTER='Honestly Speaking  ·  liste de ville / Boston  ·  Fall/Winter 2026'
TITLE='Honestly Speaking — liste de ville / Boston, Fall/Winter 2026'
STATS=[('1',"Michelin star — the city's first",True),('6','Bib Gourmand restaurants',True),('1826',"Union Oyster House — America's oldest",False)]
RANK_LEGEND='<span><span class="note">MR</span> Michelin Recommended (first-year guide)</span><span><span class="jbf">JBF 2026</span> James Beard semifinalist</span>'
COLOPHON="Compiled by Tony Abraham against Yelp, Google, The Boston Globe, Boston Magazine, OpenTable, Resy, Eater Boston and the Michelin Guide. Michelin marks reflect the 2025 Boston selection — the city's first — the most recent at time of printing. Cover: Fan Pier and the Financial District in snow, via Pexels."
AUTHOR_EXTRA='Based in New York, with field notes from all around. <em>liste de ville / Boston</em> is the third city guide, and the first written in a city\'s first Michelin year — which makes the Bib Gourmands and the "recommended" rooms the interesting part of the map.'
AUTHOR_SMALL='First edition, Fall/Winter 2026. Miami, Chicago, San Francisco, Los Angeles and Seattle to follow.'
OCC_LEGEND='occasion (editorial, by category and price)'
DECKS = {
 "Cafés & all-day / chef's neighborhood spots": "Cambridge and Somerville's chef rooms, South End enotecas, and the wine bars where Boston actually eats on a Tuesday.",
 "Speakeasies & hidden bars — descending order of amazingness": "Beneath a Greek wine bar, behind a wig shop, through a false library. Ranked, loosely, by the drink.",
 "Rooftop bars": "A low city with a harbor — the roofs, decks and beer gardens that catch the water.",
 "Bars — notable mentions": "A 50 Best entry, a Michelin cocktail award, a sake bar in a speedway, and the taverns since 1795.",
 "Coffee shops": "George Howell's town: the roasters, the North End caffès since 1929, and the bakeries that double as cafés.",
 "Restaurants": "One star, six Bibs, a long Michelin 'recommended' bench that reads like a best-of, and the seafood shacks that make the drive worth it.",
 "Brunch spots": "Southie brunch, the Paramount line, and the diners of Somerville.",
 "Off-beat & only-in-Boston": "Fried clams in Essex, roast beef on Revere Beach, Sicilian slices for cash, and a tiki palace on Route 1.",
 "Bakeries": "Flour's sticky bun, the North End cannoli war, and Watertown's Armenian bakeries.",
 "Dessert bars & sweets": "For after — or instead of — dinner.",
 "Notable mentions — scene dining, lounges & supper clubs": "Where the room is the point: the Newbury's glass roof, the Seaport steakhouses, and the hotel bars of Back Bay.",
 "Dance clubs & nightlife": "Theater District megaclubs, Lansdowne Street, and the rock rooms of Allston and Cambridge.",
}
ABOUT = {
 "Cafés": ("Boston's best everyday rooms are across the river as often as not: Pammy's, Giulia, Alden & Harlow, Sarma, Juliet. In the city, the South End's enotecas — Coppa, Toro, Bar Mezzana — and a new wave of wine bars.",
           "Picked for the room you'd return to on a weeknight. Four of Michelin's 'recommended' rooms are here (Pammy's, Oleana, Sarma, Urban Hearth), two Bibs from Karen Akunowicz's Southie pair, and the wine bars that made Boston a wine town."),
 "Speakeasies": ("Boston's hidden bars are literal: Hecate under Krasi, Offsuit behind Troquet, the Wig Shop behind an actual wig shop, Yvonne's through a library. Drink in Fort Point has no menu and no sign.",
           "Ranked by the drink, not the door. Hecate entered North America's 50 Best in 2025; Mahaniyom's Boong Boonnak won Michelin's cocktail award. The closed ones — Hawthorne, Brick & Mortar, Deep Ellum — are listed so you know what's gone."),
 "Rooftops": ("Boston is low and wet: the views are of the harbor and the Charles, from the Envoy's Lookout, the Newbury's glass roof, and the Seaport beer gardens that open when the weather does.",
           "Chosen for the view first, and stretched to include the waterfront decks and beer gardens that do the same job in a city without many true rooftops. Seasonal ones are marked; most close by November."),
 "Bars": ("A cocktail city that punches above its size — Drink and Eastern Standard trained a generation — plus the taverns that have been pouring since the Revolution.",
           "Ranked and recognized first, then institutions, hotel bars, dives, wine, beer. The Bell in Hand (1795) and Union Oyster House (1826) are on for history; the Koji Club for being the only sake bar in the Northeast; Trillium for the beer."),
 "Coffee": ("George Howell invented specialty coffee here in the 1970s; Gracenote, Render and Broadsheet carry it on; the North End caffès have been pulling espresso since 1929.",
           "Selected for the cup and the room. Ogawa is Kyoto in Downtown Crossing; Diesel and 1369 are the Cambridge institutions; the original Dunkin' in Quincy is a pilgrimage, not a recommendation."),
 "Restaurants": ("Michelin's first Boston year gave one star (311 Omakase) and six Bibs, and left O Ya, Oleana, Pammy's, Neptune and Nightshade at 'recommended' — which tells you how to read this list: the Bibs and the recommended rooms are where the city is.",
           "Grouped by distinction, then by the new guard, then the classics and the seafood shacks that justify a car. James Beard left Massachusetts out of the 2026 finals; the semifinalists — O Ya, Comfort Kitchen, Lê Madeline — are marked."),
 "Brunch": ("Southie and the South End on Sunday, the Paramount line on Beacon Hill, and the Somerville diners where the cream of wheat has a cult.",
           "Kept to places that consistently top Resy and OpenTable's weekend demand, plus the neighborhood counters you walk into. Bar Volpe holds a Bib; Eastern Standard and Contessa are the new rooms."),
 "Off-beat": ("Fried clams on the North Shore, roast beef on Revere Beach, Sicilian slices for cash until they run out, a tiki palace on Route 1, and the oldest restaurant in America.",
           "Selected for singularity. Sullivan's Castle Island won the James Beard America's Classics award in 2025; Galleria Umberto and Santarpio's are cash-only institutions; the North End cannoli rivalry is a civic duty."),
 "Bakeries": ("Flour's sticky bun, Sofra's Turkish pastries, the North End's sfogliatelle, and the Armenian bakeries of Watertown that most visitors never find.",
           "Chosen on the strength of one signature item each. Mike's vs Modern is listed as the argument it is; Bova's is on for being open at 2am; Katz Bagel in Chelsea for inventing the pizza bagel in 1938."),
 "Dessert": ("Toscanini's burnt caramel, Christina's flavors, L.A. Burdick's drinking chocolate, and the Boston cream pie that gives the city its official dessert.",
           "A mix of the destination and the institution. Kimball Farm and Richardson's are the drive-to ice cream stands; Taza is the chocolate factory you can tour."),
 "Scene": ("Where the room is the point: Contessa's glass roof, Yvonne's, the Seaport steakhouses, and the hotel bars of Back Bay.",
           "The hotel rooms and the Seaport lead; the old Back Bay guard stays. O Ya, Uni and 311 Omakase are here for the counter theater as much as the food."),
 "Nightlife": ("Music first — Royale, the Sinclair, Paradise, Roadrunner, the jazz rooms — and the Theater District clubs after.",
           "Venues and clubs together. The Middle East, Great Scott and ONCE are listed closed because the city still mourns them; Jacques Cabaret has been doing drag since 1938."),
}
R="""Pammy's|Alden & Harlow|Waypoint|Giulia|Bar Enza|Nathálie|Haley.Henry|Rebel's Guild|Spoke Wine Bar|Juliet|Sarma|Oleana|Urban Hearth|Field & Vine|Celeste|Highland Kitchen|Puritan & Co|The Table at Season to Taste|Little Donkey|Toro|Coppa|The Butcher Shop|Bar Mezzana|Shore Leave|Kava Neo-Taverna|Myers + Chang|Mida|Fox & the Knife|Bar Volpe|Chickadee|Lucca Back Bay|Krasi|Bar Lyon|Select Oyster Bar|Little Whale Oyster Bar|Mamma Maria|Carmelina's|Prezza|Marcelino's Boutique Bar|Comfort Kitchen|Lê Madeline|Nightshade Noodle Bar|Faccia a Faccia|The Salty Pig|Loyal Nine|Hecate|Offsuit|Wink & Nod|Yvonne's|Bogie's Place|Blossom Bar|Backbar|Bar Pallino|Hojoko|Mahaniyom|Eastern Standard|Equal Measure|Ruka|Contessa|Lookout Rooftop|Rooftop at Revere|Six West|Legal Harborside Roof Deck|Woods Hill Pier 4|Row 34|Committee|Lola 42|Grace by Nia|Pagu|Jahunger|Sumiao Hunan Kitchen|O Ya|Uni|Sorellina|Mooncusser|La Padrona|Bar Vlaha|Ilona|Zurito|Mariel|Prima|Dakzen|No. 9 Park|Sportello|Mistral|Ostra|Mooo|Grill 23|Deuxave|Zuma|Trade|Neptune Oyster|Tasting Counter|SRV|Banyan Bar + Refuge|Sweet Cheeks Q|Citizen Public House|Shōjō|Saltie Girl|Eventide Fenway|Atlantic Fish Co|Davio's|Ocean Prime|Mastro's|Del Frisco's|Smith & Wollensky|Piattini|Lolita|Nebo|Bricco|Antico Forno|Monica's Trattoria|Al Dente|Trattoria il Panino|Aquitaine|Gaslight|The Beehive|Lincoln Tavern|Loco Taqueria|Coppersmith|Trina's Starlite Lounge|Henrietta's Table|The Hourly Oyster House|Buttermilk & Bourbon|Bin 26 Enoteca|Ward 8|Sip Wine Bar|Noir|Alcove|Bristol Lounge|Oak Long Bar + Kitchen|The Last Hurrah|The Street Bar|Grana|Fed|Precinct Kitchen + Bar|Rowes Wharf Sea Grille patio|Harvest|Tatte|Flour Bakery + Café|Sofra|Bakey|Cafe Landwer|Zoe's""".split("|")
T="""311 Omakase|Tasting Counter|O Ya""".split("|")
O="""Abe & Louie's|Legal Sea Foods|Union Oyster House|Stephanie's on Newbury|Cafeteria|Sonsie|The Paramount|The Friendly Toast|Zaftigs|Cask 'n Flagon|Loretta's Last Call|Lansdowne Pub|Game On!|Bleacher Bar|Regattabar|Scullers Jazz Club|Time Out Market Boston|Eataly Boston""".split("|")
S="""Royale|The Grand|Bijou|Icon|Memoire|Candibar|Venu|Cure Lounge""".split("|")
W="""Galleria Umberto|Regina Pizzeria|Santarpio's|Kelly's Roast Beef|Sullivan's Castle Island|Kowloon|Mr. Bartley's Burger Cottage|Anna's Taqueria|El Pelón|Gene's Chinese Flatbread Cafe|Taiwan Cafe|Peach Farm|Winsor Dim Sum Cafe|Hei La Moon|Dumpling Cafe|Pho Pasteur|Bánh Mì Ba Le|Pho Hoa|Anh Hong|Shanti|Yankee Lobster|James Hook & Co|Belle Isle Seafood|Woodman's of Essex|The Clam Box|Roy Moore Lobster Co|Simco's|Ali's Roti|Singh's Roti Shop|Flames|Haley House Bakery Café|Suya Joint|Dudley Café|Bow Market|High Street Place|Hub Hall|Haymarket|Boston Public Market|Quincy Market|Dunkin'|Kane's Donuts|Union Square Donuts|Mike's Pastry|Modern Pastry|Bova's Bakery|Maria's Pastry Shop|Parziale's Bakery|Lyndell's Bakery|Toscanini's|Christina's|Cutty's|Giacomo's|Yume Wo Katare|Sapporo Ramen|Santouka|Dumpling House|Dumpling Daughter|Mike & Patty's|Trident Booksellers & Café|Sound Bites|Ball Square Cafe|Renee's Café|Neighborhood Restaurant|Veggie Galaxy|Cafe Luna|Centre Street Café|Ula Café|Panificio|Cafe Vanille|Kupel's Bakery|Bagelsaurus|Exodus Bagels|Mamaleh's|Pavement Coffeehouse|George Howell Coffee|Gracenote Coffee|Render Coffee|Thinking Cup|Ogawa Coffee|Curio Coffee|Broadsheet Coffee Roasters|Barrington Coffee|Jaho Coffee|Blue Bottle|1369 Coffee House|Diesel Café|Simon's Coffee Shop|Caffè Vittoria|Caffé Paradiso|Polcari's Coffee|Caffè dello Sport|Cafe Nero|The Paris Creperie|Cafe Fixe|Kohi Coffee Company|Cafe Susu|Forge Baking Company|3 Little Figs|Bloc Café|Recreo Coffee|Fazenda Coffee Roasters|City Feed and Supply|Hi-Rise Bread Company|Petsi Pies|Longfellows|Iggy's Bread|Clear Flour Bread|Tatte Harvard Square|The Wig Shop|Drink|Lucky's Lounge|Silvertone Bar & Grill|Tiki Rock|The Koji Club|Trophy Room|The Tam|Biddy Early's|Bukowski Tavern|The Sevens|Cheers|Delux Café|Wally's Cafe|Charlie's Kitchen|Grendel's Den|The Plough and Stars|Brendan Behan Pub|jm Curley|21st Amendment|Tip Tap Room|The Bell in Hand|Green Dragon|The Black Rose|Mr. Dooley's|Phoenix Landing|The Cantab Lounge|The Druid|Sligo Pub|The Burren|Croke Park|L Street Tavern|Murphy's Law|Sullivan's Tap|The Harp|Eire Pub|dbar|The Banshee|Costello's Tavern|Trillium|Harpoon Beer Hall|Night Shift|Lamplighter|Aeronaut|Remnant|Dorchester Brewing|Castle Island Brewing|Notch Brewery|Cambridge Brewing Company|Sunset Grill & Tap|Felipe's Rooftop|Coppersmith|Reelhouse|Cunard Tavern|Pier 6|The Landing at Long Wharf|Trillium Fort Point rooftop|Trillium Garden on the Greenway|Cisco Brewers Seaport|Sam Adams Downtown Taproom|Night Shift Owl's Nest|The Anchor|Bow Market courtyard|Aeronaut Brewing beer garden|Lamplighter Brewing|Dorchester Brewing rooftop|Brewer's Fork patio|Monument Restaurant & Tavern|Downeast Cider House|Fenway Park sausage carts|Time Out Market Boston|Eataly Boston|J.P. Licks|Emack & Bolio's|FoMu|Gracie's Ice Cream|Honeycomb Creamery|Picco|Ron's Gourmet Ice Cream|Kimball Farm|Bedford Farms|Richardson's|Taiyaki NYC Boston|Tous les Jours|Paris Baguette|L.A. Burdick Chocolate|Beacon Hill Chocolates|Taza Chocolate|EHChocolatier|Blackbird Doughnuts|Twin Donuts|Levain|Insomnia Cookies|Lakon Paris Patisserie|Japonaise Bakery|Ho Yuen Bakery|Great Taste Bakery|Teado|Van Leeuwen Boston|Angelato|Lizzy's Ice Cream|Levain Bakery Boston|Vinal Bakery|Danish Pastry House|Katz Bagel Bakery|Linda's Donuts|Demet's Donuts|Party Favors|Bricco Panetteria|Bricco Salumeria|Rosenfeld's Bagels|Bagel Guild|Athan's Bakery|Sevan Bakery|Massis Bakery|Arax Market|Central Bakery|Mariposa Bakery|Cafe Madeleine|Truffles Fine Confections|Wheelhouse|Zinneken's|Flour Fort Point|Roadrunner|House of Blues|Paradise Rock Club|Brighton Music Hall|The Sinclair|Lizard Lounge|Club Café|Jacques Cabaret|The Alley Bar|Cathedral Station|Havana Club|Middlesex Lounge|Crystal Ballroom|Sally O'Brien's|Toad|Atwood's Tavern|Ned Devine's|Hong Kong|Big Night Live|MGM Music Hall at Fenway|Leader Bank Pavilion""".split("|")
PLAT={}
for lst,tag in ((O,'OpenTable'),(S,'SevenRooms'),(W,'Walk-in'),(R,'Resy'),(T,'Tock')):
    for n in lst:
        n=n.strip()
        if n: PLAT[n]=tag
def lookup(name):
    if name in PLAT: return PLAT[name]
    base=name.split(' (')[0].strip()
    return PLAT.get(base)
PRICE_OVER={"311 Omakase":4,"O Ya":4,"Uni":4,"Mooncusser":4,"Tasting Counter":4,"No. 9 Park":4,"Sorellina":4,"Mistral":4,"Ostra":4,"Mooo":4,"Grill 23":4,"Abe & Louie's":4,"Zuma":4,"Ocean Prime":4,"Mastro's":4,"Del Frisco's":4,"Smith & Wollensky":4,"Davio's":3,"Deuxave":3,"Contessa":4,"Yvonne's":3,"Toro":3,"Coppa":2,"Bar Mezzana":3,"Pammy's":3,"Oleana":3,"Sarma":3,"Giulia":3,"Alden & Harlow":3,"Waypoint":3,"Juliet":3,"Urban Hearth":3,"Neptune Oyster":3,"Select Oyster Bar":3,"Row 34":3,"Woods Hill Pier 4":4,"Krasi":3,"Bar Lyon":3,"Fox & the Knife":3,"Bar Volpe":2,"Pagu":2,"Jahunger":2,"Sumiao Hunan Kitchen":2,"Mahaniyom":2,"Comfort Kitchen":2,"Lê Madeline":2,"Nightshade Noodle Bar":3,"La Padrona":3,"Eastern Standard":3,"Marcelino's Boutique Bar":3,"Hecate":3,"Offsuit":3,"Drink":3,"Wink & Nod":3,"The Wig Shop":3,"Blossom Bar":2,"Backbar":2,"Bristol Lounge":3,"Oak Long Bar + Kitchen":3,"The Last Hurrah":3,"Grana":3,"Lookout Rooftop":3,"Rooftop at Revere":3,"Six West":3,"Galleria Umberto":1,"Regina Pizzeria":1,"Santarpio's":1,"Kelly's Roast Beef":1,"Sullivan's Castle Island":1,"Mr. Bartley's Burger Cottage":1,"Anna's Taqueria":1,"El Pelón":1,"Gene's Chinese Flatbread Cafe":1,"Peach Farm":2,"Yume Wo Katare":2,"James Hook & Co":2,"Yankee Lobster":2,"Woodman's of Essex":2,"The Clam Box":2,"Kowloon":2,"Union Oyster House":3,"Mike's Pastry":1,"Modern Pastry":1,"Bova's Bakery":1,"Flour Bakery + Café":1,"Tatte":1,"Sofra":1,"The Paramount":2,"Lincoln Tavern":2,"Trina's Starlite Lounge":2,"Royale":3,"The Grand":3,"Memoire":3,"Wally's Cafe":1,"The Bell in Hand":1,"The Tam":1,"Bukowski Tavern":1,"Croke Park":1,"L Street Tavern":1}
def occasions(name, cat=None, price=0):
    o=[]
    if cat=='Restaurants':
        if price>=4: o=['Romantic','Date night']
        elif price==3: o=['Date night']
        elif price==2: o=['Casual','Date night']
        else: o=['Casual']
        if name in ('Toro','Coppa','Little Donkey','Myers + Chang','Kowloon','Legal Harborside',"Yvonne's",'Contessa','Eataly Boston','Time Out Market Boston','Neighborhood Restaurant','Regina Pizzeria',"Santarpio's"): o=o+['Group']
    elif cat=='Cafés': o=['Date night','Casual'] if price>=2 else ['Casual']
    elif cat=='Speakeasies': o=['Date night','Late night']
    elif cat=='Bars':
        o=['Late night'] if price<=1 else ['Date night','Late night']
        if 'Brewing' in name or name in ('Trillium','Harpoon Beer Hall','Night Shift','Lamplighter','Aeronaut','Remnant','Notch Brewery','Cambridge Brewing Company','Sunset Grill & Tap','Row 34'): o=['Group','Casual']
        if name in ('Bristol Lounge','Oak Long Bar + Kitchen','The Last Hurrah','Hecate','Offsuit','Drink','Wink & Nod',"Marcelino's Boutique Bar",'Bar Pallino',"Yvonne's"): o=['Romantic','Date night']
    elif cat=='Rooftops': o=['Date night','Group']
    elif cat=='Coffee': o=['Sweets','Brunch']
    elif cat=='Brunch': o=['Brunch']
    elif cat=='Off-beat': o=['Casual']
    elif cat=='Bakeries': o=['Sweets','Brunch']
    elif cat=='Dessert': o=['Sweets']
    elif cat=='Scene': o=['Group','Date night'] if price<=3 else ['Romantic','Group']
    elif cat=='Nightlife': o=['Late night','Group']
    return o
from cities.boston_itin import ITINS, GOTCHAS
NOTES_HTML='''<p>Michelin: the inaugural 2025 Boston selection, announced November 18, 2025 as part of the Northeast Cities guide — one star (311 Omakase, the city's first), six Bib Gourmands (Bar Volpe, Fox &amp; the Knife, Pagu, Jahunger, Sumiao Hunan Kitchen, Mahaniyom), and a "recommended" list that includes O Ya, Oleana, Pammy's, Sarma, Urban Hearth, Neptune Oyster and Nightshade Noodle Bar. Because this is a first-year guide, the recommended rooms are marked here (MR) — they won't be in later editions. Mahaniyom's Chompon "Boong" Boonnak won the Northeast Cities Exceptional Cocktails Award.</p><p>James Beard 2026: Massachusetts had no finalists. Semifinalists — O Ya (Outstanding Restaurant), Comfort Kitchen, Lê Madeline, The Koji Club, Gaaeng Supper Club, Lenox Sophia — are marked. Sullivan's Castle Island won the 2025 America's Classics award. Hecate entered North America's 50 Best Bars in 2025; its 2026 placing wasn't confirmed for this edition.</p><p>Occasion chips for Boston are editorial assignments, by category and price. Booking platforms are listed as best known at time of printing; the Resy app is the source of truth for the Amex credit.</p><p>Photography via Pexels (royalty-free): three photographs, cropped and reused across the twelve sections.</p>'''
