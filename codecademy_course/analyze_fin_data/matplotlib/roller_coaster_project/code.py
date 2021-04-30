import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wood.head())
print(steel.head())

# write function to plot rankings over time for 1 roller coaster here:
def rank_one(name, park, material):
  if material == "wood":
    coaster_data = wood[(wood['Name'] == name) & (wood['Park'] == park)] 
  elif material == "steel":
    coaster_data = steel[(steel['Name'] == name) & (steel['Park'] == park)]
  else: 
    print("Error en material, solo se puede 'wood' o 'steel'")
  x = coaster_data['Year of Rank']
  y = coaster_data['Rank']
  plt.plot(range(len(x)), y, marker = "o", linewidth = 2, color = "red")
  ax = plt.subplot()
  ax.set_xticks(range(len(x)))
  ax.set_xticklabels(x)
  plt.ylabel('Rank')
  plt.xlabel('Year of Rank')
  plt.legend([name], loc = 1)
  plt.title("Ranking for " + name + " Over Time")
  plt.show()

el_toro = rank_one('El Toro', 'Six Flags Great Adventure', 'wood')
print(el_toro)

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def rank_two(name1, name2, park1, park2):
  dfwood1 = wood[(wood['Name'] == name1) & (wood['Park'] == park1)]
  dfwood2 = wood[(wood['Name'] == name2) & (wood['Park'] == park2)]
  ay= plt.subplot()
  plt.plot(dfwood1['Year of Rank'], dfwood1['Rank'])
  plt.plot(dfwood2['Year of Rank'], dfwood2['Rank'])
  plt.ylabel('Rank')
  plt.xlabel('Year')
  plt.legend([name1, name2], loc = 1)
  ay.set_yticks([1, 2, 3, 4])
  plt.title("Ranking for " + name1 + ' & ' + name2 + " Over Time")

  plt.show()

el_toro_vs_boulder_dash = rank_two('El Toro', 'Boulder Dash', 'Six Flags Great Adventure', 'Lake Compounce')
print(el_toro_vs_boulder_dash)

plt.clf()

# write function to plot top n rankings over time here:
def plot_top_n(material, n):
  top_n_rankings = material[material['Rank'] <= n]
  # fig, ax = plt.subplots(figsize=(10,10))
  for one_roller_coaster_name in set(top_n_rankings['Name']):
      one_roller_coaster_datas = top_n_rankings[top_n_rankings['Name'] == one_roller_coaster_name]
      plt.plot(one_roller_coaster_datas['Year of Rank'], one_roller_coaster_datas['Rank'], marker = "o", label = one_roller_coaster_name)
  plt.legend()
  plt.title("Top " + str(n) + " Roller Coasters' Rankings")
  plt.xlabel("Year of Rank")
  plt.ylabel("Rankings")
  plt.show()

top_5 = plot_top_n(wood, 5)
print(top_5)

plt.clf()

# load roller coaster data here:
roller_coasters = pd.read_csv("roller_coasters.csv")
print(roller_coasters.head())

# write function to plot histogram of column values here:
def hist_roller(df, column):
  plt.hist(df[column], range=(2, 10), bins=len(column), normed=True)
  plt.xlabel(column.upper())
  plt.ylabel('Number of Roller Coasters')
  plt.title("The Distribution of " + column + " for Roller Coasters")
  plt.show()

speed = hist_roller(roller_coasters,'speed')
print(speed)

plt.clf()

# write function to plot inversions by coaster at a park here:
def bar_park(df, park):
  park_df = df[df['park'] == park]
  roller_coaster = park_df['name']
  inversions = park_df['num_inversions']
  ax = plt.subplot()
  ay = plt.subplot()
  plt.bar(range(len(roller_coaster)), inversions)
  ax.set_xticks(range(len(roller_coaster)))
  ax.set_xticklabels(roller_coaster)
  plt.xticks(rotation=45)
  plt.legend([park])
  plt.title("Number of Inversions for each Roller Coaster")
  plt.xlabel("Roller Coaster Name")
  plt.ylabel("Number of Inversions")
  plt.show()

park_asterix = bar_park(roller_coasters, "Parc Asterix")
print(park_asterix)

plt.clf()
    
# write function to plot pie chart of operating status here:
def operating_vs_close(df):
  operating = df[df.status == "status.operating"]
  closed = df[df.status == "status.closed.definitely"]
  
  number_of_operating = len(operating)
  number_of_closed = len(closed)
  plt.pie([number_of_operating, number_of_closed], autopct = "%1d%%")
  plt.axis("equal")
  plt.title("Current Running Condition for Roller Coasters")
  plt.legend(["Operating", "Closed Definitely"])
  plt.show()

status = operating_vs_close(roller_coasters)  
print(status)

plt.clf()
  
# write function to create scatter plot of any two numeric columns here:
def scatter_two_rollers(df, column1, column2):
  data_column1 = df[column1]
  data_column2 = df[column2]
  plt.scatter(data_column1, data_column2)
  plt.title("Relationship between " + column1 + " and " + column2)
  plt.xlabel(column1)
  plt.ylabel(column2)
  plt.show()

scatter_status_speed = scatter_two_rollers(roller_coasters, "heigth", "speed")
print(scatter_status_speed)

plt.clf()