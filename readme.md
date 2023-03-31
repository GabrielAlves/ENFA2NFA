The transition function follows a pattern like this:

transition_function = {
                        state 1 : {input X : new state after reading X},
                        state 2 : {},
                        state 3 : {input X: new state after reading X, input Y : new state after reading Y}
                        state 4 : {input X : {new state after reading X, another new state also after reading X}}
                        }