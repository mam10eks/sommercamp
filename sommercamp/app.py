from os.path import abspath, exists
from sys import argv
from streamlit import (text_input, header, title, subheader, container, markdown, sidebar, link_button, divider, set_page_config)
from pyterrier import started, init
if not started():
    init()
from pyterrier import IndexFactory
from pyterrier.batchretrieve import BatchRetrieve
from pyterrier.text import get_text


def app(index_dir) -> None:

    set_page_config(
        page_title="Wir sind Autisten",
        layout="centered",
    )

    title("Wir sind Autisten")

    sidebar.page_link("app.py", label="Was ist Autismus?") 
    sidebar.page_link("pages/app3.py", label="frühkindlicher Autismus und atypischer Autismus")
    sidebar.page_link("pages/user.py", label="Asperger-Syndrom")
    sidebar.page_link("pages/app4.py", label="Autismus und Schule")
    sidebar.page_link("pages/app5.py", label="Autismus und Beruf")
    sidebar.page_link("pages/app6.py", label="Diagnose und Therapie")
    sidebar.page_link("pages/app7.py", label="Eltern von autistischen Kindern")
    sidebar.page_link("pages/app8.py", label="Wie kann ich helfen?")
    sidebar.page_link("pages/app9.py", label="Mehr über Autismus")
   
    markdown(":star2: Vielfalt in der Welt:star2:")
    markdown(":smile: Every autistic is unique :smile:")
    query = text_input(
        label="Suchanfrage",
        placeholder="Suche...",
        value="Autismus",)

    if query == "":
        markdown("Bitte gib eine Suchanfrage ein.")
        return

    index = IndexFactory.of(abspath(index_dir))
    searcher = BatchRetrieve(
        index,
        wmodel="BM25",
        num_results=10,
    )

    text_getter = get_text(index, metadata=["url", "title", "text"])
    pipeline = searcher >> text_getter
    results = pipeline.search(query)

    import streamlit as st
    st.image("https://imageio.forbes.com/specials-images/imageserve/61cc9dc17390740da6554667/Little-boy-and-a-colorful-brain-sketch/960x0.jpg?format=jpg&width=1440", caption="a colorful autistic kid")

    divider()
    header("Suchergebnisse")

    if len(results) == 0:
        markdown("Keine Suchergebnisse.")
        return

    markdown(f"{len(results)} Suchergebnisse.")

    for _, row in results.iterrows():
        with container(border=True):
            subheader(row["title"])
            text = row["text"]
            text = text[:500]
            text = text.replace("\n", " ")
            markdown(text)
            link_button("Seite öffnen", url=row["url"])


def main():
    index_dir = argv[1]
    if not exists(index_dir):
        exit(1)
    app(index_dir)


if __name__ == "__main__":
    main()