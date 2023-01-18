# SD-Prompt-Generator
A complete expansion of javi22020's Prompt Generator script that tries to create random prompts with a structure that works well for providing inspiration. Currently generates prompts of random characters, objects/vehicles, and creatures, with random locations and visual styles. The [bad-artist](https://huggingface.co/nick-x-hacker/bad-artist) negative embeddings are recommended.

## Usage

To use, have Python installed, and download/clone [promptgen.py](https://github.com/526christian/SD-Prompt-Generator/blob/main/promptgen.py), or copy the contents and paste them into an empty document and save as promptgen.py, or whatever name you prefer. Put the .py somewhere you can access easily. Or, put it in your home folder (on Linux) or somewhere with the PATH edited on Windows, if you want to easily call the script without typing or pasting the file's path.

In a terminal/CLI, type

    python

Add a space, and drag and drop `promptgen.py` onto the terminal/CLI to automatically fill in its path. I'd suggest copying the whole command so you can quickly access the script again later.

Press 'enter' to keep generating prompts of the same type quickly, or switch to another prompt type as you please. As prompts are randomized, they will be naturally hit-or-miss, so that makes it easy to roll the dice again.

To add or remove phrases, or edit how many are tacked on the main prompt, edit the .py. The structure is pretty straightforward, so if you want to, you can even further break down the prompt categories and add them into the code as you like for more complex or specialized random prompting.

Naturally, certain phrases will be better understood by different models. For instance, "catgirl" and "splash paint art" are represented much better in anime-based models than models that focus more on realistic art.


To use the Webui script, you will need to first type 
	
	pip install gradio

Then use the steps above to start the script.

## The prompts

This script provides a variety of randomly-selected adjectives, subjects (characters, objects, creatures), settings (locations), and visual style and quality phrases. The general adjectives add randomness to the output, but also can influence the overall visual impression of an image similar to the styles. The usefulness of "quality prompts" (e.g. realistic, masterpiece, professional) despite their widespread application is debatable, but they are included nonetheless as they sometimes improve the detail of outfits and sense of depth.

I recommend using the [bad-artist](https://huggingface.co/nick-x-hacker/bad-artist) embeddings in your negative prompt, as these seem to help prevent over-representation of adjectives in the AI's output. For instance, without those 'negative embeddings', "terrifying" will make characters, well, terrifying, even if it's meant to be describing the setting.

The expanded prompt list was built off of personal experience after thousands of images generated with Stable Diffusion v1.5-based models. Artist names and existing IP were intentionally avoided for style and quality prompts to focus on getting decent-quality output off creativity alone.

## Tips + examples

If you use prompts directly without editing them, your mileage will vary depending on the model and prompt. Objects and creatures may be hard to get looking right. A UI that has attention weighting and inpainting, like [InvokeAI](https://github.com/invoke-ai/InvokeAI/), will go a long way if you like a particular prompt that isn't coming out right immediately.

As you can expect, model matters a lot. Some good general-purpose models (read: not focused on an artist's work or specific objects or styles), such as [Elldreth's StolenDreams](https://civitai.com/models/2540/elldreths-stolendreams-mix), [TheAlly's Mix II](https://civitai.com/models/3848/theallys-mix-ii-churned), [Anything and Everything](https://civitai.com/models/3661/anything-and-everything-mix-ver-15), and [Kenshi](https://civitai.com/models/3850/kenshi) work great for a lot of prompts. Some specific prompts are best tackled with a more focused model, like [Sci-Fi Diffusion](https://civitai.com/models/4404/sci-fi-diffusion-v10) for prompts of spaceships and other high-tech subjects/styles.

Good luck!

Below are some examples of images with good copy-pasted prompts made by the script, using a couple 'negative embeddings':

![003659 099091dd 3062602010](https://user-images.githubusercontent.com/122599135/212419237-8c5f4942-388b-43d0-8390-c5dfae3aff34.png)

`heavily armored operative with a intricate smartphone in a ethereal forest, fascinating, magical, emotional, low contrast, cosmic horror, eyes focus, HDR, 4k, 8k, hyperdetailed [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: TheAlly's Mix II`

![003824 d86c57ab 1173902681](https://user-images.githubusercontent.com/122599135/212448333-7b301e1f-4f0e-418a-afe4-a86082bf91f9.png)

`scarred crewwoman with a colorful gas mask in front of a cozy mesa, warm, fascinating, dramatic, winter, motion lines, glitchcore, highres, HDR, 4k, highres [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: Elldreth's Stolen Dreams`

![004205 2a48a3a0 3235613962](https://user-images.githubusercontent.com/122599135/212576997-24572de2-eba8-4c3a-8e8e-0bb943260e1b.png)

`dystopian kraken in the high seas, icy, fiery, fantastical, dim, beautifully lit, pastel colors, photorealism, studio quality, detailed, professional [sketch by bad-artist, art by bad-artist-anime, bad-hands-5, text, logo, signature]

`Model: TheAlly's Mix II`

![003689 18c8966b 2537436940](https://user-images.githubusercontent.com/122599135/212424493-770e5ccc-35f7-4c0f-9c8b-1d88b3cc8ba0.png)

`heavily armored alien with a dystopian bodysuit near a shiny cockpit, Victorian, beautiful, scuffed, thick lines, wallpaper, anime, studio quality, UHD, detailed, highres [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: Kenshi`

![003691 bd4d6aa3 743370597](https://user-images.githubusercontent.com/122599135/212424921-d6140040-39d6-41e6-b14a-ca8d8ee3a13f.png)

`Arab prince with a crystalline glass inside of a gloomy mountain, ancient, nice, cozy, after hours, eyes focus, detailed face, absurdres, studio quality, highres, hyperdetailed [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: Kenshi`

![004288 d44783df 3782731203](https://user-images.githubusercontent.com/122599135/212577489-c7fad369-c649-4969-9a11-fbe863f42d0f.png)

`sophisticated dreadnought in a large river, snowy, dark fantasy, apocalyptic, wallpaper, mysterious, portrait, masterpiece, 8k, hyperdetailed, photorealism [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: Elldreth's Stolen Dreams`

![003703 1ed7680d 2859117530](https://user-images.githubusercontent.com/122599135/212426057-851353dc-5874-4c7a-8251-fabd28771577.png)

`Asian pilot with a ancient glass near a magical snowstorm, ethereal, trippy, emotional, neon lighting, epic composition, wavy, detailed, masterpiece, realistic, photorealism [sketch by bad-artist, art by bad-artist-anime, bad-hands-5]`

`Model: Elldreth's Stolen Dreams`

## Changelog

~8 PM 1/15: Merged pull request with a bunch of new words.

~3 AM 1/15: Complete restructuring of script. Now supports selection for character prompts, large object/vehicle prompts, and creature prompts. If you select object or creature, the script will randomly select from a type of object or creature and randomly select an appropriate setting.

~10 PM 1/13: New prompt phrases across the board for variety and a couple fixes in the list. Added new category for object adjectives to improve prompt generation consistency. Should be better now. Updated readme.
