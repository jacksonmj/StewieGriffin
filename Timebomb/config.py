###
# Copyright (c) 2010, quantumlemur
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Timebomb', True)


Timebomb = conf.registerPlugin('Timebomb')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Timebomb, 'someConfigVariableName',
#     registry.Boolean(False, """Help for someConfigVariableName."""))
conf.registerGlobalValue(Timebomb, 'colors',
    registry.SpaceSeparatedListOfStrings(['AliceBlue', 'AntiqueWhite', 'Aqua',
        'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'BlanchedAlmond', 
        'Blue', 'BlueViolet', 'Brown', 'BurlyWood', 'CadetBlue', 'Chartreuse',
        'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan',
        'DarkBlue', 'DarkCyan', 'DarkGoldenRod', 'DarkGray', 'DarkGreen', 
        'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 
        'DarkOrchid', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSlateBlue',
        'DarkSlateGray', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 
        'DeepSkyBlue', 'DimGray', 'DodgerBlue', 'FireBrick', 'FloralWhite',
        'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 
        'GoldenRod', 'Gray', 'Green', 'GreenYellow', 'HoneyDew', 'HotPink', 
        'IndianRed', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'LavenderBlush',
        'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral', 'LightCyan',
        'LightGoldenRodYellow', 'LightGrey', 'LightGreen', 'LightPink', 
        'LightSalmon', 'LightSeaGreen', 'LightSkyBlue', 'LightSlateGray',
        'LightSteelBlue', 'LightYellow', 'Lime', 'LimeGreen', 'Linen', 
        'Magenta', 'Maroon', 'MediumAquaMarine', 'MediumBlue', 'MediumOrchid',
        'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 
        'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 
        'MidnightBlue', 'MintCream', 'MistyRose', 'Moccasin', 'NavajoWhite', 
        'Navy', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed', 
        'Orchid', 'PaleGoldenRod', 'PaleGreen', 'PaleTurquoise', 
        'PaleVioletRed', 'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 
        'PowderBlue', 'Purple', 'Red', 'RosyBrown', 'RoyalBlue', 
        'SaddleBrown', 'Salmon', 'SandyBrown', 'SeaGreen', 'SeaShell', 
        'Sienna', 'Silver', 'SkyBlue', 'SlateBlue', 'SlateGray', 'Snow', 
        'SpringGreen', 'SteelBlue', 'Tan', 'Teal', 'Thistle', 'Tomato', 
        'Turquoise', 'Violet', 'Wheat', 'White', 'WhiteSmoke', 'Yellow', 
        'YellowGreen'],
    """The set of possible timebomb wire colors"""))
