var SPARQLURL = "http://localhost:3030/RFinder/query";
var Ingredients = []
var IngredientsExclude = []
var shiftpressed;
var sinp = {};
var e = jQuery.Event( "keydown", { keyCode: "Enter"} );
function autocomplete(inp, arr) {
    sinp[inp.id] = $(inp);
    console.log(inp);
    let currentFocus;
    inp.addEventListener("input", function(e) {
        let a, b, i, val = this.value;
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list" + inp.id);
        a.setAttribute("class", "autocomplete-items");
        this.parentNode.appendChild(a);
        for (i = 0; i < arr.length; i++) {
          if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            b = document.createElement("DIV");
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            b.addEventListener("click", function(e) {
                inp.value = this.getElementsByTagName("input")[0].value;
                sinp[inp.id].trigger(e);
                closeAllLists();
            });
            a.appendChild(b);
          }
        }
    });
    inp.addEventListener("keydown", function(e) {
        let x = document.getElementById(this.id + "autocomplete-list" + inp.id);
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {

          currentFocus++;

          addActive(x);
        } else if (e.keyCode == 38) { 
          currentFocus--;

          addActive(x);
        } else if (e.keyCode == 13) {

          e.preventDefault();
          if (currentFocus > -1) {

            if (x) x[currentFocus].click();
          }
        }
    });
    function addActive(x) {

      if (!x) return false;

      removeActive(x);
      if (currentFocus >= x.length) currentFocus = 0;
      if (currentFocus < 0) currentFocus = (x.length - 1);

      x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {

      for (let i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
      }
    }
    function closeAllLists(elmnt) {
      let x = document.getElementsByClassName("autocomplete-items");
      for (let i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
          x[i].parentNode.removeChild(x[i]);
        }
      }
    }

    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
  }
  var ingredientsall = ["Leg Of Lamb","Parsley Root","Boba Tea","Brown Mustard Seed","Dill Seed","Tetilla Cheese","Tvp","Speckled Butter Beans","Cavolo Nero","Farfalle","Delicious Apple","Huitlacoche","Sea Salt","Pumpkin Seeds","Golden Apple","Root Beer","Lotus Roots","Monkfish","Ohba","Egg Noodles, Chinese","Mahimahi","Goat Milk","Firm Tofu","Tatsoi","Gentian Root","Sesame Oil","Golden Kiwi","American Cheese","Taleggio","Lavender","Pineapple Juice","Foie Gras","Gala Apple","Radiatore","Caltrop Starch","White Sesame Seeds","Duck Fat","Nocino","Soy Beans","Mako Shark","Crouton","Romaine Lettuce","Muenster Cheese","Hops","Nasturtium","Boston Butt Pork Roast","Licor 43","Royal Gala Apple","Jojoba","Kefir","Coconut Flour","Tarragon","Marigold","Black Vinegar","Stilton Cheese","Light Rye Flour","Walnuts","Heavy Cream","Brussels Sprouts","Beans","Black Mustard","Ice Cream","Swiss Chard","Mock Tender Steak","Chenin Blanc","Treviso","Dolphinfish","Chioggia Beet","Sour Cherry","Breadnut","Tawny Port","Pancetta","Bison","Canned Baked Beans","Blue Curacao","Bordeaux cherries","Summer Savory","Sushi","Tej","Kvass","Bacon Fat","Pork Butt","Guajillo Pepper","Red Wine","Five Spice","Bass","Pine Nut","Chunky Peanut Butter","Lima Bean","Jackfruit","Nougat","Lamb Rib","Brandy","Sauvignon Blanc","Pea Vines","Ravioli","Low-Fat Cheddar Or Colby Cheese","File Powder","Beaver","Walleye Pikerel","White Potato","Quahog Clam","Almonds","Orris Root","Ocean Whitefish","Chinese Leaves","Dried Buttermilk","Galia","Lobster","Cognac","Gelato","Arkansas Black Apple","Cassava Cake","Powdered Milk","Yeast","Raw Ham","Panko","Rice Vinegar","Pacific Prawns","Rotini","Porter","Kriek","Pipe","Tilapia","Calico Scallop","Dried Blueberries","Dulse","Pickled Plum","Blood Orange","Vinaigrette","Maca Powder","Rice","Wormwood","Nigella Seed","Squashes","Serrano Pepper","Bologna Sausage","Soybean Sprouts","Loganberry","Asparagus","Medium Sherry","Tortellini","Fresh Lychee","Clementine","Sea Bream","Almond Paste","White Soy Sauce","Chicken Thigh","Ghee","Cashews","Cointreau","Bock","Corn","lump crab meat","Sour Cream","Ground Beef","Tomatillo","Jarlsberg Cheese","Instant Coffee Powder","Mixed Spice","Raw Cashew Nuts","Edam Cheese","Chorizo","Anaheim Chili","Green Lentils","Gai Lon","Ackee","Raspberry","Seville Sour Orange","Alum Powder","Squab","Berbere","Oregano","Capon","Heavy Whipping Cream","Lemons","Chicory","Quandong","Dried Cherries","Blue Marlin","Emmer Wheat","Fried Beef Liver","Peanut Flour","Ciabatta","Syrah","Hake","Scamorza","Szechuan Buttons","Orange Juice","Rock Candy","Arborio Rice","Guajillo Chili","Cabernet Sauvignon","Tomato","Tea","Cotija","Cardamom Seed","Butterfish","Lobster Mushroom","Sweet Almond","Capers","Palm Sugar","Fenugreek","Chard","Yellow Mustard Seed","Chicaoji Chipotle Chili Sauce","Foie De Mer","Black Cherry","Candied Ginger","Apricot","Gunpowder Tea","Roasted Peanuts in shell","Venison","Cranberry","Swamp Cabbage","Anasazi Bean","Yukon Gold Potato","Brown Lentils","Haddock","Chestnut Flour","Little Gem Lettuce","Moose Meat","Peppadew","Chokeberry","Ground Ginger","Cuttlefish","Light Coconut Milk","Chicken Wings","Round Steak","Mango Juice","Onion","Salt Pork","Portobello Mushrooms","Gum Arabic","Amaretti","Yuzu","Spicebush Tea","Cottonseed Oil","Coolea Cheese","Chanterelle Mushrooms","Saint-Andre Cheese","Preserved Lemons","Cassavas","Worcestershire Sauce","Caramel","Colby Cheese","Mussel","Dried Apples","Kefalotyri Cheese","Maldon Sea Salt","Grenache","Anise","Cassia","Soft Goat Cheese","White Truffle","Turmeric","Chilean Sea Bass","Wensleydale Cheese","Dried Coconut","Rye Flour","Brewed Coffee","Bratwurst","Thai Chili Pepper","Cranberry Bean","Onion Flowers","Illawarra Plum","Chocolate Chips","Champagne","Aloe Vera","Chocolate Syrup","Veal Tongue","Snapper","Ruby Port Wine","Amaretto","Instant Dashi","Kamut","Grated Parmesan Cheese","Veal Shoulder","Port De Salut Cheese","Baking Powder","Organic Milk","Caraway whole","Dry Roasted Pecan","Scallop","Barolo","Duck Egg","Dried Porcini Mushrooms","Mesclun","Pale Ale","Brazil Nut","Spring Onion","Watermelon","Aleppo Pepper","Bonito Flakes","Langostino","Mutton","Brillat-Savarin","Ground Elk","Barley Flour","Orange Roughy","Loquat","Eel","Crab Apple","Pineapple","Hubbard Squash","Edible Pod Peas","Sarsaparilla","White Long-Grain Rice","Pinot Grigio","Japanese Rice","Coriander Seed","Mulukhia","Agnolotti","Granita","Frisée  Lettuce","Sweet Potato","Fruit Lambic","Lancashire Cheese","Jamón Serrano","Vanilla Bean","Winter Nelis Pear","Bottarga","Fontina Cheese","Rice Wine","Cardaba Banana","Bread","Fennel Seeds","Squid","Borage","Chicken Giblets","Zucchini","Split Peas","Rock Salt","Orange Peel","Mochi","Vegetables","Potato Starch","Moringa Oleifera","Apple Cider","Cheddar Cheese","Maida","Chili Flakes","Chinook Salmon","Unsweetened Cocoa Powder","Passion Fruit","Irish Whiskey","Tempeh","Papad","Double Cream","Summer Squash","Non-Fat Dry Milk","Butterscotch Chips","Ponzu","Sugar Snap Pea","Sunfish","Dry Roasted Almond","Halibut Cheeks","Orange Tomatoes","Fennel","Turkish Figs","Lemon Myrtle","Conger Eel","gochujang","Lager","Duck Meat","Maraschino Cherries","Matcha","Pomegranate Juice","Octopus","Gewurztraminer","Table Salt","Conchigliette Pasta","Splenda","Nutmeg","Lemon Verbena","Grappa","Sherry","Menta","Ground Turkey","Cupcake","Idiazabal Cheese","Pretzel","Caciotta","Hyssop","Achiote","Havarti","Small White Beans","Reduced Fat Sour Cream","Bulk Sausage","Pickled Herring","Curry","Sage Tea","Nile Perch","Rice Milk","Lucuma Powder","Florentine","Tur dal","Butterbean","Sun Dried Tomatoes","Five-Spice Powder","Alginate","Corned Beef Ribs","Vegetable Shortening","Cream Soda","Grapefruit","Soju","Coffee Beans","Kiwi Fruit","Marsala Wine","Apple Juice","Muskrat","Sheet Gelatin","Mulberry","Emu","Oloroso Sherry","Danish Blue Cheese","Sesame Paste","Cashew Butter","Vermouth","Dried Currant","Cedar Plank","Russet Potato","Black Azuki Bean","Pluot","Caviar","Parsley Leaf","Pork Kidneys","Robiola","Peppermint Leaves","Pork Ribs","Chironji","Grapefruit Juice","Imitation Crab","Crookneck Squash","Cacao","Lamb Kidneys","Rotisserie chicken","Pomelo","Wine","Flax","Culantro","Teriyaki","Iron","Boneless Rump Roast","Garlic Chives","Corn Flour","Fingerling Potato","Panch Phoron","Sunflower Seeds","Peanuts","Pine Nuts","White Cardamom Pod","Pole Beans","Pomegranate","Albacore Tuna","Broccoli","Malagueta Pepper","Clover","Soft White Wheat","Sweetened Condensed Milk","Hard Goat Cheese","Kampyo","Aperol","Lemongrass","Cocoa Powder","Perch","Yellowtail","Winter Melon","Kombu","Caribou","Wheat","Homogenized Milk","Chinese Long Bean","Bisquick","Scotch Bonnet Chillies","Safflower Oil","Jamaican Blue Mountain Coffee","Beef Suet","Kecap Manis","Grenadine Syrup","Sirloin Steak","Hyacinth Bean","Pork Sirloin Roast","Macadamia","Lingonberry","Light Tuna Canned In Water","Sweet Sherry","Lily Bulb","Ground Venison","Red Currant","Branzino","Mineral Water","Sturgeon","Dessert Wine","Polygonum","Yogurt","Pork Chop","Green Tomato","Danbo Cheese","Beef Top Round","Sweet Red Peppers","Finger Lime","Jambu","Pork Belly","Turkey Breast","Pecorino Romano","Portabella Mushrooms","Tandoori Masala","Mutton -Lamb","Blue Solaize Leeks","Broad Beans","Cultured Buttermilk","Coconut Oil","Part Skim Milk Ricotta Cheese","Flavorings, Extracts And Liqueurs","Star Anise","Wax Bean","Grana","Pitmaston Pineapple Apple","Bosc Pear","Grape Tomato","Egg White","Greek Oregano","Mastic","Lemon Aspen","Red Bean","Rack Of Lamb","Ajwain","Gelatin","Pisco","Chickpeas","Kashmiri Mirch","Mint","Prawn","Chili Bean","Salad Cream","Tellicherry","Shirataki Noodles","Gooseberries","Beef Shank","Low-Fat Vanilla Yogurt","Kimchi","Chifferi","Soybeans","Trout","White Wine Vinegar","Tamarind","Green Onion","Citron","Gourd","Black Sesame Seeds","Flageolet","Chopped Nuts","London Broil","Frisee","Farro","Beef","Aprium","Water","Irish Moss","American Pale Ale","Arrowhead","Amaranth Flour","Kumquat","Naruto","Whiskey","Cup Cheese","Valencia Orange","Green Pepper","Potatoes","Green Cauliflower","Jonagold Apple","Kumara","Cream","Angostura Bitters","Fondant","Caster Sugar","Shiso Leaves","Kent","Spelt","Royal Red Kidney Beans","Coconut","Poblano","Lamb","Blue Mussel","Cherry Heering","Madeira","Spanish Peanuts","Rainbow Trout","Ouzo","Provolone Cheese","Machaca","Spanish","Granules Garlic","Filet Mignon","Marcona Almond","Quail Egg","Maytag Blue","Unsalted Butter","Jalapeño Pepper","Chocolate Milk","Hungarian Paprika","Ocean Perch","Russian Dressing","Bresaola","Nori","Gobo","Tomme","Punt E Mes","Pink Bean","Granulated Sugar","Muffin","Achar","Alaska King Crab","Mung Beans","Nutmeg Powder","Wild Rainbow Trout","Burdock Root","Glutamic Acid Amino Acid","Red Delicious Apple","White Pepper","Ground Coriander","Acacia","Daikon Radish","Meyer Lemon","Stem Ginger","Saltpeter","Lettuce","Corn Flakes","Loin","Imperial Stout","Nicoise Olives","White Wheat Bread Flour","Custard Apple","Lamb Chops","Durian","Frozen Green Peas","Tripe","Red Pepper","Cannellini Bean","Dolcelatte","Pennette","Prosecco","Monterey Jack Cheese","Kefalograviera Cheese","Spanish Onion","Anchovy","Cream Of Tartar","Gram Flour","Dried Pumpkin Seed","Char magaz","Rose Buds","Buckwheat","Marshmallow","White Yam","Frozen Yogurt","Dwarf Choy Sum","Tortilla","Whole Grain Corn Flour","Artichokes","Baked Ham","Champagne Vinegar","Wild Boar","Grape Seed Oil","Cranberry Juice","Parmesan Cheese","Caraway Seeds","Alfalfa Sprouts","Vegetable Oil","Vermicelli","Sercial Madeira","Pequin Pepper","Whiting","Boysenberry","Rosemary","Pork","Creamed Coconut","Tabasco Pepper","Cabbage","Spices","Pedro Ximenez","Brown Sugar","Knackebrod","Caustic Soda","Flank Steak","Bitter Gourd","Chinese Five-Spice","Curry Powder","Avocado Oil","Gjetost Cheese","Peanut Butter","Blue Cheese","Sorghum","Striped Bass","Raw Papaya","Dried Plum","Beef Round","Pecorino","Pheasant","Hawaiian Sea Salt","Walnut","Beet","Pils","White Wine","Veal Breast","Pork Loin Roast","Smetana","Cavatappi","Pecorino Sardo","Palm Oil","Hot Sauce","Sago","Broccoli Raab","Lima Beans","Verjus","Saigon Cinnamon","Benedictine","Spearmint","English Breakfast Tea","Pink Eye Potato","Annato","Mcintosh Apple","Channa dall","Wakame","Cherimoya","Dashi","Sockeye Salmon","Cottage Cheese","Shichimi Togarashi","Thousand Island Dressing","Mixed Nuts","Hazel","Roma Tomatoes","Honeysuckle","Port Wine","Salsify","Gouda Cheese","Currant","Dandelion","Low-Fat Cottage Cheese","Beer","Orange Soda","Ginger Root","Haggis","Lillet","Sour or Clabbered Milk","Kidney Beans","White Onions","Black Cumin","Watercress","Poppy","Ground Pork","Alubia Criollo Beans","Sweet Vermouth","Peach","Cod","Pita Bread","Dungeness Crab","Arugula","green weed","wallnut","Escarole","Rice Noodles","Vanilla Beans","Soft Tofu","Red Cabbage","Hijiki","Oolong Tea","Ginseng","Puffed Rice","Yellow Perch","Camembert Cheese","Champagne Grapes","Soy Protein","Saba Banana","Peanut Oil","Wonderful Pomegranate","San Marzano Tomatoes","Star Fruit","Nameko Mushroom","Veal Rib","Black Rice","Heirloom Tomato","Radishes","Arrowroot","Dill Weed","Vodka","Amchoor","Long-Grain Brown Rice","Charlotte","Black Beans","Hemp Seeds","English Walnut","Cherry Tomatoes","Flax Seed","Pork Shoulder","Hazelnut Oil","Chili Pepper","Raclette","Pinot Noir","Epazote","Turbinado Sugar","Riesling Wine","Jasmine Tea","Farina","Huckleberry","Razor Clams","Spreadable Cheese","Cinnamon Stick","Saffron","Somen Noodles","Rigatoncini","Nutritional Yeast","Sweet Marsala","Savoy Cabbage","Hp Sauce","Granola","Egg Yolk","Pink Peppercorns","Snow Crab","Sambuca","Sausage","Kiwifruit","Baking Soda","Mountain Yam","Gentian","Peppercorns","Gold Rum","Brie Cheese","Rosewater","Haricot Vert","Dende Oil","Buckwheat Flour","Cusk","Coco Bean","Umeboshi Paste","Scallop Squash","Thai Chili","Moonshine","Rice Flour","Steamer Clam","Evaporated Milk","Wheat Germ","Lemon Basil","Penne Rigate","Persimmon","Lotus Seeds","Mangalitsa","Orange Pekoe Tea","Black Cardamom","Roquefort","Candlenut","Acorn","Fresh Soya","Cream Sherry","Sultana","Carpano Antica Vermouth","Laver Seaweed","Coulis","Tagliatelle","Bay Leaf","Ube Yams","Masa","Double Gloucester Cheese","Rhubarb","Dried Papaya","Tip Roast","Tapioca Pearl","Passion-Fruit Juice","Shrimp","Espelette","Tabasco Sauce","Cachaca","Raw Milk","Lardons","Guajillo","Romano Cheese","Teff Flour","Semolina","Spaghetti Alla Chitarra","Whole Wheat Flour","Collard Greens","Chaumes Cheese","Bitter Melon","Kangaroo","Salad","Quick Bread","Olive Oil","Pipramol","Coconut Milk","Beef Tongue or ox tongue","White Mustard","Vacherin Fribourgeois Cheese","Hot Dog","Sichuan Pepper","Quassia","Canned Mackerel","Pork Jowl","Gorgonzola","Lemon Grass","Acorn Squash","Candy Roaster Squash","Dark Corn Syrup","Fennel Pollen","Agave","Broccoflower","Frozen Peas","Collar","Anchovy Paste","Nopales","Red Kidney Beans","Sesame","Manicotti","Flat Iron Steak","Dark Rum","Whitefish","Semisweet Chocolate","Sugar Pumpkin","Stevia Powder","Chia","St-Germain Liqueur","Bourbon","Chartreuse Liqueur","Goose Liver","Mesquite Wood","kalaunji","Dried Ginger","Black Valentine Green Bean","Wild Leek","Ham Shank","Granny Smith Apple","Short Ribs","Bakers' Ammonia","Shallots","Lecithin Granules","Yellow Tomatoes","Mozzarella Cheese","Short Grain White Rice","Lamb Loin","Country Ham","Orecchiette","Methidana","Cavatelli","Canola Oil","Bee Pollen","Arak","Marzipan","Ancho Chile Pepper","Habanero Chili","Salami","Sucanat","Soy Yogurt","Butter Nut","Salish Smoked Salt","Single Cream","Juniper Berries","Dublin Bay Prawn","Napa Cabbage","Bushfood","Milk Stout","Cornbread","Poppy Seed","Sencha","Mission Fig","Israeli Couscous","Scotch Ale","Buttermilk","Sake","Great Northern Beans","Anelli","Cinnamon","Aniseed Myrtle","Ginkgo","Bamboo Shoots","Self-Rising Corn Meal","Black Bean","Ground Chuck","Flying Fish","Cactus Pear","Cookies","Breadfruit","Sweet Granadilla","Turnip Greens","Dried Cranberry","Fuji Apple","Groundnut","Jujube","Prosciutto","Green Food Coloring","Konnyaku","Yellow Beans","Roselle","Anisette","Maple Syrup","Spiced Rum","Green Cardamom Pod","Horseradish","Kasuri Methi","Fiori","Mocha Coffee","Labneh","Lilikoi","Butter","Hapu'upu'u","Pertsovka","Elderflower","Caul Fat","Cilantro","Avocado","Tahini","Gefilte Fish","Pineapple Mint","Salt Cod","Bluefish","Mustard Seed","Cocoa Beans","Arame","Green Beans","Whole Milk Ricotta Cheese","Soba Noodles","Za'atar","Canadian Bacon","Piloncillo","Brown Mushrooms","Non-Fat Milk","Whole Grain Wheat Flour","Pacific Rockfish","Sesame Seed","Applejack","Skirt Steak","Pickling Spice","Fish Sauce","Chinese Radish","Daikon","Pecan","Leek","Enoki Mushrooms","Beef Eye Round","Spinach","Carob","Thyme","Vegetable Juice Cocktail","Copper","Sweet Orange","Lamb Shoulder","Liquorice","Charnushka","Poultry Seasoning","Chicken Neck","Elk","Plaice","Sea Scallop","Basturma","Asafoetida","Shredded Parmesan Cheese","Penne","Pure Grain Alcohol","Coriander seed whole","Yellow Cornmeal","Dried Peaches","Fresh Corn","Chrysanthemum","Spirulina","White Seasme Seed","Khoya","Mahleb","Liquid Pectin","Gruyere Cheese","Corn Syrup","Teff","Sea Urchin Roe","Pickling Cucumbers","Celery Seeds","Grana Padano","Bonito","Ricotta Salata","Mirepoix","Reserve Port","Stevia","Ostrich","King Bolete","White Port","Dried Bananas","Schnapps","Panela","Tamari","Pink Lady   Apple","Kreplach","Red Snapper","White Vinegar","Fava Beans","Straw Mushroom","Patty Pans","Guava","Kobe Beef","Sichuan Peppercorns","Mustard Oil","Corn Starch","Ground Veal","Provolone","Wild Rice","elbow macaroni","Atta Flour","Reblochon Cheese","Chicken Fat","Red Raspberry Leaf","Pear","Candle Nut","Garlic","Zinfandel","Oxtail","Bulgar","Whisky","Chia Seeds","Ada","Sticky Rice","Turkey","Garlic Scapes","Kailan","Sweetbreads","Bacon Grease","Masoor Dal","Umeboshi","Dry Beans","Basket Cheese","Ajmud","Chestnut","Vinegar","Skim Milk","Mustard","Medium-Grain White Rice","New Potato","Ginger Ale","Pork Loin","Spaghetti Squash","Pacific Cod","Aguardiente","Beef Tri-Tip","Cavendish Banana","Fennel Tea","Chlorella","Mackerel","Vietnamese Mint","Goose Fat","Gala Apples","Whipping Cream","Jicama","Anejo Rum","Phyllo Dough","Veal Loin","Basmati Rice","Oat Milk","Pollock","Water Spinach","Wood Ear","Fleur De Sel","Prune","Yellow Bell Peppers","Persian Cucumber","Fluke","Bean Sprouts","Quince","Oats","Peppermint","Ti Leaves","Apple Wood","Watermelon Radish","Pastis","Sausage Casings","Evaporated Cane Juice","Matcha Green Tea","Crabapple","French Green Lentils","Elicoidali","Cheese Analogue","Creme De Cassis","Morels","Vanilla Bean Bruleê","Crystallized Ginger","Atlantic Salmon","Viili","Ice","Meringue","Papaya Nectar","Herring","Spiny Lobster","Lime","Red Drum","Fromage Frais","Wolfberry","Yuzu Paste","Milk, Dry (Whole)","Ground Bison","Salted Butter","Sea Grape","Sirloin","Low-Fat Plain Yogurt","Almond Meal","Satsuma","Cubed Lamb","Cola","Ogonori","Mandu","Salt","Red Chili Pepper","Custard","Vegetable Broth","Balsamic Vinegar","Chrysanthemum Leaves","Beef Brisket","Crostini","Quail","Black Walnut","Fructose","Vanilla Extract","Blue Crab","Squash Blossoms","Agar Agar","Natto","Red Potato","Kabocha","Sea Bass","Braeburn Apple","Maitake Mushrooms","Endive","Eau-De-Vie","Aspartame","Cheese Curd","Almond Butter","Marmalade","Rooibos Tea","Peeli Mirchi","Lard","Orzo","Malabathrum","Part Skim Milk Mozzarella Cheese","Mediterranean Mussels","Sage Leaf","Beef Chuck Steak","Tequila","Key Lime","Brewed Tea","Pasilla","Pickled Walnuts","Boneless Pork Chop","Urad Dal","Fennel Bulb","Cactus","Tuiles","Langoustine","Sweet Potatoes","Sunflower Oil","Bottle Gourd","Banana Flowers","Strawberry","Kidney Bean","Queen Crab","All Blue Potato","Cinnamon Oil","Matsutake","Armagnac","Pandanus","Chicken Drumstick","Tarama","Sorrel","Broccoli Rabe","Yam","Soy Milk","Broiler Chicken","Claret","Willow","Veal Sirloin","Quark Cheese","Asiago","Spaghettini","Beef Porterhouse Steak","Egg Matzo","Chicken Leg","Reduced Fat Peanut Butter","Pawpaw","Pork Blood","Skate Wing","Violet","Black Pepper","Licorice","Coconut Water","Canned Straw Mushrooms","Winter Squash","Miso","Mushrooms","Pectin","Creme De Violette","Celery","Squirrel","Raspberries","California Bay Leaf","Clarified Butter","Olives","Applejack Brandy","Sweet Pepper","Long Pepper","Mangosteen","Beaufort Cheese","Unsweetened Baking Chocolate","Pie","Berry","Squid Ink","New Zealand Spinach","Sambuca Liqueur","Sablefish","Sage","Mandarin Orange","Chinese Chives","Beef Flank Steak","Emmentaler Cheese","Ale","Puffed Millet","Habanero Pepper","Turmeric powder (Arabic)","Prune Juice","Wheat Bran","Seitan","Rutabagas","Nettles","Mace","Indian Cayenne Pepper","Korean Radish","Bread Stuffing","Muscovado Sugar","Flax Seed Oil","Goose","Luffa","Gin","Rome Apple","Black Currant","Amber/Red Ale","Dark Rye Flour","Ikura","Winter Wheat","Triple Sec","Seasoned Breadcrumbs","Speck","Bear Meat","Dark Soy Sauce","Lamb Heart","Muscadine","Kinako","Organic Klamath Pearl Potatoes","Roquefort Cheese","Qasuri methi","Canned Pink Salmon","Peppers","Fontina","Chipotle Peppers","Wattleseed","Instant Coffee","Parsnip","Bran Flakes","Rattan jot","Turbot","Worchestershire Sauce","Bucatini","Bitter Almond","Mesquite Powder","Blueberry","Instant Long-Grain White Rice","Remoulade","Long-Grain White Rice","Top Sirloin","Chinese Rose Wine","Coffee Liqueur","Mung Bean Sprouts","Calamondin","Mousse","Pink Salmon","Cauliflower","Dekopon","Soy Flour","Absinthe","Bok Choy","Jasmine","Savory","Guanciale","Corn Oil","Black Mission Fig","Green Peas","Campari","Dried Figs","Kohlrabi","Kalamata Olive","Low Fat Swiss Cheese","Soymilk","Rock Cornish Hen","Red Grouper","Salmon","Rice Bran Oil","Fino Sherry","Egg","White Pea Bean","Tangerine Juice","Cantaloupe","Dried Apricots","Chicken Feet","Bread Crumbs","White Tequila","Pappardelle","Mako","Mustard Powder","Geoduck","Green Garlic","Hearts Of Palm","Seabeans","Vitamin D","Thai Basil","2% Milk","Mulberries","Fideos","Wasabi","Fat Free Cream Cheese","Onion Powder","Chives","Navy Beans","Figs","Vitamin C","Asian Pear","Herbes De Provence","Light Sour Cream","Monosodium Glutamate","Garcinia Indica","Rose","Oatmeal","Half And Half","Minced Lamb","Chinese Cabbage","Yautia","Pickling Cucumber","Eggplant","Clotted Cream","Veal","Zucchini Flower","Fettuccine","Lemon Sole","Fermented Bean Paste","Calendula","Baby Back Ribs","Cuvée (Wine)","Mirin","Tapioca","Cream Cheese","Ground Chicken","Black Peppercorns","Morel Mushroom","Lentils","Oyster Mushrooms","Mortadella","Aburage","Suji","Chayote","Almond Extract","Argan Oil","Beet Powder","Oaxaca Cheese","French Dressing","Beef Tenderloin","Tonic Water","Alligator","Black Raisin","Chloride","Cherry Tomato","Mostaccioli","Buttercup Squash","Celeriac","Hickory","Herbsaint","Chardonnay","Canned Clams","Mustard Cress","Pumpkin Seed Oil","Rib-Eye Steak","Maccheroni","Lingcod","Miracle Whip","Tofu","Ojri","Kosher Salt","Triticale","Filini","Queso Asadero","Sweet Chocolate","Lamb Neck","Black Olives","Shaoxing Wine","Lapsang Souchong","Fregula","Opo Squash","Orange","Unsweetened Dutch Process Cocoa","Meritage","Non-Fat Cottage Cheese","Raisin","Light Soy Sauce","Nectarine","Manchego","Carp","Merlot","Taro Leaves","Adzuki Beans","Cornflour","Cucumber","Marjoram","Capsicum","Rye Whisky","Beech Mushroom","Tilefish","Cocoa Nibs","Green Chilli / Bird's eye chilli","Ground Nutmeg","Calcium","Chocolate Mint","Turkey Heart","Yu Choy Sum","Lemon Balm","Grape","Aji Molido","Escargot","Root Vegetables","Beef Tripe","Winter Savory","Cider","Lamb Knuckle","White Beans","Clam","Japanese Cucumber","Matzo Farfel","Wheat Germ Oil","Honey Dijon","Broccoli Sprouts","Cinnamon Tea","Rose Water","Beef Heart","Pancakes","Chickpea Flour","Rock Shrimp","Dried Mango","Corn Salad","Pak Choi","Sand Plum","Farmer Cheese","Silkie Black Chicken","Bean Thread Noodles","Hominy","Pompano","Praline","Goji Berry","Quinoa","Elephant Garlic","White Wheat Flour","Tafia","Kelp","Barley","Anardana","Kmmel","Dried Longan","Tasso","Conch","Finger Millet","Smoked Paprika","Popcorn","Mafaldine","Poi","Hazelnut","Poha","Malanga","Bartlett Pear","Almond Milk","Cayenne Pepper","Spaghetti","Cellophane Noodles","Green Peppercorns","Butter Clam","Conchiglie","Tarts","Shimla mirch","Ziti","Coriander Powder","Macadamia Nuts","Kielbasa","Lamb Liver","Fume Blanc","Ground Cumin","Dried Strawberries","Chicory Greens","Shark","Toasted Sesame Seed","Nigella Seeds","Bournvita","Garam Masala","Tapas","Rosemary Leaf","Linguine","Graham Flour","Red Chilli Whole","Abalone","Arctic Char","Caesar Dressing","Japanese Knotweed","Cumin","Potato","Sangiovese","Food Coloring","Potato Starch Flour","Grape Leaves","Coriander whole","Allspice","Powdered Sugar","Dried Pineapple","Soba","Lillet Blanc","Pimento","Boneless Ham","Beef Rib","Coltsfoot","Pigeon Peas","Wheat Beer","Angelica","Sorbet","Glutinous Rice Flour","Thai Eggplant","Kirsch","Kaffir Lime","White Kidney Bean","Whoopie Pie","Corned Beef Brisket","Tuna","Empanada","Whole Wheat Matzo","Marrow Bean","Oatmeal Stout","Prune Puree","Malmsey Madeira","Xylitol","Tomino","Burgundy Wine","Pigs' Feet","Pretzel Salt","Autumn Olives","Vidalia Onion","Pattypan Squash","Pernod","Flounder","Club Soda","Matzo","Kataifi","Chile Pepper","Medjool Date","Chamomile","Unagi","Extra Virgin Olive Oil","Mezcal","Micro Greens","Liqueur","Ras El Hanout","Jerusalem Artichokes","Carrot","White Vermouth","Jaggery","Feta Cheese","Kirby Cucumber","Rum","Shiitake","Broadbeans","Mexican Oregano","Coffee","Salted Salmon","Tangerine","Black-Eyed Peas","Melon","Acey Mac Apple","Marrow","blue cornmeal","Tortiglioni","Semisoft Goat Cheese","Choy Sum","Green Bananas","Red Mullet","Pig Stomach","Cherry","Samba Rice","Tomato Paste","Sriracha Sauce","Oat Bran","Honeycomb Tripe","Ricotta","Citric Acid","Flaxseed","Wheat Flour","Soy","Corn, Sweet White","Cubeb","Golden Delicious Apple","Boiled Peanuts","Cocoa Butter Oil","Liquid Smoke","Cream Of Coconut","Coke","Parmigiano Reggiano","White Cornmeal","Brown Ale","Cardamom Green","Agave Syrup","Molasses","Sataw","Wood Violets","Sel Gris","Halibut","Mascarpone","Midori","Pumpkin Flowers","Parsley","Taro Root","Sumac","Orange Extract","Scotch Bonnet Pepper","Fowl","Yellowfin Tuna","Chive Blossoms","Yoghurt","Witloof Chicory","Arrowroot Powder","Pumpkin","Veal Kidney","Blanched Almonds","White Radish","Dried Beef","Tangerines","Turkey Live","Aspic","Galangal","Raw Tahini","Sweet Onion","Hazelnut Milk","Veal Shank","Preserved Tofu","karhi patta","Sassafras","Seasoned Rice Vinegar","Xanthan Gum","Cara Cara Oranges","Reblochon","Ginger","Safflower","Reposado Tequila","Active Dry Yeast","Butternut Squash","Mezze Penne","Turkey Gizzard","Paprika","Pearl Millet","Smelt","All-Purpose Flour","Comice Pear","Bacon","Sucker","Soft Red Winter Wheat","Chervil","Blackeyed Peas","Egg Substitutions","Lamb Shank","Baby Carrots","Pork Fat","Light Corn Syrup","Water Chestnut","Royal Cumin","Parboiled Rice","Chili Powder","Plantain","Sea Vegetable","Juniper Berry","Iberian Raw Cured Ham","Pepper Jack Cheese","Mooli","Dried Pears","Chicharrones","Psyllium","Cardamom Brown","Wild Coho Salmon","Popsicle","Choux Pastry","Tripel","Campanelle","Grated Carrot","Swordfish","Dandelion greens","Ham Steak","Whey","Light Beer","Tiffin","Fenugreek Leaf","Quark","Rue","Angel Hair Pasta","Yellow Plum","Camel","Brunello","Cereal","Top Round Steak","Gurr","Baby Corn","Rice Bran","Lime Juice","Jonathan Apple","Rotelle","Purple Sweet Potato","Golden Syrup","Mullet","Barramundi","Light Rum","Alfalfa","Puff Pastry","taco","Margarine","Baby Lima Bean","Snow Peas","Karela","Chicken Breast Tenders","Dates","Bouquet Garni","Sodium","Ice Wine","Broken Wheat","Pork Spareribs","Pork Liver","Shortening","Light Cream","Chutney","Wild Rabbit","Tobiko","Potassium","French Beans","White Chocolate","Ketchup","Arrowroot Flour","Papaya","Chowder","Iceberg Lettuce","Custard Powder","Gluten","Oyster Sauce","Manila","Romano","Apples","Snap Peas","Riberry","Hatch Chili Pepper","Chayote Squash (Choko)","Grains Of Paradise","Pork Fatback","Earl Grey Tea","Casarecce","Pork Tenderloin","Whole Milk","Cinnamon Apple","Kala Namak","Canned Crab Meat","Tepary Bean","Swiss Cheese","Black Raspberry","Soybean Oil","Chana Dal","Cranberry Juice Cocktail","Honey","Low Fat Cream Cheese","Red Leicester Cheese","Shad","Brut Champagne","Blackberry","White Corn","Whole Chicken","Brown Rice Flour","Thyme Blossoms","Bean Flour","Farmed Catfish","Halloumi Cheese","Navel Oranges","Maple Sugar","Green Tea Powder","Calamaretti","Pinto Beans","Neufchatel Cheese","Sojni Ki Phalli","Saltines","Red Leaf Lettuce","Yeast Cake","Okra","Bananas","Jus","Pilsner","Lemon Peel","Veal Liver","Black Cherries","Frog","Butterhead Lettuce","Buffalo Milk","Elderberry","Compote","Ridged Gourd","Almond Oil","Pistachio","Mountain Pepper","Tapioca Flour","Mock Cream","Onion Flake","Puy Lentils","Multigrain","Pepperoncini","Hoisin Sauce","Miso Paste","Radicchio","Hemp Milk","Roughy","Rye","Pecorino Siciliano","Amontillado Sherry","Demerara Sugar","Lemon Juice","Marlin","Kaffir Lime Leaves","Fior Di Latte","Wild Ginger","Renkon","Ramps","Cape Gooseberries","Beef T-Bone Steak","Basil","Couscous","Carnaroli","Amaranth Leaves","Holly","Lovage","Cress","Grand Marnier","Chicken Breast","Escabeche","Shredded Wheat","Horse Gram","Karhi leaves","Black Tea","Star Anise Seed","Manila Clams","Maize","Guar Gum","Wild Crayfish","Scotch Whiskey","Yacón","Beet Greens","pecan nuts","Ti","Apple Cider Vinegar","Non-Stick Cooking Spray","Purslane","Kale","Fusilli","Jasmine Rice","Sardine","Oat Flour","Fat Free Sour Cream","Milkfish","Brick Cheese","Gammon","Snow Pea Shoots","Raw Macadamia Nut","Black Mustard Seed","Bulgur","Flaxseed Oil","Malt Syrup","Sprouted Wheat","Fiddlehead Ferns","Spaghettoni","Calvados","Fondue","Shin","Galliano","Tiger Shrimp","Nutella","Mozzarella Di Bufala Campana","Cannelloni","Soy Sauce","Bocconcini","Red Banana","Mint Tea","Dill","Pearl Onion","Turnip","Condensed Milk","Yellow Corn","Pea Sprouts","Malai","Stout","Melba","Honeydew","English Cucumbers","Ice Milk","Radish","Walnut Oil","Grits","European John Dory","Chicken Liver","Rigatoni","Hartshorn","Banana Pepper","Hibiscus Flowers","Mango","1% Milk","Dried Jujube","Indian Gooseberry","Hemp Seed","Truffle","Mustard Greens","Lemon Thyme","Garlic Powder","Golden Beet"]
  autocomplete(document.getElementById("keyin"), ingredientsall);
  autocomplete(document.getElementById("keyinEx"), ingredientsall);


