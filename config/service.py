def read_txt(path):
    try:
        with open(path, 'r') as f:
            db_config = {}
            for line in f:
                try:
                    key, value = line.strip().split('=')
                    db_config[key] = value
                except:
                    pass
            return db_config
    except FileNotFoundError:
        print(f"\U0001F6AB Erro: arquivo {path} não encontrado.")
        return {}
    except Exception as e:
        print(f"\U0001F6AB Erro ao ler arquivo {path}: {str(e)}")
        return {}