# More from mniip: Aero, Aero blue, African violet, Air Force blue (RAF), Air Force blue (USAF), Air superiority blue, Alabama Crimson, Alice blue, Alizarin crimson, Alloy orange, Almond, Amaranth, Amazon, Amber, SAE/ECE Amber (color), American rose, Amethyst, Android Green, Anti-flash white, Antique brass, Antique bronze, Antique fuchsia, Antique ruby, Antique white, Ao (English), Apple green, Apricot, Aqua, Aquamarine, Army green, Arsenic, Arylide yellow, Ash grey, Asparagus, Atomic tangerine, Auburn, Aureolin, AuroMetalSaurus, Avocado, Azure, Azure mist/web, Baby blue, Baby blue eyes, Baby pink, Baby powder, Baker-Miller pink, Ball Blue, Banana Mania, Banana yellow, Barbie pink, Barn red, Battleship grey, Bazaar, B'dazzled blue, Beau blue, Beaver, Beige, Big dip o’ruby, Bisque, Bistre, Bistre brown, Bitter lemon, Bitter lime, Bittersweet, Bittersweet shimmer, Black, Black bean, Black leather jacket, Black olive, Blanched Almond, Blast-off bronze, Bleu de France, Blizzard Blue, Blond, Blue, Blue (Crayola), Blue (Munsell), Blue (NCS), Blue (pigment), Blue (RYB), Blue Bell, Blue-gray, Blue-green, Blue sapphire, Blue-violet, Blue yonder, Blueberry, Bluebonnet, Blush, Bole, Bondi blue, Bone, Boston University Red, Bottle green, Boysenberry, Brandeis blue, Brass, Brick red, Bright cerulean, Bright green, Bright lavender, Bright maroon, Bright navy blue, Bright pink, Bright turquoise, Bright ube, Brilliant lavender, Brilliant rose, Brink pink, British racing green, Bronze, Bronze Yellow, Brown (traditional), Brown (web), Brown-nose, Brunswick green, Bubble gum, Bubbles, Bud green, Buff, Bulgarian rose, Burgundy, Burlywood, Burnt orange, Burnt sienna, Burnt umber, Byzantine, Byzantium, Cadet, Cadet blue, Cadet grey, Cadmium green, Cadmium orange, Cadmium red, Cadmium yellow, Café au lait, Café noir, Cal Poly green, Cambridge Blue, Camel, Cameo pink, Camouflage green, Canary yellow, Candy apple red, Candy pink, Capri, Caput mortuum, Cardinal, Caribbean green, Carmine, Carmine (M&P), Carmine pink, Carmine red, Carnation pink, Carnelian, Carolina blue, Carrot orange, Castleton green, Catalina blue, Catawba, Cedar Chest, Ceil, Celadon, Celadon Blue, Celadon Green, Celeste (colour), Celestial blue, Cerise, Cerise pink, Cerulean, Cerulean blue, Cerulean frost, CG Blue, CG Red, Chamoisee, Champagne, Charcoal, Charleston green, Charm pink, Chartreuse (traditional), Chartreuse (web), Cherry, Cherry blossom pink, Chestnut, China pink, China rose, Chinese red, Chinese violet, Chocolate (traditional), Chocolate (web), Chrome yellow, Cinereous, Cinnabar, Cinnamon, Citrine, Citron, Claret, Classic rose, Cobalt, Cocoa brown, Coconut, Coffee, Columbia blue, Congo pink, Cool black, Cool grey, Copper, Copper (Crayola), Copper penny, Copper red, Copper rose, Coquelicot, Coral, Coral pink, Coral red, Cordovan, Corn, Cornell Red, Cornflower blue, Cornsilk, Cosmic latte, Cotton candy, Cream, Crimson, Crimson glory, Cyan, Cyan (process), Cyber Grape, Cyber yellow, Daffodil, Dandelion, Dark blue, Dark blue-gray, Dark brown, Dark byzantium, Dark candy apple red, Dark cerulean, Dark chestnut, Dark coral, Dark cyan, Dark electric blue, Dark goldenrod, Dark gray, Dark green, Dark imperial blue, Dark jungle green, Dark khaki, Dark lava, Dark lavender, Dark liver, Dark liver (horses), Dark magenta, Dark midnight blue, Dark moss green, Dark olive green, Dark orange, Dark orchid, Dark pastel blue, Dark pastel green, Dark pastel purple, Dark pastel red, Dark pink, Dark powder blue, Dark raspberry, Dark red, Dark salmon, Dark scarlet, Dark sea green, Dark sienna, Dark sky blue, Dark slate blue, Dark slate gray, Dark spring green, Dark tan, Dark tangerine, Dark taupe, Dark terra cotta, Dark turquoise, Dark vanilla, Dark violet, Dark yellow, Dartmouth green, Davy's grey, Debian red, Deep carmine, Deep carmine pink, Deep carrot orange, Deep cerise, Deep champagne, Deep chestnut, Deep coffee, Deep fuchsia, Deep jungle green, Deep lemon, Deep lilac, Deep magenta, Deep mauve, Deep moss green, Deep peach, Deep pink, Deep ruby, Deep saffron, Deep sky blue, Deep Space Sparkle, Deep Taupe, Deep Tuscan red, Deer, Denim, Desert, Desert sand, Diamond, Dim gray, Dirt, Dodger blue, Dogwood rose, Dollar bill, Donkey Brown, Drab, Duke blue, Dust storm, Earth yellow, Ebony, Ecru, Eggplant, Eggshell, Egyptian blue, Electric blue, Electric crimson, Electric cyan, Electric green, Electric indigo, Electric lavender, Electric lime, Electric purple, Electric ultramarine, Electric violet, Electric yellow, Emerald, English green, English lavender, English red, English violet, Eton blue, Eucalyptus, Fallow, Falu red, Fandango, Fandango pink, Fashion fuchsia, Fawn, Feldgrau, Feldspar, Fern green, Ferrari Red, Field drab, Firebrick, Fire engine red, Flame, Flamingo pink, Flattery, Flavescent, Flax, Flirt, Floral white, Fluorescent orange, Fluorescent pink, Fluorescent yellow, Folly, Forest green (traditional), Forest green (web), French beige, French bistre, French blue, French lilac, French lime, French mauve, French raspberry, French rose, French sky blue, French wine, Fresh Air, Fuchsia, Fuchsia (Crayola), Fuchsia pink, Fuchsia rose, Fulvous, Fuzzy Wuzzy, Gainsboro, Gamboge, Generic viridian, Ghost white, Giants orange, Ginger, Glaucous, Glitter, GO green, Gold (metallic), Gold (web) (Golden), Gold Fusion, Golden brown, Golden poppy, Golden yellow, Goldenrod, Granny Smith Apple, Grape, Gray, Gray (HTML/CSS gray), Gray (X11 gray), Gray-asparagus, Gray-blue, Green (color wheel) (X11 green), Green (Crayola), Green (HTML/CSS color), Green (Munsell), Green (NCS), Green (pigment), Green (RYB), Green-yellow, Grullo, Guppie green, Halayà úbe, Han blue, Han purple, Hansa yellow, Harlequin, Harvard crimson, Harvest Gold, Heart Gold, Heliotrope, Hollywood cerise, Honeydew, Honolulu blue, Hooker's green, Hot magenta, Hot pink, Hunter green, Iceberg, Icterine, Illuminating Emerald, Imperial, Imperial blue, Imperial purple, Imperial red, Inchworm, Independence, India green, Indian red, Indian yellow, Indigo, Indigo (dye), Indigo (web), International Klein Blue, International orange (aerospace), International orange (engineering), International orange (Golden Gate Bridge), Iris, Irresistible, Isabelline, Islamic green, Italian sky blue, Ivory, Jade, Japanese indigo, Japanese violet, Jasmine, Jasper, Jazzberry jam, Jelly Bean, Jet, Jonquil, June bud, Jungle green, Kelly green, Kenyan copper, Keppel, Khaki (HTML/CSS) (Khaki), Khaki (X11) (Light khaki), Kobe, Kobi, Kombu green, KU Crimson, La Salle Green, Languid lavender, Lapis lazuli, Laser Lemon, Laurel green, Lava, Lavender (floral), Lavender (web), Lavender blue, Lavender blush, Lavender gray, Lavender indigo, Lavender magenta, Lavender mist, Lavender pink, Lavender purple, Lavender rose, Lawn green, Lemon, Lemon chiffon, Lemon curry, Lemon glacier, Lemon lime, Lemon meringue, Lemon yellow, Liberty, Licorice, Light apricot, Light blue, Light brown, Light carmine pink, Light coral, Light cornflower blue, Light crimson, Light cyan, Light fuchsia pink, Light goldenrod yellow, Light gray, Light green, Light khaki, Light medium orchid, Light moss green, Light orchid, Light pastel purple, Light pink, Light red ochre, Light salmon, Light salmon pink, Light sea green, Light sky blue, Light slate gray, Light steel blue, Light taupe, Light Thulian pink, Light yellow, Lilac, Lime (color wheel), Lime (web) (X11 green), Lime green, Limerick, Lincoln green, Linen, Lion, Little boy blue, Liver, Liver (dogs), Liver (organ), Liver chestnut, Lumber, Lust, Magenta, Magenta (Crayola), Magenta (dye), Magenta (Pantone), Magenta (process), Magenta haze, Magic mint, Magnolia, Mahogany, Maize, Majorelle Blue, Malachite, Manatee, Mango Tango, Mantis, Mardi Gras, Maroon (Crayola), Maroon (HTML/CSS), Maroon (X11), Mauve, Mauve taupe, Mauvelous, Maya blue, Meat brown, Medium aquamarine, Medium blue, Medium candy apple red, Medium carmine, Medium champagne, Medium electric blue, Medium jungle green, Medium lavender magenta, Medium orchid, Medium Persian blue, Medium purple, Medium red-violet, Medium ruby, Medium sea green, Medium slate blue, Medium spring bud, Medium spring green, Medium sky blue, Medium taupe, Medium turquoise, Medium Tuscan red, Medium vermilion, Medium violet-red, Mellow apricot, Mellow yellow, Melon, Metallic Seaweed, Metallic Sunburst, Mexican pink, Midnight blue, Midnight green (eagle green), Midori, Mikado yellow, Mint, Mint cream, Mint green, Misty rose, Moccasin, Mode beige, Moonstone blue, Mordant red 19, Moss green, Mountain Meadow, Mountbatten pink, MSU Green, Mughal green, Mulberry, Mustard, Myrtle green, Nadeshiko pink, Napier green, Naples yellow, Navajo white, Navy blue, Navy purple, Neon Carrot, Neon fuchsia, Neon green, New Car, New York pink, Non-photo blue, North Texas Green, Nyanza, Ocean Boat Blue, Ochre, Office green, Old burgundy, Old gold, Old lace, Old lavender, Old mauve, Old moss green, Old rose, Old silver, Olive, Olive Drab (web) (Olive Drab #3), Olive Drab #7, Olivine, Onyx, Opera mauve, Orange (color wheel), Orange (Crayola), Orange (Pantone), Orange (RYB), Orange (web color), Orange peel, Orange-red, Orchid, Orchid pink, Orioles orange, Otter brown, Outer Space, Outrageous Orange, Oxford Blue, OU Crimson Red, Pakistan green, Palatinate blue, Palatinate purple, Pale aqua, Pale blue, Pale brown, Pale carmine, Pale cerulean, Pale chestnut, Pale copper, Pale cornflower blue, Pale gold, Pale goldenrod, Pale green, Pale lavender, Pale magenta, Pale pink, Pale plum, Pale red-violet, Pale robin egg blue, Pale silver, Pale spring bud, Pale taupe, Pale turquoise, Pale violet-red, Pansy purple, Paolo Veronese green, Papaya whip, Paris Green, Pastel blue, Pastel brown, Pastel gray, Pastel green, Pastel magenta, Pastel orange, Pastel pink, Pastel purple, Pastel red, Pastel violet, Pastel yellow, Patriarch, Payne's grey, Peach, Peach (Crayola), Peach-orange, Peach puff, Peach-yellow, Pear, Pearl, Pearl Aqua, Pearly purple, Peridot, Periwinkle, Persian blue, Persian green, Persian indigo, Persian orange, Persian pink, Persian plum, Persian red, Persian rose, Persimmon, Peru, Phlox, Phthalo blue, Phthalo green, Pictorial carmine, Piggy pink, Pine green, Pink, Pink lace, Pink lavender, Pink-orange, Pink pearl, Pink Sherbet, Pistachio, Platinum, Plum (traditional), Plum (web), Pomp and Power, Popstar, Portland Orange, Powder blue (web), Princeton orange, Prune, Prussian blue, Psychedelic purple, Puce, Pumpkin, Purple (HTML/CSS), Purple (Munsell), Purple (X11), Purple Heart, Purple mountain majesty, Purple navy, Purple pizzazz, Purple taupe, Purpureus, Quartz, Queen blue, Queen pink, Rackley, Radical Red, Rajah, Raspberry, Raspberry glace, Raspberry pink, Raspberry rose, Raw umber, Razzle dazzle rose, Razzmatazz, Razzmic Berry, Red, Red (Crayola), Red (Munsell), Red (NCS), Red (Pantone), Red (pigment), Red (RYB), Red-brown, Red devil, Red-orange, Red-violet, Redwood, Regalia, Resolution blue, Rhythm, Rich black, Rich brilliant lavender, Rich carmine, Rich electric blue, Rich lavender, Rich lilac, Rich maroon, Rifle green, Robin egg blue, Rocket metallic, Roman silver, Rose, Rose bonbon, Rose ebony, Rose gold, Rose madder, Rose pink, Rose quartz, Rose red, Rose taupe, Rose vale, Rosewood, Rosso corsa, Rosy brown, Royal azure, Royal blue (traditional), Royal blue (web), Royal fuchsia, Royal purple, Royal yellow, Ruber, Rubine red, Ruby, Ruby red, Ruddy, Ruddy brown, Ruddy pink, Rufous, Russet, Russian green, Russian violet, Rust, Rusty red, Sacramento State green, Saddle brown, Safety orange (blaze orange), Safety yellow, Saffron, St. Patrick's blue, Salmon, Salmon pink, Sand, Sand dune, Sandstorm, Sandy brown, Sandy taupe, Sangria, Sap green, Sapphire, Sapphire blue, Satin sheen gold, Scarlet, Scarlet (Crayola), Schauss pink, School bus yellow, Screamin' Green, Sea blue, Sea green, Seal brown, Seashell, Selective yellow, Sepia, Shadow, Shampoo, Shamrock green, Sheen Green, Shimmering Blush, Shocking pink, Shocking pink (Crayola), Sienna, Silver, Silver chalice, Silver Lake blue, Silver pink, Silver sand, Sinopia, Skobeloff, Sky blue, Sky magenta, Slate blue, Slate gray, Smalt (Dark powder blue), Smitten, Smoke, Smokey topaz, Smoky black, Snow, Soap, Sonic silver, Space cadet, Spanish bistre, Spanish carmine, Spanish crimson, Spanish blue, Spanish gray, Spanish orange, Spanish sky blue, Spanish viridian, Spiro Disco Ball, Spring bud, Spring green, Star command blue, Steel blue, Steel pink, Stil de grain yellow, Stizza, Stormcloud, Straw, Strawberry, Sunglow, Sunray, Sunset, Sunset orange, Super pink, Tan, Tangelo, Tangerine, Tangerine yellow, Tango pink, Taupe, Taupe gray, Tea green, Tea rose (orange), Tea rose (rose), Teal, Teal blue, Teal deer, Teal green, Telemagenta, Tenné (Tawny), Terra cotta, Thistle, Thulian pink, Tickle Me Pink, Tiffany Blue, Tiger's eye, Timberwolf, Titanium yellow, Tomato, Toolbox, Topaz, Tractor red, Trolley Grey, Tropical rain forest, True Blue, Tufts Blue, Tulip, Tumbleweed, Turkish rose, Turquoise, Turquoise blue, Turquoise green, Tuscan, Tuscan brown, Tuscan red, Tuscan tan, Tuscany, Twilight lavender, Tyrian purple, UA blue, UA red, Ube, UCLA Blue, UCLA Gold, UFO Green, Ultramarine, Ultramarine blue, Ultra pink, Umber, Unbleached silk, United Nations blue, University of California Gold, Unmellow yellow, UP Forest green, UP Maroon, Upsdell red, Urobilin, USAFA blue, USC Cardinal, USC Gold, University of Tennessee Orange, Utah Crimson, Vanilla, Vanilla ice, Vegas gold, Venetian red, Verdigris, Vermilion (cinnabar), Vermilion (Plochere), Veronica, Violet, Violet (color wheel), Violet (RYB), Violet (web), Violet-blue, Violet-red, Viridian, Viridian green, Vivid auburn, Vivid burgundy, Vivid cerise, Vivid orchid, Vivid sky blue, Vivid tangerine, Vivid violet, Warm black, Waterspout, Wenge, Wheat, White, White smoke, Wild blue yonder, Wild orchid, Wild Strawberry, Wild Watermelon, Windsor tan, Wine, Wine dregs, Wisteria, Wood brown, Xanadu, Yale Blue, Yankees blue, Yellow, Yellow (Crayola), Yellow (Munsell), Yellow (NCS), Yellow (Pantone), Yellow (process), Yellow (RYB), Yellow-green, Yellow Orange, Yellow rose, Zaffre, Zinnwaldite brown, Zomp, 

    
conf.registerGlobalValue(Timebomb, 'shortcolors',
        registry.SpaceSeparatedListOfStrings(['red', 'orange', 'yellow', 
            'green', 'blue', 'purple', 'pink', 'black', 'brown', 'gray', 
            'white'],
        """The set of possible timebomb wire colors when there are few
                wires"""))

