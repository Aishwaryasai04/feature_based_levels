from typing import Concatenate, ContextManager


class FileSystem:
    def __init__(self):
        self.files={}
    def create(self, path, content):
        self.files[path]=content
    def read(self, path):
        return self.files.get(path, "File not found")
    def delete(self, path):
        return self.files.pop(path, None) is not None
    def append(self, path, content):
        if path in self.files:
            self.files[path] += content
        else:
            self.files[path]= content
    def mkdir(self, path):
        if path not in self.files:
            self.files[path]={}
            return True
        if isinstance(self.files[path], dict):
            return False
        return False
    def ls(self, path):
        node= self.files.get(path, None)

        if node is None:
            return []
        if isinstance(node, str):
            return [path.split("/")[-1]]
        if isinstance(node, dict):
            return sorted(node.keys())



fs= FileSystem()
fs.create("/a.txt", "hello")
print(fs.read("/a.txt"))
print(fs.read("/b.txt"))

fs.create("/a.txt", "world")
print(fs.read("/a.txt"))
print(fs.delete("/a.txt"))
print(fs.delete("/b.txt"))

fs.append("/a.txt", "World!")
fs.append("/b.txt", "You got this!")
print(fs.read("/a.txt"))
print(fs.read("/b.txt"))
fs.create("/readme.txt", "hi")
fs.mkdir("/readme.txt")
print(type(fs.files["/readme.txt"]) is str)

fs.mkdir("/docs")
print(fs.files)
print(fs.ls("/a.txt"))
print(fs.ls("/docs"))
print(fs.ls("/nope"))
