import os

import streamlit.components.v1 as components
import streamlit as st

# Toggle this to True when creating a release
_RELEASE = True

if _RELEASE:

    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/build")

    _st_vtkjs = components.declare_component("streamlit_vtkjs", path=build_dir)
else:
    _st_vtkjs = components.declare_component(
        "streamlit_vtkjs", url="http://localhost:3001"
    )


def st_vtkjs(file=None, menu=True, key="lala"):
    return _st_vtkjs(file=file, menu=menu, key=key)


if not _RELEASE:
    st.set_page_config(
      page_title="Test VTKJS in Streamlit",
      layout="wide"
    )

    st.title("VTKJS in Streamlit!")

    _file = st.file_uploader(
        label=".vtkjs scene uploader", type=['vtkjs'], help="Upload a .vtkjs scene file"
    )

    file = None

    if _file is not None:
        file = _file.getvalue()

    columns = st.columns([1, 1])

    for i in range(0, 2):
        with columns[i]:
            st_vtkjs(file, True, 'foo-' + str(i))
            st_vtkjs(file, True, 'bar-' + str(i))

    st.write(_file)
