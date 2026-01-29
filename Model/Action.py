from Model.Predicate import Predicate
from Model.State import State
from typing import Optional # baraye typing errore python


class Action:
    def __init__(
        self,
        action_name: str,
        positive_preconditions: list[Predicate] | set[Predicate],
        negative_preconditions: list[Predicate] | set[Predicate],
        add_list: list[Predicate] | set[Predicate],
        delete_list: list[Predicate] | set[Predicate],
    ):
        self.action_name = action_name
        self.positive_preconditions = set(positive_preconditions)
        self.negative_preconditions = set(negative_preconditions)
        self.add_list = set(add_list)
        self.delete_list = set(delete_list)


    def is_relevant(self, state: State) -> bool:
        """
        An action is relevant in backward planning if it can achieve
        at least one literal in the current goal state.
        """
        return (
            len(self.add_list & state.literals) > 0
            or len(self.delete_list & state.literals) > 0
            or len(self.positive_preconditions & state.literals) > 0
            or len(self.negative_preconditions & state.literals) > 0
        )
        #returns true if at least one of these is true.

    def regress(self, state: State) -> Optional[State]: #Regression can fail, so the return type should be optional.

        """
        Backward planning regression:
        - Remove action add effects from the goal
        - Add action delete effects
        - Add positive preconditions
        - Remove negative preconditions
        """

        # If the action deletes something required by the goal → invalid
        if self.delete_list & state.literals:
            return None

        new_literals = set(state.literals)

        # Remove achieved goals
        new_literals -= self.add_list

        # Add action preconditions
        new_literals |= self.positive_preconditions

        # Remove negative preconditions
        new_literals -= self.negative_preconditions

        new_state = State(self.action_name, list(new_literals))
        new_state.parent = state
        return new_state

    def progress(self, state: State) -> Optional[State]:
        """
        Forward planning progression:
        - Apply add effects
        - Apply delete effects
        """

        new_literals = set(state.literals)

        new_literals |= self.add_list
        new_literals -= self.delete_list

        new_state = State(self.action_name, list(new_literals))
        new_state.parent = state
        return new_state

    def is_applicable(self, state: State) -> bool:
        """
        Forward planning applicability test:
        - All positive preconditions must hold
        - No negative preconditions may hold
        """
        return (
            self.positive_preconditions.issubset(state.literals)
            and self.negative_preconditions.isdisjoint(state.literals)
        )


    def __str__(self) -> str:
        return (
            f"Action: {self.action_name}"
            + f"\nPositive preconditions: {self.positive_preconditions}"
            + f"\nNegative preconditions: {self.negative_preconditions}"
            + f"\nAdd list: {self.add_list}"
            + f"\nDelete list: {self.delete_list}\n"
        )

    def __repr__(self) -> str:
        return str(self)
