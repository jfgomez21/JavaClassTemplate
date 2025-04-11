import os

class BufferList(list):
    name = "/path/to/your/project/src/main/java/abc/Main.java"

    def __init__(self, *args):
        super().__init__(*args)

    def append(self, element, index = None):
        if index is None:
            if isinstance(element, list):
                for item in element:
                    super().append(item)
            else:
                super().append(element)
        else:
            if isinstance(element, list):
                self[index:index] = element
            else:
                super().insert(index, element)
        
class Buffer:
    buffer = BufferList()

current = Buffer()

properties = { "has('win32')" : "0", "getcwd()" : "/path/to/your/project", "cursor" : (1, 0) }

def eval(arg):
    if arg in properties:
        return properties[arg]

    return None

def set_cwd(path, relative_name):
    properties["getcwd()"] = path

    current.buffer.name = os.path.join(path, relative_name)

def set_win32(enable):
    properties["has('win32')"] = "1" if enable else "0"
