# Reflection Blog Post 

**Note: Renzo and Zach did the reflection blog post together.**

## *Overall, what did you achieve in your project?*

We made a recommendation engine based on network analysis using a multitude of Python libraries into the framework of a seamless website. We also achieved a goal in learning how to conduct network analysis and understand networks more than we did at the start of the quarter/project.


## *What are two aspects of your project that you are especially proud of?*

Two things that we're both especially proud of include the functionality/UI of our website, as well as the pretty centrality-based network visualizations we made.

For the website interface, we're proud that the user is able to interact with the website and not stick with a static website. The drop-down menu and slider from the *Dash* callbacks in our website were, in our opinion, quite **nice**.

For our network visualizations, we're proud in how we were able to glean some mathematical insight from the data we had. We also think that, combined with the *Dash* callbacks, we were able to make visualizations that were actually interpretable and useful for the recommendation engine.

## What are **two** things you would suggest doing to further improve your project?*

Two things we would like to improve on are the recommendation algorithm and the user inputs forr our recommendation algorithm.

First, using a propensity score like we discussed would provide better results, as we could use multimodal, data-integrated approaches by including data from other resources and creating a score. Doing this would allow us to find which shows had the smallest Euclidean distance between the score based on the user's inputs and give out better recommendations rather than just a naive network-based system.

Next, we would like to incorporate more user interaction besides just the drop-down menu and slider. Getting information from users, like what genre, year, and a link to the show they wanted to use as its show of reference would make it more custom for the user.


## How does what you achieved compare to what you set out to do in your proposal? (if you didn't complete everything in your proposal, that's fine!)

Initially, we sought to implement a cutting edge clustering algorithm and then to use it on a simulation study and present a Python package.

Clearly, our final project is just a *tad* bit different, being a more applied project with centrality-based "clustering." This occurred when we pivoted away from the Amazon Reviews dataset that we initially wanted to use. Instead, we created a more user-oriented project that hosts a website and network visualizations to help recommend media to the user.

## *What are three things you learned from the experience of completing your project? Data analysis techniques? Python packages? Git + GitHub? Etc?*
1. We learned how to use *NetworkX* and how to conduct basic network analysis in Python (as well as data manipulation with different types of graphs). (NetworkX)
2. We learned how to use Dash to integate attractive data visualization into a website. (Dash, flask)
3. Finally, we learned the importance of having good data. Our data, as explained in the presentation, was a 2xN matrix with mutually exclusive values (column-wise), meaning we couldn't do as much clustering analysis because we were limited to what our basic network statistics gave us. The mutual exclusion of column-wise values effectively made the connections between nodes clearly sparse, which gave us probems.

## *How will your experience completing this project will help you in your future studies or career? Please be as specific as possible.*
**Renzo:**
This project has taught me a tremendous amount about how to effectively collaborate on a technical project. Understanding git was essential to navigating collaboration, and this project taught me how to navigate git as well as the importance of being meticulous and organizing code properly. Following graduation I will be working as a management consultant, specifically aligned to an analytical team, so I believe the experiences learned from this project will help me in my career. I thoroughly enjoyed my experiences working on this project and hope to continue using Python throughout my career!


**Zach:**
Personally, this helped me understand just how difficult even "basic" network analysis is. My experiences from UM this summer with networks was a more statistical approach that helped me understand summary statistics, but I still lacked the ability to expertly apply current algorithms in use for clustering analysis, as well as fail to recognize early on the limitations of our data. Even with this, it has still helped me understand that I have a lot to learn in network-linked data. Despite being difficult, I am still very excited for the opportunity to conduct research with such data (and hopefully more complex) in my journey in higher education! Hopefully, I can take what I learned from this project as a graduate researcher and apply the lessons that I've learned, as well as the experience I now have with Python libraries involving network analysis.


## Special Thanks

Lastly, we'd like to thank Professor Phil Chodrow for being such an amazing professor this quarter. He was extremely supportive and insightful in giving us direction in both the projects and other assignments. We both thoroughly enjoyed going to lecture everyday, and we hope to have the privilege to take another class with him before we graduate.

*- Team Karasuno*

