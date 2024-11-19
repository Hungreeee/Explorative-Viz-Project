import sys, os
sys.dont_write_bytecode = True

from datetime import time, timedelta
import streamlit.components.v1 as components
from streamlit_carousel import carousel

import pandas as pd
import streamlit as st
from streamlit_modal import Modal

st.set_page_config(page_title="Why is Vietnam's traffic so scary to foreigners?", layout="wide")

def open_file(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, "r", encoding="utf8") as file:
        content = file.read()
    return content

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Newsreader:wght@400&family=DM+Serif+Text:wght@400');

    h1, h2, h3, h4, h5, h6 {
        font-family: 'DM Serif Text';  
        font-weight: 500;
    }

    p, li {
        font-family: 'Newsreader';  
    }

    .st-bn {
        display: flex;
        justify-content: space-around;
    }

    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 20px !important; 
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Why is Vietnam's traffic so scary to foreigners?")

###

st.markdown("# Introduction")

col1, col2 = st.columns(spec=[0.5, 0.5])
with col1: 
    st.markdown("""
    Vietnam is experiencing rapid urbanization, with its cities expanding at an unprecedented pace. This growth has placed immense pressure on the country's transportation infrastructure, particularly its road systems, which struggle to meet the rising demand. The result is frequent traffic congestion that, to outsiders, may appear chaotic and intimidating due to the constant flow of motorbikes, cars, and other vehicles moving in seemingly unstructured patterns.

    Traffic congestion in Vietnam arises from a combination of factors, including limited infrastructure, inconsistent traffic management, and unique driving behaviors. The heavy reliance on motorbikes, narrow roads in older urban areas, and insufficient public transportation options exacerbate the situation, leading to longer commute times, increased pollution, and reduced quality of life.

    This project uses visual tools to analyze and illustrate Vietnam's traffic situation, exploring its defining characteristics and the factors contributing to the perceived chaos. By highlighting key issues and their root causes, the project aims to offer a deeper understanding of Vietnam's traffic dynamics, providing insights that could help address urban mobility challenges and reduce congestion in the future.
    """)

with col2:
    st.image("images/saigon-traffic-jam.jpg", use_column_width=True, caption="Average traffic in Saigon, Vietnam")

###

st.markdown("# Sentiment Analysis")

st.markdown("""
Sentiment analysis was conducted by applying data mining techniques to extract and analyze text data from [Reddit posts](https://www.google.com/search?q=traffic+vietnam+site%3Awww.reddit.com&rlz=1C1UEAD_enFI1059FI1059&oq=traffic+vietnam+site%3Awww.reddit.com&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDg2NDhqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8). Thirteen posts were selected from the search result, and their content along with the associated comments under each post are extracted and cleaned. From the pre-processed text data, it is possible to identifying the underlying emotions, keywords, or opinions, providing valuable insights into user perspectives of Vietnam's traffic situation.
""")

st.markdown("## N-gram analysis")

st.markdown("The processed text data is then tokenized, breaking the text into individual words or terms. Following tokenization, the text is further analyzed by dividing it into bi-grams and tri-grams, which are sequences of two and three consecutive tokens, respectively. By using these n-gram models, we can identify recurring phrases, which are useful in discovering the frequently discussed topics. This step allows for a deeper understanding of the relationships between words in the text, capturing important patterns and context that may not be evident before.")

st.markdown('A word cloud has been created based on the aggregated list of the most frequent bi-grams and tri-grams extracted from the text data. This visualization highlights several key topics, with phrases such as "red light," and "traffic light" standing out, indicating general discussions about traffic rules and road signs. Additionally, terms like "cross street" and "cross road" reflect the frequent discussions to how travelers discuss navigating or crossing the road, which directly relates to our topic. The word cloud also reveals more negative key phrases, such as "right way" (right of way, a very common issue in Vietnam where drivers take pedestrian space), "road rage," "drive wrong," and "traffic accid" (traffic accident), which suggest concerns about aggressive driving and road safety.')

st.image("plots/combined_wordcloud.png", caption="Bigram and trigram wordcloud")

st.markdown('To further enhance the visualization of important key terms, distribution bar plots of the most frequent bi-grams and tri-grams have been generated. These plots provide a clearer and more precise view of the term frequencies, making it easier to identify significant phrases and patterns. Alongside general traffic-related topics, such as "right way" (right of way) and "traffic signal," the plots also highlight concerning negative topics like "run red light," "wrong side road," and "traffic accid" ("traffic accident"). These terms suggest a strong focus on dangerous driving behaviors and safety issues in Vietnamese\'s traffic.')

col1, col2 = st.columns(spec=[0.5, 0.5])
with col1:
    st.components.v1.html(open_file("plots/bigram_freq.html"), height=400)
