from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Generic, Iterable, TypeVar


S = TypeVar("S", bound=Enum)
E = TypeVar("E", bound=Enum)
C = TypeVar("C")

Action = Callable[[C], None]


class InvalidTransition(Exception):
    pass


@dataclass
class StateMachine(Generic[S, E, C]):
    transitions: dict[tuple[S, E], tuple[S, Action[C]]] = field(default_factory=dict)

    def add_transition(
        self, from_state: S, event: E, to_state: S, func: Action[C]
    ) -> None:
        self.transitions[(from_state, event)] = (to_state, func)

    def next_transition(self, state: S, event: E) -> tuple[S, Action[C]]:
        try:
            return self.transitions[(state, event)]
        except KeyError as error:
            raise InvalidTransition() from error

    def handle(self, ctx: C, state: S, event: E) -> S:
        next_state, action = self.next_transition(state, event)
        action(ctx)
        return next_state

    def transition(self, from_state: S | Iterable[S], event: E, to_state: S):
        from_states = tuple(from_state) if isinstance(from_state, Iterable) else (from_state,)

        def decorator(func: Action[C]) -> Action[C]:
            for state in from_states:
                self.add_transition(state, event, to_state, func)
            return func

        return decorator
