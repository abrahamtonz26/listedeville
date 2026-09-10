# -*- coding: utf-8 -*-
import re
SLUG='miami'; NAME='Miami'
MD='/mnt/user-data/outputs/liste-de-ville-miami-2026.md'
OUT_HTML='/mnt/user-data/outputs/liste-de-ville-miami-2026-magazine.html'
OUT_PDF='/mnt/user-data/outputs/liste-de-ville-miami-2026.pdf'
IMG_DIR='/home/claude/img_miami'; COVERBAND='/home/claude/coverband_miami.jpg'
H1='Mi<i>ami</i>'
TAG='The best of the best in the city — must-visit, unique, a rockstar in its own right. The first edition.'
MAST='No. 5 · liste de ville / Miami · Fall/Winter 2026'
FOOTER='Honestly Speaking  ·  liste de ville / Miami  ·  Fall/Winter 2026'
TITLE='Honestly Speaking — liste de ville / Miami, Fall/Winter 2026'
STATS=[('14','Michelin stars in the 2026 Florida selection',True),('18','Bib Gourmand restaurants',True),('2',"bars in North America's 50 Best 2026",False)]
RANK_LEGEND='<span><span class="note">GS</span> Michelin Green Star</span><span><span class="note">NT50</span> New Times Top 50 Bars 2026</span>'
COLOPHON='Compiled by Tony Abraham against Yelp, Google, Miami New Times, Eater Miami, OpenTable, Resy and the Michelin Guide. Michelin marks reflect the 2026 Florida selection (May 2026), the most recent at time of printing; only stars, Green Stars and Bib Gourmands are shown. Cover: Brickell from across Biscayne Bay, via Pexels.'
AUTHOR_EXTRA='Based in New York, with field notes from all around. <em>liste de ville / Miami</em> is the fourth city guide — a city where the ventanita and the two-star tasting room are a ten-minute drive apart, and both belong on the list.'
AUTHOR_SMALL='First edition, Fall/Winter 2026. Chicago, San Francisco, Los Angeles and Seattle to follow.'
OCC_LEGEND='occasion (editorial, by category and price)'
SEARCH_HINT='(try “ventanita”, “Little Havana”, “omakase”)'
DECKS = {
 "Cafés & all-day / chef's neighborhood spots": "Coconut Grove's chef rooms, Little River's wine bars, and the all-day cafés between the beach and the bay.",
 "Speakeasies & hidden bars — descending order of amazingness": "Behind a porta-potty door, up a food-hall mezzanine, inside a listening room. Ranked, loosely, by the drink.",
 "Rooftop bars": "Forty floors over Brickell, a pool at the Freehand, the Miami River at golden hour.",
 "Bars — notable mentions": "Two on the 50 Best, the cantinero's stage in Little Havana, and the dives since 1926.",
 "Coffee shops": "Cafecito windows, Wynwood roasters, and the Cuban bakeries where Miami actually starts its day.",
 "Restaurants": "Fourteen Michelin stars, eighteen Bibs, a Thomas Keller in Surfside, and the Cuban, Haitian and Peruvian kitchens you won't find better outside their home countries.",
 "Brunch spots": "Sunday in the Grove, on the river, and at the ventanita.",
 "Off-beat & only-in-Miami": "Fritas, croquetas, batidos, stone crabs to go, and a fruit stand on the way to the Keys.",
 "Bakeries": "Pastelitos, guava and cheese; challah in Wynwood; a two-star pastry chef's counter in Coral Gables.",
 "Dessert bars & sweets": "For after — or instead of — dinner.",
 "Notable mentions — scene dining, lounges & supper clubs": "Where the room is the point: Brickell's fish tanks, Design District's dining rooms, and the Faena.",
 "Dance clubs & nightlife": "Club Space at sunrise, LIV at the Fontainebleau, and Ball & Chain on Calle Ocho.",
}
ABOUT = {
 "Cafés": ("Miami's neighborhood rooms are in the Grove, Little River and the Upper East Side more than the Beach: Krüs, Chug's, Boia De, La Natural, Phuc Yea. The Bibs cluster here.",
           "Picked for the room you'd return to on a weeknight. Eleven of Miami's eighteen Bibs are on this list, plus Los Félix and Ariete with stars. Itamae AO is flagged: its 2025 star wasn't in the 2026 list at press time."),
 "Speakeasies": ("Miami hides its best bars in plain sight — Bar Kaiju on a food-hall mezzanine, ViceVersa behind a downtown door, Bodega's behind a porta-potty. The rest are the hotel bars and the Little Havana stages.",
           "Ranked by the drink. ViceVersa (№46) and Bar Kaiju (№70) are on the 50 Best; Dante's HiFi is the listening bar; Café La Trova is here because the cantinero show is theater. The closed ones are listed so you know."),
 "Rooftops": ("A city built for the view: Sugar forty floors over Brickell, the pools of Mid-Beach, the Miami River at sunset. Stretched to include the waterfront decks, which do the same job.",
           "Chosen for the view first. Where the drink matters too — Sugar, Astra, Watr — it's noted. The Miami River places are the ones locals would send you to over the Beach."),
 "Bars": ("Julio Cabrera's Café La Trova is the soul of the scene; Sweet Liberty and Broken Shaker built the modern one; the dives — Mac's Club Deuce, Ted's, Churchill's — are the counterweight.",
           "Ranked and recognized first, then institutions, hotel bars, dives, wine, beer. New Times' Top 50 Bars 2026 is the local cross-check."),
 "Coffee": ("Miami runs on cafecito. The ventanitas at Versailles and La Carreta, the 3:05pm colada, and then the third-wave roasters of Wynwood and Little River.",
           "Selected for the cup and the ritual. Panther is the roaster; Pasión del Cielo the Cuban-style chain worth the stop; the ventanitas are where you'll understand the city."),
 "Restaurants": ("The 2026 Florida guide gave Miami fourteen stars — L'Atelier the only two-star in the state — and eighteen Bibs. Around them: the Design District's dining rooms, Brickell's scene, and the Cuban, Haitian and Peruvian kitchens that are the actual city.",
           "Grouped by distinction, then the new guard, then the classics. Joe's Stone Crab is seasonal (October–May); Versailles is a civic institution. The Bibs and the Little Havana block are where to read slowly."),
 "Brunch": ("Sunday means the Grove, the river, or a Cuban breakfast at a ventanita. The Beach's hotel brunches are the spectacle; the neighborhood ones are the food.",
           "Kept to places that consistently top Resy and OpenTable's weekend demand plus the counters you walk into. Nine Bibs and two starred rooms do brunch here."),
 "Off-beat": ("Fritas, croquetas, batidos, a 24-hour Nicaraguan fritanga, stone crabs from the takeout window, and a fruit stand on the road to the Keys.",
           "Selected for singularity — things that could only be here. Robert Is Here, Alabama Jack's and Knaus Berry Farm justify the drive south; the Little Havana counters justify everything else."),
 "Bakeries": ("Pastelitos de guayaba at Vicky and Karla, challah at Zak the Baker, Antonio Bachour's counter in Coral Gables, and the Hialeah bakeries most visitors never reach.",
           "Chosen on the strength of one signature item each. Pinecrest Bakery is on for being open at 3am; El Brazo Fuerte for 1968."),
 "Dessert": ("Azucar's Abuela Maria, the batido, the flan at Versailles, and a two-star mignardise cart in the Design District.",
           "A mix of the destination and the institution. Half of this list is Cuban, because that's the sweet tooth Miami has."),
 "Scene": ("Where the room is the point: the fish tanks of Brickell, the Design District's dining rooms, the Faena's theater, and Joe's since 1913.",
           "Brickell and the Beach lead; the Design District's starred rooms are here for the scene as much as the food. Soho Beach House is on because everyone will ask."),
 "Nightlife": ("Club Space's terrace at sunrise, LIV at the Fontainebleau, E11even's 24 hours, and the live Cuban music on Calle Ocho.",
           "Clubs and stages together. Story, Treehouse and Rockwell are listed closed; Ultra, III Points and Art Basel week are on because they change the calendar."),
}
R="""Mandolin Aegean Bistro|Michael's Genuine|Krüs Kitchen|Los Félix|Chug's Diner|Tâm Tâm|Phuc Yea|La Natural|Zitz Sum|Cotoa|Barra Callao|To Be Determined|Boia De|Ariete|Jaguar Sun|Margot|Lagniappe|Macchialina|Sardinia Enoteca|Stubborn Seed|Mila|Threefold Café|All Day|Niu Kitchen|Kaido|Sereia|Erba|Mano Libera|Bistro Ocho Miami|Elyu Omakase|El Turco|Hometown Barbecue Miami|Lucali|Blue Collar|Mignonette|Sushi Garage|Pastis Miami|Sant Ambroeus|Casa Tua Cucina|Itamae AO|EntreNos|ViceVersa|Bar Kaiju|Dante's HiFi|Sweet Liberty|Foxhole|The Anderson|Lost Boy Dry Goods|Mama Tried|Better Days|Broken Shaker|Esotico|Over Under|Bar Bastille|Café La Trova|Medium Cool|Tropezón|Le Chick|Casa Florida|Bar Bevy|Le Jardinier|Cote Miami|Elcielo Miami|Hiden|Ogawa|Shingo|Tambourine Room by Tristan Brandt|The Surf Club Restaurant|Mutra|Bachour|Ghee Indian Kitchen|Sanguich de Miami|Tinta y Café|Double Luck|Sadelle's|Carbone Miami|Contessa Miami|Casadonna|Palma|Sunny's Steakhouse|Sunny's|Klaw|Amara at Paraiso|Fiola Miami|Uchi Miami|Naoe|Makoto|Papi Steak|Gekko|Sexy Fish|Komodo|Swan|Kiki on the River|Seaspice|La Mar by Gastón Acurio|Cantina La Veinte|Bakan|Los Fuegos by Francis Mallmann|Pao by Paul Qui|Boulud Sud|Estiatorio Milos|Joe's Stone Crab|Prime 112|Casa Tua|The Forge|Byblos|Motek|Juvia|Yardbird|Osaka Nikkei|Toscana Divino|Cipriani Downtown Miami|Il Gabbiano|Novecento|KYU|Rosie's|Azabu|Wabi Sabi by Shuji|Mr. Mandolin|Harry's Pizzeria|Stanzione 87|La Leggenda|Ironside Pizza|Greenstreet Cafe|Big Pink|Front Porch Café|Glass & Vine|Lulu in the Grove|Lulu|Monty's Sunset|Monty's Raw Bar|Rusty Pelican|Lightkeepers|Shuckers|Sugar|Rosa Sky|Astra|No. 3 Social|Watr at the 1 Rooftop|Area 31|Serena Rooftop|Lona|Higher Ground|Terras|Deck Sixteen|Level 25|Sky Yard|Casa Neos|Baia Beach Club|Strawberry Moon|Nikki Beach|Bâoli Miami garden|Bâoli|Zuma|Hakkasan|Nobu Miami|Nusr-Et Miami|Chotto Matte|Le Sirenuse|Champagne Bar at the Surf Club|The Bar at the Setai|Bleau Bar|Lido Bayside|Krüs Kitchen|Coyo Taco|Taquiza|Chef Adrianne's Vineyard Restaurant|Cvi.che 105|Pisco y Nazca|Mister O1 Extraordinary Pizza|Bagel Emporium|Zak the Baker|Rosetta Bakery|True Loaf|Madruga Bakery|Sweet Caroline|Bar Rita|The Sylvester|El Patio Wynwood|Bar One|Batch Gastropub|Kill Your Idol|Rec Room|Do Not Sit On The Furniture|Gramps|Kush|Boxelder|The Corner|Blackbird Ordinary|Ball & Chain|Hoy Como Ayer|Bar Nancy|Taurus|Barracuda Taphouse|Jolene Sound Room""".split("|")
T="""L'Atelier de Joël Robuchon|Hiden|Ogawa|Shingo|Naoe|Azabu|Tambourine Room by Tristan Brandt""".split("|")
O="""Versailles|La Carreta|Old's Havana|Puerto Sagua|Garcia's Seafood Grille & Fish Market|Casablanca|Captain Jim's Seafood|Fontainebleau pool bar|Faena Theater|The Fillmore Miami Beach""".split("|")
S="""LIV|E11even|Club Space|Floyd|Basement Miami|Mayami|Oasis Wynwood|Wall Lounge|Le Rouge|M2|Mango's Tropical Café|Strawberry Moon|Nikki Beach|Soho Beach House""".split("|")
W="""Versailles ventanita|La Carreta ventanita|El Palacio de los Jugos|Los Pinareños Frutería|Islas Canarias|Vicky Bakery|Karla Bakery|Sergio's|Luis Galindo's Latin American|Chef Creole|Naomi's Garden|Clive's Cafe|Azucar Ice Cream|Domino Park|La Camaronera|El Rey de las Fritas|El Mago de las Fritas|Enriqueta's|La Sandwicherie|Mac's Club Deuce|Ted's Hideaway|Churchill's Pub|Las Rosas|Alabama Jack's|Robert Is Here|Knaus Berry Farm|Redland Fruit & Spice Park|Schnebly Redland's Winery|Joe's Take Away|Yambo|Shorty's BBQ|El Toro Taco|1-800-Lucky|Wynwood Marketplace|Time Out Market Miami|The Citadel|Panther Coffee|Vice City Bean|Imperial Moto|Pasión del Cielo|Eternity Coffee Roasters|Café Demetrio|Alaska Coffee Roasting|Latin Cafe 2000|Pinecrest Bakery|Buena Vista Deli|El Exquisito|Miam Café|Small Tea|Books & Books Café|Coral Bagels|Cindy Lou's Cookies|The Salty Donut|Crumb on Parchment|OTL|Dr. Smood|Pura Vida|Bebito's Café|Bebito's|Café Curuba|Delicias de España|Doce Provisions|La Ventana|Fireman Derek's|Night Owl Cookies|Chocolate Fashion|Blue Bottle Miami|Dasher & Crank|Wynwood Parlor|Bianco Gelato|Cielito Artisan Pops|Morelia Gourmet Paletas|Frice Cream|Mr. Kream|Cream Parlor|Kung Fu Tea|Gilbert's Bakery|Toasted Bagelry|Bagel Bar East|Bunnie Cakes|Le Macaron|Ladurée Miami|Paris Baguette|Tous les Jours|B Bistro + Bakery|Little Bread|Charlotte Bakery|La Provence|Manolo|La Boulangerie Boul'Mich|Misha's Cupcakes|Icebox Café|Divine Delicacies|Cuban Guys|Sweetness Bake Shop|Ricky Bakery|Yisell Bakery|El Brazo Fuerte|Old Lisbon's pastéis de nata|A La Folie|Union Beer Store|J. Wakefield Brewing|Veza Sur|Wynwood Brewing|Tripping Animals|Unbranded Brewing|The Tank|Lincoln's Beard|M.I.A. Beer Company|Sandbar Lounge|Fox's Lounge|Cubaocho|ATV Records|Bayfront Park|III Points|Art Basel week|Kaseya Center concerts|Adrienne Arsht Center|Hard Rock Live|Miami Beach Bandshell|Coyo Taco's back room|Vinya Wine""".split("|")
PLAT={}
for lst,tag in ((O,'OpenTable'),(S,'SevenRooms'),(W,'Walk-in'),(R,'Resy'),(T,'Tock')):
    for n in lst:
        n=n.strip()
        if n: PLAT[n]=tag
