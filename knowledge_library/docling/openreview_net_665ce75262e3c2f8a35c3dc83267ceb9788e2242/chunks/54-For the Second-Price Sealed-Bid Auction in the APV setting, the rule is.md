## For the Second-Price Sealed-Bid Auction in the APV setting, the rule is

- In this game, you will participate in an auction for a prize against {{num\_bidders}} other bidders. You will play this game for {{n}} rounds.
- At the start of each round, bidders will see their value for the prize. Your value for the prize will be calculated as follows:
1. First we will randomly draw a common value between {{common\_low}} and {{common\_high}}, with all values equally likely.
2. Then, for each bidder, a private taste adjustment will be drawn between 0 and {{private}}, with all values equally likely.
- Your value for the prize is equal to the common value plus your private taste adjustment. You will not learn the common value or your private taste adjustment separately. This means that each person in your group may have a different value for the prize. However, if you have a high value, it is more likely that other people in your group have a high value.
- After learning your value, you will submit a bid privately at the same time as the other bidders. Bids must be between $0 and ${{common\_high + private}} in ${{increment}} increments.
- The highest bidder wins the prize and pays the secondhighest bid. If you win, your earnings will increase by your value for the prize, and decrease by the second-highest bid. If you don't win, your earnings will remain unchanged.
- After each auction, we will display all bids and the winner's profits. Ties for the highest bid will be resolved randomly.

```
1620 1621 1622 1623 1624 1625 1626 1627 1628 1629 1630 1631 1632 1633 1634 1635 1636 1637 1638 1639 1640 1641 1642 1643 1644 1645 1646 1647 1648 1649 1650 1651 1652 1653 1654 1655 1656 1657 1658 1659 1660 1661 1662 1663 1664 1665 1666 1667 1668 1669 1670 1671 1672 1673 In this game, you will participate in an auction for a prize against {{num_bidders}} other bidders. You will play this game for {{n}} rounds. At the start of each round, bidders will see their perceived value for the prize - a noisy measurement of the true value of the prize. Your perceived value for the prize will be calculated as follows: 1. For each round, a common value will be drawn between {{common_low}} and {{common_high}}, with all values equally likely to be drawn. 2. For each person, a private noisy adjustment will be drawn between -{{private}} and {{private}}, with all values equally likely to be drawn. We will tell you your perceived value, the sum of the common value and the private noise adjustment. However, everyone's true value for the prize is equal to the shared common value. After learning your perceived value, you will submit a bid privately at the same time as the other bidders. Bids must be between $0 and ${{ common_high + private}} in ${{increment}} increments. The highest bidder wins the prize and pays the secondhighest bid. If you win, your earnings will increase by the true value for the prize, and decrease by the second-highest bid. If you don't win, your earnings will remain unchanged. After each auction, we will display all bids and the winner's profits. Ties for the highest bid will be resolved randomly. For the Standard eBay auction with proxy bidding (T1), the rule is In this game, you will participate in an eBay auction for an item against {{num_bidders}} other bidders. This auction will last for {{num_rounds}} days. All dollar amounts in this game are in US Dollars ($). Item Details: Item Description: {{item_description}} Item Condition: {{item_condition}} Your Private Value: At the start of each round, bidders will see their value for the item, randomly drawn between $0 and ${{private}}, with all values equally likely. After learning your value for the item, you will submit a maximum bid. Bids must be between $0 and ${{private}} in ${{ increment}} increments. Auction Format: This is an eBay auction. The auction starts at ${{ start_price}} and will last for {{num_rounds}} days. eBay uses "proxy bidding." This means that if you wish to enter the auction, you should submit your maximum bid, and eBay will automatically bid on your behalf, up to your
```

```
1674 1675 1676 1677 1678 1679 1680 1681 1682 1683 1684 1685 1686 1687 1688 1689 1690 1691 1692 1693 1694 1695 1696 1697 1698 1699 1700 1701 1702 1703 1704 1705 1706 1707 1708 1709 1710 1711 1712 1713 1714 1715 1716 1717 1718 1719 1720 1721 1722 1723 1724 1725 1726 1727 maximum, only as much as necessary to maintain your position as the highest bidder. Each day you will see the current price and have the opportunity to increase your maximum bid. If you do not want to increase your maximum bid, then output HOLD. You may place bids at any point during the auction, even on the final day. No bidder will know if they (or anyone else) is the last bidder on the final day. The highest bidder wins the prize and pays the auction price at the time the auction's clock expired. If you win, your earnings will increase by your value for the prize, and decrease by the final auction price. If you don't win, your earnings will remain unchanged. Ties for the highest bid will be resolved randomly. For the eBay auction with a modified closing rule (T2), the rule is In this game, you will participate in an eBay auction for an item against {{num_bidders}} other bidders. This auction will last for {{num_rounds}} days. All dollar amounts in this game are in US Dollars ($). Item Details: Item Description: {{item_description}} Item Condition: {{item_condition}} Your Private Value: At the start of each round, bidders will see their value for the item, randomly drawn between $0 and ${{private}}, with all values equally likely. After learning your value for the item, you will submit a maximum bid. Bids must be between $0 and ${{private}} in ${{ increment}} increments. Auction Format: This is an eBay auction with a closing rule. The auction starts at ${{start_price}} and will last for {{num_rounds}} days. eBay uses "proxy bidding ." This means that if you wish to enter the auction, you should submit your maximum bid, and eBay will automatically bid on your behalf, up to your maximum, only as much as necessary to maintain your position as the highest bidder. Each day you will see the current price and have the opportunity to increase your maximum bid. If you do not want to increase your maximum bid, then output HOLD. This auction also has a closing rule. This means that if a new maximum bid is placed on the last day, the auction will automatically extend by another day. This extension will continue to be applied as long as new maximum bids are placed on the final
```

