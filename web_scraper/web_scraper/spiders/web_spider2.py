# to run
# scrapy crawl web_spider2 -o results.csv

# To view html response
# scrapy shell (url)

import scrapy
class WebSpider(scrapy.Spider):
    
    # Name of spider
    name = 'web_spider2'

    # Starting point: Jumanji (2019) imdb url
    start_urls = ['https://www.imdb.com/title/tt7975244/']

    def parse(self, response):
        """
        This parse method starts on the home page of a movie's imdb page
        and then navigates to the cast and crew page and runs the parse_full_credits method

        """

        # Find the cast and crew page
        next_page = response.css("li.ipc-inline-list__item a")[2].attrib["href"]

        # If the cast and crew page exists, update the url, and move to it
        if next_page:
            next_page = response.urljoin(next_page) # Update url
            yield scrapy.Request(next_page, callback = self.parse_full_credits) # Move to page and run parse_full_credits

    def parse_full_credits(self, response):
        """
        This parse method starts on the cast and crew page and yields a scrapy.Request 
        for every actor listed on the page. Only includes cast members.
        """

        # Iterate through table of actors
        for i in range(len(response.css("table.cast_list td:not([class]) a"))):
            cast_page = response.css("table.cast_list td:not([class]) a")[i].attrib["href"] # Get cast member id
            cast_page = response.url.rsplit("/", 4)[0] + cast_page # Update url for each cast member
            yield scrapy.Request(cast_page, callback = self.parse_actor_page) # Move to cast member page and run parse_actor_page

    def parse_actor_page(self, response):
        """ 
        This parse method starts on the page of an actor and extracts all of the projects 
        that the actor has worked on. Then it yields a dictionary of the actor and the project title.
        """
        
         # Iterate through all of the projects
        for project in response.css("div.filmo-category-section")[0].css("div.filmo-row"):
            # If any of the projects are Video Games we skip
            if any("Video Game" in x for x in project.css("*::text").extract()):
                pass 
            else:
                actor_name = response.css("span.itemprop::text").get() # Get actor name
                movie_or_TV_name = project.css("b a::text").get() # Get project title

                # Yield results in a dictionary
                yield {
                    "actor" : actor_name,
                    "movie_or_TV_name" : movie_or_TV_name
                }

