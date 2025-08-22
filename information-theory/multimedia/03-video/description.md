# Video Compression

We've discussed audio, let's now turn our attention to video.
In order to determine how much storage video requires, we must first find out how video is represented digitally.

## What's a Video

A video is actually nothing more than a quick succession of images.
How many images per second are actually used varies a lot: for movies this tends to be 24, which is more or less the minimum
if we want to perceive it as a movie and not as a slideshow.
Higher frame rates make for a smoother experience: gamers expect 60fps, but prefer 144fps, and professional esports players go up to 240fps or even higher.

## Single Frame

Now we need to know how to digitize a single image.
This is achieved by putting a `W`&times;`H` grid over the image.
For each square (*pixel*) in this grid, we must pick a single color.

Consider this image:

![Blade Runner](br.jpg)

If we put a grid over this image of approximately 50x30 pixels, we get

![Blade Runner](br2.jpg)

We can see that some detail appears to have been lost during the digitization process.
Luckily we can increment the number of pixels, which will lead to a sharper result:

![Blade Runner](br5.jpg)

The number of squares in the grid is called the *resolution*.
The higher the resolution, the smaller the pixels, the better the image quality.

So, given a resolution of `W` by `H` pixels, we have `W`&times;`H` pixels (colors) to store per image.
How much a single pixel takes was discussed in a previous challenge.

## Compression

Let's actually calculate how large a 2 hour movie would be.
We assume the following:

* Its frame rate is 24fps.
* The movie has a resolution of 1920x1080.
* Colors are represented using 24 bits.

Putting all of this together gives us a total of around 1000 GiB.
In other words, it would take 142 MiB per second (not considering audio).
Imagine if you would need that much bandwidth to watch a movie online.

Luckily, compression helps us out again and reduces the storage requirements dramatically.
We don't delve into this, as this would be a course of its own (and involves *lots* of complex maths).

## Question

Let's find out how much storage compression saves.
When using the Netflix app on PC, you can press CTRL+ALT+SHIFT+D to view some technical information.
We started watching a Sandman episode and got

```text
...
Playing bitrate (a/v): 128 / 3502 (1920x1080)
...
Framerate: 23.976
...
```

Using this information:

* Resolution 1920 x 1080
* 24 bits per pixel
* 23.976 fps
* 3502 kibibits per second for Netflix's video stream

How many times smaller does Netflix's compression make the video?
