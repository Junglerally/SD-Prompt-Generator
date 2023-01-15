import random as rn

prompts = {

    "adjectives": {

        "visadjcts": ['pretty', 'relaxing', 'calm', 'quiet', 'wonderful', 'nice', 'incredible', 'amazing', 'cozy', 'beautiful', 'ominous', 'gloomy', 'post-apocalyptic', 'warm', 'stunning', 'breathtaking', 'fascinating', 'peaceful', 'surreal', 'celestial', 'ancient', 'ethereal', 'dramatic', 'horrific', 'terrifying', 'emotional', 'dystopian', 'dark', 'magical', 'psychedelic', 'apocalyptic', 'fantasy', 'dark fantasy', 'alien', 'otherworldly', 'foggy', 'Victorian', 'trippy', 'desolate', 'eldritch', 'gothic', 'futuristic', 'snowy', 'fantastical', 'lush', 'mysterious', 'icy', 'fiery', 'grand', 'western',],

        "objadjcts": ['futuristic', 'glowing', 'ornate', 'scuffed', 'pristine', 'rustic', 'floral', 'intricate', 'smooth', 'shiny', 'dusty', 'dirty', 'colorful', 'high-tech', 'modern', 'cute', 'magical', 'ancient', 'detailed', 'refined', 'unique', 'vintage', 'polished', 'elegant', 'sophisticated', 'complex', 'damaged', 'worn', 'weathered', 'archaic', 'stealthy'],

        "charadjcts": ['armored', 'heavily armored', 'divine', 'cyborg', 'medieval', 'steampunk', 'stylish', 'angelic', 'female', 'male', 'confused', 'lost', 'old', 'young', 'attractive', 'intimidating', 'battered', 'cute', 'modern', 'dirty', 'scarred', 'determined', 'bearded', 'caped', 'shrouded', 'Latin American', 'Caucasian', 'African', 'Indian', 'Arab', 'Asian', 'happy', 'overjoyed', 'lone', 'joyful', 'sad', 'pensive', 'evil', 'bloody', 'robed', 'fashionable', 'tough', 'masked', 'tattooed', 'crazy', 'shadowed', 'elegant', 'stealthy', 'western',],

    },

    "subjects": {

        "characters": {

            "people": ['man', 'woman', 'girl', 'boy', 'assassin', 'bounty hunter', 'knight', 'stormtrooper', 'robot', 'soldier', 'man', 'woman', 'samurai', 'vampire', 'catgirl', 'wolf girl', 'cowgirl', 'cowboy', 'jedi', 'warrior', 'sorcerer', 'human woman', 'human man', 'human girl', 'human boy', 'prince', 'princess', 'king', 'queen', 'god', 'goddess', 'demigod', 'survivor', 'villain', 'hero', 'traveler', 'spaceman', 'space marine', 'explorer', 'wayfarer', 'chef', 'swordsman', 'scout', 'schoolgirl', 'schoolboy', 'motorcyclist', 'hunter', 'demon', 'angel', 'pilot', 'crewman', 'fox girl', 'wizard', 'emperor', 'viking', 'ninja', 'alien', 'businessman', 'guard', 'operative', 'scientist', 'police officer', 'serial killer', 'cultist', 'romantic couple', 'friends', 'spirit', 'crewwoman', 'Little Red Riding Hood', 'chancellor', 'witch', 'pirate', ],

            "charobjects": ['knife', 'weapon', 'flower', 'plushie', 'mirror', 'glass', 'shadow', 'cape', 'backpack', 'dress', 'suit', 'bodysuit', 'artifact', 'map', 'fighter', 'sword', 'carbine', 'smartphone', 'book', 'walking stick', 'drink', 'lantern', 'mask', 'gas mask', 'hat', 'tattoos', 'guitar', 'crystal', 'gem', 'ring', 'jewelry', 'bandana', 'amulet', 'shield', 'pouch', 'headphones', 'gloves', 'scarf',],

        },
        
        "creatures": {

            "land_creatures": ['dog', 'cat', 'frog', 'Oni', 'golem', 'unicorn', 'pegasus', 'basilisk', 'hellhound', 'gnome', 'fairy', 'skinwalker', 'bigfoot', 'hamster', 'eagle', 'raccoon', 'opossum', 'tiger', 'panther', 'wendigo', 'dwarf', 'goblin', 'chimera', 'kitsune', 'bunny', 'serpent', 'horse', 'jinn', 'minotaur', 'mammoth', 'deer', 'Anubis', 'monster', 'werewolf', 'elephant',],

            "air_creatures": ['phoenix', 'hawk', 'eagle', 'bat', 'owl', 'hummingbird', 'bird', 'bee', 'bumblebee', 'dragon', 'griffin',],

            "sea_creatures": ['shark', 'Cthulu', 'kraken', 'megalodon', 'fish', 'octopus', 'Lochness Monster', 'sea monster', 'giant squid', 'deep sea giant isopod', 'crab', 'lobster', 'mermaid', 'leviathan', 'water dragon',],

        },
        
        "large_objects": {

            "land": ['tree', 'tree of life', 'statue', 'monument', 'tank', 'train', 'motorcycle', 'mech suit', 'AT-AT', 'pickup truck', 'semi truck', 'car', 'sports car', 'muscle car', 'exotic car', 'personnel carrier', 'missile launcher',],

            "sea": ['ship', 'galleon', 'pirate ship', 'frigate', 'boat', 'submarine', 'aircraft carrier', 'navy', 'speedboat', 'The Flying Dutchman', 'dreadnought', 'icebreaker', 'cruise ship', 'hovercraft'],

            "air": ['fighter jet', 'space shuttle', 'dropship', 'fighter', 'starfighter', 'shuttle', 'helicopter', 'attack helicopter', 'bomber jet', 'biplane', 'blimp', 'passenger jet'],

            "space": ['spaceship', 'starfighter', 'space station', 'satellite', 'dropship', 'Star Destroyer', 'capital spaceship', 'space dreadnought', 'starship', 'starfighter carrier', 'space dock', 'futuristic military spaceship', 'futuristic exploration spaceship', 'luxury spaceship', 'interstellar drone', 'alien ship', 'X-Wing', 'Millenium Falcon', 'The Discovery', 'Lunar Lander', 'Voyager II', 'voyager probe', 'space telescope', 'International Space Station',],

        },

    },

    "settings": {

        "people_sets": ['street', 'beach', 'mountainous landscape', 'landscape', 'lake', 'city', 'river', 'valley', 'house near a lake', 'house', 'house near the beach', 'skyscrapers', 'nature', 'town', 'forest', 'swamp', 'urban landscape', 'natural landscape', 'alien landscape', 'city streets', 'town streets', 'liminal space', 'abandoned building', 'fort', 'thunderstorm', 'snowstorm', 'nature park', 'battlefield', 'castle', 'detailed background', 'epic sky', 'kitchen', 'bedroom', 'living room', 'office', 'throne room', 'cockpit', 'fireplace', 'cargo bay', 'dock', 'meadow', 'stream', 'cave', 'stadium', 'alleyway', 'market', 'theater', 'workshop', 'field', 'farm', 'barn', 'path', 'jungle', 'pond', 'highway', 'underground cave', 'skyline', 'horizon', 'desert', 'mesa', 'misty island', 'Arctic landscape', 'cottage', 'cabin in the woods', 'tunnel', 'hilly landscape', 'bathroom', 'village', 'dining room', 'hotel', 'library', 'Library of Alexandria', 'pyramids', 'shop', 'suburb', 'waterfall', 'pier', 'fountain', 'volcanic landscape', 'laboratory', 'haunted house', 'prison', 'factory', 'canyon', 'church', 'colosseum', 'roller coaster', 'palace', 'bridge', 'tundra', 'aquarium', 'hallway', 'military base'],

        "creature_sets": {

            "land": ['street', 'beach', 'mountainous landscape', 'landscape', 'lake', 'city', 'river', 'valley', 'house near a lake', 'house', 'house near the beach', 'skyscrapers', 'nature', 'town', 'forest', 'swamp', 'urban landscape', 'natural landscape', 'alien landscape', 'city streets', 'town streets', 'liminal space', 'abandoned building', 'fort', 'thunderstorm', 'snowstorm', 'nature park', 'battlefield', 'castle', 'detailed background', 'epic sky', 'kitchen', 'bedroom', 'living room', 'office', 'throne room', 'cockpit', 'fireplace', 'cargo bay', 'dock', 'meadow', 'stream', 'cave', 'stadium', 'alleyway', 'market', 'theater', 'workshop', 'field', 'farm', 'barn', 'path', 'jungle', 'pond', 'highway', 'underground cave', 'skyline', 'horizon', 'desert', 'mesa', 'misty island', 'Arctic landscape', 'cottage', 'cabin in the woods', 'tunnel', 'hilly landscape', 'bathroom', 'village', 'dining room', 'hotel', 'library', 'Library of Alexandria', 'pyramids', 'shop', 'suburb', 'waterfall', 'pier', 'fountain', 'volcanic landscape', 'laboratory', 'haunted house', 'prison', 'factory', 'canyon', 'church', 'colosseum', 'roller coaster', 'palace', 'bridge', 'tundra', 'aquarium', 'hallway', 'military base'],

            "air": ['street', 'beach', 'mountainous landscape', 'landscape', 'lake', 'city', 'river', 'valley', 'house near a lake', 'house', 'house near the beach', 'skyscrapers', 'nature', 'town', 'forest', 'swamp', 'urban landscape', 'natural landscape', 'alien landscape', 'city streets', 'town streets', 'liminal space', 'abandoned building', 'fort', 'thunderstorm', 'snowstorm', 'nature park', 'battlefield', 'castle', 'detailed background', 'epic sky', 'cargo bay', 'dock', 'meadow', 'stream', 'cave', 'stadium', 'alleyway', 'market', 'theater', 'workshop', 'field', 'farm', 'barn', 'path', 'jungle', 'pond', 'highway', 'underground cave', 'skyline', 'horizon', 'desert', 'mesa', 'misty island', 'Arctic landscape', 'cityscape', 'cottage', 'cabin in the woods', 'tunnel', 'hilly landscape', 'village', 'hotel', 'library', 'Library of Alexandria', 'pyramids', 'shop', 'suburb', 'waterfall', 'pier', 'fountain', 'volcanic landscape', 'laboratory', 'haunted house', 'prison', 'factory', 'canyon', 'church', 'colosseum', 'roller coaster', 'palace', 'bridge', 'tundra', 'aquarium', 'military base', 'sea', 'ocean', 'navy'],

#Sea creature settings and object relations are combined for sake of making sense in output. Feel free to change this if you wish.

            "sea": ['in the high seas', 'in an underwater landscape', 'in a coral reef', 'in an underwater trench', 'in the ocean', 'in a giant lake', 'in the ocean by an island', 'underwater beneath a ship', 'in the deep ocean', 'in the Arctic Ocean',],

        },

        "object_sets": {

            "land": ['street', 'beach', 'mountainous landscape', 'landscape', 'lake', 'city', 'river', 'valley', 'house near a lake', 'house', 'house near the beach', 'nature', 'town', 'forest', 'swamp', 'urban landscape', 'natural landscape', 'alien landscape', 'city streets', 'town streets', 'liminal space', 'abandoned building', 'fort', 'thunderstorm', 'snowstorm', 'nature park', 'battlefield', 'castle', 'detailed background', 'epic sky', 'cargo bay', 'dock', 'meadow', 'stream', 'stadium', 'alleyway', 'street market', 'theater', 'workshop', 'field', 'farm', 'barn', 'path', 'jungle', 'pond', 'highway', 'skyline', 'horizon', 'desert', 'mesa', 'Arctic landscape', 'cottage', 'cabin in the woods', 'tunnel', 'hilly landscape', 'village', 'hotel', 'library', 'Library of Alexandria', 'pyramids', 'shop', 'suburb', 'waterfall', 'pier', 'fountain', 'volcanic landscape', 'laboratory', 'haunted house', 'prison', 'factory', 'canyon', 'church', 'colosseum', 'roller coaster', 'palace', 'bridge', 'tundra', 'aquarium', 'hallway', 'military base'],

#Sea object settings and object relations are combined for sake of making sense in output. Feel free to change this if you wish.
            
            "sea": ['in a stormy ocean', 'underwater', 'in the high seas', 'in a large river', 'docked at port', 'at battle at sea', 'outside of an island', 'on the water near land', 'in the Arctic Ocean', 'in the Caribbean Sea', 'in the Bermuda Triangle', 'in a naval battle', 'in a large lake'],

            "air": ['street', 'beach', 'mountainous landscape', 'landscape', 'lake', 'city', 'river', 'valley', 'house near a lake', 'house', 'house near the beach', 'nature', 'town', 'forest', 'swamp', 'urban landscape', 'natural landscape', 'alien landscape', 'city streets', 'town streets', 'liminal space', 'abandoned building', 'fort', 'thunderstorm', 'snowstorm', 'nature park', 'battlefield', 'castle', 'detailed background', 'epic sky', 'cargo bay', 'dock', 'meadow', 'stream', 'stadium', 'street market', 'theater', 'workshop', 'field', 'farm', 'barn', 'jungle', 'pond', 'highway', 'skyline', 'horizon', 'desert', 'mesa', 'Arctic landscape', 'cottage', 'cabin in the woods', 'hilly landscape', 'village', 'hotel', 'library', 'Library of Alexandria', 'pyramids', 'shop', 'suburb', 'waterfall', 'pier', 'volcanic landscape', 'laboratory', 'haunted house', 'prison', 'factory', 'canyon', 'church', 'colosseum', 'roller coaster', 'palace', 'bridge', 'tundra', 'aquarium', 'hallway', 'military base'],

            "space": ['space station in outer space', 'mothership in outer space', 'planetary ring in outer space', 'nebula', 'supernova remnant', 'magnetar', 'pulsar in outer space', 'accretion disk', 'irregular galaxy', 'black hole', 'star system in outer space', 'binary star system in outer space', 'fleet of starships in outer space', 'orbital elevator', 'dyson sphere in outer space', 'ring planet in outer space', 'wormhole in outer space', 'gas giant in outer space', 'moon in outer space', 'Earth', 'alien planet in outer space', 'exoplanet in outer space', 'rogue planet in outer space', 'comet in outer space', 'asteroid in outer space', 'star in outer space', 'Orion Nebula', 'galaxy', 'exotic planet in outer space', 'exotic star in outer space', 'exotic star system in outer space', 'artificial planet in outer space', 'alien megastructure in outer space', 'megastructure in outer space', 'battle in outer space', 'orbital bombardment',],

        },

        "subjrelations": {

            "land": ['near a', 'in a', 'next to a', 'in front of a', 'inside of a', 'outside of a',],

            "air_creatures": ['flying above a', 'flying by a', 'flying in front of a', 'flying past a', 'perched by a',],

            "air_objects": ['flying above a', 'flying by a', 'flying in front of a', 'flying past a', 'landing by a', 'flying close above a',],

            "space_objects": ['orbiting a', 'flying towards a', 'flying in a', 'docking with a', 'in a', 'flying by a', 'flying by a', 'floating by a', 'flying in front of a', 'orbiting in front of a'],
        },
    },

    "vismodifiers": {

        "styles": ['oil painting', 'minimalistic', 'natural', 'colored', '35mm', 'award-winning photography', 'cinematic lighting', 'limited palette', 'pastel colors', 'cyberpunk', 'render', 'rendered in unreal engine', 'photo', 'glitch art', 'space art', 'high contrast', 'low contrast', 'epic composition', 'nighttime', 'vivid colors', 'soft lighting', 'wavy', 'extradimensional', 'depth of field', 'tonemapping', 'illustration', 'digital painting', 'line art', 'ink', 'color field painting', 'god rays', 'saturated', 'desaturated', 'tonal colors', 'full body', 'eyes focus', 'anime', 'aerial view', 'street level view', 'panoramic', 'hard edge', 'thick lines', 'color page', 'precise lineart', 'neon lighting', 'sun rays', 'nostalgic', 'brutalism', 'high resolution scan', 'winter', 'spring', 'autumn', 'summer', 'studio lighting', 'bokeh', 'motion lines', 'wallpaper', 'muted colors', 'colorgrading', 'vintage', 'aesthetic', 'cosmic horror', 'abstract art', 'simple background', 'synthwave', 'splatter paint style', 'portrait', 'vaporwave', 'concept art', 'cartoon', 'simplistic', 'dim', 'blurred background', 'ambient lighting', 'intense shadows', 'slow motion', 'reflections', 'detailed face', 'animecore', 'astrophotography', 'biomechanical', 'darkwave', 'deathpunk', 'glitchcore', 'glowwave', 'holographic', 'beautifully lit', 'technopunk', 'sci-fi', 'crystalline'],

        "genmetas": ['realistic', '8k', '4k', 'detailed', 'hyperdetailed', 'sharp focus', 'masterpiece', 'absurdres', 'highres', 'professional', 'photorealism', 'studio quality', 'HQ', 'UHD', 'HDR',],

    },
}
# Configure number of visual/style adjectives, style modifiers, and quality modifiers to tack on after the main component of the prompt
numadjectives = 3
numstyles = 3
numquality = 4

