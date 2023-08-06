import os
import json
import requests
from urllib.parse import urlparse, parse_qs
import configparser
from datetime import date
import pandas as pd


def get_ms_config(ini_file, tgt_svc):
    config = configparser.ConfigParser()
    config.read(ini_file)
    base_url = config[tgt_svc]['base_url']
    token_params = {
        "grant_type": "CREDENTIAL",
        "app_id": config[tgt_svc]['app_id'],
        "app_secret": config[tgt_svc]['app_secret'],
        "tgt_svc": config[tgt_svc]['tgt_svc'],
        "user_id": config[tgt_svc]['user_id']
    }
    return base_url, token_params


def getToken(base_url, params):
    body = json.dumps(params)
    headers = {
        'Content-type': 'application/json'
    }
    url = base_url + 'token'
    r = requests.post(url, data=body, headers=headers)
    # print (r.json())
    with open('response_token_body.json', 'w') as outfile:
        json.dump(r.json(), outfile, ensure_ascii=False)
    access_token = r.json().get("access_token")
    print('{url} 请求响应时间：{used_time}, access_token={access_token}' \
          .format(url=url, used_time=r.elapsed.total_seconds(), access_token=access_token))
    return access_token


def getData(access_token, url, save_res_to_file=False):
    headers = {
        'Content-type': 'application/json',
        'X-ENP-AUTH': access_token
    }
    # print (url)
    r = requests.get(url, headers=headers)
    print('{0} 请求响应时间：{1}'.format(url, r.elapsed.total_seconds()))
    if r.status_code != requests.codes.ok:
        print('erorr:')
        print(r.text)
    if save_res_to_file:
        with open('response_body.json', 'w') as outfile:
            json.dump(r.json(), outfile, ensure_ascii=False)
    data = r.json().get('data')
    result = []
    for record in data:
        result.append(record['attributes'])

    if len(data) > 0:
        next_link = r.json().get('links').get('next')
    else:
        next_link = ''
    return result, next_link


# 获取数据湖数据的funcation
def get_datalake_data(tgt_svc, api_path, load_all=False, save_res_to_file=False):
    base_url, token_params = get_ms_config('envision.ini', tgt_svc)
    access_token = getToken(base_url, token_params)
    url = base_url + api_path
    result = []
    result, next_link = getData(access_token, url, save_res_to_file)
    while load_all and next_link != None:
        data, next_link = getData(access_token, next_link)
        result = result + data
    return result


# 获取挂接服务数据的function
def get_proxy_api_data(tgt_svc, api_path, return_data_path=None):
    base_url, token_params = get_ms_config('envision.ini', tgt_svc)
    access_token = getToken(base_url, token_params)
    #print('access_token:'+access_token)
    url = base_url + api_path
    headers = {
        'Content-type': 'application/json',
        'X-ENP-AUTH': access_token
    }
    r = requests.get(url, headers=headers)
    print('{0} 请求响应时间：{1}'.format(url, r.elapsed.total_seconds()))
    if r.status_code != requests.codes.ok:
        print('erorr:')
        print(r.text)
    if not return_data_path:
        return r.json()
    result = r.json().get(return_data_path)
    return result


def post_to_datalake_data_from_ex_server(access_token, url, body={}, save_res_to_file=False):
    headers = {
        'Content-type': 'application/json',
        'X-ENP-AUTH': access_token
    }
    # print (url)
    body = json.dumps(body)
    r = requests.post(url, headers=headers, data=body)
    print('{0} 请求响应时间：{1}'.format(url, r.elapsed.total_seconds()))
    if r.status_code != requests.codes.ok:
        print('erorr:')
        print(r.text)
    if save_res_to_file:
        with open('response_body.json', 'w') as outfile:
            json.dump(r.json(), outfile, ensure_ascii=False)
    data = r.json().get('data')
    result = []
    for record in data:
        result.append(record['attributes'])

    if len(data) > 0:
        next_link = r.json().get('links').get('next')
    else:
        next_link = ''
    return result, next_link


# 获取挂接服务数据的function
def get_datalake_data_from_ex_server(tgt_svc, prnName, lakeTableName, body={}, load_all=False, save_res_to_file=False):
    base_url, token_params = get_ms_config('envision.ini', tgt_svc)
    access_token = getToken(base_url, token_params)
    #print('access_token:' +access_token)
    url = base_url + 'it/lightning/exsap/api/oa/tables?prnName={prnName}&lakeTableName={lakeTableName}' \
        .format(prnName=prnName, lakeTableName=lakeTableName)
    headers = {
        'Content-type': 'application/json',
        'X-ENP-AUTH': access_token
    }

    result = []
    result, next_link = post_to_datalake_data_from_ex_server(access_token, url, body, save_res_to_file)
    while load_all and next_link != None:
        print('next_link=' + next_link)
        qs = parse_qs(urlparse(next_link).query)
        page_size = qs['page[limit]'][0]
        offset = qs['page[offset]'][0]
        ex_next_link = url + '&pageSize={page_size}&offset={offset}'.format(page_size=page_size, offset=offset)
        data, next_link = post_to_datalake_data_from_ex_server(access_token, ex_next_link)
        result = result + data
    return result


# 调用微服务
def post_to_ms(tgt_svc, api_path, body={}, save_res_to_file=False):
    base_url, token_params = get_ms_config('envision.ini', tgt_svc)
    access_token = getToken(base_url, token_params)
    url = base_url + api_path
    headers = {
        'Content-type': 'application/json',
        'X-ENP-AUTH': access_token
    }
    # print (url)
    body = json.dumps(body)
    r = requests.post(url, headers=headers, data=body)
    print('{0} 请求响应时间：{1}'.format(url, r.elapsed.total_seconds()))
    if r.status_code != requests.codes.ok:
        print('erorr:')
        print(r.text)
    if save_res_to_file:
        with open('response_body.json', 'w') as outfile:
            json.dump(r.json(), outfile, ensure_ascii=False)
    return r.json()


def put_to_ms(tgt_svc, api_path, body={}, save_res_to_file=False):
    base_url, token_params = get_ms_config('envision.ini', tgt_svc)
    access_token = getToken(base_url, token_params)
    url = base_url + api_path
    headers = {
        'Content-type': 'application/json',
        'X-ENP-AUTH': access_token
    }
    # print (url)
    body = json.dumps(body)
    r = requests.put(url, headers=headers, data=body)
    print('{0} 请求响应时间：{1}'.format(url, r.elapsed.total_seconds()))
    if r.status_code != requests.codes.ok:
        print('erorr:')
        print(r.text)
    if save_res_to_file:
        with open('response_body.json', 'w') as outfile:
            json.dump(r.json(), outfile, ensure_ascii=False)
    return r.json()


def save_json_data(records, to_file_name):
    df = pd.DataFrame(records)
    data_dir = './data/{}'.format(str(date.today()))
    os.makedirs(data_dir, exist_ok=True)
    df.to_json('{}/{}.json'.format(data_dir, to_file_name), orient='records', force_ascii=False)
    print('save {} to {}'.format(to_file_name, '{}/{}.json'.format(data_dir, to_file_name)))
    df.to_excel('{}/{}.xlsx'.format(data_dir, to_file_name), index=False)
    print('save {} to {}'.format(to_file_name, '{}/{}.xlsx'.format(data_dir, to_file_name)))
