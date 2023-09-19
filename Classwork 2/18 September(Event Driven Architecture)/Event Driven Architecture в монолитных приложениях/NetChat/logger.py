class Logger:
    Instance = None
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3
    TRACE = 4
    names = ["[E]","[W]", "[I]", "[D]", "[T]", ]

    COLORS = {
        ERROR:'\033'
    }
    ENDCOLOR = '\033'

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.Instance = super(Logger, cls).__new__(cls)
    #     return cls.Instance


    def __init__(self, log_level, stdout=True, file = None):
        self.log_level = log_level
        self.stdout = stdout
        self.file = file
        Logger.Instance = self

    def log(self, log_level, *args, **kwargs):
        if log_level <= self.log_level:
            message = ' '.join(map(str, args))
            formatted_message = f"[{log_level}] {message}"
            if self.stdout:
                color = self.COLOR.get(log_level, '')
                end_color = self.ENDCOLOR if color else ''
                print(f"{color}{formatted_message}{end_color}", **kwargs)
            if self.file:
                with open(self.file, 'a') as f:
                    f.write(formatted_message + '\n')