import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)


try:
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            print('Name: ' + p['name'])
            print('Website: ' + p['website'])
            print('From: ' + p['from'])
            print('')
except FileNotFoundError as e:                              # it is only excute when file not found
    print(e)
except Exception as e1:                                   # it is  default excption block
    print(e1)
else:                                                    # else part will excute when there is no Exception found
    print("else part i dont know when it will execute")
finally:                                                 # finnaly will execute at any point of time whether execption or not
    print('execution is completed')


