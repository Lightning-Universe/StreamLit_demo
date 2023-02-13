# StreamLit Template Application in 2 steps

[![Lightning](https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white)](https://lightning.ai)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/Lightning-AI/metrics/blob/master/LICENSE)

## 1. Setup

Create a virtual environment with python 3.8+ and run

```bash
pip install -r requirements.txt
```

## 2. Run the StreamLit Application

```bash
lightning build app app.py
```

#### Application Details

In the file `app.py`, import the `StreamlitFrontend` and pass it a render_fn method.

```python
    from lightning.frontend import StreamlitFrontend
    from lightning.utilities.state import AppState

    class StreamlitUI(LightningFlow):

        ...

        def configure_layout(self):
            return StreamlitFrontend(render_fn=render_fn)
```

The render_fn method takes an `AppState` argument. The AppState contains the attribute of the `StreamlitUI` and can be changed with Streamlit UI.

Below, clicking the Streamlit button, this will change the flip `should_print` value of the `StreamlitUI` state.

```py
def render_fn(state: AppState):
    import streamlit as st

    should_print = st.button("Should print to the terminal ?")

    if should_print:
        state.should_print = not state.should_print

    st.write("Currently printing." if state.should_print else "Currently waiting to print.")
```
