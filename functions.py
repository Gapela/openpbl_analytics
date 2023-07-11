import json
from bd import bd
from statistics import mean

###################
### POST METHOD ###
###################

def get_all():
    '''gets all data in the firestore and append into a list.
    this will work with small data base, but may struggle with larger databases.'''

    docs = bd.collection(u'sessions').stream()
    data = []
    
    for doc in docs:
        data.append(doc.to_dict())
    
    return data

def get_one_email(email):
    '''
    - get one session by email.
    - returns a list.
    '''
    docs = bd.collection(u'sessions').where(u'user_email', u'==', email).stream()

    for doc in docs:
        data = doc.to_dict()
    
    return data

#######################
### FUNCTIONS GERAL ###
#######################

def dados_quiz(dados):
    '''
    - make a count about questions: total, corrects and wrongs.
    - returns a dict. and values returns int
    '''
    quiz_list = dados['quiz_list']

    results = [a['result'] for a in quiz_list]

    total = len(results)
    corretas = results.count(1)
    incorretas = results.count(0)

    response = {
        "total": total,
        "corretas": corretas,
        "incorretas": incorretas
    }

    return response


def media_alunos_geral():
    '''
    - import all data from cloud firestore.
    - checks each quiz_list student.
    - response is a dict: total
        - total (mean)
        - corrects(mean)
        - incorrects(mean)
    '''
    dados_alunos = bd.collection(u'sessions').stream()

    total = []
    corretas = []
    incorretas = []

    for aluno in dados_alunos:
        aluno_dict = dados_quiz(aluno.to_dict())

        total.append(aluno_dict['total'])
        corretas.append(aluno_dict['corretas'])
        incorretas.append(aluno_dict['incorretas'])

    response = {
        "total": round(mean(total)),
        "corretas": round(mean(corretas)),
        "incorretas": round(mean(incorretas))
    }

    return response