conf.registerChannelValue(Timebomb, 'randomExclusions',
        registry.SpaceSeparatedListOfStrings([], 
        """A list of nicks who should be excluded from being 
            randombombed"""))
            
conf.registerChannelValue(Timebomb, 'exclusions',
        registry.SpaceSeparatedListOfStrings([], 
        """A list of nicks who should be completely excluded from being 
            bombed"""))

conf.registerChannelValue(Timebomb, 'allowBombs', 
        registry.Boolean(False, """Determines whether timebombs are allowed 
            in the channel."""))

conf.registerChannelValue(Timebomb, 'bombHistory',
        registry.SpaceSeparatedListOfStrings([], 
        """Timestamps, senders and victims for previous bombs in the channel"""))

conf.registerChannelValue(Timebomb, 'rateLimitTime',
        registry.Integer(1800, """Time in seconds for which previous bombs are remembered and count towards the rate limit"""))

conf.registerChannelValue(Timebomb, 'rateLimitSender', 
        registry.Float(5.0, """Mean bombs/hour allowed in the past rateLimitTime from each host"""))

conf.registerChannelValue(Timebomb, 'rateLimitVictim', 
        registry.Float(3.0, """Mean bombs/hour allowed in the past rateLimitTime targeting a particular nick"""))

conf.registerChannelValue(Timebomb, 'rateLimitTotal', 
        registry.Float(9.0, """Total mean bombs/hour allowed in the past rateLimitTime"""))

