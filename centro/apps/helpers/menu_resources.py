
def menuResources(data: list, list_data: list, model: any, last_id: int, id_padre=0):
    id_last_resources = last_id
    
    for i in data:
        if id_padre != 0:
            list_data.append(model(
                path=i['path'], link=i['link'], icono=i['icono'], method=i['method'], titulo=i['titulo'], id_padre=id_padre, id=list_data[-1].id +1 ))
        else:
            list_data.append(model(
                path=i['path'], link=i['link'], icono=i['icono'], method=i['method'], titulo=i['titulo'], id_padre=i['id_padre'], id=id_last_resources+1))
        id_last_resources += 1
        if 'items' in i and len(i['items']) > 0:
            menuResources(data=i['items'], list_data=list_data, model=model,
                          last_id=id_last_resources, id_padre=list_data[-1].id)
    return list_data
