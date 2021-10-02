def calc_average():
    '''Er worden vijf scores ingevoerd
vervolgens ga je van die vijf scores het gemiddelde berekenen'''
    score1 = float(input('Voer de behaalde score in'))
    score2 = float(input('Voer de behaalde score in'))
    score3 = float(input('Voer de behaalde score in'))
    score4 = float(input('Voer de behaalde score in'))
    score5 = float(input('Voer de behaalde score in'))
    
    gemiddelde = (score1+score2+score3+score4+score5)/5
    return(gemiddelde)
def main():
    print(calc_average())
main()

def determine_grade():
    '''Er wordt een score ingevoerd en deze wordt vervolgens terug gestuurd als een letter voor je score'''
    score = float(input('van welke score wil je een letter als score?'))
    if score >=90 and score <=100:
        print('A')
    elif score >=80 and score <=89:
        print('B')
    elif score >=70 and score <=79:
        print('C')
    elif score >=60 and score <=69:
        print('D')
    elif score <= 60:
        print('F')
def main():
    determine_grade()
main()
    
