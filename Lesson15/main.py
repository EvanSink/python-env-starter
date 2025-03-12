from nrclex import NRCLex
import customer_survey as cs

def dataAnalysis(data):
    print(data)
    text1 = NRCLex(data)
    rawE = data.raw_emotion_scores
    topE = data.top_emotions

def main():

    survey_result_str = cs.survey()
    dataAnalysis(survey_result_str)
    pass
