import random as rn
import re
from promptwords import prompts

# Configure number of visual/style adjectives, style modifiers, and quality modifiers to tack on after the main
# component of the prompt. Default is 3 adjectives, 3 style modifiers, 4 quality modifiers, and promptmatrix False.
numadjectives = 3
numstyles = 3
numquality = 4
usepromptmatrix = False


def main(prompts):
    while True:
        prompt_type = input(
            "\nEnter '1' for character-focused prompt, '2' for object-focused prompt, '3' for creature-focused prompt, "
            "'4' to change prompt settings, or '0' to stop the script: ")
        if prompt_type == '1':
            again = True
            while again:
                prompt = charprompt(prompts)
                giveprompt(prompts, prompt, numstyles, numquality)
                repeat = input(
                    "Press 'Enter' for another character-focused prompt, or any other key + 'Enter' to return: ")
                again = '' == repeat
        elif prompt_type == '2':
            again = True
            while again:
                prompt = objprompt(prompts)
                giveprompt(prompts, prompt, numstyles, numquality)
                repeat = input(
                    "Press 'Enter' for another object-focused prompt, or any other key + 'Enter' to return: ")
                again = '' == repeat
        elif prompt_type == '3':
            again = True
            while again:
                prompt = creaprompt(prompts)
                giveprompt(prompts, prompt, numstyles, numquality)
                repeat = input(
                    "Press 'Enter' for another creature-focused prompt, or any other key + 'Enter' to return: ")
                again = '' == repeat
        elif prompt_type == '4':
            changesettings()
        elif prompt_type == '0':
            break

def charprompt(prompts):
    listadj = ', '.join(rn.sample(prompts["adjectives"]["visadjcts"], numadjectives))
    character = rn.choice(prompts["adjectives"]["charadjcts"]) + ' ' + rn.choice(
        prompts["subjects"]["characters"]["people"])
    obj = rn.choice(prompts["adjectives"]["objadjcts"]) + ' ' + rn.choice(
        prompts["subjects"]["characters"]["charobjects"])
    setting = rn.choice(prompts["settings"]["subjrelations"]["land"]) + ' ' + rn.choice(
        prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["people_sets"])
    prompt = character + ' ' + 'with a ' + obj + ' ' + setting + ', ' + listadj + ', '
    return prompt

def objprompt(prompts):
    listadj = ', '.join(rn.sample(prompts["adjectives"]["visadjcts"], numadjectives))
    # Picks random type of main subject object
    randobjtype = rn.choice(list(prompts["subjects"]["large_objects"]))
    # To apply random setting according to what kind of setting the object is for
    if randobjtype == "land":
        setting = rn.choice(prompts["settings"]["subjrelations"]["land"]) + ' ' + rn.choice(
            prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["object_sets"]["land"])
    elif randobjtype == "sea":
        setting = rn.choice(prompts["settings"]["object_sets"]["sea"])
    elif randobjtype == "air":
        setting = rn.choice(prompts["settings"]["subjrelations"]["air_objects"]) + ' ' + rn.choice(
            prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["object_sets"]["air"])
    elif randobjtype == "space":
        setting = rn.choice(prompts["settings"]["subjrelations"]["space_objects"]) + ' ' + rn.choice(
            prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["object_sets"]["space"])
    mainobject = rn.choice(prompts["adjectives"]["objadjcts"]) + ' ' + rn.choice(
        prompts["subjects"]["large_objects"][randobjtype])
    prompt = mainobject + ' ' + setting + ', ' + listadj + ', '
    return prompt

