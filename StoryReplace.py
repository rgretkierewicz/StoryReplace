story =  """ 
    She donned a black cape adorned with glittering stars, a mustache that seemed to have a life of its own, 
    and a top hat three times her size. With an infectious evil cackle, she proclaimed herself \"Professor Snickerdoodle, 
    the Master of Mayhem!\" Her inventions were as comical as they were devious. 
    He built an army of fluffy mechanical minions called \"Fuzzybots\" to carry out her wacky schemes. 
    These Fuzzybots, resembling cuddly teddy bears with gears and springs, wreaked havoc by delivering tickle attacks to unsuspecting 
    townsfolk and causing uncontrollable giggling fits. In pursuit of the ultimate evil invention, Snarfle created the 
    \"Giggletron 9000\" a giant contraption that shot out bubbles filled with laughing gas. His plan was to cover the entire kingdom 
    in laughter until they begged for mercy. However, every time he tested the Giggletron 9000, 
    it malfunctioned and covered him in a colorful explosion of bubbles, earning him the nickname \"Bubblebeard the Silly.\" 
    Despite her numerous failures, Snarfle remained undeterred. Her relentless pursuit of villainy was met with laughter and cheer 
    rather than fear and dread. The people of Fluffingtonia couldn't help but find his antics endearing, and her \"evil\" plots 
    often brought the kingdom closer together. As much as he wanted to be the most feared villain, Professor Snarfle McBoomwhiskers 
    couldn't escape the fact that his heart was filled with kindness and good intentions. He may have behaved like a cartoon villain, 
    but deep down, he was a lovable harengon with a knack for hilarity and a heart as fluffy as a marshmallow. 
    And so, with a mischievous glint in his eye and a spring in his step, Professor Snarfle McBoomwhiskers continues to 
    invent and plot, bringing joy, laughter, and the occasional harmless chaos to the delightful realm of Fluffingtonia. 
    For in the end, being a lovable and silly villain is all part of the fun in this extraordinary land of cotton candy wonders!
    """

story_replacers = {"Snarfle" : "Snickerdoodle",
                   " his " : " her ",
                   " he " : " she ",
                   " His " : " Her ",
                   " He " : " She ",
                   " him " : " her "}

for k, v in story_replacers.items():
    story = story.replace(k , v)

print(story)
