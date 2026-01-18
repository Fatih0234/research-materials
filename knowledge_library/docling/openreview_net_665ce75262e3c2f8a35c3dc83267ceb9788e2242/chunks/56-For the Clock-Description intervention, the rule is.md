## For the Clock-Description intervention, the rule is

In this game, you will participate in an auction for a prize against {{num\_bidders}} other bidders. You will play this game for {{n}} rounds.

At the start of each round, bidders will see their value for the prize, randomly drawn between $0 and ${{private}}, with all values equally likely.

After learning your value, you will submit a bid privately at the same time as the other bidders. Bids must be between $0 and ${{ private}} in ${{increment}} increments.

**FIRST STAGE: Sealed Bid**

You will submit a sealed bid privately at the same time as the other bidders. This bid will serve as your automatic exit price in the next stage.

**SECOND STAGE: Ascending Clock (Simulation)**

After the sealed bid stage, we will simulate an ascending clock auction.

- The clock will start at $0 and increase in increments of ${{increment}}.

The clock will display the current price. You will also see that there are a total of {{num bidders}} bidders participating, although you do not know other bidder's values.

If the current price on the clock reaches or exceeds your sealed bid from the first stage, you will automatically exit the auction. The auction ends when only one bidder is left remaining in the second stage based on their bid from the first stage.

**END OF AUCTION**

If you win, your earnings will increase by your value for the prize and decrease by the clock price at the end of the auction. If you don't win, your earnings will remain unchanged.

1890

1891

1892

1893

1894

1895

1896

1897

1898

1899

1900

1901

1902

1903

1904

1905

1906

1907

1908

1909

1910

1911

1912

1913

1914

1915

1916

1917

1918

1919

1920

1921

1922

1923

1924

1925

1926

1927

1928

1929

1930

1931

1932

1933

1934

1935

1936

1937

1938

1939

1940

1941

1942

1943

After each auction, we will display all bids and the winner's profits. Ties for the highest bid will be resolved randomly.
