class FARule(object):

    """
    Represents a rule of a DFA
    """

    def __init__(self, state, character, nextstate):

        self.state = state
        self.character = character
        self.nextstate = nextstate

    def applies(self,state, character):

        if self.state == state and self.character == character:
            return True

        else:
            return False

    def follow(self):

        return self.nextstate

    def __repr__(self):

        return '#FARule # {} {} {} '.format(self.state, 
                                            self.character, 
                                            self.nextstate)
    

class FARulebook(object):

    def __init__(self, rules):

        self.rules = rules

    def next_state(self, state, character):


        return self.rule_for(state, character).follow()


    def rule_for(self, state, character):

        for rule in self.rules:
            if rule.applies(state, character):
                return rule

class DFA(object):

    def __init__(self, current_state, accept_states, rulebook):

        self.current_state = current_state
        self.accept_states = accept_states
        self.rulebook = rulebook


    def accepting(self):

        return self.current_state in self.accept_states

    def read_character(self, character):

        self.current_state = rulebook.next_state(self.current_state, character)

        return

    def read_string(self, string):

        for char in string:
            self.read_character(char)

        return

class DFADesign(object):

    def __init__(self, start_state, accept_states, rulebook):

        self.start_state = start_state
        self.accept_states = accept_states
        self.rulebook = rulebook


    def make_dfa(self):

        return DFA(self.start_state, self.accept_states, self.rulebook)

    def accepts(self, string):

        dfa = self.make_dfa()

        dfa.read_string(string)

        return dfa.accepting()





if __name__=="__main__":

    rules = []

    rules.append(FARule(1, 'a', 2))
    rules.append(FARule(2, 'a', 2))
    rules.append(FARule(3, 'a', 3))
    rules.append(FARule(1, 'b', 1))
    rules.append(FARule(2, 'b', 3))
    rules.append(FARule(3, 'b', 3))
    rulebook = FARulebook(rules)
    # print(rulebook.next_state(1, 'a'))

    dfa = DFA(1, [3],rulebook)

    dfa.read_string('ab')
    print(dfa.accepting())
    # dfa.read_string('abbabba')
    # print(dfa.accepting())

    dfa_design = DFADesign(1, [3],rulebook)

    print(dfa_design.accepts('a'))
    # dfa_design = DFADesign(1, [3],rulebook)
    print(dfa_design.accepts('baa'))
    # dfa_design = DFADesign(1, [3],rulebook)
    print(dfa_design.accepts('baba'))










