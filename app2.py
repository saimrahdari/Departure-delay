import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go


def load_unique_values():
    unique_airline_codes = ['UA', 'DL', 'NK', 'WN', 'AA', 'YX', 'AS', 'B6', 'OH', 'G4', 'EV', 'OO', '9E', 'MQ',
                            'F9', 'YV', 'QX', 'HA']
    unique_origins = ['FLL', 'MSP', 'DEN', 'MCO', 'DAL', 'DCA', 'HSV', 'IAH', 'SEA', 'ATL', 'RDU', 'MDW', 'BDL',
                      'BWI', 'STT', 'SRQ', 'JFK', 'GRR', 'DFW', 'CLT', 'ORD', 'LAS', 'TUL', 'USA', 'SLC', 'BNA',
                      'AUS', 'IND', 'MHT', 'SFO', 'PRC', 'BOS', 'LAX', 'SMF', 'DTW', 'SAT', 'MSY', 'CMH', 'STL',
                      'SJU', 'PHX', 'TPA', 'LGA', 'PHL', 'GRK', 'ILM', 'JLN', 'MKE', 'BIL', 'BLI', 'CHS', 'RIC',
                      'GSO', 'MCI', 'EWR', 'ELP', 'SDF', 'HPN', 'SAN', 'BHM', 'SJC', 'ASE', 'HNL', 'MAF', 'BUF',
                      'TUS', 'SYR', 'MSN', 'FAT', 'FWA', 'LAN', 'ABI', 'ICT', 'CMI', 'OAK', 'IAD', 'EUG', 'MIA',
                      'CHA', 'BTV', 'RSW', 'PDX', 'SNA', 'PIT', 'OGG', 'HRL', 'BIS', 'SHR', 'BOI', 'RNO', 'GSP',
                      'MLB', 'GRB', 'CRW', 'LGB', 'OKC', 'PVD', 'YAK', 'CID', 'FSD', 'HYS', 'VPS', 'ROC', 'SAV',
                      'CLE', 'RDD', 'ANC', 'DVL', 'SWO', 'BUR', 'PIR', 'HOU', 'PBI', 'MLI', 'AZA', 'MKG', 'PNS',
                      'MYR', 'GTF', 'LSE', 'RDM', 'ORF', 'KOA', 'MQT', 'COS', 'CVG', 'MOB', 'AVL', 'BTR', 'JNU',
                      'CDC', 'SPS', 'ECP', 'JAX', 'SBN', 'RAP', 'AMA', 'JMS', 'SFB', 'ABQ', 'ALB', 'BGM', 'MGM',
                      'MEM', 'ONT', 'TVC', 'GEG', 'OMA', 'ISP', 'DLH', 'PIE', 'PSP', 'ACY', 'BJI', 'LBB', 'SHV',
                      'TTN', 'PIA', 'GNV', 'PWM', 'BZN', 'BRW', 'MFR', 'GPT', 'ATW', 'DSM', 'CKB', 'SGU', 'SBA',
                      'OTZ', 'BGR', 'XNA', 'CAE', 'SGF', 'PGD', 'VLD', 'CPR', 'LIH', 'JAN', 'OAJ', 'ABE', 'EGE',
                      'CRP', 'FNT', 'WRG', 'FCA', 'CHO', 'MRY', 'SCE', 'AEX', 'MCW', 'RST', 'SIT', 'BMI', 'ACV',
                      'GCC', 'LFT', 'ITO', 'ABY', 'GRI', 'BPT', 'APN', 'TLH', 'FSM', 'ALO', 'FAY', 'GJT', 'IAG',
                      'FLG', 'LBE', 'CAK', 'BFL', 'VEL', 'STX', 'TYS', 'EYW', 'AVP', 'KTN', 'EVV', 'BRO', 'SWF',
                      'LIT', 'GGG', 'MSO', 'PSC', 'SLN', 'SBP', 'BIH', 'MLU', 'HOB', 'DAY', 'DBQ', 'ROW', 'LEX',
                      'PIH', 'EWN', 'ESC', 'SUX', 'PAE', 'CNY', 'CDV', 'COU', 'LBF', 'MFE', 'PSE', 'LAR', 'FAI',
                      'SCC', 'MTJ', 'SJT', 'AGS', 'MDT', 'ELM', 'HDN', 'MOT', 'IDA', 'FAR', 'GFK', 'JAC', 'LAW',
                      'SUN', 'IMT', 'LCH', 'CLL', 'PHF', 'TRI', 'BET', 'PBG', 'BQN', 'BRD', 'DAB', 'DRO', 'STS',
                      'ROA', 'DDC', 'INL', 'ORH', 'TXK', 'CWA', 'BFF', 'DHN', 'SCK', 'LRD', 'BTM', 'IPT', 'PIB',
                      'HYA', 'PVU', 'LBL', 'AZO', 'ACK', 'YUM', 'DRT', 'COD', 'LNK', 'SHD', 'CIU', 'HLN', 'LWB',
                      'MEI', 'SAF', 'CYS', 'ABR', 'LCK', 'RKS', 'GCK', 'LWS', 'EAR', 'GTR', 'CSG', 'RFD', 'BLV',
                      'TYR', 'CMX', 'PAH', 'JST', 'TOL', 'PSG', 'MHK', 'YKM', 'EAT', 'SPI', 'BQK', 'TWF', 'PUB',
                      'DEC', 'ACT', 'HHH', 'PLN', 'HIB', 'GUC', 'ITH', 'OME', 'MBS', 'BFM', 'ADQ', 'LYH', 'RHI',
                      'ALW', 'DLG', 'ALS', 'MMH', 'XWA', 'SPN', 'MVY', 'ERI', 'PGV', 'HGR', 'ATY', 'SMX', 'HVN',
                      'CGI', 'BKG', 'DIK', 'AKN', 'RIW', 'FLO', 'GUM', 'EAU', 'TBN', 'HTS', 'PSM', 'EKO', 'PUW',
                      'FOD', 'CDB', 'WYS', 'OTH', 'VCT', 'PPG', 'OGS', 'ISN', 'ART', 'ILG', 'OWB', 'OGD', 'STC',
                      'GST', 'UIN', 'ADK']
    unique_destinations = ['EWR', 'SEA', 'MSP', 'SFO', 'DFW', 'OKC', 'BOS', 'DCA', 'LAX', 'FAI', 'BDL', 'BNA',
                           'ATL', 'MSY', 'IAH', 'ORD', 'CHS', 'ACY', 'PNS', 'RDU', 'IAD', 'GEG', 'SFB', 'RNO',
                           'ABQ', 'BOI', 'MCI', 'TPA', 'BIL', 'TUS', 'DTW', 'DAB', 'MHT', 'DEN', 'LGA', 'SAT',
                           'SLC', 'DAL', 'MCO', 'CLT', 'SAN', 'RSW', 'ELP', 'JFK', 'PHL', 'PWM', 'SBP', 'KOA',
                           'GSP', 'LAS', 'VLD', 'MIA', 'MKE', 'PSP', 'OAK', 'BHM', 'PDX', 'MFR', 'MFE', 'VPS',
                           'ORF', 'AUS', 'MDW', 'PHX', 'PIT', 'PIE', 'OMA', 'BUR', 'CID', 'BLI', 'EGE', 'ALB',
                           'EWN', 'AVL', 'BQN', 'MOB', 'IND', 'BUF', 'SDF', 'FLL', 'SJU', 'HNL', 'GRR', 'HLN',
                           'MEM', 'SNA', 'BWI', 'LGB', 'SAV', 'GFK', 'SMF', 'CVG', 'LIH', 'SGU', 'TLH', 'RIC',
                           'CDV', 'MSO', 'SRQ', 'STL', 'LEX', 'LIT', 'ISP', 'OTZ', 'HSV', 'ONT', 'PBI', 'HOU',
                           'JAC', 'ANC', 'MLB', 'JNU', 'ACY', 'SYR', 'MLI', 'BTR', 'CAK', 'LBE', 'CRW', 'IAH',
                           'CAE', 'TYS', 'PVD', 'RAP', 'ATW', 'MYR', 'SBA', 'ROC', 'AVP', 'GRB', 'CPR', 'ASE',
                           'LFT', 'SAF', 'FAT', 'GRK', 'BMI', 'CHO', 'DLH', 'FCA', 'SPI', 'BTV', 'ECP', 'HSV',
                           'MLB', 'ISP', 'CRP', 'MDT', 'MFR', 'OAJ', 'AVP', 'MRY', 'GPT', 'TUL', 'AMA', 'GJT',
                           'RAP', 'LAW', 'FCA', 'LBB', 'LFT', 'DRO', 'MTJ', 'BIL', 'SPI', 'MEI', 'SIT', 'HLN',
                           'JMS', 'DVL', 'INL', 'MKG', 'EKO', 'IDA', 'BET', 'ALW', 'PLN', 'BJI', 'CIU', 'BTM',
                           'BGM', 'PIR', 'EAU', 'IMT', 'HIB', 'ACV', 'RHI', 'ESC', 'SUX', 'MOT', 'ECP', 'AVP',
                           'LSE', 'ITH', 'GCC', 'CPR', 'PSC', 'BPT', 'BFL', 'BFF', 'RKS', 'COD', 'IPT', 'RFD',
                           'YKM', 'PSE', 'HYS', 'CMX', 'DLH', 'ABR', 'HLN', 'RFD', 'TYR', 'CMX', 'PAH', 'JST',
                           'TOL', 'PSG', 'MHK', 'YKM', 'EAT', 'SPI', 'BQK', 'TWF', 'PUB', 'DEC', 'ACT', 'HHH',
                           'PLN', 'HIB', 'GUC', 'ITH', 'OME', 'MBS', 'BFM', 'ADQ', 'LYH', 'RHI', 'ALW', 'DLG',
                           'ALS', 'MMH', 'XWA', 'SPN', 'MVY', 'ERI', 'PGV', 'HGR', 'ATY', 'SMX', 'HVN', 'CGI',
                           'BKG', 'DIK', 'AKN', 'RIW', 'FLO', 'GUM', 'EAU', 'TBN', 'HTS', 'PSM', 'EKO', 'PUW',
                           'FOD', 'CDB', 'WYS', 'OTH', 'VCT', 'PPG', 'OGS', 'ISN', 'ART', 'ILG', 'OWB', 'OGD',
                           'STC', 'GST', 'UIN', 'ADK']
    return unique_airline_codes, unique_origins, unique_destinations


