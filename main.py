import os


class Pydb():
  def __init__(self, name):
    self.name = name + '.sql'
    self.temp = []
    with open((self.name), 'a+') as f:
      if os.stat(self.name).st_size <= 0:
        with open('pattern.txt', 'r') as f1:
          for line in f:
            self.temp.append(line)
          if len(self.temp) < 1:
            for line in f1:
              f.write(line)
            self.temp = []

  def add(self, key, volume):
    if type(key) != int:
      self.check(key)
    self.check(volume)
    new_add = (key + ' ' + volume + '\n')
    with open((self.name), 'a') as fa:
      fa.writelines(new_add)

  def repl(self):
    if os.stat(self.name).st_size > 0:
      with open(self.name) as fr:
        first_line = fr.readline().strip('\n')
        new_line = str(int(first_line) + 1) + '\n'
        a=fr.readlines()
        a.insert(0, new_line)
        with open(self.name, 'w') as file:
          file.writelines(a)

  def check(self, vol):
    a = vol.split()
    if len(a) != 1:
      print('Error')
    print(a)


test = Pydb("test")
test.add('Привет', 'мир')
