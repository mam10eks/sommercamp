from os.path import abspath, exists
from sys import argv
from streamlit import (text_input, header, title, subheader, 
    container, markdown, link_button, divider, set_page_config)
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
    markdown(":star2: Vielfalt in der Welt:star2:")
    markdown(":smile: Every autistic is unique :smile:")
    query = text_input(
        label="Suchanfrage",
        placeholder="Suche...",
        value="Alles über Autismus",)


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
            link_button("Seite öffnen", url=row["url"]
            )

def main():
    index_dir = argv[1]
    if not exists(index_dir):
        exit(1)
    app(index_dir)

if __name__ == "__main__":
    main()

