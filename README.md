# combination-calculator
A programme calculates the combination in python

We often face choosing in daily life and we can hardly meet a chance to get all of them. (~~小朋友才做选择，我，什么都要！~~) Then, we need to face this combination problem. 


Combination problem means we need to choose n things from m. The formula is as follow:


![1](http://latex.codecogs.com/svg.latex?C^n_m=\frac{m!}{n!(m-n)!})


For example, there are 4 maid cafe in Guangzhou and I would like to choose 2 to go at the same time(Warning! かげぶんしんのじゅつ ！). After putting the numbers in the formular, we find that there are 6 different choices.


![2](http://latex.codecogs.com/svg.latex?C_{4}^{2}=\frac{4!}{2!2!}={6})


Since the limitation on human, we can't be in two maid cafe at the  same time. Thus, here comes the permutation problem. 


Permutation means we need to put the order into consider. Thus, we remove the "n!" in denominator and denote as A.


![3](http://latex.codecogs.com/svg.latex?A^n_m=\frac{m!}{(m-n)!})


Now, I choose 2 maid cafe from 4 in Guangzhou for spending the afternoon and night, respectivly. Putting the numbers in the formula and get the result 12 which means if I want to try all the different choices, 12 days are needed. (~~Unless I possess the time leap skill~~)


![4](http://latex.codecogs.com/svg.latex?A^n_m=\frac{4!}{(2)!}=12)
