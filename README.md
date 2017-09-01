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

Here, people in shared rooms are responsible for 40.39772727272727% of the rent, and people in singles are responsible for the remaining 59.60227272727273% of the rent.

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

I've taken a number of steps to try and fix this, but representing the relationships between the various factors and rent, with the additional complexity of some relationships being more affecting than others, required too much guesswork. There is definitely a linear relationship between square footage and room quality, but going beyond this requires too much subjectivity.

I think that it behooves us to first consider how overall percentages come into play (i.e. do we really feel alright with a difference of nearly 5% between the most expensive room and the least), and how large these steps should be. From here, we should adjust based on quality or desireability.

So bearing this in mind, I've layed out the following scheme:

| room | % of rent |
| --- | --- |
| daniel | 12.420454545454545 |
| grady | 11.920454545454545 |
| francis | 11.420454545454545 |
| kim/aziz | 8.75 |
| maya/dan/seb | 7.632575757575758 |
| kelly | 12.920454545454545 |
| ari| 10.920454545454545 |

Here we take the average single rent (11.920454545454545), and adjust `+/- 0.5%` for ranking based on desireability (Kelly > Daniel > Grady > Francis > Ari). For the shared rooms, I just kind of threw out `8.75%` (from an average of  8.238636363636363) as appropriate for the doublet, and the triplets followed from there. 

With the Sof situation, if we halve Francis's rent, it becomes 5.7102272727272725%, which seems too low for a shared space. I suggest that we up it to between 6 and 6.5 percent and distribute the extra rent evenly among the remaining rooms. 

If we put *SoFran* at 6.5, an extra 0.17550505050505222% is added to the remaining 9.
