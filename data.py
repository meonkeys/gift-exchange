participants = ['Alvin',
 'Arno',
 'Azula',
 'Betty',
 'Edgar',
 'Martin',
 'Melanie',
 'Omari',
 'Richard',
 'Samuel']

# OK to include folks from last year not in this year
last_years_pairs = [('Alvin', 'Richard'),
 ('Arno', 'Melanie'),
 ('Azula', 'Arno'),
 ('Betty', 'Samuel'),
 ('Edgar', 'Alvin'),
 ('Martin', 'Betty'),
 ('Melanie', 'Azula'),
 ('Omari', 'Martin'),
 ('Richard', 'Omari'),
 ('Samuel', 'Edgar')]

# groups of people that shouldn't give to one another
families = ['Alvin',
 'Arno',
 ('Azula', 'Betty', 'Edgar', 'Omari'),
 ('Martin', 'Melanie', 'Richard', 'Samuel')]
