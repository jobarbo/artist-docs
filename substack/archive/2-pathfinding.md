---
title: "#2 - Pathfinding"
pubDate: 2023-03-03
link: https://jbarbeau.substack.com/p/2-pathfinding
slug: 2-pathfinding
---

## Preparation for the journey

If you want updates on my creative journey, don't hesitate to subscribe! All blog posts are free but if you're a collector and really like my stuff, you can subscribe for a small amount. It helps me a lot on my creative journey and you will receive exclusive pre order on future long-form releases and printed collections.

## Getting to base camp

More often than not, when I start a new project, I don't really know what i'll do. Sometimes I will have a very basic idea in the back of my mind or like, a basic set of rules.

I always start with a mostly empty canvas with an ellipse in the center, It's a bit like my own version of Hello World. My current working environment is a modified version of the [FX(hash) webpack boilerplate](https://github.com/fxhash/fxhash-webpack-boilerplate). It's a very basic file system that is made for creating long-form project and publish them on the fx(hash) platform.

I could talk about what longform and shortform is but my friend Dan Catt made a pretty thorough video on his youtube channel a couple of week ago so I will just link it here for those interested: [What is long-form generative art](https://www.youtube.com/watch?v=-rE5tQSVVJs).

So let's get back to pathfinding. My starting canvas would look like that:

Then I would try stuff like moving the circle on the canvas to get my creative brain flowing. For this one, I decided to make a circle packing algorithm.In Generative Art, circle packing is a technique used where circles are packed tightly together within a specific boundary, such as a rectangle or a shape, without overlapping each other. The circles are often randomly sized and placed according to a set of rules determined by the artist.

Here is a basic Circle Packing output

## Getting the lay of the land

Even though it's visually interesting. It's just a visual representation of an algorithm in it's most simple form. I often use such algorithm as a starting basecamp for exploring the neighborhood. 

At this time I was pretty underwhelmed by the time it took to load the whole thing. It loaded in a bit less than 23 seconds, it may seems like nothing but if someone want to see the live render, a 23 second loading screen can be pretty boring. The time it takes is understandable though. The program start by Adding a circle and check if it's colliding with the previous circle. If not, it is displayed. If it's colliding, the current circle is deleted and then drawn elsewhere and the program will verify again, until it finds a place to put it. 

There is a limited number of tries it can go through though. If the number of attempt surpass the threshold, the program will consider that all possible circle have been placed and then complete. This is to prevent infinite loop and crashing the browser.

## Setting Camp

I wanted the optimise the loading or at the very least create the illusion that the whole rendering was faster. I recently learned a trick for that with generator functions*. I use them in a way that give the impression that the rendering of the piece is faster. Instead of generating all the elements of an artwork in a loop and then rendering them (like 10k ellipses with collision detection), you can use a generator function to render the elements one at a time or per batch, which can create the illusion that the artwork is being created in real-time.

For example, you could use a generator function to generate each shape on-the-fly and render it to the canvas before moving on to the next shape or whatever. This can create the impression of a fast, dynamic rendering process that is constantly evolving.

I will talk about generator function a bit more in a following post.

## Foraging for sticks

Once I felt the base was solid, started experimenting with different colors, and trying removing the fill colour and play with strokes. It was okay but nothing that hooked me.

In order to aid in debugging, I decided that the program would draw a line between the current circle and any existing circle it was colliding with. It gave this thing: 

I thought that this had real visual potential so I decided to just remove the circles and focus only on the lines. To give them a sens of tactile depth, I had the idea to render to more lines under each one. One would be blue with a small offset to the right and the other one would be red with a small offset to the left. It gave something pretty interesting.

## Starting a fire

From there, I knew I hade something and tried a bunch of stuff. This section will be example heavy so bear with me :)

Here I tried using the OVERLAY blend mode and it gave this pretty interesting output

Then I tried with different colours and sizes : 

I then decided to put back the circle AND use the blending mode, It gave some cool space type composition that I find really interesting.

## Seeing in the dark

The next day, I had the idea of removing the original ellipses and replacing the lines with a series of ellipses really close to each other.

Next idea i had is that the ellipses that would be closer to the center of each section would be bigger and they would get smaller and smaller the further away they get from the center. I also gave each ellipses the same treatment as the lines, which meant that each small ellipse would also have two other ellipses underneath with small offset. One would be darker and the other one would be lighter.

Now this was something else, I feels 3d and organic. It render an illusion of shadows but it's all a fraud, an optical illusion.

## Surviving and harvesting

My stay in this weird part of the forest is still ongoing, but I have found a plentiful source of creative sustenance. Now I need to exploit it in a sustainable fashion. I already have a couple of nice gems here that I want to share with you all before going back to work.

## To Be Continued

Stay tuned for the follow up on this journey! Thanks everyone for reading, it really matters to me :) Have a great weekend!
