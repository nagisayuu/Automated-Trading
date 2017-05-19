import tree
rf=tree.getrankfunction(tree.buildhiddenset())
tree.evolve(2,500,rf,mutationrate=0.2,breedingrate=0.1,pexp=0.7,pnew=0.1)
