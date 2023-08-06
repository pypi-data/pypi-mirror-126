from typing import Optional, cast

from rich import box
from rich.align import Align
from rich.console import RenderableType
from rich.panel import Panel
from rich.text import Text
from textual import events
from textual.widget import Reactive, Widget
from textual.widgets import Button, Footer
from textual_inputs import TextInput

from chkapi.events import (
    CancelSearch,
    FinishSearch,
    FocusRecent,
    Search,
    SetUrl,
    UrlChanged,
    UrlTyped,
)


class URLButton(Button, can_focus=True):
    has_focus: Reactive[bool] = Reactive(False)
    mouse_over: Reactive[bool] = Reactive(False)
    label: str = "GO"

    def __init__(self, label=label):
        super().__init__(label=label)

    def render(self):
        return Panel(
            Align.center(self.label),
            box=box.HEAVY if self.mouse_over else box.ROUNDED,
            style="black on white" if self.has_focus else "white on black",
            height=3,
        )

    async def on_focus(self) -> None:
        self.has_focus = True

    async def on_blur(self) -> None:
        self.has_focus = False

    async def on_enter(self) -> None:
        self.mouse_over = True

    async def on_leave(self) -> None:
        self.mouse_over = False

    async def on_click(self) -> None:
        self.has_focus = False
        await self.emit(UrlChanged(self))


class URLField(TextInput):
    def __init__(self, url):
        super().__init__(value=url, title="URL")

    @property
    def url(self) -> str:
        return self.value

    async def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
            await self.emit(UrlChanged(self))
        if event.key == "down":
            await self.emit(FocusRecent(self))
        else:
            await self.emit(UrlTyped(self))


class AutocompleteWidget(Widget):
    urls: list[str]
    current: int = -1

    def __init__(self) -> None:
        self.urls = []
        super().__init__(name=None)

    async def on_mount(self):
        self.visible = False
        self.layout_offset_y = 3

    def hide(self):
        self.visible = False
        self.refresh(layout=True)
        self.current = None

    def show(self):
        self.visible = True
        self.refresh(layout=True)

    def on_focus(self):
        self.current = 0
        self.refresh()

    def show_recent(self, recent):
        self.log(recent)
        if recent:
            self.urls = recent
            self.show()
        else:
            self.urls = []
            self.hide()

    async def on_key(self, event: events.Key):
        if event.key == "down":
            self.move_current_up()
        elif event.key == "up":
            self.move_current_down()
        elif event.key == "enter":
            await self.select_current()

    def move_current_up(self):
        self.current += 1
        self.current = self.current % len(self.urls)
        self.refresh()

    def move_current_down(self):
        self.current -= 1
        if self.current == -1:
            self.current = len(self.urls) - 1
        self.refresh()

    async def select_current(self):
        await self.emit(SetUrl(self, self.urls[self.current]))
        self.current = -1
        self.hide()

    def render(self):
        text = Text()
        for i, url in enumerate(self.urls):
            text.append(url + "\n", "red on yellow" if self.current == i else "")
        return Panel(text)


class CommandPrompt(TextInput):
    def on_mount(self):
        self.visible = False

    async def show(self):
        self.visible = True
        await self.focus()

    async def hide(self):
        self.visible = False
        self.value = ""

    async def on_key(self, event: events.Key) -> None:
        event.prevent_default().stop()
        await super().on_key(event)
        if event.key == "escape":
            await self.hide()
            await self.emit(CancelSearch(self))
            return
        if event.key == "enter":
            await self.hide()
            await self.emit(FinishSearch(self))
            return
        await self.emit(Search(self, self.value))


class ApiFooter(Footer):
    response_time: Reactive[Optional[float]] = Reactive(None)

    def on_mount(self):
        self.response_time = None

    def render(self) -> RenderableType:
        content = cast(Text, super().render())
        if self.response_time:
            return Text.assemble(
                content,
                Text(
                    f"Response time: {self.response_time:.2f}s",
                    style="white on dark_green",
                    justify="right",
                ),
            )
        return content

    def update_keys(self):
        self._key_text = None
        # self.refresh()


class MessageWidget(Widget):
    message: RenderableType

    def on_mount(self):
        self.visible = False
        self.layout_offset_y = 5

    def show(self, message: str):
        self.message = message
        self.visible = True

    def render(self) -> RenderableType:
        return Panel(Align.center(self.message), style="red on black")

    def hide(self):
        self.visible = False


class HeadersWidget(Widget):
    headers: dict

    def on_mount(self):
        self.visible = False
        self.layout_offset_y = 3

    def show(self, headers: dict):
        self.headers = headers
        self.visible = True

    def hide(self):
        self.visible = False

    def render(self) -> RenderableType:
        column_len = max([len(key) for key in self.headers.keys()])
        formatted_headers = [
            f"{key.ljust(column_len)}: {val}" for key, val in self.headers.items()
        ]
        return Panel("\n".join(formatted_headers))

    def on_key(self, event):
        if event.key == "escape":
            self.hide()