function addIngredient(input) {
    ing = cleaninput(input.value);
    console.log(event);
    if (event.key == "Enter") {
        $("#keyinautocomplete-listkeyin").attr("hidden", true);
        $("#toptop").fadeOut("fast",this.empty);
        if (validateInput(ing)) {
            if (!Ingredients.includes(ing)) {
                if (!IngredientsExclude.includes(ing)) {
                    console.log(buildIngredientBadge(ing, "success"));
                    console.log($("#IngredientList"));
                    Ingredients.push(ing);
                    $("#IngredientList").append(buildIngredientBadge(ing, "success"));
                    console.log(input);
                    //getRecipes();
                } else {
                    toast("<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\">" +
                        "<strong>" + ing + "</strong> is already included in your list of unwanted Ingredients!" +
                        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
                        "<span aria-hidden=\"true\">&times;</span>" +
                        "</button>" +
                        "</div>");
                };
            } else {
                toast("<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\">" +
                    "<strong>" + ing + "</strong> is already included in your list of wanted ingredients!" +
                    "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
                    "<span aria-hidden=\"true\">&times;</span>" +
                    "</button>" +
                    "</div>");
            }
            input.value = ''
        }else{
            toast("<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\">" +
            "This ingredient is not in our database!" +
            "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
            "<span aria-hidden=\"true\">&times;</span>" +
            "</button>" +
            "</div>");
        }

        // if (shiftpressed) {
        //     console.log(Ingredients);
        //     console.log("MAGIC QUERY");
        // }
    } else {
        if (event.key == "Shift") {
            shiftpressed = true;
        }
        console.log(event.key);
    }

};