with col2:
    st.components.v1.html(open_file("plots/trigram_freq.html"), height=400)


st.markdown("## Topic modelling")

st.markdown('To better understand the thematic aspect of the discussions, we perform topic modelling by clustering the TF-IDF vectors of the posts/comments. This is done with some background processing (remove too rare and too frequent terms) to ensure that the semantic meaning of the text is more accurately represented. The vectorized values are divided into unique groups (hard clustering) of similar meaning using a clustering alogrithm.')

st.markdown('For each cluster, we assign the most frequent terms, including bi-grams and tri-grams, along with a sentiment score. These terms serve as key indicators for interpreting the central themes or topics within each cluster. The sentiment score, on the other hand, provides a qualitative measure of the overall tone of the cluster, allowing us to inspect whether the discussions are primarily negative or positive.')

st.components.v1.html(open_file("plots/topic_model.html"), height=1000)

st.markdown("""
The majority of the topics being discussed are negative, which is further emphasized by the key terms associated with them. For instance, one of the most frequently discussed topics revolves around *pedestrian right of way* (topic 10), which highlights concerns about the safety and treatment of pedestrians in traffic. Another common issue is *red light running* (topic 6), a common traffic violation that reflects the lack of adherence to traffic signals. *Road rage* (topic 3) also appears frequently, indicating frustration and aggressive behavior among drivers. These recurring themes suggest that there is a notable negative perception of the traffic environment, possibly reflecting the challenges and dangers that foreign visitors encounter when navigating the streets.

On the other hand, there is a group of more positive topic, which surprisingly is related to crossing the streets (*cross street*, *cross road*). Possibly, people are sharing tips and strategies for safely crossing roads in a chaotic traffic environment, which appears to be more focused on guidance and support. This contributes to a more positive-oriented discussions, contrast to the more negative discussions about traffic violations and road safety concerns.
""")

st.markdown('Overall, the Reddit discussion reveals a primarily negative sentiment for Vietnamese traffic environment. The frequent topics of discussion, such as pedestrian right of way, red light running, and road rage, highlight the safety concerns, frustrations, and aggressive behaviors that foreigners experienced while travelling in Vietnam, especially in urban cities.')

###

st.markdown("# The Current Traffic Situation")

st.markdown("## Traffic Visualization")

st.markdown("Now that we have gained some insight into how others perceive Vietnam's traffic, it's time to explore the situation firsthand. This section presents a visual representation of the traffic conditions, allowing us to better understand the challenges and patterns of traffic flow.")

st.markdown("Below is a gallery showcasing images of traffic in Vietnam, capturing the diverse and often chaotic nature of daily commuting in the country. These images give a glimpse into the challenges faced daily by drivers and pedestrians. As one can observe, there are not much organization in how Vietnamese drives, car lanes and sidewalk are overwhelmed by the motorcyclists, drivers very often weave in front of others, etc. All contributes to this chaotic scene.")

test_items = [
    dict(
        title="Slide 1",
        text="CAT",
        img="images/saigon-traffic-jam.jpg",
    ),
    dict(
        title="Slide 1",
        text="A tree in the savannah",
        img="images/la-circulation-au-vietnam-1024x682.jpg",
    ),
    dict(
        title="Slide 2",
        text="A wooden bridge in a forest in Autumn",
        img="images/maxresdefault.jpg",
    ),
    dict(
        title="Slide 3",
        text="A distant mountain chain preceded by a sea",
        img="images/Traffic-jams-in-Vietnam.jpg",
    ),
]

carousel(items=test_items, width=1, container_height=500, interval=4000)

st.markdown("This map illustrates the typical aggregated traffic intensity in Ho Chi Minh City for each half-an-hour period from 6:00 to 21:30. From this map, we can observe the peak traffic hours pattern, which occur around 6:00-9:00, 13:00-15:30, and 16:30-18:30, corresponding to morning commutes, lunchtime breaks, and evening rush hour. The map also shows that traffic congestion (represented by red spots) is present throughout most of the day, which is notable.")

# Add slider for selecting the time period
time_index = st.slider(
    "Select Time Period",
    min_value=time(6, 00), 
    max_value=time(21, 30),
    value=time(9, 00),
    step=timedelta(minutes=30),
)
time_label = '_'.join(str(time_index).split(':')[:-1])
st.components.v1.html(open_file(f"plots/traffic_flow/traffic_map_period_{time_label if time_label != '20_30' else '20_00'}.html"), height=500)

st.markdown("")

st.markdown("""
### Traffic Accidents
""")

