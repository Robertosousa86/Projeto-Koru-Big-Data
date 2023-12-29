from unidecode import unidecode

class DataClear:
  def __init__(self, dataframe,column_name,column_state_name) :
    self.dataframe = dataframe
    self.column_name = column_name
    self.column_state_name = column_state_name

  def count_city_name(self,city_name,state):
    condition = self.dataframe[(self.dataframe[self.column_name] == city_name) & (self.dataframe[self.column_state_name] == state)]

    if not condition.empty:
      total = condition[self.column_name].tolist()
    else:
      return print('Erro ao encontrar a cidade. Verifique os dados.')

    return print(f'Total de cidades com o nome {city_name}:', len(total))
  
  def change_city_name(self,city_name,state_name, new_name):
    condition = (self.dataframe[self.column_name] == city_name) & (self.dataframe[self.column_state_name] == state_name)

    if condition.empty:
        print('Erro ao encontrar a cidade. Verifique os dados.')
    else:
        self.dataframe.loc[condition, self.column_name] = new_name
    
    return print(f'Antigo nome registrado: {city_name}. Novo nome registrado: {new_name}')
  
  def total_accents(self, column_name):
    total_accents = self.dataframe[column_name].str.contains('[^\x00-\x7F]', regex=True)
    
    result = total_accents.sum()
    
    return print(f'Total de palavras que atendem ao padrão: {result}')
    
  
  def cleaning_accents(self, column_name):
    self.dataframe[column_name] = self.dataframe[column_name].apply(unidecode)

    total = self.total_accents(column_name)

    return total