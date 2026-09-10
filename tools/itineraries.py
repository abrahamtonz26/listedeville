# -*- coding: utf-8 -*-
# Three ready-to-follow food itineraries for a first-time visitor, drawn only from the list.
# Each stop: (time, place, what to do). Every place named here is on the liste de ville.

ITINS = [
 {
  "key":"one-day","title":"One day","deck":"Downtown, on foot. The single day that shows a first-timer why New Yorkers argue about food.",
  "who":"You land in the morning and leave tomorrow. Everything is below 14th Street except the nightcap, and nothing needs a taxi.",
  "book":"Book one thing: dinner. Everything else is walk-in.",
  "days":[
   {"label":"The day","stops":[
     ("8:30","Devoción (Flatiron)","A flat white from beans roasted days after landing from Colombia. Or a cruller at Daily Provisions on Union Square if the line is shorter."),
     ("9:30","Russ & Daughters Cafe (LES)","The classic board: nova, scallion cream cheese, everything bagel. Book on Resy the night before; or take it away from the 1914 shop on Houston Street."),
     ("11:00","Mei Lai Wah → Alimama (Chinatown)","Walk south. One baked pork bun, one mochi doughnut. Both under $5, both worth the detour."),
     ("12:30","Katz's Delicatessen (LES)","Pastrami on rye, cut to order. Take the ticket they hand you at the door and do not lose it. Tip the cutter a couple of dollars and he'll slide you a taste."),
     ("2:30","Dominique Ansel Bakery (SoHo)","Skip the Cronut queue unless you're early; the DKA and the frozen s'more are the real order. Then wander west into the Village."),
     ("4:30","Levain Bakery (West Village)","One chocolate-chip walnut cookie, split two ways. It's a meal."),
     ("6:00","Dante (Greenwich Village)","A negroni at the bar that made them famous. Sit outside if it's warm."),
     ("7:30","Semma (West Village) ★","South Indian, Michelin-starred, NYT №7. Reservations open on Resy 30 days out at 10am — set an alarm. Backup, same walk: Via Carota (walk-in, put your name down at 5:30) or Rezdôra (Resy)."),
     ("10:00","Attaboy (LES)","No menu, no sign. Tell them what you like. Walk-in only; the line moves. If it's long, Double Chicken Please is two blocks away."),
   ]},
  ]},
 {
  "key":"three-day","title":"Three days","deck":"Downtown, then Brooklyn, then uptown. One borough a day, one big dinner a night.",
  "who":"A long weekend. Day one is the one-day plan; days two and three cross the river and go north.",
  "book":"Book three dinners the day reservations open (see gotchas), and one lunch: Jean-Georges.",
  "days":[
   {"label":"Day 1 · Downtown","stops":[
     ("All day","Follow the one-day plan","Coffee at Devoción, bagels at Russ & Daughters, Katz's for lunch, the Village in the afternoon, Semma for dinner, Attaboy after."),
   ]},
   {"label":"Day 2 · Brooklyn","stops":[
     ("9:00","Radio Bakery (Greenpoint)","The cardamom bun and the ham-and-cheese croissant. Get there before ten; they sell out."),
     ("10:30","Devoción (Williamsburg)","The original roastery, under a skylight the size of a tennis court. Coffee two."),
     ("12:00","L'Industrie Pizzeria (Williamsburg)","One burrata slice, standing up. Then walk the waterfront to Domino Park."),
     ("2:00","Maison Premiere (Williamsburg)","Oysters and an absinthe drip at the marble bar — 50 Best №40. Book on Resy; the garden is the seat to ask for."),
     ("4:00","Bar Blondeau (Wythe Hotel)","Sixth-floor view of Manhattan for the price of a glass of wine. Beats every ticketed observation deck."),
     ("7:30","Lilia (Williamsburg)","Missy Robbins' pasta. Resy, 28 days out, and it goes in seconds — use Notify. Backups within ten minutes' walk: Misi (same chef, easier), Francie ★, Bonnie's (Cantonese-American, Bib)."),
     ("10:00","Union Pool → Nowadays","A dive with a taco truck in the yard, then a car to Ridgewood for the best sound system in the city. Or stay put: Bar Madonna (50 Best №36) is three blocks from Lilia."),
   ]},
   {"label":"Day 3 · Uptown","stops":[
     ("9:00","Barney Greengrass (UWS)","The Sturgeon King, since 1908. Sturgeon and eggs, a bialy, cash-friendly, no reservations — arrive before 9:30 on a weekend."),
     ("10:30","Central Park → Cafe Sabarsky (UES)","Walk across the park to the Neue Galerie for a Viennese coffee and a slice of Sachertorte in the most beautiful room on Fifth Avenue."),
     ("12:30","Jean-Georges (Columbus Circle) ★★","The two-course lunch prix fixe is the best-value Michelin meal in America. Book on OpenTable; ask for a table by the window over the park."),
     ("3:30","Bemelmans Bar (The Carlyle)","Ludwig Bemelmans' murals, a martini, and a piano from 5:30. No cover before then; jackets are not required but everyone looks like they tried."),
     ("6:00","Bar SixtyFive (Rainbow Room, 30 Rock)","Sunset from the 65th floor with the Empire State straight ahead. Dress code enforced — no sneakers, no shorts. Book on OpenTable."),
     ("8:00","Le Bernardin (Midtown) ★★★","Eric Ripert's fish, three stars for three decades. Resy, 30 days out. Backup: Le Coucou ★ (SoHo, Resy) or Cote ★ (Flatiron, Resy) if you'd rather end downtown."),
     ("10:30","The Campbell (Grand Central)","A nightcap in a 1920s railroad magnate's office, then the train home. Or Bemelmans again — after 9:30 it costs a cover, and it's worth it."),
   ]},
  ]},
 {
  "key":"five-day","title":"Five days","deck":"The three-day plan, plus Queens and one day that is entirely about the splurge.",
  "who":"Enough time to eat like a resident: the outer boroughs, an omakase counter, a speakeasy crawl, and a proper Sunday brunch.",
  "book":"This is a reservations trip. Set alarms for Semma, Lilia, Le Bernardin and your omakase; the rest is walk-in.",
  "days":[
   {"label":"Days 1–3","stops":[
     ("All","Follow the three-day plan","Downtown, Brooklyn, uptown."),
   ]},
   {"label":"Day 4 · Queens","stops":[
     ("10:00","7 train to Jackson Heights","Take the 7 from Grand Central; the ride is part of the trip. Bring cash — many of the best things today don't take cards."),
     ("10:30","Lhasa Fast Food (Jackson Heights)","Tibetan momos, through the back of a phone shop on 74th Street. Phayul (Bib) is upstairs across the road if you want the spicier version."),
     ("12:00","Kabab King (Jackson Heights)","NYT №100 and the mayor's canteen. Chicken tikka, seekh kebab, and the naan straight from the tandoor. Walk-in, cash-friendly."),
     ("1:30","Corona Plaza street vendors","Two stops east. Tacos, tlayudas, and esquites from the carts under the 103rd Street station. Cash only."),
     ("3:00","Nan Xiang Xiao Long Bao (Flushing)","Ride the 7 to the end for the soup dumplings, then White Bear for wontons in chili oil. Walk-in; expect a line at Nan Xiang, and it moves fast."),
     ("6:30","Casa Enrique (Long Island City)","Back toward Manhattan on the 7. Chiapas-style Mexican that held a Michelin star for a decade. Resy."),
     ("9:00","Dutch Kills (Long Island City)","A serious cocktail bar four blocks from the train, then one stop home."),
   ]},
   {"label":"Day 5 · The splurge, and Sunday","stops":[
     ("11:00","Golden Diner (Two Bridges) or Sadelle's (SoHo)","Brunch. Golden Diner's Thai tea pancakes and honey-butter egg sandwich (Resy, or a short wait); Sadelle's for the bagel tower if you want the room."),
     ("1:30","Chelsea Market → Los Tacos No.1","Adobada tacos at the counter, then the High Line north to Hudson Yards."),
     ("3:30","Overstory (FiDi, 64th floor)","50 Best №33. Resy. Go at golden hour; the terrace wraps around the building."),
     ("5:30","Speakeasy crawl, East Village","PDT (through the phone booth in Crif Dogs — same-day tables on Resy at 3pm), then Death & Co across Avenue A (Resy), then Amor y Amargo (walk-in) for bitters."),
     ("8:30","Omakase: Sushi Sho ★★★ or Sushi Nakazawa ★","Sushi Sho is the new three-star; Tock, weeks out. Nakazawa is the one you can actually get: Tock, and the lounge takes walk-ins. Alternative splurge: Eleven Madison Park ★★★ (Resy; plant-based) or Per Se ★★★ (Tock; the four-course salon menu is the value play)."),
     ("11:00","Le Bain (The Standard) or Public Records (Gowanus)","Le Bain for the Meatpacking rooftop and the plunge pool; Public Records for the hi-fi room. Either way, you've earned it."),
   ]},
  ]},
]