def lookup(name):
    if name in PLAT: return PLAT[name]
    base=name.split(' (')[0].strip()
    return PLAT.get(base)
PRICE_OVER={"L'Atelier de Joël Robuchon":4,"Le Jardinier":4,"Stubborn Seed":4,"Cote Miami":4,"Boia De":3,"Ariete":3,"Elcielo Miami":4,"Hiden":4,"Los Félix":3,"Ogawa":4,"Shingo":4,"Tambourine Room by Tristan Brandt":4,"The Surf Club Restaurant":4,"Mutra":4,"Itamae AO":4,"EntreNos":4,"Krüs Kitchen":3,"Carbone Miami":4,"Papi Steak":4,"Gekko":4,"Sexy Fish":4,"Komodo":4,"Swan":3,"Casadonna":4,"Kiki on the River":4,"Seaspice":4,"Zuma":4,"Cipriani Downtown Miami":4,"Nusr-Et Miami":4,"Mila":4,"Juvia":4,"Casa Tua":4,"Byblos":3,"Prime 112":4,"Joe's Stone Crab":4,"Estiatorio Milos":4,"Nobu Miami":4,"Hakkasan":4,"Los Fuegos by Francis Mallmann":4,"Pao by Paul Qui":4,"The Forge":4,"Le Sirenuse":4,"Makoto":4,"Carpaccio":3,"Contessa Miami":4,"Uchi Miami":4,"KYU":3,"Bakan":3,"Sunny's Steakhouse":4,"Amara at Paraiso":3,"Klaw":4,"La Mar by Gastón Acurio":3,"Cantina La Veinte":3,"Osaka Nikkei":3,"Toscana Divino":3,"Il Gabbiano":4,"Fiola Miami":4,"Naoe":4,"Azabu":4,"Wabi Sabi by Shuji":3,"Pastis Miami":3,"Sadelle's":3,"Macchialina":3,"Jaguar Sun":2,"Niu Kitchen":3,"Kaido":3,"Sereia":3,"Erba":3,"Palma":3,"Mandolin Aegean Bistro":3,"Michael's Genuine":3,"Tâm Tâm":2,"Chug's Diner":2,"Phuc Yea":2,"La Natural":2,"Zitz Sum":2,"Tinta y Café":1,"Bachour":2,"Ghee Indian Kitchen":2,"El Turco":2,"Hometown Barbecue Miami":2,"Lucali":2,"Sanguich de Miami":1,"Cotoa":2,"Barra Callao":2,"Double Luck":2,"To Be Determined":2,"Versailles":2,"La Carreta":1,"Versailles ventanita":1,"La Carreta ventanita":1,"El Palacio de los Jugos":1,"Los Pinareños Frutería":1,"Islas Canarias":1,"Vicky Bakery":1,"Karla Bakery":1,"Sergio's":1,"Luis Galindo's Latin American":1,"Chef Creole":1,"Naomi's Garden":1,"Clive's Cafe":1,"Azucar Ice Cream":1,"La Camaronera":1,"El Rey de las Fritas":1,"El Mago de las Fritas":1,"Enriqueta's":1,"La Sandwicherie":1,"Puerto Sagua":1,"Big Pink":2,"Bebito's":1,"Bebito's Café":1,"Old's Havana":2,"Doce Provisions":2,"Yambo":1,"Shorty's BBQ":1,"Robert Is Here":1,"Alabama Jack's":2,"Knaus Berry Farm":1,"Joe's Take Away":3,"Garcia's Seafood Grille & Fish Market":2,"Casablanca":2,"Captain Jim's Seafood":2,"Shuckers":2,"Rusty Pelican":3,"Lightkeepers":3,"Coyo Taco":1,"Taquiza":1,"Mister O1 Extraordinary Pizza":2,"Café La Trova":3,"ViceVersa":3,"Bar Kaiju":3,"Sweet Liberty":2,"Dante's HiFi":3,"Medium Cool":3,"Broken Shaker":2,"Mac's Club Deuce":1,"Ted's Hideaway":1,"Churchill's Pub":1,"Las Rosas":1,"Ball & Chain":2,"Bar Nancy":1,"Hoy Como Ayer":2,"Taurus":1,"Gramps":1,"Kush":2,"The Corner":1,"Sugar":3,"Rosa Sky":3,"Astra":3,"Watr at the 1 Rooftop":3,"Level 25":3,"Nikki Beach":4,"Bâoli":4,"LIV":4,"E11even":4,"Club Space":3,"Floyd":2,"Basement Miami":3,"Mayami":3,"Wall Lounge":4,"Le Rouge":3,"M2":3,"Mango's Tropical Café":2,"Cubaocho":2,"Soho Beach House":4,"Faena Theater":4,"Le Jardinier's desserts":4,"L'Atelier's mignardises":4,"Stubborn Seed's dessert counter":4}
def occasions(name, cat=None, price=0):
    o=[]
    if cat=='Restaurants':
        if price>=4: o=['Romantic','Date night']
        elif price==3: o=['Date night']
        elif price==2: o=['Casual','Date night']
        else: o=['Casual']
        if name in ('Carbone Miami','Papi Steak','Gekko','Sexy Fish','Komodo','Swan','Casadonna','Kiki on the River','Seaspice','Zuma','Cipriani Downtown Miami','Nusr-Et Miami','Mila','Juvia','Byblos','Prime 112','Joe\'s Stone Crab','KYU','Bakan','Versailles','1-800-Lucky','Time Out Market Miami','The Citadel','Yardbird'): o=o+['Group']
    elif cat=='Cafés': o=['Date night','Casual'] if price>=2 else ['Casual']
    elif cat=='Speakeasies': o=['Date night','Late night']
    elif cat=='Bars':
        o=['Late night'] if price<=1 else ['Date night','Late night']
        if 'Brewing' in name or name in ('Boxelder','Union Beer Store','Veza Sur','Tripping Animals','Unbranded Brewing','The Tank',"Lincoln's Beard",'M.I.A. Beer Company','J. Wakefield Brewing'): o=['Group','Casual']
        if name in ('Champagne Bar at the Surf Club','Le Sirenuse','The Bar at the Setai','ViceVersa','Bar Kaiju',"Dante's HiFi",'Medium Cool','Margot','Lagniappe'): o=['Romantic','Date night']
    elif cat=='Rooftops': o=['Date night','Group']
    elif cat=='Coffee': o=['Sweets','Brunch']
    elif cat=='Brunch': o=['Brunch']
    elif cat=='Off-beat': o=['Casual']
    elif cat=='Bakeries': o=['Sweets','Brunch']
    elif cat=='Dessert': o=['Sweets']
    elif cat=='Scene': o=['Group','Date night'] if price<=3 else ['Romantic','Group']
    elif cat=='Nightlife': o=['Late night','Group']
    return o
