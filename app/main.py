import modules2
import readcsv 
import charts
import pandas as pd
def run():
  
  #sin pandas
  '''
   data = readcsv.read_csv('./data.csv')
   data = list(filter(lambda item : item['Continent'] == 'South America',data))
   countries = list(map(lambda x: x['Country/Territory'], data))
   percentages = list(map(lambda x: x['World Population Percentage'], data))
   charts.generate_pie_chart(countries, percentages)
   '''
   #Con Pandas 
  df = pd.read_csv('data.csv')
  df =df[df['Continent'] == 'Africa']
   
  countries=df['Country/Territory'].values
  percentages=df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)
  
  data = readcsv.read_csv('./data.csv')
  country=input('Digite el pais=>')
  result = modules2.population_by_country(data,country)
  
  if len(result) > 0:
     country=result[0]
     pais=country['Country/Territory']
     labels, values = modules2.get_population(country)
     #labels1=list(labels)
     #values1=list(values)
     charts.generate_bar_char(pais,labels, values)
  
  
     

     
if __name__== '__main__':
  run()
    
   
 

    