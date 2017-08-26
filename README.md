# Rent Calculation Utility for Scenic House

Our total square footage is `1626`, and our total rent is $`8800`, putting us at ~`5.41` a square foot.

Our current setup, using rent as a percentage:
| room | % of rent |
| --- | --- |
| daniel | 11.988636363636364|
| grady | 11.988636363636364 |
| francis | 12.272727272727273 |
| kim/aziz | 9.03409090909091 |
| maya/dan/seb | 7.443181818181818 |
| kelly | 12.5 |
| ari| 10.852272727272727 |

If we calculate rent as proportional to square footage, using the formula: 
`total_rent * (room_n_footage / (total_sq_footage - common_space))`, we get this breakdown:

| room | rent |
| --- | --- | 
| daniel: | 473.99965862817294 |
| grady: | 1489.5905976445347 |
| francis: | 799.5123259613275 |
| kim/aziz: | 1206.9932457145644 (603.4966228572822 each) |
| maya/dan/seb: | 2823.3986003755094 (941.1328667918365 each)|
| kelly: | 1206.9932457145644 |
| ari: | 799.5123259613275 |

This some obvious caveats. Rent for the triple is the 2nd most expensive, and rent for Danny G's room (which everyone seemed to want) is the least expensive. In a sentence, this method assumes that square footage is the only priority, when in reality we care about closets, natural light, shared space, views, aesthetics, and random bonuses (like sinks, patio access, or a private roof). 

So try and fix this, I rated rooms on these categories. The scores can be positive or negative and are between -5 and 5:

| room | closets | :sunny: | shared | :sunrise: | :cool: |
| --- | --- | --- | --- | --- | --- | 
| daniel | 4 | 5 | 10/10 | 10/10 | 10/10 |
| grady | 2/10 | 2/10 | 10/10 | 3/10 | 6/10 |
| francis | 6/10 | 7/10 | 10/10 | 5/10 |  2/10 |
| kim/aziz | 8/10 | 10/10 | 5/10 | 10/10 | 0/10 |
| maya/dan/seb | 3/10 | 10/10| 1/10 | 9/10 | 0/10 |
| kelly | 10/10 | 10/10 | 10/10 | 10/10 | 8/10 |
| ari | 7/10 | 2/10 | 10/10 | 2/10 | 1/10 |

These category scores are then normalized to two and added to one to give us the multiplier. For instance, Daniel's closet multiplier would be `1.2`, and Grady's would be `.96`.

Using this method, and the scores above, we get the following rent breakdown:
| room | rent |
| --- | --- |
| | |