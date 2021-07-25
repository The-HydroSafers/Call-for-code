#  saving our model
torch.save(model, 'model.pth')

#loading our model
model = torch.load('model.pth')