function addIngredientExclude(input) {
    ing = cleaninput(input.value);
    if (event.key == "Enter") {
        $("#keyinExautocomplete-listkeyinEx").attr("hidden", true);
        $("#toptop").fadeOut("fast",this.empty);
        if (validateInput(ing)) {
            if (!IngredientsExclude.includes(ing)) {
                if (!Ingredients.includes(ing)) {
                    console.log(buildIngredientBadgeExclude(ing, "danger"));
                    console.log($("#IngredientList"));
                    IngredientsExclude.push(ing);
                    $("#IngredientList").append(buildIngredientBadgeExclude(ing, "danger"));
                    console.log(input);
                    //getRecipes();
                } else {
                    toast("<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\">" +
                        "<strong>" + ing + "</strong> is already included in your list of wanted Ingredients!" +
                        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
                        "<span aria-hidden=\"true\">&times;</span>" +
                        "</button>" +
                        "</div>");
                };
            } else {
                toast("<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\">" +
                    "<strong>" + ing + "</strong> is already included in your list of unwanted ingredients!" +
                    "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
                    "<span aria-hidden=\"true\">&times;</span>" +
                    "</button>" +
                    "</div>");
            }
            input.value = ''
        }else{
            toast("<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\">" +
            "This ingredient is not in our database!" +
            "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
            "<span aria-hidden=\"true\">&times;</span>" +
            "</button>" +
            "</div>");
        }
        // if (shiftpressed) {
        //     console.log(Ingredients);
        //     console.log("MAGIC QUERY");
        // }
    } else {
        if (event.key == "Shift") {
            shiftpressed = true;
        }
        console.log(event.key);
    }
};

