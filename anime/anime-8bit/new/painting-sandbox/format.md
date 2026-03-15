### Map

#### Noise

##### Perlin

|# 生成 Perlin 噪音<br />noise\_data = long\_grid(x = seq(0, 5, length.out = grid\_size), <br />                       y = seq(0, 5, length.out = grid\_size)) \|><br />  mutate(value = gen\_perlin(x, y, frequency = 1, seed = 42))|
|-|



##### Simplex

|# 生成 Simplex 噪音<br />noise\_data = long\_grid(x = seq(0, 5, length.out = grid\_size), <br />                       y = seq(0, 5, length.out = grid\_size)) \|><br />  mutate(value = gen\_simplex(x, y, frequency = 1, seed = 42))|
|-|



#### Perlin

code

|/\*\* Perlin在論文中給的五次方淡出公式<br /> \* t的範圍為０到１<br /> \* 以fade(t)取得到的值也是０到１，但是<br /> \* 在t=0與t=1的附近，fade(t)變化量趨近於０<br /> \*/<br />function fade(t: number): number {<br />    return t \* t \* t \* ((6 \* t - 15) \* t + 10);<br />}|
|-|

#### Perlin-PLUS

##### regular

|/\*\* Perlin在論文中給的五次方淡出公式<br /> \* t的範圍為０到１<br /> \* 以fade(t)取得到的值也是０到１，但是<br /> \* 在t=0與t=1的附近，fade(t)變化量趨近於０<br /> \*/<br />function fade(t: number): number {<br />    return (t \* t \* t \* ((6 \* t - 15) \* t + 10)) + ((t / 5) \* (t / 5) \* (t / 5) \* ((6 \* (t /  5) - 15) \* (t / 5) + 10));<br />}|
|-|



### Human

|/\*\* example is  age and gender=male etc<br />\*/<br />Generate\_Human(Age=25, Gender=Male, Ethnic=Asian, Seed=8888)|
|-|



#### Human-Plus

|/\*\* example is  age and gender=male etc, and added cloth seed<br />\*/<br />Generate\_Human(Age=25, Year=2026, Gender=Male, Ethnic=Asian, Country=Japan, Seed=8888, ClothSeed=9999)|
|-|





