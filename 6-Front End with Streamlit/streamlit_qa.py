import streamlit as st
import requests, json
from annotated_text import annotated_text
st.set_page_config(
    page_title="Naturalangue",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
    )

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    
def icon(icon_name):
    st.markdown(f'<i class="fa fa-external-link" aria-hidden="true"></i>', unsafe_allow_html=True)

remote_css("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")

st.markdown('<h1 style="text-align: center">Covid QA</h1>', unsafe_allow_html=True)

st.sidebar.header("Options")
top_k_reader = st.sidebar.slider("Max. number of answers", min_value=1, max_value=10, value=3, step=1)
top_k_retriever = st.sidebar.slider("Max. number of documents from retriever", min_value=1, max_value=10, value=3, step=1)


st.markdown('<h3>Question</h3>', unsafe_allow_html=True)
question = st.text_input("Put your query", value="What are the symptoms of COVID")
button = st.button('Get Answer')
st.text("")
st.text("")

if button:
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = {
         'question': question, 'num_answers': top_k_reader, 'num_docs': top_k_retriever
    }
    response = requests.post('http://host.docker.internal:85/query', headers=headers, data=json.dumps(data))
    result = response.json()

    print(result)
    #result = {'answer': {'query': 'who is the father of arya', 'no_ans_gap': -9.128407001495361, 'answers': [{'answer': 'Dr Shanthi Viswanathan', 'score': -1.2638678550720215, 'probability': 0.006202994845807552, 'context': ' period with plans needed for an exit strategy in the future.$$$Dr Shanthi Viswanathan contributed to the study design, conceptualization, acquisition', 'offset_start': 64, 'offset_end': 86, 'offset_start_in_doc': 28757, 'offset_end_in_doc': 28779, 'document_id': 'ab8a910156406e85534af294ecc0b83d', 'meta': {'sha': 'dca07dbefc86802cb7ccdbbca740aea9e4ea0433', 'title': 'Management of Idiopathic CNS inflammatory diseases during the COVID-19 pandemic: Perspectives and strategies for continuity of care from a South East Asian Center with limited resources.', 'publish_time': '2020-07-03', 'authors': 'Viswanathan, S.', 'url': 'https://doi.org/10.1016/j.msard.2020.102353; https://www.sciencedirect.com/science/article/pii/S2211034820304284?v=s5; https://www.ncbi.nlm.nih.gov/pubmed/32653804/; https://api.elsevier.com/content/article/pii/S2211034820304284', 'abstract': "The Covid-19 pandemic poses a grave health management challenge globally of unprecedented nature. Management of idiopathic Central Nervous system inflammatory disorders (iCNSID) such as Multiple sclerosis, Neuromyelitis optica and its spectrum disorders and related conditions during this pandemic needs to be addressed with affirmative and sustainable strategies in order to prevent disease related risks, medication related complications and possible COVID-19 disease associated effects. Global international iCNSIDs agencies and recent publications are attempting to address this but such guidance is not available in South East Asia. Here we outline prospectively qualitatively and quantitatively novel strategies at a tertiary center in Malaysia catering for neuroimmunological disorders despite modest resources during this pandemic. In this retrospective study with longitudinal follow-up, we describe stratification of patients for face to face versus virtual visits in the absence of formal teleneurology, stratification of patients for treatment according to disease activity, rescheduling, deferring initiation or extending treatment intervals of certain disease modifying therapies(DMT's) or immunosuppressants(IS), especially those producing lymphocyte depletion in MS and the continuation of IS in patients with NMO/NMOSD. Furthermore, we highlight the use off-label treatments such as Intravenous immunoglobulins/rituximab,bridging interferons/Teriflunomide temporarily replacing more potent DMT choices,supply challenges of IS/DMT'sand tailoring blood watches and neuroimaging surveillance based on the current health needs to stave off the pandemic and prevent at risk patients with iCNSID/health care workers from possibly being exposed to the COVID-19."}}, {'answer': 'Guthy Jackson', 'score': -1.3159641027450562, 'probability': 0.010259977541863918, 'context': 'al MS Society(USA),the Association of British Neurologists(ABN), the Guthy Jackson Charitable Foundation Website (GJCFW) as well as current literature', 'offset_start': 69, 'offset_end': 82, 'offset_start_in_doc': 6089, 'offset_end_in_doc': 6102, 'document_id': 'ab8a910156406e85534af294ecc0b83d', 'meta': {'sha': 'dca07dbefc86802cb7ccdbbca740aea9e4ea0433', 'title': 'Management of Idiopathic CNS inflammatory diseases during the COVID-19 pandemic: Perspectives and strategies for continuity of care from a South East Asian Center with limited resources.', 'publish_time': '2020-07-03', 'authors': 'Viswanathan, S.', 'url': 'https://doi.org/10.1016/j.msard.2020.102353; https://www.sciencedirect.com/science/article/pii/S2211034820304284?v=s5; https://www.ncbi.nlm.nih.gov/pubmed/32653804/; https://api.elsevier.com/content/article/pii/S2211034820304284', 'abstract': "The Covid-19 pandemic poses a grave health management challenge globally of unprecedented nature. Management of idiopathic Central Nervous system inflammatory disorders (iCNSID) such as Multiple sclerosis, Neuromyelitis optica and its spectrum disorders and related conditions during this pandemic needs to be addressed with affirmative and sustainable strategies in order to prevent disease related risks, medication related complications and possible COVID-19 disease associated effects. Global international iCNSIDs agencies and recent publications are attempting to address this but such guidance is not available in South East Asia. Here we outline prospectively qualitatively and quantitatively novel strategies at a tertiary center in Malaysia catering for neuroimmunological disorders despite modest resources during this pandemic. In this retrospective study with longitudinal follow-up, we describe stratification of patients for face to face versus virtual visits in the absence of formal teleneurology, stratification of patients for treatment according to disease activity, rescheduling, deferring initiation or extending treatment intervals of certain disease modifying therapies(DMT's) or immunosuppressants(IS), especially those producing lymphocyte depletion in MS and the continuation of IS in patients with NMO/NMOSD. Furthermore, we highlight the use off-label treatments such as Intravenous immunoglobulins/rituximab,bridging interferons/Teriflunomide temporarily replacing more potent DMT choices,supply challenges of IS/DMT'sand tailoring blood watches and neuroimaging surveillance based on the current health needs to stave off the pandemic and prevent at risk patients with iCNSID/health care workers from possibly being exposed to the COVID-19."}}, {'answer': 'Abboud', 'score': -2.4730982780456543, 'probability': 0.009177026338875294, 'context': 'VIG and TPE was thought to be safer. 9, 10, 11, 22 Brownlee W et al and Abboud H et al highlighted the importance of cautious IS continuation in patie', 'offset_start': 72, 'offset_end': 78, 'offset_start_in_doc': 23716, 'offset_end_in_doc': 23722, 'document_id': 'ab8a910156406e85534af294ecc0b83d', 'meta': {'sha': 'dca07dbefc86802cb7ccdbbca740aea9e4ea0433', 'title': 'Management of Idiopathic CNS inflammatory diseases during the COVID-19 pandemic: Perspectives and strategies for continuity of care from a South East Asian Center with limited resources.', 'publish_time': '2020-07-03', 'authors': 'Viswanathan, S.', 'url': 'https://doi.org/10.1016/j.msard.2020.102353; https://www.sciencedirect.com/science/article/pii/S2211034820304284?v=s5; https://www.ncbi.nlm.nih.gov/pubmed/32653804/; https://api.elsevier.com/content/article/pii/S2211034820304284', 'abstract': "The Covid-19 pandemic poses a grave health management challenge globally of unprecedented nature. Management of idiopathic Central Nervous system inflammatory disorders (iCNSID) such as Multiple sclerosis, Neuromyelitis optica and its spectrum disorders and related conditions during this pandemic needs to be addressed with affirmative and sustainable strategies in order to prevent disease related risks, medication related complications and possible COVID-19 disease associated effects. Global international iCNSIDs agencies and recent publications are attempting to address this but such guidance is not available in South East Asia. Here we outline prospectively qualitatively and quantitatively novel strategies at a tertiary center in Malaysia catering for neuroimmunological disorders despite modest resources during this pandemic. In this retrospective study with longitudinal follow-up, we describe stratification of patients for face to face versus virtual visits in the absence of formal teleneurology, stratification of patients for treatment according to disease activity, rescheduling, deferring initiation or extending treatment intervals of certain disease modifying therapies(DMT's) or immunosuppressants(IS), especially those producing lymphocyte depletion in MS and the continuation of IS in patients with NMO/NMOSD. Furthermore, we highlight the use off-label treatments such as Intravenous immunoglobulins/rituximab,bridging interferons/Teriflunomide temporarily replacing more potent DMT choices,supply challenges of IS/DMT'sand tailoring blood watches and neuroimaging surveillance based on the current health needs to stave off the pandemic and prevent at risk patients with iCNSID/health care workers from possibly being exposed to the COVID-19."}}], 'node_id': 'Reader'}}

    for each in result['answer']['answers']:
        title = each['meta']['title']
        url = each['meta']['url'].split(';')[0]
        tokens = []
        tokens.append(each['context'][:each['offset_start']-1])
        tokens.append( 
            (each['context'][each['offset_start']:each['offset_end']], 'ANS', '#faa')
        )
        tokens.append(each['context'][each['offset_end']:])
        col1,col2 = st.beta_columns([5,1])
        col1.markdown(f'<span style="font-size: 16; font-weight:bold;">{title}</span><a href={url} target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>', unsafe_allow_html=True)
        col2.markdown(f'<input type="button" value="Confidence: {int(each["probability"]*100)}%">', unsafe_allow_html=True)
        st.text("")
        col1, col2 = st.beta_columns([2,4])
        col1.markdown(f'<span style="font-size: 16; font-weight:bold;">Publish time: {each["meta"]["publish_time"]}\
                    <br>Authors: {each["meta"]["authors"]}</span>', unsafe_allow_html=True)
        annotated_text(*tokens)

