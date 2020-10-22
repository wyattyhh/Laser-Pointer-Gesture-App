import pickle

from HiddenMarkovModel import HiddenMarkovModel

ges_dict = None

def initML_pw():
    training_file = ['UPDOWN', 'DOWNUP', 'DOWNRIGHT', 'DOWNLEFT', 'UPRIGHT', 'UPLEFT']
    all_models = []
    for file in training_file:
        file_name = 'training_sourse/' + file + '.pickle'
        with open(file_name, 'rb') as f:
            obs = pickle.load(f)
        temp = {'X': list(), 'Y': list()}
        for j in range(0, 100):
            temp['X'].append(obs['X'][j])
            temp['Y'].append(obs['Y'][j])
        if file == 'CIRCLE':
            all_models.append(HiddenMarkovModel(4, file, temp))
        else:
            all_models.append(HiddenMarkovModel(2, file, temp))
    return all_models


def initML_main(dict):

    # convert keys of gesture dictionary to a list
    ges_list = []
    for key,value in dict.items():
        if value and value > 0:
            ges_list.append(key.text().upper())

    all_models = []
    for file in ges_list:
        file_name = 'training_sourse/' + file + '.pickle'
        with open(file_name, 'rb') as f:
            obs = pickle.load(f)
        temp = {'X': list(), 'Y': list()}
        for j in range(0, 100):
            temp['X'].append(obs['X'][j])
            temp['Y'].append(obs['Y'][j])
        if file == 'CIRCLE':
            all_models.append(HiddenMarkovModel(4, file, temp))
        else:
            all_models.append(HiddenMarkovModel(2, file, temp))
    return dict, all_models