```
1728 1729 1730 1731 1732 1733 1734 1735 1736 1737 1738 1739 1740 1741 1742 1743 1744 1745 1746 1747 1748 1749 1750 1751 1752 1753 1754 1755 1756 1757 1758 1759 1760 1761 1762 1763 1764 1765 1766 1767 1768 1769 1770 1771 1772 1773 1774 1775 1776 1777 1778 1779 1780 1781 day. No bidder will know if they (or anyone else) is the final bidder on the last day. The highest bidder wins the prize and pays the auction price at the time the auction's clock expired. If you win, your earnings will increase by your value for the prize, and decrease by the final auction price. If you don't win, your earnings will remain unchanged. Ties for the highest bid will be resolved randomly. For the standard eBay auction with a hidden reserve price (T3), the rule is In this game, you will participate in an eBay auction for an item against {{num_bidders}} other bidders. This auction will last for {{num_rounds}} days. All dollar amounts in this game are in US Dollars ($). Item Details: Item Description: {{item_description}} Item Condition: {{item_condition}} Your Private Value: At the start of each round, bidders will see their value for the item, randomly drawn between $0 and ${{private}}, with all values equally likely. After learning your value for the item, you will submit a maximum bid. Bids must be between $0 and ${{private}} in ${{ increment}} increments. Auction Format: This is an eBay auction with a hidden reserve price. The auction starts at ${{start_price}} and will last for {{num_rounds}} days. eBay uses "proxy bidding." This means that if you wish to enter the auction, you should submit your maximum bid, and eBay will automatically bid on your behalf, up to your maximum, only as much as necessary to maintain your position as the highest bidder. Each day you will see the current price and have the opportunity to increase your maximum bid. If you do not want to increase your maximum bid, then output HOLD. You may place bids at any point during the auction, even on the final day. However, if no bidder produces a maximum bid above the hidden reserve price, the seller will retain the good and the bidders will be informed that there is currently no bidder in the lead. No bidder will know if they (or anyone else) is the final bidder on the last day. If the reserve is met, the highest bidder wins the prize and pays the auction price at the time the auction's clock expired. If you win, your earnings will increase by your value for the prize, and decrease by the final auction price. If you don't
```

1782 1783 1784 1785 1786 1787 1788 1789 1790 1791 1792 1793 1794 1795 1796 1797 1798 1799 1800 1801 1802 1803 1804 1805 1806 1807 1808 1809 1810 1811 1812 1813 1814 1815 1816 1817 1818 1819 1820 1821 1822 1823 1824 1825 1826 1827 1828 1829 1830 1831 1832 1833 1834 1835 win, your earnings will remain unchanged. Ties for the highest bid will be resolved randomly. For the eBay auction with a modified closing rule and a hidden reserve price (T4), the rule is In this game, you will participate in an eBay auction for an item against {{num\_bidders}} other bidders. This auction will last for {{num\_rounds}} days. All dollar amounts in this game are in US Dollars ($). Item Details: Item Description: {{item\_description}} Item Condition: {{item\_condition}} Your Private Value: At the start of each round, bidders will see their value for the item, randomly drawn between $0 and ${{private}}, with all values equally likely. After learning your value for the item, you will submit a maximum bid. Bids must be between $0 and ${{private}} in ${{ increment}} increments. Auction Format: This is an eBay auction with a hidden reserve price and a closing rule. The auction starts at ${{ start\_price}} and will last for {{num\_rounds}} days. eBay uses "proxy bidding." This means that if you wish to enter the auction, you should submit your maximum bid, and eBay will automatically bid on your behalf, up to your maximum, only as much as necessary to maintain your position as the highest bidder. Each day you will see the current price and have the opportunity to increase your maximum bid. If you do not want to increase your maximum bid, then output HOLD. You may place bids at any point during the auction, even on the final day. However, if no bidder produces a maximum bid above the hidden reserve price, the seller will retain the good and the bidders will be informed that there is currently no bidder in the lead. This auction also has a closing rule. This means that if a new maximum bid is placed on the last day, the auction will automatically extend by another day. This extension will continue to be applied as long as new maximum bids are placed on the final day. No bidder will know if they (or anyone else) is the last bidder on the final day. If the reserve is met, the highest bidder wins the prize and pays the auction price at the time the auction's clock expired. If you win, your earnings will increase by your value for the prize, and decrease by the final auction price. If you don't win, your earnings will remain unchanged. Ties for the highest bid will be resolved randomly.

1836

1837

1838

1839

1840

1841

1842

1843

1844

1845

1846

1847

1848

1849

1850

1851

1852

1853

1854

1855

1856

1857

1858

1859

1860

1861

1862

1863

1864

1865

1866

1867

1868

1869

1870

1871

1872

1873

1874

1875

1876

1877

1878

1879

1880

1881

1882

1883

1884

1885

1886

1887

1888

1889
