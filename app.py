from lightning import LightningApp, LightningFlow
from lightning.frontend import StreamlitFrontend
from lightning.utilities.state import AppState


class StreamlitUI(LightningFlow):
    def __init__(self):
        super().__init__()
        self.message_to_print = "Hello World!"
        self.should_print = False
        self.counter = 0

    def configure_layout(self):
        return StreamlitFrontend(render_fn=render_fn)


def render_fn(state: AppState):
    # The provided AppState contains StreamlitUI state e.f `message_to_print` and `should_print`.
    # By accessing them or overriding them, this would be communicated to the flow.
    import streamlit as st

    should_print = st.button("Click to increment the counter.")

    msg = f"Currently incrementing counter. " if state.should_print else "Waiting for you to click the button. "
    st.write(msg + f"Counter value is `{state.counter}/100`")

    st.progress(state.counter)

    if should_print:
        # Negate the `StreamlitUI` should_print value.
        state.should_print = not state.should_print


class HelloWorld(LightningFlow):
    def __init__(self):
        super().__init__()
        self.streamlit_ui = StreamlitUI()

    def run(self):
        # This becomes True when you click the UI button.
        if self.streamlit_ui.should_print:
            print(f"{self.streamlit_ui.counter}: {self.streamlit_ui.message_to_print}")
            self.streamlit_ui.counter += 1
        if self.streamlit_ui.counter >= 100:
            self.streamlit_ui.counter = 0

    def configure_layout(self):
        return [{"name": "StreamLitUI", "content": self.streamlit_ui}]


app = LightningApp(HelloWorld())
