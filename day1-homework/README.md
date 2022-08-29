# QBB2022 - Day 1 - Homework Exercises Submission

1.
Error: Instead of a variable in the given data source file, the variable 'nuc' is a variable defined in the script. When `awk` wants to use it, we need to add `nuc` into `awk` expression as an external variable. Thus, we can use option `-v`, and remove the $ before `nuc` in `if` expression. The corrected expression should be like: `awk -v nuc=$nuc '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c`

Result: 
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G

This data makes sense. Because, normally, transition possibility should be higher than transvertion's due to the chemical structure similarity. 