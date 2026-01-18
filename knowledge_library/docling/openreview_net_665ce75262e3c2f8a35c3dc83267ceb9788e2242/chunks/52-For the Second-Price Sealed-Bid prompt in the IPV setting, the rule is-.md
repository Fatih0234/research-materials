## For the Second-Price Sealed-Bid prompt in the IPV setting, the rule is:

- In this game, you will participate in an auction for a prize against {{num\_bidders}} other bidders. You will play this game for {{n}} rounds.
- At the start of each round, bidders will see their value for the prize, randomly drawn between $0 and ${{private}}, with all values equally likely. After learning your value, you will submit a bid privately at the same time as the other bidders.

- 1458 1459 1460 1461 1462 1463 1464 1465 1466 1467 1468 1469 1470 1471 1472 1473 1474 1475 1476 1477 1478 1479 1480 1481 1482 1483 1484 1485 1486 1487 1488 1489 1490 1491 1492 1493 1494 1495 1496 1497 1498 1499 1500 1501 1502 1503 1504 1505 1506 1507 1508 1509 1510 Bids must be between $0 and ${{private}} in ${{ increment}} increments. The highest bidder wins the prize and pays the secondhighest bid. If you win, your earnings will increase by your value for the prize, and decrease by the second-highest bid. If you don't win, your earnings will remain unchanged. After each auction, we will display all bids and the winner's profits. Ties for the highest bid will be resolved randomly. For the Third-Price Sealed-Bid prompt in the IPV setting, the rule is: In this game, you will participate in an auction for a prize against {{num\_bidders}} other bidders. You will play this game for {{n}} rounds. At the start of each round, bidders will see their value for the prize, randomly drawn between $0 and ${{private}}, with all values equally likely. After learning your value, you will submit a bid privately at the same time as the other bidders. Bids must be between $0 and ${{private}} in ${{ increment}} increments. The highest bidder wins the prize and pays the thirdhighest bid. If you win, your earnings will increase by your value for the prize, and decrease by the third-highest bid. If you don't win, your earnings will remain unchanged. If there are less than three bids, no one will win the auction. After each auction, we will display all bids and the winner's profits. Ties for the highest bid will be resolved randomly. For the All-Pay Sealed-Bid prompt in the IPV setting, the rule is: In this game, you will participate in an auction for a prize against {{num\_bidders}} other bidders. You will play this game for {{n}} rounds. At the start of each round, bidders will see their value for the prize, randomly drawn between $0 and ${{private}}, with all values equally likely. After learning your value, you will submit a bid privately at the same time as the other bidders. Bids must be between $0 and ${{private}} in ${{ increment}} increments. The highest bidder wins the prize. All bidders ( including the winner) pay their submitted bid. If you win, your earnings will increase by your value for the prize, and decrease by your bid. If you don't win, your earnings will still decrease by your bid. After each auction, we will display all bids and all bidders' profits. Ties for the highest bid will be resolved randomly.
- 1511 For the Ascending Clock auction (AC) in the APV setting, the rule is

1512

1513

1514

1515

1516

1517

1518

1519

1520

1521

1522

1523

1524

1525

1526

1527

1528

1529

1530

1531

1532

1533

1534

1535

1536

1537

1538

1539

1540

1541

1542

1543

1544

1545

1546

1547

1548

1549

1550

1551

1552

1553

1554

1555

1556

1557

1558

1559

1560

1561

1562

1563

1564

1565

- In this game, you will participate in an auction for a prize against {{num\_bidders}} other bidders. You will play this game for {{n}} rounds.
- At the start of each round, bidders will see their value for the prize. Your value for the prize will be calculated as follows:
1. First we will randomly draw a common value between {{common\_low}} and {{common\_high}}, with all values equally likely.
2. Then, for each bidder, a private taste adjustment will be drawn between 0 and {{private}}, with all values equally likely.
- Your value for the prize is equal to the common value plus your private taste adjustment. You will not learn the common value or your private taste adjustment separately. This means that each person in your group may have a different value for the prize. However, if you have a high value, it is more likely that other people in your group have a high value.
- The auction proceeds as follows: First, you will learn your value for the prize. Then, the auction will start. We will display a price to everyone in your group that starts at 0 and counts upwards in {{ increment}} USD increments, up to a maximum of {{ common\_high + private}}. At any point, you can choose to leave the auction, and anytime a bidder leaves, we will broadcast that information to all the remaining bidders.
- When there is only one bidder left in the auction, that bidder will win the prize at the current price. If you win, your earnings will increase by your value for the prize, and decrease by the current price. If you don't win, your earnings will remain unchanged.
- After each auction, we will display all bids and the winner's profits. Ties for the highest bid will be resolved randomly.