conf.registerChannelValue(Timebomb, 'minWires',
        registry.PositiveInteger(2, """Determines the minimum number of wires 
            a timebomb will have."""))

conf.registerChannelValue(Timebomb, 'maxWires',
        registry.PositiveInteger(4, """Determines the maximum number of wires 
            a timebomb will have."""))

conf.registerChannelValue(Timebomb, 'minTime',
        registry.PositiveInteger(45, """Determines the minimum time of a 
            timebomb timer, in seconds."""))

conf.registerChannelValue(Timebomb, 'maxTime',
        registry.PositiveInteger(70, """Determines the maximum time of a 
            timebomb timer, in seconds."""))

conf.registerChannelValue(Timebomb, 'minRandombombTime',
        registry.PositiveInteger(60, """Determines the minimum time of a 
            randombomb timer, which should in general be greater than the 
            minimum targeted bomb time, to allow someone who's not paying 
            attention to respond."""))

conf.registerChannelValue(Timebomb, 'maxRandombombTime',
        registry.PositiveInteger(120, """Determines the maximum time of a 
            randombomb timer, which should in general be greater than the 
            maxiumum targeted bomb time, to allow someone who's not paying 
            attention to respond."""))

conf.registerChannelValue(Timebomb, 'showArt',
        registry.Boolean(False, """Determines whether an ASCII art bomb should 
            be shown on detonation, or a simple message."""))

conf.registerChannelValue(Timebomb, 'bombActiveUsers',
        registry.Boolean(True, """Determines whether only active users 
            should be randombombed"""))

conf.registerChannelValue(Timebomb, 'joinIsActivity',
        registry.Boolean(False, """Determines whether channel joins should 
            count as activity for randombombs"""))

conf.registerChannelValue(Timebomb, 'allowSelfBombs',
        registry.Boolean(False, """Allow the bot to bomb itself?"""))

conf.registerChannelValue(Timebomb, 'idleTime',
        registry.PositiveInteger(30, """The number of minutes before someone 
            is counted as idle for randombombs, if idle-checking is 
            enabled."""))

conf.registerChannelValue(Timebomb, 'showCorrectWire',
        registry.Boolean(False, """Determines whether the correct wire will be
            shown when a bomb detonates."""))

conf.registerGlobalValue(Timebomb, 'debug',
        registry.Boolean(False, """Determines whether debugging info will be
            shown."""))

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