def creaprompt(prompts):
    listadj = ', '.join(rn.sample(prompts["adjectives"]["visadjcts"], numadjectives))
    # Picks random type of creature
    randcreatype = rn.choice(list(prompts["subjects"]["creatures"]))
    # To apply random setting according to what kind of setting the creature is for
    if randcreatype == "land_creatures":
        setting = rn.choice(prompts["settings"]["subjrelations"]["land"]) + ' ' + rn.choice(
            prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["creature_sets"]["land"])
    elif randcreatype == "sea_creatures":
        setting = rn.choice(prompts["settings"]["creature_sets"]["sea"])
    elif randcreatype == "air_creatures":
        setting = rn.choice(prompts["settings"]["subjrelations"]["air_creatures"]) + ' ' + rn.choice(
            prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["creature_sets"]["air"])
    creature = rn.choice(prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(
        prompts["subjects"]["creatures"][randcreatype])
    prompt = creature + ' ' + setting + ', ' + listadj + ', '
    return prompt

def giveprompt(prompts, prompt, numstyles, numquality):
    # Add all the styles and quality words to the prompt, and if prompt matrix is enabled use | instead of , for styles.
    if not usepromptmatrix:
        prompt += ', '.join(rn.sample(prompts["vismodifiers"]["styles"], numstyles)) + ', ' + ', '.join(
            rn.sample(prompts["vismodifiers"]["genmetas"], numquality))
    else:
        prompt += ', '.join(rn.sample(prompts["vismodifiers"]["genmetas"], numquality)) + ' | ' + ' | '.join(
            rn.sample(prompts["vismodifiers"]["styles"], numstyles))
    # Print the prompt
    print()
    print(prompt)
    print()

def changesettings():
    global numadjectives
    global numstyles
    global numquality
    global usepromptmatrix
    changing_settings = True
    #Opening currently-running script in read mode and saving as a string assigned to variable so text can be modified 
    with open(__file__, "r") as f:
        script = f.read()
    while changing_settings:
        setting_to_change = input(
            "\nEnter the number corresponding to the setting you want to change; '1' for the number of adjectives, "
            "'2' for the number of styles, '3' for quality modifiers, or '4' to use or disable A111 prompt matrix for "
            "style phrases: ")
        if setting_to_change == '1':
            inputting = True
            while inputting:
                setting_value = int(input("Enter a value: "))
                numadjectives = setting_value
                script = re.sub(f"numadjectives = \d+", f"numadjectives = {setting_value}", script)
                inputting = False
        elif setting_to_change == '2':
            inputting = True
            while inputting:
                setting_value = int(input("Enter a value: "))
                numstyles = setting_value
                script = re.sub(f"numstyles = \d+", f"numstyles = {setting_value}", script)
                inputting = False
        elif setting_to_change == '3':
            inputting = True
            while inputting:
                setting_value = int(input("Enter a value: "))
                numquality = setting_value
                script = re.sub(f"numquality = \d+", f"numquality = {setting_value}", script)
                inputting = False
        elif setting_to_change == '4':
            inputting = True
            while inputting:
                setting_value = input("Enter t (true) or f (false): ")
                if setting_value == 't':
                    setting_value = True
                    # Re.sub interferes with multiple of the same variable assignments, so this extra assignment is a workaround
                    usepromptmatrix = setting_value
                    # The assignment string in this argument will change every time user changes setting, but won't affect anything
                    # as long as we remember to reset the usepromptmatrix setting using the script after testing
                    script = re.sub(f"usepromptmatrix = False", f"usepromptmatrix = {setting_value}", script)
                elif setting_value == 'f':
                    setting_value = False
                    # Re.sub interferes with multiple of the same variable assignments, so this extra assignment is a workaround
                    usepromptmatrix = setting_value
                    # The assignment string in this argument will change every time user changes setting, but won't affect anything
                    # as long as we remember to reset the usepromptmatrix setting using the script after testing
                    script = re.sub(f"usepromptmatrix = True", f"usepromptmatrix = {setting_value}", script)
                inputting = False
        #Writing currently-running script to save changes from re.sub
        with open(__file__, "w") as f:
            f.write(script)
        print('\nCURRENT SETTINGS \nAdjectives:', numadjectives, '\nStyles:', numstyles, '\nQuality modifiers:',
              numquality, '\nUse A111 prompt matrix for style phrases:', usepromptmatrix)
        repeat = input("Press 'Enter' to change another setting, or any other key + 'Enter' to return: ")
        print()
        changing_settings = '' == repeat

if __name__ == "__main__":
    main(prompts)
