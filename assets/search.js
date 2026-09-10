/* listedeville — site-wide search & filters sheet. Opens from the nav "Search" tab on every page. */
(function(){
var CITIES=[["new-york","New York"],["boston","Boston"],["washington-dc","Washington, DC"],["miami","Miami"],["chicago","Chicago"],["san-francisco","San Francisco"],["los-angeles","Los Angeles"],["seattle","Seattle"]];
var CATS=["Cafés","Speakeasies","Rooftops","Bars","Coffee","Restaurants","Brunch","Off-beat","Bakeries","Dessert","Scene","Nightlife"];
var ONLY=[["stars",'<span class="star">★</span> Michelin-starred'],["bib",'<span class="bib">Bib</span> Bib Gourmand'],["ranked","Ranked (50 Best / NYT)"],["amex",'<span class="amex">Amex ✓</span> Resy credit'],["new","New since last edition"],["visited",'<span class="been">been</span> Tony\'s been'],["jbf",'<span class="jbf">JBF 2026</span> James Beard nominee'],["showclosed","Show closed"]];
var PLAT=["Resy","Tock","OpenTable","SevenRooms","Walk-in"];
var OCC=[["Romantic","Romantic"],["Date night","Date night"],["Casual","Casual"],["Group","Group / lively"],["Brunch","Brunch &amp; daytime"],["Late night","Late night"],["Sweets","Coffee &amp; sweets"]];
var here=(location.pathname.split("/")[1]||""); var isCity=CITIES.some(function(c){return c[0]===here});
var S={city:isCity?here:"new-york",q:"",cats:{},f:{},p:{},o:{},pr:{}};
if(isCity){var u=new URLSearchParams(location.search);S.q=u.get("q")||"";u.getAll("cat").forEach(function(c){S.cats[c]=1});ONLY.forEach(function(k){if(u.get(k[0])==="1")S.f[k[0]]=1});u.getAll("p").forEach(function(p){S.p[p]=1});u.getAll("o").forEach(function(o){S.o[o]=1});u.getAll("pr").forEach(function(x){S.pr[x]=1});}
function chips(sel,arr,store,attr){return arr.map(function(a){var v=Array.isArray(a)?a[0]:a,l=Array.isArray(a)?a[1]:a;return '<button type="button" class="chip" data-'+attr+'="'+v+'" aria-pressed="'+(store[v]?"true":"false")+'">'+l+'</button>'}).join("")}
var el=document.createElement("div");el.className="ss";el.id="ss";el.hidden=true;el.setAttribute("role","dialog");el.setAttribute("aria-label","Search & filters");
el.innerHTML='<div class="ssin"><div class="sshead"><p class="eyebrow">Search &amp; filters</p><button type="button" class="ssx" id="ssx" aria-label="Close">×</button></div>'+
'<div class="ssrow"><label class="sscity"><span class="lbl">City</span><select id="sscity">'+CITIES.map(function(c){return '<option value="'+c[0]+'"'+(c[0]===S.city?" selected":"")+'>'+c[1]+'</option>'}).join("")+'</select></label>'+
'<input id="ssq" type="search" placeholder="Search a place, a neighborhood, a cuisine…" autocomplete="off" aria-label="Search places" value=""></div>'+
'<div class="rows"><span class="lbl">Lists</span>'+chips(0,CATS,S.cats,"c")+'</div>'+
'<div class="rows"><span class="lbl">Only</span>'+chips(0,ONLY,S.f,"f")+'</div>'+
'<div class="rows"><span class="lbl">Book on</span>'+chips(0,PLAT,S.p,"p")+'</div>'+
'<div class="rows"><span class="lbl">Occasion</span>'+chips(0,OCC,S.o,"o")+'</div>'+
'<div class="rows"><span class="lbl">Price</span>'+chips(0,[["1","$"],["2","$$"],["3","$$$"],["4","$$$$"]],S.pr,"pr")+'</div>'+
'</div><div class="ssbar"><span id="sscount"></span><span><button type="button" class="pill" id="ssreset">Clear all</button><a class="pill solid" id="ssgo" href="#">Show places</a></span></div>';
document.body.appendChild(el);
var $=function(s){return el.querySelector(s)}; $("#ssq").value=S.q;
var cache={};
function load(slug,cb){if(cache[slug])return cb(cache[slug]);fetch("/assets/"+slug+".json").then(function(r){return r.json()}).then(function(d){cache[slug]=d.items;cb(d.items)}).catch(function(){cb(null)})}
function has(o){for(var k in o)return true;return false}
function match(d){
  if(d.closed&&!S.f.showclosed&&!S.q)return false;
  if(has(S.cats)&&!S.cats[d.cat])return false;
  if(S.f.stars&&!d.stars)return false; if(S.f.bib&&!d.bib)return false; if(S.f.ranked&&!(d.na50||d.nyt))return false;
  if(S.f.amex&&!d.amex)return false; if(S.f.new&&!d.new)return false; if(S.f.visited&&!d.visited)return false; if(S.f.jbf&&!d.jbf)return false;
  if(has(S.o)&&!d.occ.some(function(o){return S.o[o]}))return false;
  if(has(S.pr)&&!S.pr[String(d.price)])return false;
  if(has(S.p)&&!S.p[d.platform||""])return false;
  if(S.q){var q=S.q.toLowerCase();var hay=(d.name+" "+d.place+" "+d.cat+" "+d.group+" "+d.notes.join(" ")+" "+(d.platform||"")+" "+(d.jbf||"")+" "+d.occ.join(" ")).toLowerCase();if(hay.indexOf(q)<0)return false}
  return true}
function url(){var q=new URLSearchParams();if(S.q)q.set("q",S.q);Object.keys(S.cats).forEach(function(c){q.append("cat",c)});Object.keys(S.f).forEach(function(k){q.set(k,"1")});Object.keys(S.p).forEach(function(p){q.append("p",p)});Object.keys(S.o).forEach(function(o){q.append("o",o)});Object.keys(S.pr).forEach(function(x){q.append("pr",x)});var s=q.toString();return "/"+S.city+"/"+(s?"?"+s:"")}
var name=function(){return CITIES.filter(function(c){return c[0]===S.city})[0][1]};
function update(){$("#ssgo").href=url();var slug=S.city;$("#sscount").textContent="…";load(slug,function(items){if(S.city!==slug)return;if(!items){$("#sscount").textContent="";$("#ssgo").textContent="Open "+name();return}var n=items.filter(match).length;$("#sscount").textContent=n+" of "+items.length+" places in "+name();$("#ssgo").textContent="Show "+n+" places";});
  el.querySelectorAll(".chip").forEach(function(b){var d=b.dataset,st=d.c?S.cats:d.f?S.f:d.p?S.p:d.o?S.o:S.pr,v=d.c||d.f||d.p||d.o||d.pr;b.setAttribute("aria-pressed",st[v]?"true":"false")})}
el.addEventListener("click",function(e){var b=e.target.closest(".chip");if(!b)return;var d=b.dataset,st=d.c?S.cats:d.f?S.f:d.p?S.p:d.o?S.o:S.pr,v=d.c||d.f||d.p||d.o||d.pr;if(st[v])delete st[v];else st[v]=1;update()});
$("#ssq").addEventListener("input",function(e){S.q=e.target.value;update()});
$("#sscity").addEventListener("change",function(e){S.city=e.target.value;update()});
$("#ssreset").onclick=function(){S.q="";S.cats={};S.f={};S.p={};S.o={};S.pr={};$("#ssq").value="";update()};
var tab=document.getElementById("searchtab");
function open(){el.hidden=false;document.body.classList.add("ssopen");tab&&tab.setAttribute("aria-expanded","true");update();setTimeout(function(){$("#ssq").focus()},60)}
function close(){el.hidden=true;document.body.classList.remove("ssopen");tab&&tab.setAttribute("aria-expanded","false")}
if(tab)tab.addEventListener("click",function(e){e.preventDefault();el.hidden?open():close()});
$("#ssx").onclick=close; document.addEventListener("keydown",function(e){if(e.key==="Escape"&&!el.hidden)close()});
if(location.hash==="#search")open();
})();
