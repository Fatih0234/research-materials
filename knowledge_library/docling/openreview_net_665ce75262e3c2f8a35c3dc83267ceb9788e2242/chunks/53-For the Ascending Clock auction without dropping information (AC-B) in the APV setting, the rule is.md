## For the Ascending Clock auction without dropping information (AC-B) in the APV setting, the rule is

- In this game, you will participate in an auction for a prize against {{num\_bidders}} other bidders. You will play this game for {{n}} rounds.
- At the start of each round, bidders will see their value for the prize. Your value for the prize will be calculated as follows:
1. First we will randomly draw a common value between {{common\_low}} and {{common\_high}}, with all values equally likely.
2. Then, for each bidder, a private taste adjustment will be drawn between 0 and {{private}}, with all values equally likely.
- Your value for the prize is equal to the common value plus your private taste adjustment. You will not learn the common value or your private taste adjustment separately. This means that each person in your group may have a different value for the

1566

1567

1568

1569

1570

1571

1572

1573

1574

1575

1576

1577

1578

1579

1580

1581

1582

1583

1584

1585

1586

1587

1588

1589

1590

1591

1592

1593

1594

1595

1596

1597

1598

1599

1600

1601

1602

1603

1604

1605

1606

1607

1608

1609

1610

1611

1612

1613

1614

1615

1616

1617

1618

- 1619 For the Second-Price Sealed-Bid auction in the Common Value setting, the rule is
- prize. However, if you have a high value, it is more likely that other people in your group have a high value.
- The auction proceeds as follows: First, you will learn your value for the prize. Then, the auction will start. We will display a price to everyone in your group that starts at 0 and counts upwards in {{ increment}} USD increments, up to a maximum of {{ common\_high + private}}. At any point, you can choose to leave the auction, but we will not tell any bidder when someone leaves.
- When there is only one bidder left in the auction, that bidder will win the prize at the current price. If you win, your earnings will increase by your value for the prize, and decrease by the current price. If you don't win, your earnings will remain unchanged.
- After each auction, we will display all bids and the winner's profits. Ties for the highest bid will be resolved randomly.