def main(prompts):
    while True:
        #List of random visual impression adjectives from above number
        prompt_type = input("Enter '1' for character-focused prompt, '2' for object-focused prompt, '3' for creature-focused prompt, or '0' to stop the script: ")
        if prompt_type == '1':
            again = True
            while again: 
                prompt = charprompt(prompts)
                giveprompt(prompts, prompt, numstyles, numquality)
                repeat = input("Press 'Enter' for another character-focused prompt, or any other key + 'Enter' to return: ")
                again = repeat == ''
        elif prompt_type == '2':
            again = True
            while again:
                prompt = objprompt(prompts)
                giveprompt(prompts, prompt, numstyles, numquality)
                repeat = input("Press 'Enter' for another object-focused prompt, or any other key + 'Enter' to return: ")
                again = repeat == ''
        elif prompt_type == '3':
            again = True
            while again:
                prompt = creaprompt(prompts)
                giveprompt(prompts, prompt, numstyles, numquality)
                repeat = input("Press 'Enter' for another creature-focused prompt, or any other key + 'Enter' to return: ")
                again = repeat == ''
        elif prompt_type == '0':
            break

def charprompt(prompts):
            listadj = ', '.join(rn.sample(prompts["adjectives"]["visadjcts"], numadjectives))
            character = rn.choice(prompts["adjectives"]["charadjcts"]) + ' ' + rn.choice(prompts["subjects"]["characters"]["people"]) 
            obj = rn.choice(prompts["adjectives"]["objadjcts"]) + ' ' + rn.choice(prompts["subjects"]["characters"]["charobjects"])
            setting = rn.choice(prompts["settings"]["subjrelations"]["land"]) + ' ' + rn.choice(prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["people_sets"])
            prompt = character + ' ' + 'with a ' + obj + ' ' + setting + ', ' + listadj + ', '
            return prompt

