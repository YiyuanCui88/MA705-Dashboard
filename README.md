# MA705 Final Project

This repository contains files used in the MA705 dashboard project.

Use Markdown to write your readme.md file.  Here is a [cheatsheet](https://www.markdownguide.org/cheat-sheet/).

The final dashboard is deployed on Heroku [here](https://ma705bostonuniversities.herokuapp.com).

## Dashboard Description

In this project, I’m interested in seeing the rental market of several selected areas (zip codes) in Massachusetts. The rental market has been going through quite a lot of changes since covid break, and different cities and areas may have different trends due to the remote working and lock down during in the past. These five different zip codes are associated with different cities covering from the east to the west of Massachusetts. 


This dashboard shows the total rentals in different cities and years, and average price of rentals in each month, and the top ten average rental price in combination with the corresponding population and household income in different format. By using three different filters, the users can easily check out the rental market of homes with different number of bedrooms in different cities and years, and have a good understanding of the rental market since the covid break. 



### Data Sources

Brief description of where/how you got the data and how it was processed.

Firstly, through Realty Mole Property on Rapid API [here](https://rapidapi.com/realtymole/api/realty-mole-property-api), I obtained the rental data of five different zip codes from five different cities through API requests. Additional data of the selected zip codes, including population and median household income were obtained through Massachusetts Demographics by Cubit [here](https://www.massachusetts-demographics.com/). The five API request.py files have been saved in ‘Data_Collection_API’ folder.

Secondly, I processed the .json data of each city obtained through API to data frame which were saved into .csv files. Then, I did data wrangling to integrate the data file of these five cities into one MasterFile. The five city csv files and wrangling.py file have been saved in ‘Data_Wrangling’ folder.

Lastly, I used the MaterFile as the data frame to create the interactive dashboard. 



### Other Comments

Anything you'd like to add
