## Clock-Description

FIRST STAGE: Sealed Bid You will submit a sealed bid privately at the same time as the other bidders. This bid will serve as your automatic exit price in the next stage.

SECOND STAGE: Ascending Clock (Simulation)

After the sealed bid stage, we will simulate an ascending clock auction. The clock will start at 0 and increase in increments of increment. The clock will display the

100

80

60-

40

20-

100 -

80 -

60

40

20

Bids vs. Values (menu\_intervention)

Data Points

LOESS Smoothed

20

Data Points

- LOESS Smoothed

--- y = x

100 -

80 -

60 -

Bids vs. Values (proxy\_intervention)

Data Points

LOESS Smoothed

Bids

<!-- image -->

2128

2129

2130

2131

2132

2133

2134

2135

2136

2137

2138

2139

2140

2141

2142

2143

2144

2145

2146

2147

2148

2149

2150

2151

2152

2153

2154

2155

2156

2157

2158

2159

80 -

60 -

Bids vs. Values (nash\_intervention)

Data Points

LOESS Smoothed

Figure 11: Results for SPSB with the six interventions, IPV environment. The green dotted line represents the scenario of bid=value, blue dots are bids from agents, and the red line is the LOESS smoothed curve of bids. Menu and proxy framings reduce scatter but still hug the region below the green y = x line. The Nash-deviation framing tilts the curve almost exactly onto the 45-degree line. The dominant-strategy advice panel shows the tightest clustering, whereas the 'Wrong Strategy' panel visibly drags the red curve toward y = v/ 2 .

current price. You will also see that there are a total of { num bidders } bidders participating, although you do not know other bidder's values. If the current price on the clock reaches or exceeds your sealed bid from the first stage, you will automatically exit the auction. The auction ends when only one bidder is left remaining in the second stage based on their bid from the first stage. END OF AUCTION
