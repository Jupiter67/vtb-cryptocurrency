from yaml import load, SafeLoader


class Settings:
    host: str
    port: str
    vtb_public_key: str
    vtb_private_key: str
    pg_host: str
    pg_port: str
    pg_user: str
    pg_password: str
    pg_database: str

    def __init__(self):
        with open('settings.yaml', 'r') as f:
            config = load(f, SafeLoader)
        for i in dir(self):
            if not i.startswith('__'):
                self.__setattr__(i, config.get(i))
