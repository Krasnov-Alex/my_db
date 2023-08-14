class Pydb():
  def __init__(self, name):
    self.name = name
    with open((name + '.pydb'), 'a') as f:
      pass

  def add(self, key, volume):
    self.check(key)
    self.check(volume)
    new_add = (key + ' ' + volume + '\n')
    with open((self.name + '.pydb'), 'a') as f:
      f.writelines(new_add)

  def check(self, vol):
    a = vol.split()
    if len(a) != 1:
      print('Error')
    print(a)


test = Pydb("test")
test.add('Привет', 'мир')
