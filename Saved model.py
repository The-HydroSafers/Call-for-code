#  saving our model

#in pytorch pth
torch.save(model, 'model.pth')

#in tensorflow h5
torch.save(model, 'model.h5')
#loading our model
model = torch.load('model.pth')
