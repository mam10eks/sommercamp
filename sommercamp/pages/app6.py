from streamlit import (text_input, header, title, subheader, container, markdown, sidebar, link_button, divider, set_page_config)

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

divider()
header("Diagnose und Therapie")

import streamlit as st
st.image("https://www.autoinflammation.de/sites/autoinflammation_de/files/styles/twoup_layout_desktop_1080/public/2020-11/autoinflammation-diagnose-rgb.webp", caption="Diagnose", use_column_width=True)

subheader("Diagnose")
markdown("Die Diagnose von Autismus erfolgt in der Regel durch eine Kombination von Verhaltensbeobachtungen und standardisierten Tests. Die Diagnose sollte von einem Facharzt für Kinder- und Jugendpsychiatrie oder einem Kinder- und Jugendpsychologen gestellt werden. Die Diagnose kann in der Regel ab dem 2. Lebensjahr gestellt werden, in einigen Fällen auch schon früher. Die Diagnose kann auch im Erwachsenenalter gestellt werden, wenn die Symptome erst dann auffällig werden.")
link_button("Mehr über Diagnose", "https://www.neurologen-und-psychiater-im-netz.org/kinder-jugendpsychiatrie-psychosomatik-und-psychotherapie/stoerungen-erkrankungen/autismus-spektrum-stoerung-ass/diagnostik/")
divider()
subheader("Therapie")
markdown("Immer wieder wird behauptet, dass autistische Menschen geheilt werden können. Berichte von spektakulären Heilungserfolgen sind natürlich geeignet, große Hoffnungen zu erzeugen. Tatsächlich ist aber zum gegenwärtigen Zeitpunkt eine vollständige Heilung nicht möglich und eine völlig selbständige Lebensführung nur in Einzelfällen bekannt. Auch bei den am stärksten zur Kompensation befähigten Menschen bleiben Auffälligkeiten in der Kommunikation, in der Selbständigkeit und im Sozialverhalten bestehen.")
link_button("Mehr Informationen","https://www.familienhandbuch.de/babys-kinder/behinderung/arten/TherapienbeiAutismus.php")
link_button("Möglichkeiten","https://www.neurologen-und-psychiater-im-netz.org/kinder-jugendpsychiatrie-psychosomatik-und-psychotherapie/stoerungen-erkrankungen/autismus-spektrum-stoerung-ass/therapie/")