function shiftUp() {
    shiftpressed = false;
}

function buildIngredientBadge(Ingredient, indicator) {
    console.log("<span class=\"badge badge-" + indicator + "\">" + Ingredient + "<span class=\"closebtn\" onclick=\"closeChip(this,\'" + Ingredient + "\')\">&times;</span></span>");
    return "<span class=\"badge badge-" + indicator + "\">" + Ingredient + "<span class=\"closebtn\" onclick=\"closeChip(this,\'" + Ingredient + "\')\">&times;</span></span>";
};
function buildIngredientBadgeExclude(Ingredient, indicator) {
    console.log("<span class=\"badge badge-" + indicator + "\">" + Ingredient + "<span class=\"closebtn\" onclick=\"closeChipExclude(this,\'" + Ingredient + "\')\">&times;</span></span>");
    return "<span class=\"badge badge-" + indicator + "\">" + Ingredient + "<span class=\"closebtn\" onclick=\"closeChipExclude(this,\'" + Ingredient + "\')\">&times;</span></span>";
};

function closeChip(chip, toDelete) {
    Ingredients.splice(Ingredients.indexOf(toDelete), 1);
    chip.parentElement.style.display = "none";
    //getRecipes();
};


function closeChipExclude(chip, toDelete) {
    IngredientsExclude.splice(IngredientsExclude.indexOf(toDelete), 1);
    chip.parentElement.style.display = "none";
    //getRecipes();
};

