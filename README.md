# CNF-Evaluator
This program takes formulas in conjunctive normal form and outputs the possible truth values of the formula as well as whether the formula is "satisfiable," "logically valid," or "unsatisfiable."
Example of CNF formula: (~K1 v K2) & (K2 v ~K3).
The user is prompted for the number of conjuncts in the formula (e.g. in example: 2).
The user is then prompted for the terms within each disjunctive clause (e.g. in example, disjunct 1: ~K1 K2, disjunct 2: K2 ~K3).
Program outputs list containing truth values for different interpretations of formula.
Ends by outputting satisfiable, unsatisfiable, or logically valid.