GOTCHAS = [
 ("Reservations open on a schedule, not when you remember.", "Most Resy restaurants release tables 30 days out at 9 or 10am ET (Lilia: 28 days). Set alarms, use Resy's Notify for waitlists, and add your Amex to Resy for Global Dining Access and Platinum Nights, which unlock tables the public can't see. Walk-ins: arrive at 5:15 for a 5:30 opening, or take a bar seat — most places save some."),
 ("Cash is not dead here.", "Lucali, Di Fara, Punjabi Deli, most Jackson Heights and Corona Plaza vendors, and Peter Luger (cash or debit only — no credit cards) all want it. Carry $100 in small bills on the Queens day."),
 ("The Katz's ticket.", "They hand you a ticket at the door; every counter marks it; you pay on the way out. Lose it and it's a $50 fee. Tip the cutter a few dollars in cash before he slices."),
 ("Tip 20%, and the price isn't the price.", "Menus exclude 8.875% sales tax, and 18–22% tip is expected on the pre-tax total. Some restaurants now add a service charge — check the bill before tipping again. Bartenders: a dollar or two per drink, 20% on cocktails."),
 ("Dress codes are real in a few places.", "Bar SixtyFive, The Polo Bar, Le Bernardin and Per Se enforce them — no shorts, no sneakers, and jackets are expected at the last two. Bemelmans and the speakeasies don't care, but a collared shirt goes further everywhere."),
 ("Bring ID, even if you're sixty.", "Every bar cards. A passport or driver's license; a photo on your phone won't work. Speakeasies also have house rules — no photos at Attaboy and PDT, no standing at the bar at Angel's Share."),
 ("Monday and Tuesday are the quiet days.", "Many restaurants close one or both (Lucali is closed Tuesdays; Semma and Lilia are closed Mondays). Rooftops are seasonal and weather-dependent — Serra by Birreria and Rooftop Reds are summer-only; call before crossing town in November."),
 ("Three neighborhoods a day, not five.", "The subway is fast but the city is big. Tap in with any contactless card or phone (OMNY) — no MetroCard needed, and fares cap after 12 rides in a week. Late-night in Brooklyn and Queens, take a car."),
 ("Use the Amex credit like a New Yorker.", "The Platinum credit is $100 per quarter and doesn't roll over; the Gold is $50 twice a year. Pay with the enrolled card at any Resy venue showing the 'Resy Credit eligible' badge (Tock venues too from September 15). No need to book through Resy — just pay with the card. Check which quarter you're in before the splurge dinner."),
 ("Anything marked verify, verify.", "A handful of places on the list have been reported closed, moved or renamed since this edition went to press. Thirty seconds on Resy or Google before you get in a cab."),
 ("The bagel rules.", "Order it by cream cheese, not by 'plain': 'everything with scallion' is the New York order. Don't ask for it toasted at Russ & Daughters, Utopia or Apollo — a fresh bagel isn't. And no, it's not the water."),
 ("One for the road.", "Airport lounges count: Pierre Hermé at the Delta lounge and The 1850 bar at the Centurion Lounge are both at JFK, and both on this list."),
]
