Title:  Casseville Checkers
date: 2025-12-24
Slug: cassville-checkers
Category: Blog 
Tags:  website, python, machine learning
Authors: Kyle Cranmer



 <div >
 <img src="{filename}/images/casseville-checkers.jpeg" alt="Cassville checkers board" width="35%"  style="float: right;"/>

Cassville Checkers is a marble racing board game that has been played by my wife's family for generations. The game is played on a handmade wooden board with a distinctive ring track. Marbles race around a circular track, competing to be the first to get all their pieces home.

I've wanted to try coding up this game in a reinforcement learning environment for a lont time. I started to do this back in 2018, but I didn't make it very far and it was never a high priority. 

But recently, a friend of mine (Sidharth Mishra-Sharma) encouraged me to try using claude code (from Anthropic). This is an advanced agentic AI coding tool. I used this project as a test case, and I was very impressed. 

 </div><br />

<br clear="all" />

 Not only did claude code create the RL environment, I also had it build a web user interface to play the game and help me debug it. I also had it write some benchmarking scripts to analyze the game and write it all up in a reproducible way using MyST:

 * [Project on GitHub](https://github.com/cranmer/cassville-checkers)
 * [A report analyzing different strategies for playing the game](https://theoryandpractice.org/cassville-checkers/)

<div>
<img src="{filename}/images/casseville_checkers_UI_screenshot.png" alt="Cassville checkers board" width="90%" style="display: block; margin: auto;" />
<div style="text-align: center; font-style: italic;">A screenshot of the  the Cassville checkers web version.</div>
</div>
