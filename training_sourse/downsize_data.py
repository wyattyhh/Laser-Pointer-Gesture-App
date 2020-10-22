import pickle

ges_num = 100


def store(data, type, file_name):
    temp = {'X': list(), 'Y': list()}
    for i in range(0, ges_num):
        temp['X'].append(data[i])
        temp['Y'].append(type)
    with open(file_name, "wb") as scores:
        pickle.dump(temp, scores)

def downsizing(list):
    while len(list) > 100:
        list = [list[i] for i in range(len(list)) if i % 2 == 0]
    return list

def downsize_data(type):
    file_name = 'training_sourse/' + type + '.pickle'
    with open(file_name, 'rb') as f:
        obs = pickle.load(f)
    ges_data = []
    ges_data_temp = []
    for j in range(0, 100):
        ges_data_temp.append(obs['X'][j]) # 100 groups of points
    for i in ges_data_temp:
        j = downsizing(i)
        ges_data.append(j)
    file_name = 'training_sourse/' + type + '_ds.pickle'
    store(ges_data, type, file_name)
    print('File downsizing completed. File Path:'+file_name)

def test(type):
    file_name = 'training_sourse/' + type + '_ds.pickle'
    with open(file_name, 'rb') as f:
        obs = pickle.load(f)
    ges_data = []
    ges_data_temp = []
    for j in range(0, 100):
        ges_data_temp.append(obs['X'][j])
    print('Test List Length: ' + str(len(ges_data_temp[1])))

def do_task(type):
    downsize_data(type)
    test(type)


gestures = ['UPDOWN','DOWNUP','LEFTRIGHT','RIGHTLEFT','CROSS','CIRCLE']
for i in gestures:
    do_task(i)