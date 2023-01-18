import random as rn
import gradio as gr

from promptgen import prompts

# Configure number of visual/style adjectives, style modifiers, and quality modifiers to tack on after the main component of the prompt

def charprompt(prompts, numadj):
            listadj = ', '.join(rn.sample(prompts["adjectives"]["visadjcts"], numadj))
            character = rn.choice(prompts["adjectives"]["charadjcts"]) + ' ' + rn.choice(prompts["subjects"]["characters"]["people"]) 
            obj = rn.choice(prompts["adjectives"]["objadjcts"]) + ' ' + rn.choice(prompts["subjects"]["characters"]["charobjects"])
            setting = rn.choice(prompts["settings"]["subjrelations"]["land"]) + ' ' + rn.choice(prompts["adjectives"]["visadjcts"]) + ' ' + rn.choice(prompts["settings"]["people_sets"])
            prompt = character + ' ' + 'with a ' + obj + ' ' + setting + ', ' + listadj + ', '
            return prompt

def objprompt(prompts, numadj):
            listadj = ', '.join(rn.sample(prompts["adjectives"]["visadjcts"], numadj))
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

def creaprompt(prompts, numadj):
            listadj = ', '.join(rn.sample(prompts["adjectives"]["visadjcts"], numadj))
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

def createprompt(prompt_type, numadj, numstyles, numquality, promptmatrix):
    global prompts

    if(prompt_type == "Character"):
        prompt = charprompt(prompts, numadj)

    elif(prompt_type == "Object"):
        prompt = objprompt(prompts, numadj)

    elif(prompt_type == "Creature"):
        prompt = creaprompt(prompts, numadj)

    if(promptmatrix):
        prompt += ', '.join(rn.sample(prompts["vismodifiers"]["genmetas"], numquality)) + ' | ' + ' | '.join(rn.sample(prompts["vismodifiers"]["styles"], numstyles))

    else:
        prompt += ', '.join(rn.sample(prompts["vismodifiers"]["styles"], numstyles)) + ', ' + ', '.join(rn.sample(prompts["vismodifiers"]["genmetas"], numquality))


    return prompt

demo = gr.Interface(
    createprompt,
    [
        gr.Dropdown(["Character", "Object", "Creature"]), #Type dropdown
        gr.Slider(0, 10, value=3, step=1), #Adjectives slider
        gr.Slider(0, 10, value=3, step=1), #Styles slider
        gr.Slider(0, 10, value=4, step=1), #Quality slider
        gr.Checkbox(value=False, label="Prompt matrix for styles?") #Prompt matrix checkbox
    ],
    "text")
demo.launch()

if __name__ == "__main__":
    main(prompts)