col1, col2 = st.columns(spec=[0.3, 0.7])
with col1:
    st.markdown("As traffic volume increases, traffic accidents become more frequent. Between 2013 and 2021, reported accident cases showed a general decline, reaching their lowest point in 2021. However, casualty numbers steadily decreased during this period, with a significant drop observed between 2019 and 2020. This reduction can be attributed to the strict social distancing measures implemented during the COVID-19 pandemic.")
    st.markdown("However, in the years following the pandemic (2022-2023), as restrictions eased, both the number of accidents and the casualty rate saw a significant rise, peaking in 2022.As social distancing restrictions were lifted, people returned to their regular commuting patterns. This sudden surge in vehicle numbers created more opportunities for accidents to occur.")

with col2:
    st.components.v1.html(open_file("plots/traffic_accidents.html"), height=400)

### 

st.markdown("# Causes")

###

st.markdown("## Motorbikes")

st.markdown("Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam.")

col1, col2 = st.columns(spec=[0.5, 0.5])
with col1:
    st.components.v1.html(open_file("plots/transport_mode_percent.html"), height=400)

with col2:
    st.components.v1.html(open_file("plots/ownership_asia.html"), height=400)

st.markdown("Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam.")

col1, col2 = st.columns(spec=[0.5, 0.5])
with col1:
    st.markdown("Okay, we get it")
    st.markdown("Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam.")
    st.markdown("Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam.")
    st.markdown("Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems.")

with col2:
    st.markdown(
        f"""
        <iframe width="560" height="315" 
        src="https://www.youtube.com/embed/Sy9v6U63Nd0" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
        </iframe>
        """,
        unsafe_allow_html=True
    )

st.markdown("Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam.")

_, col1, _ = st.columns(spec=[0.01, 0.2, 0.01])

with col1:
    st.components.v1.html(open_file("plots/annual_volume.html"), height=400)

st.markdown("Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam.")

###

st.markdown("## Population Density")

st.markdown("Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam. Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam.")

_, col1, _ = st.columns(spec=[0.25, 0.45, 0.25])

with col1:
    st.components.v1.html(open_file("plots/population_density.html"), height=800)

st.markdown("Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam. Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam.")

###

st.markdown("## The Human Factor")

st.markdown("### Poor driving norms")

col1, col2 = st.columns(spec=[0.5, 0.4])
with col1: 
    st.markdown("""
    Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam.

    This project will use visual tools to demonstrate the traffic situation as well as its characteristics - what really makes the traffic chaotic? This will help the audience to understand the key issues, sources of problem, and the nature of the traffic in Vietnam. 
                
    Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. As urbanization happens so quickly, the infrastructures are struggling to handle the increased traffic. This in turn causes traffic congestion, which can seem to be very chaotic and even scary to many outsiders travelling in Vietnam. This project will use visual tools to demonstrate the traffic situation as well as its characteristics - what really makes the traffic chaotic? This will help the audience to understand the key issues, sources of problem, and the nature of the traffic in Vietnam. Vietnam's cities are growing fast, and this rapid expansion is putting a huge strain on the country's road systems. 
    """)

with col2:
    st.image("images/Traffic-Vietnam.jpg", use_column_width=True, caption="Average traffic in Saigon, Vietnam")

st.markdown("### Road Familiarity and Collective Understanding")

st.markdown(" The traffic feels chaotic due to the sheer number of vehicles and the seeming disregard for formal rules. Many Vietnamese drivers are highly familiar with local roads and adopt riskier driving behaviors, such as weaving through gaps or speeding through intersections. Drivers also have high collective understanding to understand how the others are driving and adjust their movement accordingly. This of course introduces a level of unpredictability for tourists or non-local drivers unfamiliar with these patterns, but in fact is “organized” in some sort of way.")

_, col1, _ = st.columns(spec=[0.3, 0.4, 0.3])
with col1: 
    st.markdown(
        f"""
        <iframe width="560" height="315" 
        src="https://www.youtube.com/embed/fm0cX7P6PSw" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
        </iframe>
        """,
        unsafe_allow_html=True
    )

st.markdown(" The traffic feels chaotic due to the sheer number of vehicles and the seeming disregard for formal rules. Many Vietnamese drivers are highly familiar with local roads and adopt riskier driving behaviors, such as weaving through gaps or speeding through intersections. Drivers also have high collective understanding to understand how the others are driving and adjust their movement accordingly. This of course introduces a level of unpredictability for tourists or non-local drivers unfamiliar with these patterns, but in fact is “organized” in some sort of way.")

st.markdown("# Conclusion")

st.markdown(" The traffic feels chaotic due to the sheer number of vehicles and the seeming disregard for formal rules. Many Vietnamese drivers are highly familiar with local roads and adopt riskier driving behaviors, such as weaving through gaps or speeding through intersections. Drivers also have high collective understanding to understand how the others are driving and adjust their movement accordingly. This of course introduces a level of unpredictability for tourists or non-local drivers unfamiliar with these patterns, but in fact is “organized” in some sort of way.")