config = {}

cfg_file = open('config.ini', encoding='utf-8')
my_config = cfg_file.readlines()
cfg_file.close()

current_section = ""


for x in my_config:
    res = x.split("=")
    key = res[0]
    key = key.strip()
    if len(res) == 1:
        if key.startswith('[') and key.endswith(']'):
            current_section = key[1:-1]
            config[current_section] = {}
    else:
        value = res[1]
        value = value.strip()
        if key.startswith('#') or key.startswith(';'):
            continue
        if value.lower() in ['true', 'yes', 'on']:
            value = True
        elif value.lower() in ['false', 'no', 'off']:
            value = False
        elif value.isdigit():
            value = int(value)
        config[current_section][key] = value

print(config)

