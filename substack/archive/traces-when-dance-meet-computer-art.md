---
title: "Traces: When dance meet computer art."
pubDate: 2024-04-10
link: https://jbarbeau.substack.com/p/traces-when-dance-meet-computer-art
slug: traces-when-dance-meet-computer-art
---

I'm going to try to make this one a lot shorter than the other one. Let's see if I manage to do it or not.

Back in May of last year, I got contacted by Philipp Contag-Lada about a project that would incorporate collaboration between computer art and dance. The project was funded by the German federal government commissioner for culture and the media and it was such a wild idea that I could not say no to this.

I was also super fortunate to be a part of this project with other amazing artist like Moodsoup, Arwan Beetooh, Danica Schlosser and Philipp Contag-Lada himself.

## How does it work?

Philip and the Interface project has developed a way to motion capture dance choreographies. The data captured from this would then be outputted into a very large json file that would store all the movement of all the limbs of the human body, 30 times per second(30fps) for the duration of the dance sequence. As artist, we could then use this data to interpret it visually through computer art.

The Interfaces team had already setup a live server on their website with a couple of example. This was real helpful for me to get my bearings with the data provided. In the above picture, each circle represent a joint and each line represent a "bone". Starting from this I could really start having fun and find way to visually interpret dance movement.

## The secrect ingredient

Around the same time that I started working on the project, I ordered a small MIDI controller from Intech called the "Grid". 

Using the grid, I mapped the four knobs on the top row to the particles width, hue, saturation and brightness respectively.

Then I divided the choreography's length (total number of frames) by four and attributed each forth to it's respective slider.

The buttons on the bottom row we're mapped to utility functions:

- Deleting the particle (but keeping what was drawn)

- Clearing the canvas completely 

- Switching theme (bright or dark)

- Changing the perlin noise octaves

That way, I could effectively scrub through the coreography without having to find the perfect frame number. Also I could incorporate movement into the output and I think this is real important since the main subjects are dancers.

How it works is that each joint from the dancers act as an origin cluster node for the particles. So when I unleash them using the midi controller, they start from there and then they spread out. That way I could keep the silhouette in the composition and I think it really helps to tell a story.

Here's a really good example where you can see the particle starting point and the silhouette.

## The Collection

After playing with the Algorithm, I was able to get very satisfying artwork and sent them to 7pc so they can work on the exhibition. 

Here's the two chosen artwork for that first exhibit.

## The first exhibit

The Interface project was exhibited at the Hanover Opera House in Germany during the last week of march 2024. It's the first exhibit for the project and I'm sure it won't be the last. It's such an amazing experience to see our work displayed in such a beautiful setting. 

Here's a short video from Philipp that explains a bit more about the project and the exhibition: 

The complete Traces collection which includes a total of seven artwork is available to collect on OBJKT here : [https://objkt.com/collections/KT1Tw7BRpsMomGE4bf3bxjAc4AgNV8xq7BYb](https://objkt.com/collections/KT1Tw7BRpsMomGE4bf3bxjAc4AgNV8xq7BYb)

## What's next?

While the Traces collection of the Interface project is done. My contribution to the project isn't. I've been working more and more with the intech grid and it's a lot of fun. 

I have programmed different ID to each page of the controller. so when I click the utility button (hidden on the side) it changes page which make the grid like a totally different controller. There is 4 page total, so it means that I can map a total of 48 functions to that little machine. That's amazing.

I also have been working with rotation and different noise scale and particle displacement techniques. Here's a sneek peak of the the state of my research.

## DANCE OFF!

Well that's it! I hope you liked it and it wasn't a drag to read. I know I said it'd be shorter but it's a hard thing to respect lol. Next time will be a shorter one, I promise!

In the meantime, have a nice rest of the week and see you soon!
