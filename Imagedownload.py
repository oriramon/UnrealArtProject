from imaginairy import imagine, imagine_image_files, ImaginePrompt, WeightedPrompt, LazyLoadingImage


prompts = ImaginePrompt("a scenic landscape")
    # ImaginePrompt("a bowl of fruit"),
    # ImaginePrompt([
    #     WeightedPrompt("cat", weight=1),
    #     WeightedPrompt("dog", weight=1),
    # ]),
    # ImaginePrompt(
    #     "a spacious building", 
    #     init_image=LazyLoadingImage(url=url)
    # ),
    # ImaginePrompt(
    #     "a bowl of strawberries", 
    #     init_image=LazyLoadingImage(filepath="mypath/to/bowl_of_fruit.jpg"),
    #     mask_prompt="fruit OR stem{*2}",  # amplify the stem mask x2
    #     mask_mode="replace",
    #     mask_modify_original=True,
    # ),
    # ImaginePrompt("strawberries", tile_mode=True),
# ]
# for result in imagine(prompts):
#     # do something
# prompts.save("my_image.jpg")

# or

imagine_image_files(prompts, outdir="./my-art")
