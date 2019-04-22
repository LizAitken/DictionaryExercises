ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
#Ramit's email
print(ramit['email'])
#Ramit's first interest
print(ramit['interests'][0])
#Jasmine's email
print(ramit['friends'][0]['email'])
#Jan's second interest
print(ramit['friends'][1]['interests'][1])