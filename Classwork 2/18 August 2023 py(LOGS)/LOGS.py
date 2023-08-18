import sys

print(sys.argv)
# нужно для вывода этого:
# нужно написать python (название файла.py) --level debug
# и после выйдут эти данные:


# PS C:\Users\КостюшокА\Classwork github AK\Classwork_python\Classwork 2\18 August 2023 py(LOGS)> python LOGS.py --level debug
# ['LOGS.py', '--level', 'debug']
# [E] Ошибка: сервер недоступен! 193.56.9.102

class Levels:
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3
    TRACE = 4
    names = ("[E]", "[W]", "[I]", "[D]", "[T]")

def _log(level, *args, **kwargs):
    if level >= len(Levels.names):
        return
    if level > current_log_level:
        return
    print(Levels.names[level], *args, **kwargs)
    # В print ставить * символ значит делать print не сам список или словарь, а его СОДЕРЖИМОЕ(скобки не будет видно) 


def logE(*args, **kwargs):
    _log(Levels.ERROR, *args, **kwargs)

def logW(*args, **kwargs):
    _log(Levels.WARNING, *args, **kwargs)

def logI(*args, **kwargs):
    _log(Levels.INFO, *args, **kwargs)

def logD(*args, **kwargs):
    _log(Levels.DEBUG, *args, **kwargs)

def logT(*args, **kwargs):
    _log(Levels.TRACE, *args, **kwargs)


current_log_level = Levels.ERROR

if __name__ == "__main__":
    # print(sys.argv)

    if "--level" in sys.argv:
        result = sys.argv.index("--level") + 1
        desired_level = sys.argv[result]
        if desired_level == "debug":
            current_log_level = Levels.DEBUG
        elif desired_level == "info":
            current_log_level = Levels.INFO
        elif desired_level == "warning":
            current_log_level = Levels.WARNING
        elif desired_level == "trace":
            current_log_level = Levels.TRACE
        elif desired_level == "error":
            current_log_level = Levels.ERROR

    logI("Новый клиент подключился id = ", 9847953, end="!\n")
    logE("Ошибка: сервер недоступен!", "193.56.9.102")
    logT("main() called")
    logW("Пароль не очень надежный:", "*******")
    logD("Это debug сообщение")

# *args - список
# **kwargs - словарь

# PS C:\Users\КостюшокА\Classwork github AK\Classwork_python\Classwork 2\18 August 2023 py(LOGS)> python LOGS.py --level debug
# ['LOGS.py', '--level', 'debug']
# [E] Ошибка: сервер недоступен! 193.56.9.102
