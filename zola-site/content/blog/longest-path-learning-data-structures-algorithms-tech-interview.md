+++
title = "Longest Path into Learning Data Structures and Algorithms for the Tech Interview"
date = "2020-06-27"
description = "A nontraditional software developer's path through bootcamp, Princeton, and MIT courses to build the algorithms foundation needed for technical interviews."
template = "blog-post.html"
[taxonomies]
categories = ["Field Notes"]
tags = ["algorithms", "data-structures", "technical-interviews", "education", "nontraditional-careers"]
[extra]
editorial_track = "field-notes"
+++

_This was originally published on 2020-06-27._

I am a nontraditional software developer. I do not have a Computer Science (CS)
degree. Instead, I opted to get a Software Engineering degree. It is interesting
that in our industry, most people who have CS degrees do not call themselves
computer scientists. Instead, they call themselves engineers. From what I can
tell, most Software Engineering jobs do not require hardcore CS skills, yet most
companies still interview software engineers for core CS skills.

The game is this: if you want a job at Google or Facebook, you need to learn
core algorithms and data structures. Most bootcamps teach some data structures
and algorithms, but most bootcamps do not spend enough time on these core areas.

## My First Attempts

At first, I tried following along with Udacity's [Data Structures and Algorithms
in Python][udacity] course. I found the content entertaining and engaging, but
not deep enough. At my bootcamp, we covered all the same content in a very
similar fashion, but I found myself feeling unready when I started doing mock
interviews.

About that time, I found the following Princeton courses:

- [Algorithms, Part I][princeton-part-1]
- [Algorithms, Part II][princeton-part-2]

I started with Part I, which really helped me reinforce some of my previous
knowledge. These courses are based on Java instead of Python, but that was not a
big deal. The main issue for me was that I could not get some of the code
running locally in a reasonable amount of time.

I finished the first course and some of the second. I stopped because I felt as
if I was missing a lot of information. The lectures focused on proofs and
understanding the complexity of the algorithms. There was too much jargon I had
to look up to follow along. Things like "induction" at this stage made me feel
that I needed to go study some alien math. I love math, by the way.

So far, I felt as if I could not learn this information by myself. There were
knowledge obstacles that I kept finding. It was like hitting an invisible wall
or force field. I felt as if I could not steal the fire from the gods.

Around this time, I learned about the book [_Cracking the Coding
Interview_][cracking]. I looked at this book, read some of the first chapters,
and decided that it was not for me. The book is geared toward traditional
software engineers. The only thing I gathered from the first chapter was that
this stuff is hard since even software engineers need a self-help book.

Surprisingly, the fact that the data structures and algorithms I needed to learn
to pass a technical interview were not easy made me feel better. All this time,
I thought I was trying to climb a wall with zero tools.

## The MIT Turning Point

I was about ready to give up. While searching YouTube for algorithm tutorials, I
found a random video about [dynamic programming from MIT's 6.006
course][mit-dynamic-programming].

"Oh, cool. This is a lecture about dynamic programming from MIT," I thought to
myself. "I am probably not going to understand anything being discussed, so I
might as well watch it to see how it feels to be in an MIT lecture."

I felt that I was going to watch something akin to a nuclear fusion lecture. I
had seen lectures like this pop up from other institutions, but I always
underestimated how much of the content I could absorb. I watched the lecture
and, to my surprise, I understood everything about it. And there were three more
lectures about dynamic programming! This was a turning point for me.

I started watching the [whole MIT 6.006 Introduction to Algorithms
class][mit-6-006] from the beginning. I had a physical notebook with me to
simulate sitting in the classroom, and I did the problems by hand.

I knew about sorting algorithms, but I had never heard about counting sort
(which can sort numbers in linear time). I learned about polynomial time and
non-polynomial time. I finally understood what people meant by P = NP and why
some do not agree. I learned what DAG means (directed acyclic graph) and which
algorithms to use with them.

I wondered how much more I could have learned by then if I had started with this
course. I also wondered how much my previous exposure had actually prepared me
for the course. Is this the curse of knowledge?

The advantage of a classroom setting is that instructors assume you do not know,
so they explain things from the ground up. This is what I was missing in other
sources. Other sources made small assumptions about things I did not know. If a
topic during a lecture was not clear, I could watch a whole hour of the
recitation portion, which covered some subjects in more detail.

I want to believe that once you know how to do simple programming, taking a
course like MIT 6.006 should not be impossible.

## What to Study for the Interview

Google's interview guidance said:

> Algorithms that are used to solve Google problems include sorting (plus
> searching and binary search), divide-and-conquer, dynamic
> programming/memoization, greediness, recursion, or algorithms linked to a
> specific data structure. Know Big-O notations (for example, run time) and be
> ready to discuss complex algorithms like Dijkstra and A\*.
>
> Think about what efficiency means in terms of runtime and space used. For
> example, in exceptional cases insertion sort or radix sort are much better
> than the generic QuickSort/MergeSort/HeapSort answers.
>
> Data structures most frequently used are arrays, linked lists, stacks, queues,
> hash sets, hash maps, hash tables, dictionaries, trees and binary trees,
> heaps, and graphs. You should know the data structure inside out, and what
> algorithms tend to go along with each data structure.

Source: [Google's software engineering and technical interview
guidance][google-interviews].

Everything Google listed above is what you would learn in a college-level
introduction to data structures and algorithms class like [MIT 6.006
Introduction to Algorithms][mit-6-006] (and, to be safe, probably some selected
topics from a design and analysis of algorithms class like [MIT
6.046J][mit-6-046j]).

If you are a nontraditional developer like me, you probably need to "take" the
classes above. Do not just watch the lectures or recitations. Do the problems by
hand. When I say by hand, I mean do the problem on a board or in a notebook.
Doing the problems on a whiteboard, blackboard, or notebook will help you with
the technical interview, which is mostly based on the contents of these classes.

If you are between jobs, you could probably do them in a few weeks. I would
suggest taking your time to absorb the topics.

Happy coding!

[cracking]: https://www.crackingthecodinginterview.com/
[google-interviews]:
  https://www.google.com/about/careers/applications/
[mit-6-006]:
  https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
[mit-6-046j]:
  https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/
[mit-dynamic-programming]: https://www.youtube.com/watch?v=OQ5jsbhAv_M
[princeton-part-1]: https://www.coursera.org/learn/algorithms-part1
[princeton-part-2]: https://www.coursera.org/learn/algorithms-part2
[udacity]:
  https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513