def objprompt(prompts):
            listadj = ', '.join(rn.sample(prompts["adjectives"]["visadjcts"], numadjectives))
            #Picks random type of main subject object
            randobjtype = rn.choice(list(prompts["subjects"]["large_objects"]))
            #To apply random setting according to what kind of setting the object is for
            if randobjtype == "land":
                setting = rn.choice(prompts["settings"]["subjrelations"]["land"]) + ' ' + rn.choice(prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["object_sets"]["land"])
            elif randobjtype == "sea":
                setting = rn.choice(prompts["settings"]["object_sets"]["sea"])
            elif randobjtype == "air":
                setting = rn.choice(prompts["settings"]["subjrelations"]["air_objects"]) + ' ' + rn.choice(prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["object_sets"]["air"])
            elif randobjtype == "space":
                setting = rn.choice(prompts["settings"]["subjrelations"]["space_objects"]) + ' ' + rn.choice(prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["object_sets"]["space"])
            mainobject = rn.choice(prompts["adjectives"]["objadjcts"]) + ' ' + rn.choice(prompts["subjects"]["large_objects"][randobjtype])
            prompt = mainobject + ' ' + setting + ', ' + listadj + ', '
            return prompt

def creaprompt(prompts):
            listadj = ', '.join(rn.sample(prompts["adjectives"]["visadjcts"], numadjectives))
            #Picks random type of creature
            randcreatype = rn.choice(list(prompts["subjects"]["creatures"]))
            #To apply random setting according to what kind of setting the creature is for
            if randcreatype == "land_creatures":
                setting = rn.choice(prompts["settings"]["subjrelations"]["land"]) + ' ' + rn.choice(prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["creature_sets"]["land"])
            elif randcreatype == "sea_creatures":
                setting = rn.choice(prompts["settings"]["creature_sets"]["sea"])
            elif randcreatype == "air_creatures":
                setting = rn.choice(prompts["settings"]["subjrelations"]["air_creatures"]) + ' ' + rn.choice(prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["creature_sets"]["air"])
            creature = rn.choice(prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["subjects"]["creatures"][randcreatype]) 
            prompt = creature + ' ' + setting + ', ' + listadj + ', '
            return prompt

def giveprompt(prompts, prompt, numstyles, numquality):
            prompt += ', '.join(rn.sample(prompts["vismodifiers"]["styles"], numstyles)) + ', ' + ', '.join(rn.sample(prompts["vismodifiers"]["genmetas"], numquality))
            print()
            print(prompt)
            print()

if __name__ == "__main__":
    main(prompts)
