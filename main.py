from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class EventManager(ABC):
    @abstractmethod
    def subscribe(self, listener: Listener) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, listener: Listener) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Editor(EventManager):
    _state: str = None
    _listeners: List[Listener] = []
    f = None
    file = None
    k = 0

    def subscribe(self, listener: Listener) -> None:
        if issubclass(type(listener), Listener):
            if listener not in self._listeners:
                print("Editor: Listener is subscribed")
                self._listeners.append(listener)
            else:
                raise "The [listener] has already subscribed"
        else:
            raise "The [listener] is of the wrong type"

    def unsubscribe(self, listener: Listener) -> None:
        if listener in self._listeners:
            print("Editor: Listener is subscribed")
            self._listeners.remove(listener)
        else:
            raise "The [listener] is not subscribed"

    def notify(self) -> None:
        print("Editor: Notifying listeners...")
        for listener in self._listeners:
            listener.update(self)

    def plus(self) -> None:
        self.k += 1
        self._state = "plus"
        self.notify()

    def minus(self) -> None:
        self.k -= 1
        self._state = "minus"
        self.notify()


class Listener(ABC):
    @abstractmethod
    def update(self, event: EventManager) -> None:
        pass


class ListenerA(Listener):
    plus: int = None

    def update(self, event: EventManager) -> None:
        print("ListenerA has been notified")
        if event._state == "plus":
            self.plus = event.k


class ListenerB(Listener):
    minus: int = None

    def update(self, event: EventManager) -> None:
        print("ListenerB has been notified")
        if event._state == "minus":
            self.minus = event.k


if __name__ == "__main__":
    _editor = Editor()

    listener_a = ListenerA()
    _editor.subscribe(listener_a)

    listener_b = ListenerB()
    _editor.subscribe(listener_b)

    _editor.plus()
    _editor.minus()

    _editor.unsubscribe(listener_a)

    _editor.minus()