function validateInput(input) {
    return ingredientsall.includes(input);
};



function toast(toast) {
    $("#toptop").empty();
    $("#toptop").append(toast);
    $("#toptop").fadeIn("slow");
};

function getRecipes() {
    //if(3<0){
    if( (Ingredients !=undefined && Ingredients.length >0) || (IngredientsExclude !=undefined && IngredientsExclude.length >0)){
        reqData = {};
        $("#loading").attr("hidden",false);
        $("#RecipeTable tbody").empty();
        queryString = buildQuery();
        reqData['query'] = queryString;
        $.post(SPARQLURL,data=reqData,handleRecipes);
    }else{
        $("#RecipeTable tbody").empty();
        toast("<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\">" +
        "Please enter (<strong>un</strong>)<strong>wanted</strong> ingredient(s)." +
        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
        "<span aria-hidden=\"true\">&times;</span>" +
        "</button>" +
        "</div>");
    }
};


function getRecipes2() {
    //if(3<0){
    if( (Ingredients !=undefined && Ingredients.length >0) || (IngredientsExclude !=undefined && IngredientsExclude.length >0)){
        reqData = {};
        $("#loading").attr("hidden",false);
        $("#RecipeTable tbody").empty();
        queryString = buildQuery2();
        reqData['query'] = queryString;
        $.post(SPARQLURL,data=reqData,handleRecipes2);

    }else{
        $("#RecipeTable tbody").empty();
        toast("<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\">" +
        "Please enter (<strong>un</strong>)<strong>wanted</strong> ingredient(s)." +
        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
        "<span aria-hidden=\"true\">&times;</span>" +
        "</button>" +
        "</div>");
    }
};

