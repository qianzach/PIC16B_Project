# Network Analysis Recommendation Engine
By: Renzo Tanaka-Wong and Zach Qian
<br>
<img src="television.png" alt="logo" heeight=100% width=100%/>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#About-The-Project">About The Project</a>
      <ul>
        <li><a href="#Motivation">Motivation</a></li>
        <li><a href="#Built-With">Built With</a></li>
        <li><a href="#Components">Components</a></li>
        <ul>
          <li><a href="#Webscraper">Webscraper</a></li>
          <li><a href="#Dashboard">Dashboard</a></li>
      </ul>
      </ul>
    </li>
    <li><a href="#Local-Installation-Guide">Local Installation Guide</a></li>
    <li><a href="#Ethics">Ethics</a></li>
    <li><a href="#Limitations">Limitations</a></li>
    <li><a href="#References">References</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
If you have ever wondered what other shows the actors from your favorite TV show or movie also appear in, look no further!
This project is a TV Show/Movie/Anime/(you name it) recommendation engine powered by network analysis, which provides recommendations based on the number of shared actors of a particular TV show, movie, or anime.

### Motivation
-- Insert description -- 

### Built With
* [Scrapy](https://scrapy.org/):
Scrapy is a free and open-source web-crawling framework written in Python. We used Scrapy to scrape web data and create our network data. 
* [Flask](https://flask.palletsprojects.com/en/2.0.x/):
Flask is a Python package used for web development. We used Flask to develop the server for our website as well as to integrate certain navigation components of our website.
* [NetworkX](https://networkx.org/):
NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. We used NetworkX to construct and analyze the complex relationships between actors and their projects.
* [Plotly](https://plotly.com/):
Plotly is a python library for complex, dynamic, and interactive data visualization. We used plotly to visualize our network graphs. 
* [Dash](https://plotly.com/dash/):
Dash is a Python framework for creating interactive web applications. We used Dash to integrate flask and plotly to make a dynamic dashboard. 

### Components
There are two main components to this project:

#### Webscraper
Using Scrapy, we created two webscrapers for finding shared actors on IMDb. The first scraper is designed for scraping anime data, and the second scraper is designed for all other TV shows and movies. Both scrapers starts on the IMDb page of a selected show, movie, or anime. Then they navigates to the Cast & Crew page and iterate through the cast members. The anime scraper then specifically searches for the origin of each actor (as there are both English-speaking and Japanese-speaking voice actors) and finds those that are from Japan. Then for each of these actors, it extracts a complete list of the projects they are a part of, excluding video games. The second scraper similary extracts the data, but it does not search for the origin of the actors. Both scrapers then reuturn the data as a csv file.

#### Dash Board
After scraping our datasets, we built an interactive dashboard using Scrapy and Dash that allows users to interact with the different datasets and explore the complex networked relationships between actors and their shared projects. The dashboard has two interactive elements: a dropdown menu to select the project and a slider to customize the nodes. After the user selects a project and slides the slider ot a specified integer value, the plot updates for the user specifications through a comprehensive function found in functions.py. The function instantiates a graph, constructs nodes and edges from the data of the selected project, and omits nodes that have degrees less than the specificed number of connections. The output is a plotly graph, with recommendations color coded by degree strength. 

<!-- INSTALLATION GUIDE -->
## Local Installation Guide
To install and run the application locally: 
1. Clone the repo
   ```sh
   $ git clone https://github.com/qianzach/PIC16B_Project.git
   ```
2. Install packages  
   ```sh
   $ pip install -r requirements.txt
   ```
3. Activate environment
   ```sh
   $ conda activate PIC16B
   ```
4. Navigate to directory and run application
   ```sh
   $ cd PIC16B_Project
   $ python run.py
   ```
5. Open the following address in a web browser
   ```sh
   http://127.0.0.1:8050/
   ```



<!-- ETHICS -->
## Ethics 
-- Insert Description --

<!-- LIMITATIONS -->
## Limitations
-- Insert Description --

<!-- REFERENCES -->
## References
-- Insert Description --