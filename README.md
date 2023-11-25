# Mahjong-Basic-Winning-Hand
An assistant for any mahjong player to check if they have a winning hand

## Problem Statement
People where I live (Singapore) are too busy and can only play mahjong during CNY. Sometimes you forget if your hand is a winning hand and you take the time to look online on winning hands and amount of profits.

Disclaimer: Just for the lols. Will use the Singapore version of mahjong. 

## Solution
A web application that allows you to take a picture/upload your picture and checks if the hand is a winning hand.

## Complexities

### Not all tiles are in hand
Some tiles might be placed shown which might make it more difficult.

A way to solve this is to have 3 separate pictures.

1. Main hand
2. Faced up hand
3. Flowers and Animals

### Photo is Blur
People might be using a toaster to take a picture of their mahjong hand. 

1. If the resolution of their camera is trash, then we will need to fine tune the model that we use to detect the tiles better
2. The picture might cut off some of the hands. Might need to create a bounding box for them to take a picture of their hands in.

### Different types of Mahjong sets
This is gonna be rough. There are many sets available in the market. And to train the model to recognize all the different sets will be difficult.
Currently I dont have any preliminary ideas of how to solve this.

## Tech Stack
Undecided lol.

## Algorithm
The first algorithm that I can think of is a backtracking algorithm.

There are some complexities. For example, your tiles might not be arranged properly.


```
function checkWinningHand() {
    
    
}
```