function handleRecipes(recipeData, error) {
    console.log(error);
    console.log(recipeData);
    if (error == "success") {
        $("#loading").attr("hidden",true);
        $("#RecipeTable tbody").fadeIn("middle");
        console.log($("#RecipeTable"));
        recipeData.results.bindings.forEach(
            (elem) => 
            {
                let useCount = 0;
                missingCount = parseInt(elem.count.value)-Ingredients.length + '';
                ings = JSON.parse("[\""+elem.ings.value+"\"]");
                markedIngs="";
                ings.forEach((recipeIng)=>{
                    if(Ingredients.includes(recipeIng)){
                        useCount = useCount + 1 ;
                        recipeIng = "<b>"+recipeIng+"</b>";
                        markedIngs = recipeIng+"<br>" + markedIngs;
                        return;
                    }
                    markedIngs+= recipeIng+"<br>";
                })
                console.log(ings);
                $("#RecipeTable > tbody:last-child").append("<tr><td>"+elem.title.value+"</td><td>"+useCount+"</td><td>"+missingCount+"</td><td>"+markedIngs+"</td></tr>");
            }
        );
    };
};


function handleRecipes2(recipeData, error) {
    console.log(error);
    console.log(recipeData);
    $("#RecipeTable tbody").empty();
    if (error == "success") {
        $("#loading").attr("hidden",true);
        $("#RecipeTable tbody").fadeIn("middle");
        console.log($("#RecipeTable"));
        recipeData.results.bindings.forEach(
            (elem) => 
            {
                let useCount = 0;
                console.log(elem);
                missingCount = parseInt(elem.count.value);
                ings = JSON.parse("[\""+elem.ings.value+"\"]");
                markedIngs="";
                ings.forEach((recipeIng)=>{
                    if(Ingredients.includes(recipeIng)){
                        useCount = useCount + 1;
                        missingCount = missingCount - 1;
                        recipeIng = "<b>"+recipeIng+"</b>";
                        markedIngs = recipeIng+"<br>" + markedIngs;
                        return;
                    }
                    markedIngs+= recipeIng+"<br>";
                })
                console.log(ings);
                $("#RecipeTable > tbody:last-child").append("<tr><td>"+elem.title.value+"</td><td>"+useCount+"</td><td>"+missingCount+"</td><td>"+markedIngs+"</td></tr>");
            }
        );
        sortUsed();
    };
};
function sortUsed(){
    console.log(sortUsed);
    let table = document.getElementById("RecipeTable");
    switching = true;
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
      //start by saying: no switching is done:
      switching = false;
      rows = table.rows;
      /*Loop through all table rows (except the
      first, which contains table headers):*/
      for (i = 1; i < (rows.length - 1); i++) {
        //start by saying there should be no switching:
        shouldSwitch = false;
        /*Get the two elements you want to compare,
        one from current row and one from the next:*/
        x = rows[i].getElementsByTagName("TD")[1];
        console.log(x);
        y = rows[i + 1].getElementsByTagName("TD")[1];
        //check if the two rows should switch place:
        if (x.innerHTML < y.innerHTML) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
      if (shouldSwitch) {
        /*If a switch has been marked, make the switch
        and mark that a switch has been done:*/
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
      }
    }
}
function buildQuery() {
    result = "SELECT DISTINCT ?title (COUNT (DISTINCT ?ingredient) as ?count) (GROUP_CONCAT(DISTINCT ?ing; SEPARATOR=\"\\\",\\\"\")as ?ings)"
/*    for (let i = 0; i <= Ingredients.length - 1; i++) {
        element = Ingredients[i];
    };*/
    result = result +" WHERE { " +
        "?recipelink <http://purl.org/dc/terms/title> ?title."+
        "?recipelink <http://linkedrecipes.org/schema/ingredient> ?ingLink."+
        "?ingLink <http://www.w3.org/2000/01/rdf-schema#label> ?ing."+
        "?recipelink <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://linkedrecipes.org/schema/Recipe>.";
    if(Ingredients !=undefined && Ingredients.length >0){
        for (let i = 0; i <= Ingredients.length - 1; i++) {
            element = Ingredients[i];
            console.log("append " + element);
            result = result.concat("?recipelink <http://linkedrecipes.org/schema/ingredient> ?ingredientlink" + i + ".");
            result = result.concat("?ingredientlink"+i+" <http://www.w3.org/2000/01/rdf-schema#label> \"" + element + "\".");
        };
    }
    if(IngredientsExclude !=undefined && IngredientsExclude.length >0){
        result = result +"FILTER NOT EXISTS {   VALUES ?lable2 { ";
        for (let i = 0; i <= IngredientsExclude.length - 1; i++) {
            element = IngredientsExclude[i];
            console.log("append " + element);
            result = result.concat("\"" + element + "\" ");
        };
        result = result +" } ?recipelink <http://linkedrecipes.org/schema/ingredient> ?ingredientlink2. ?ingredientlink2 <http://www.w3.org/2000/01/rdf-schema#label> ?lable2. } ";
    }

    console.log(result = result.concat("?recipelink <http://linkedrecipes.org/schema/ingredient> ?ingredientlink. ?ingredientlink <http://www.w3.org/2000/01/rdf-schema#label> ?ingredient} GROUP BY ?recipelink ?title ORDER BY ASC(?count) LIMIT 300"));
    //console.log(result = result.concat("?recipelink <http://linkedrecipes.org/schema/ingredient> ?ingredientlink. ?ingredientlink <http://www.w3.org/2000/01/rdf-schema#label> ?ingredient} GROUP BY ?recipelink ?title ORDER BY DESC(?count)"));
    return result;
};

