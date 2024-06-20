def read_from_workers(path):
    with open(path, 'r') as f:
        return f.readlines()
