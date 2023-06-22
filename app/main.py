import modules2
import readcsv 
import charts

def run():
   data = readcsv.read_csv('./data.csv')
   data = list(filter(lambda item : item['Continent'] == 'South America',data))
   countries = list(map(lambda x: x['Country/Territory'], data))
   percentages = list(map(lambda x: x['World Population Percentage'], data))
   charts.generate_pie_chart(countries, percentages)
   country=input('Digite el pais=>')
   result = modules2.population_by_country(data,country)
   if len(result) > 0:
     country=result[0]
     print(country['Country/Territory'])
     labels, values = modules2.get_population(country)
     #labels1=list(labels)
     #values1=list(values)
     charts.generate_bar_char('Colombia',labels, values)
   
  
     

     
if __name__== '__main__':
  run()
    
   
 

    