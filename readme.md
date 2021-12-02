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
    <li><a href="#Discussion">Discussion</a></li>
    <li><a href="#References">References</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
If you have ever wondered what other shows the actors from your favorite TV show or movie also appear in, look no further!
This project is a TV Show/Movie/Anime/(you name it) recommendation engine powered by network analysis, which provides recommendations based on the number of shared actors of a particular TV show, movie, or anime.

### Motivation
Since the beginning of the project, we knew we wanted to work with some type of network-linked data. However, networks and graphs are extremely diverse in data science, mathematics, and computer science. Thus, we initially began with the [amazon reviews dataset](https://www.cs.cornell.edu/~arb/data/amazon-reviews/). As the quarter progressed, Team Karasuno wanted to tailor a capstone project to Asian culture, specifically Japanese culture. As both members of Team Karasuno identify with the AAPI community, we wanted to work on a project that not only represented our interests but also something that represented something in our culture, being anime. Anime is a Japanese film or TV show, and both members have fond memories of shows, such as *Naruto*, *Death Note*, *Demon Slayer*, and *Black Clover*. Because of this, we decided to think about how we could better recommend new anime-watchers using a given anime show and networks. Specifically, we used the forever-popular show, *Naruto: Shippuden* as our basis. Having watched this show in the Japanese version with English subtitles, we used the empirical observation that both of us enjoyed watching shows that had voice actors coming from other shows. Therefore, we based our recommendation system to select shows that had the most mutual voice actors in the show.

Through this inspiration, we wanted to work on an anime recommendation engine purely based on networks. However, it is important to note that this system can be replicated using other shows not limited to anime. We explore this as well in our project, leading to a generalized recommendation engine for shows and movies from all countries.


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
Using Scrapy, we created two webscrapers for finding shared actors on IMDb. The first scraper is designed for scraping anime data, and the second scraper is designed for all other TV shows and movies. Both scrapers start on the IMDb page of a selected show, movie, or anime. Then they navigate to the Cast & Crew page and iterate through the list of cast members. The anime scraper then specifically searches for the origin of each actor (as there are both English-speaking and Japanese-speaking voice actors) and finds those that are from Japan. Then for each of these actors, it extracts a complete list of the projects they are a part of, excluding video games. The second scraper similary extracts the data, but it does not search for the origin of the actors, and is used for all other TV shows and movies. Both scrapers then reuturn the data as a csv file.

#### Dash Board
After scraping our datasets, we built an interactive dashboard using Flaks, Plotly, and Dash that allows users to interact with the different datasets and explore the complex networked relationships between actors and their shared projects. The dashboard has two interactive elements: a dropdown menu to select the project and a slider to customize the nodes. After the user selects a project and slides the slider to a specified integer value, the plot updates to refelct the user specifications through a function found in functions.py. The function instantiates a graph, constructs nodes and edges from the data of the selected project, and omits nodes that have degrees less than the specificed number of connections. The output is a plotly graph, with recommendations color coded by degree strength. 

<!-- INSTALLATION GUIDE -->
## Local Installation Guide
To install and run the application locally: 
1. Clone the repo
   ```sh
   $ git clone https://github.com/qianzach/PIC16B_Project.git
   ```
2. Create environment
   ```sh
   $ conda create --PIC16B <env> --file requirements.txt
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
Although we see no ethical issues for our project, we want to recognize and emphasize that network analyses similar to our project can still be ethically harmful. In social network analysis (SNR), it is very much possible to violate ethical standards. In [Carl Kadushin's *Who benefits from network analysis: ethics of social network research*](https://doi.org/10.1016/j.socnet.2005.01.005), it becomes evident that basic data collection, such as demographic information on patients and study subjects can lead to not only spurious connections, but is a potential issue in data leak, as well as confidentiality. Another example would include military interrogation through connecting mutual suspects/subjects of interests in warfare, which can use similar models as our project.

We see that although not directly having ethical concerns, the applications of our analysis can still raise concerns.

<!-- LIMITATIONS -->
## Limitations
In our project, there exists two primary limitations, namely in data and the selection schema.

First, since our data is purely based off matrix of dimension $(2,n)$ with mutually exclusive values, we are unable to perform cluster analysis because the only cluster would trivially be the source nodes in our directed graph. Note that because of this mutual exclusion, directed graphs will yield the same results, as no show will appear in another show, and no voice actor will appear in another voice actor. Thus, we are unable to conduct more intensive computations/network summary statistics, such as local clustering coefficients. This leads to our second issue, as we are *slightly* pigeonholed to using a naive centrality-based recommendation system. 

<!-- DISCUSSION -->
## Discussion
In our project, the first thing we would like to improve would be data collection. In our recommendation system, it would be interesting to approach the model with a multimodal perspective. In particular, we could use the network centrality in combination with basic statistics, such as net revenue, year, etc to recommend shows mathematically. Providing user inputs (preference of type of anime, year, genre, previously watched shows, etc.) would allow us to create some sort of propensity score. After this, we would take the Euclidean distance between the generated value and that of the shows in a given database and return the top 5 recommendataions with the least distance apart. Doing so would alleviate the naivete of our model. 


<!-- REFERENCES -->
## References
For website anatomy: 

- https://dash.plotly.com/basic-callbacks
- https://dash.plotly.com/dash-core-components/slider
- https://www.youtube.com/watch?v=fakRnkw0s9o

For network analysis and visualization:

- https://networkx.org/
- https://plotly.com/python/network-graphs/