with open('dep_delay_model.pkl', 'rb') as file:
    dep_delay_model = pickle.load(file)
with open('arr_delay_model.pkl', 'rb') as file:
    arr_delay_model = pickle.load(file)
with open('reasons_model.pkl', 'rb') as file:
    reasons_model = pickle.load(file)

st.title('Flight Delay Prediction')
load_unique_values()

unique_airline_codes, unique_origins, unique_destinations = load_unique_values()

airline_code = st.selectbox('Airline Code', options=load_unique_values()[0])  # Using unique airline codes
origin = st.selectbox('Origin', options=load_unique_values()[1])  # Using unique origins
dest = st.selectbox('Destination', options=load_unique_values()[2])  # Using unique destinations
dep_hour = st.slider('Departure Hour', 0, 23, 12)
arr_hour = st.slider('Arrival Hour', 0, 23, 12)
air_time = st.number_input('Air Time (minutes)', value=120)

if st.button("Predict Delays"):

    X_input_dep = pd.DataFrame({
        'ORIGIN': [origin],
        'AIRLINE_CODE': [airline_code],
        'DEST': [dest],
        'DEP_HOUR': [dep_hour],
        'ARR_HOUR': [arr_hour],
        'AIR_TIME': [air_time]
    })

    predicted_dep_delay = dep_delay_model.predict(X_input_dep)[0]
    st.write(f'Predicted Departure Delay: {predicted_dep_delay:.2f} minutes')

    X_input_arr = X_input_dep.copy()
    X_input_arr['DEP_DELAY'] = predicted_dep_delay

    predicted_arr_delay = arr_delay_model.predict(X_input_arr)[0]
    st.write(f'Predicted Arrival Delay: {predicted_arr_delay:.2f} minutes')

    total_delay = predicted_dep_delay + predicted_arr_delay
    st.write(f'Total Delay: {total_delay:.2f} minutes')

    X_input_reasons = X_input_arr.copy()
    X_input_reasons['ARR_DELAY'] = predicted_arr_delay
    X_input_reasons['TOTAL_DELAY'] = total_delay

    try:
        prediction = reasons_model.predict(X_input_reasons)
        prediction_df = pd.DataFrame(prediction, columns=['CARRIER', 'LATE_AIRCRAFT', 'NAS', 'SECURITY', 'WEATHER'])

        st.write("Predicted Delay Reasons:")
        st.write(prediction_df)
        fig_pie = go.Figure(data=[
            go.Pie(labels=prediction_df.columns, values=prediction_df.iloc[0])
        ])
        fig_pie.update_layout(title='Predicted Delay Reasons Percentages')
        st.plotly_chart(fig_pie)

    except Exception as e:
        st.error(f"Error predicting delay reasons: {e}")

   
