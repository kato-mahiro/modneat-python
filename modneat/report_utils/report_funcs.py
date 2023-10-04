import re
import modneat

def load_experiment_settings(path_of_command_file:str) -> dict:
    #load experiment settings
    setting_path = path_of_command_file
    with open(setting_path) as f:
        settings = f.read()
    matches=re.findall(r'(\w+)=(\S+)', settings) #キーと値のペアを取得
    tmp_dict = {key: value for key, value in matches}

    # dict itemのうち、"'something'" のような文字列を 'something' に変換
    experiment_settings = {}
    for key, value in tmp_dict.items():
        after = re.findall(r'["\'](.*?)["\']', value)
        if(len(after) == 0):
            experiment_settings[key] = value
        else:
            experiment_settings[key] = after[0]
    
    return experiment_settings

def get_speciated_population(population) -> dict:
    #種ごとの代表個体が入ったdict{種ID: [Member, Member, ...]}を取得
    #各Memberはfitnessの降順にソートされている
    #ベスト、25%、50%、75%、ワーストの5個体が入っている
    populations = population
    s = populations.species
    species_num = len(s.species)
    species_id_set = s.species.keys()
    print(species_id_set)
    speciated_dict = {}
    #singleSpeciesObject = list(s.species.items())[0][1]
    #print(singleSpeciesObject.members)
    for sid in species_id_set:
        member_list = list(s.species[sid].members.values())
        member_list.sort(key=lambda x: x.fitness, reverse=True)

        selected_member_list = []
        selected_member_list.append(member_list[0])
        selected_member_list.append(member_list[ int(len(member_list)*0.25) ])
        selected_member_list.append(member_list[ int(len(member_list)*0.5) ])
        selected_member_list.append(member_list[ int(len(member_list)*0.75) ])
        selected_member_list.append(member_list[-1])

        speciated_dict[sid] = selected_member_list
    return speciated_dict

def get_best_of_each_species(population) -> dict:
    #種ごとのベスト個体が入ったdict{種ID: Member}を取得
    populations = population
    s = populations.species
    species_num = len(s.species)
    species_id_set = s.species.keys()
    print(species_id_set)
    speciated_dict = {}
    #singleSpeciesObject = list(s.species.items())[0][1]
    #print(singleSpeciesObject.members)
    for sid in species_id_set:
        member_list = list(s.species[sid].members.values())
        member_list.sort(key=lambda x: x.fitness, reverse=True)
        best_member = member_list[0]

        speciated_dict[sid] = best_member
    return speciated_dict