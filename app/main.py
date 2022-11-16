# %%
import utils
import read_csv
import charts
import pandas as pd

def run():
    ''' se cambia codigo para usar pandas
    data_filtered = list(filter(lambda item :item["Continent"] == 'South America',data)).copy()
    countries = list(map(lambda x : x ['Country/Territory'],data_filtered))
    percentages = list(map(lambda x : x ['World Population Percentage'],data_filtered))
    '''
    df = pd.read_csv('data.csv')
    df = df[df['Continent']== 'Africa']

    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries,percentages)

    data = read_csv.read_csv('./data.csv')
    country = input('Type the country =>').title()
    resul = utils.population_by_country(data,country)

    if len(resul) > 0:
        country = resul[0]
        labels, values = utils.get_population(country)
        # print(labels, values)
        charts.generate_bar_chart(country['Country/Territory'],labels,values)


if __name__ == '__main__':
    run()

# %%