from cities.miami_itin import ITINS, GOTCHAS
NOTES_HTML='''<p>Michelin: the 2026 Florida selection, announced May 28, 2026 — the first to cover the entire state. Miami holds fourteen stars (L'Atelier de Joël Robuchon the only two-star in Florida for a fifth year; Mutra in North Miami the new one-star, the first kosher restaurant in the world with a star), three Green Stars (Krüs Kitchen, Los Félix, Stubborn Seed) and eighteen Bib Gourmands, with Barra Callao, Cotoa, Double Luck and To Be Determined added this year. Itamae AO's 2025 star was not in the 2026 list at press time and is flagged to verify.</p><p>Bars: North America's 50 Best Bars 2026 (April 22, 2026) — Café La Trova №42, ViceVersa №46, Bar Kaiju №70 on the extended list. ViceVersa was a 2025 James Beard Best New Bar finalist; Café La Trova has been nominated for Outstanding Bar. Miami New Times' Top 50 Bars 2026 is the local cross-check.</p><p>Occasion chips for Miami are editorial assignments, by category and price. Booking platforms are listed as best known at time of printing; the Resy app is the source of truth for the Amex credit. Joe's Stone Crab is seasonal — mid-October to May.</p><p>Photography via Pexels (royalty-free): two photographs, cropped and reused across the twelve sections.</p>'''
