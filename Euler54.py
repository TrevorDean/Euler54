 #Project Euler 54
 #https://projecteuler.net/problem=54
 #1. P1 P2 win counter
 #2 Read in hand 1 evaluate, read in hand 2 evaluate
 #3 h1 > h2?
 #4 Function that finds if flush
 #5 Function for if straight
 #6 Function for if pair, then if 3, if 4, or if full house
 '''








High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
Flush
Straight
Paired
High
Is flush? if yes then is straight flush? how high
Remove Flush Designation from hands
Is straight? How high?
    if (C1 - C2 = 1 )
Is paired, compare cards, If C1 == C2 == C3 == C4 or C2 == C3 == C4 == C5
    return quads
    if (C1 = C2 = C3 and C4 == C5) or (C3 == C4 == C5 and C1 == C2)
        return fullhouse
    if (C1 = C2 = C3 and C4 != C5) or (C2 == C3 == C4 and C1 != C5) or (C3 == C4 == C5 and C1 != C2)
        return trips
    if C1 == C2 or C2 == C3
        if C3 == C4 or C4 == C5
            return 2pair
    if C1 == C2 or C1 == C3 or C1 == C4 or C1 == C5 or C2 == C3 or C2 == C4 or C2 == C5 or C3 == C4 or C3 == C4 or C3 == C5 or C4 == C5
        return 1pair
    Else
        return HighCard

 '''




