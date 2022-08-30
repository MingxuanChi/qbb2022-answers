Good work overall! 

3. Running grep -w | wc | cut for each number gets you the right answer. Running bits of code over and over has to happen sometimes, but also can take more time if you have a lot of inputs and increases the possibility of human error. 

A couple better options are: 

* sort and uniq -c, as you suggested
* a for loop, looping through the numbers 1 through 15. 

But the way you are doing it gets you the right answer! 

A quick notes about this line: "$((305+17+17+30+62+228+992+678+79+377+808+148+1050+156+654))"

This gave you the error message: '-bash: 5601: command not found'. What's going on here is that bash correctly interprets this equation and calculates the number 5601. This is then interpreted by bash as a command, and bash tries to look for a command called "5601". If you want to print out the number, you can use the command echo. The following code would work well:

echo $((305+17+17+30+62+228+992+678+79+377+808+148+1050+156+654))

4. Similar to the above, uniq -c would be a more rigorous way of doing this, but your solution works. 

5. b. Your solution works, but a quicker way to write this would be "cut -f 1-9,13". This makes a really big difference when you want to extract a lot of columns from a larger file

d. Interesting idea with enclosing 'AF=1' in quotes. This prevents you from counting lines that have AF!=1 but, say, AFR_AF=1. A different way of getting the solution here would be to cut out the INFO field, and then cut it again, splitting on semicolons. 

Overall this is very well done! 

– Andrew
