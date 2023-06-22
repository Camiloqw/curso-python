
import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig('pie1.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie2.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)


def generate_bar_char(name,labels,values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f'./img/{name}.png')
  plt.close()
'''
if __name__=='__main__':
  labels = ['a','b', 'c']
  values = [100,50,110]
  generate_bar_char(labels,values)

  '''