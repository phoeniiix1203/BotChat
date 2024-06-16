def convert_dialogue_format(dialogue_list):
    formatted_dialogue = ""
    for conversation in dialogue_list:
        for i, line in enumerate(conversation):
            speaker = 'A' if i % 2 == 0 else 'B'
            formatted_dialogue += f"{speaker}: {line}<chat_end>\n"
    return formatted_dialogue

# 示例输入
dialogue_list = [['May I speak to you, Mr. Hall?', "Sure, Sonya. What's the problem?"], ["I've been having trouble with my car. It just won't start, no matter what I do. Any advice?", "Oh, that's frustrating! First, check if you have enough fuel. Also, make sure the battery is charged. If it's cold outside, the battery might struggle. If those are okay, it could be a starter issue. Maybe try jump-starting it with a portable battery pack. If that doesn't work, it might be best to call a mechanic."], ["Thanks, Sonya. I'll check the fuel and battery. I'm in a bit of a rush, so I'll try the jump-start option first. If that doesn't work, I'll have to call for help. Fingers crossed!", 'Sounds like a plan! Good luck, Sonya. Hope your car starts up soon. If you need any more tips or help, feel free to ask. Stay positive!'], ["Thanks, I appreciate it. I'll let you know how it goes. Keeping my fingers crossed!", "You're welcome, Sonya! I'm rooting for you. Feel free to update me later. Safe driving!"], ["Will do, Sonya. Thanks for your support. I'll let you know if I need any more advice or if I get it running smoothly. Stay tuned!", "Absolutely, Sonya! I'm here whenever you need. Updates are always welcome. Stay optimistic and keep me posted on your car's progress. Take care!"], ["Thanks, Sonya. I'll keep you posted. Your support has been really helpful. Stay well!", "You're welcome, Sonya! I'm glad I could help. Don't hesitate to reach out if you need anything else. Stay safe and well!"], ["Thanks, Sonya. Your encouragement has been a big help. I'll definitely keep you updated. Stay healthy and happy!", "You're very welcome, Sonya! I'm here whenever you need. Updates are great, and I'm wishing you all the best. Stay healthy and happy too!"], ["Thanks, Sonya. Your kindness means a lot. I'll keep you posted on my car's status. Stay well and have a great day!", "You're so welcome, Sonya! I'm glad I could assist. Updates on your car are always appreciated. Have a fantastic day and take care!"]]

# 转换对话格式
formatted_dialogue = convert_dialogue_format(dialogue_list)

# 打印转换后的对话
print(formatted_dialogue)
