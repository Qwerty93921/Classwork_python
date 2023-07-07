config = {}

cfg_file = open("config.ini", encoding="utf-8")
my_config = cfg_file.readlines()
cfg_file.close()

current_section = ""



for x in my_config:
    res = x.split("=")
    key = res[0]
    key = key.strip()

    if len(res) == 1:
        if key.startswith("[") and key.endswith("]"):
            current_section = key[1:-1]
            config[current_section] = {}
    else:
        res[1] = res[1].strip()

        if key.startswith("#") or key.startswith(";"):
            continue
        if res[1].lower() in ["true", "yes", "on"]:
            res[1] = True
        elif res[1].lower() == ["false", "no", "off"]:
            res[1] = False
        elif res[1].isdigit():
            res[1] = int(res[1])
        config[current_section][key] = res[1]

print(config)


# strip убирает символы по бокам от элемента строки
# {} - пустой словарь