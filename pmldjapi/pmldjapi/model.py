import pickle

# Create and train your machine learning model
model = ...

# Save your model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