function cleaninput(input) {
    if (input.substring(input.length - 1) == ' ') {
        console.log("recursive: ")
        return cleaninput(input.substring(0, input.length - 1));
    }
    console.log("returned");
    return input;
}
function buildQuery2() {
    result = "SELECT DISTINCT ?title (COUNT (DISTINCT ?ing) as ?count) (GROUP_CONCAT(DISTINCT ?ing; SEPARATOR=\"\\\",\\\"\")as ?ings)"
/*    for (let i = 0; i <= Ingredients.length - 1; i++) {
        element = Ingredients[i];
    };*/
    let IngsQuoted = "\"" + Ingredients.join("\" \"") + "\"";
    console.log("FAGGOT");
    result = result +" WHERE { " +
        "VALUES ?ingredient {"+
        IngsQuoted+
        "}. "+
        "?recipelink <http://purl.org/dc/terms/title> ?title."+
        "?recipelink <http://linkedrecipes.org/schema/ingredient> ?ingLink."+
        "?ingLink <http://www.w3.org/2000/01/rdf-schema#label> ?ingredient."+
        "?recipelink <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://linkedrecipes.org/schema/Recipe>."+
        "?recipelink <http://linkedrecipes.org/schema/ingredient> ?ingredientLink."+
        "?ingredientLink <http://www.w3.org/2000/01/rdf-schema#label> ?ing.";
    if(IngredientsExclude !=undefined && IngredientsExclude.length >0){
        result = result +"FILTER NOT EXISTS {   VALUES ?lable2 { ";
        for (let i = 0; i <= IngredientsExclude.length - 1; i++) {
            element = IngredientsExclude[i];
            console.log("append " + element);
            result = result.concat("\"" + element + "\" ");
        };
        result = result +" } ?recipelink <http://linkedrecipes.org/schema/ingredient> ?ingredientlink2. ?ingredientlink2 <http://www.w3.org/2000/01/rdf-schema#label> ?lable2. } ";
    }

    console.log(result = result.concat("} GROUP BY ?recipelink ?title ORDER BY ASC(?count) LIMIT 300"));
    //console.log(result = result.concat("?recipelink <http://linkedrecipes.org/schema/ingredient> ?ingredientlink. ?ingredientlink <http://www.w3.org/2000/01/rdf-schema#label> ?ingredient} GROUP BY ?recipelink ?title ORDER BY DESC(?count)"));
    return result;
};