import yaml

class Configure_storer:
  def __init__(self,file_path):
    with open(file_path,'rb') as f:
      self.data = yaml.load(f)
      print('Configure as folllowing:')
      print(self.data)

  def get_data(self):
    return self.data
 
if __name__ == '__main__':
  config = Configure('./config/config.yml')
  

