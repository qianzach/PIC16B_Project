# PIC16B_Project
Fall 2021 Capstone Project for PIC 16B (Advanced Data Science with Python) with Renzo Tanaka-Wong

## Abstract
Network analysis is a discipline of mathematics that is studied to identify relations among social structures through the use of networks and graph theory. For our project, we are broadly interested in exploring network-linked data to explore clustering methods, that is the aggregation of dense groups in our data, building a clustering algorithm to be tested against current clustering methods in practice, as well as exploring advanced visualization techniques to examine the complex relationships in our data. If our project proceeds smoothly, we hope to further explore simulation methods to understand how diseases and other social phenomenons spread throughout populations.
## Planned Deliverables
For our deliverable, we plan on creating an algorithm on our own or implement a bleeding-edge clustering method given network-linked data. Furthermore, we also intend to provide a simulation study alongside the algorithm itself. 
A full success would be successfully implementing our own clustering method or a novel method from literature. A partial success would be to implement multiple well-known clustering methods and provide an exhaustive method analysis of the clustering algorithms (analyzing results and determining which one was better and then understanding how and why mathematically in conjunction with the data we used).

## Resources Required
Several resources will be required in order to complete our project. First, we will need access to network-linked data. We are currently in the process of finding specific datasets that pique our interest from the following [collection of datasets](https://www.cs.cornell.edu/~arb/data/). Secondly, we will require learning materials -  from research papers to online tutorials - in order to learn the ins and outs of network analysis. Through this we hope to learn the mathematical intuition behind network analysis and how it can be directly implemented in Python.
## Tools and Skills Required
Not only will we need to use our skills from PIC 16A and PIC 16B, but we will also need to do additional learning on network science and understanding the mathematics of networks, as our project is directly about network-linked data. In terms of packages, we will use standard numpy and pandas, as well as networkx. If we want to do prediction modeling, I would like to use a deep learning library, such as tensorflow or pytorch. We would also be using some of the skills learned from *Networks: An Introduction* by Newman to learn how to perform network analysis, specifically clustering analysis. 
## What You Will Learn
What we hope to learn from our capstone project is the skills required to perform analysis on network-linked data, as well as learning how to understand networks mathematically and what summary statistics are used and interpreted. It also goes without being said that we will learn how to better use deep learning tools and Python libraries specifically built for network analysis. Lastly, we will learn how to develop algorithms and/or become more knowledgeable on current clustering analysis algorithms in the literature, as well as learn how to implement these methods. Personally, I hope this will enhance my interest in networks, as I would like to conduct applications-based research on networks in biostatistical and statistical settings. 
## Risks
Potential limitations to our project include our limited understanding of network analysis and limitations to our data. The first obstacle we may face is having a limited understanding of network analysis. Since this topic is a foreign topic to our team, we will have to start by developing an understanding of the math and theory behind network links, graphs, and clustering algorithms before implementing our code. Our understanding will thus determine the depth and scope of our project. Another limitation to our project may be our data. Since we are interested in clustering algorithms, we may find that our data lacks the depth and complexity we desire. Additionally if our data has multiple links, we may be looking at a hypergraph problem which will be out of our scope. Thus, carefully sourcing and selecting our data will be essential.
## Ethics
Network analysis is an important topic surrounding social constructs. It helps us understand how populations are partitioned, how communities are formed, and how information spreads. Through this project we hope to create a deliverable that benefits communites that are at-risk or more vulnerable to social phenomenons. For example, while we have not decided on our data, if we proceed with disease data we hope to identify communities that might be harmed by the spread of a disease to help mitigate and prevent its spread. We can also detect certain social behaviors and trends among groups and communities to better understand how they come about and segment them. While there are many positive implications from our project, there are also potential harms that we must address. Clustering will likely favor abundant data, so if our data is lacking in certain areas, there will be potential misinterpretations or incorrect and trivial conclusions. Thus, this project may harm under represented groups. However, overall we believe this project will be useful and important to society since understanding how social groups are partitioned will help us understand what types of groups and communities exist, and understanding how groups are networked and related can be useful for preventing disease spreads.
## Tentative Timeline
In the first two weeks of our project we plan to find our data (either by scraping or using an existing dataset) and will complete exploratory data analysis on it. In the following two weeks we will begin to explore clusters and visualization methods for our linked data. Finally, in the last two weeks we will create and implement a custom clustering algorithm and run simulations on our data. 
