def signup(client, username, name, email, password1, password2, age, gender, height, weight):
    return client.post('/sign-up', data=dict(
        username=username,
        name=name,
        email=email,
        password1=password1,
        password2=password2,
        age=age,
        genderOptions=gender,
        height=height,
        weight=weight
    ), follow_redirects=True)

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)
