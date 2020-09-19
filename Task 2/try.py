import pickle

model = pickle.load(open('model.pkl', 'rb'))

prediction = model.predict([[9.25]])

print(prediction[0])