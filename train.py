def train_model(model=model,xtrain=xtrain,ytrain=ytrain,xvalid=xvalid, yvalid=yvalid):
    # learning rate
    lr = 0.01
    # Maximum training epochs
    epochs = 20
    # Maximum allowed ratio of validation to training loss
    t2vRatio = 1.2
    # Consecutive epochs before halting if validation loss exceeds above limit
    t2vEpochs = 3

    # Batch size
    batch_size = 300
    train_model.batch_size = batch_size

    # Number of training batches per epoch
    train_batch = ntrain // batch_size
    print(train_batch,'training batches')
    train_model.train_batch = train_batch

    # Validation batches
    valid_batch = nvalid // batch_size
    print(valid_batch, 'validation batches')
    train_model.valid_batch = valid_batch

    # test batch 
    test_batch = -(-ntest//batch_size)
    print(test_batch,'test batches')
    train_model.test_batch = test_batch

    # incase of any class imbalance
    CEweights = torch.zeros(nClasses)

    for i in ytrain.tolist():
        # cater for any class imbalances
        CEweights[i].add_(1)

    # Weights should be inversely related to count
    CEweights = 1. / CEweights.clamp_(min=1)
    # The weights should average to 1
    CEweights = (CEweights * nClasses/ CEweights.sum()).to(dev)

    # initialize an optimizer
    opti = om.SGD(model.parameters(), lr = lr)


    epochs_used = []
    training_accuracy = []
    train_loss = []
    valid_loss = []
    valid_accuracy = []
    test_loss = []
    test_accuracy = []

    for i in range(epochs):
        # Set model for training
        model.train()
        epochLoss = 0
        # shuffle data for random batches
        permute = torch.randperm(ntrain)

        xtrain = xtrain[permute, :, :, :]
        ytrain = ytrain[permute]

        # iterate over batches
        for j in range(train_batch):
            opti.zero_grad()

            xbatch = xtrain[j*batch_size: (j+1) * batch_size, :, :, :].to(dev)
            ybatch = ytrain[j*batch_size: (j+1) * batch_size].to(dev)
            # evaluate predictions
            y = model(xbatch)
            # compute the loss
            loss = F.cross_entropy(y, ybatch, weight=CEweights)
            #add loss
            epochLoss += loss.item()
            # back propagate
            loss.backward()
            # update model weights using optimizer
            opti.step()
            # epochLoss.append(loss.item())

        validLoss = 0
        permute = torch.randperm(nvalid)
        # go through similar proces without backpropagation and optimization
        xvalid = xvalid[permute, :, :, :]
        yvalid = yvalid[permute]

        # set model to evaluation mode
        with torch.no_grad(): # shut down gradient descent temporarily
            for j in range(valid_batch):
                opti.zero_grad()
                xbatch = xvalid[j*batch_size:(j+1)*batch_size, :, :, :].to(dev)
                ybatch = yvalid[j*batch_size:(j+1)*batch_size].to(dev)
                y = model(xbatch)
                validLoss += F.cross_entropy(y, ybatch, weight=CEweights).item()
        # average loss over batches and print it out
        epochLoss /= train_batch
        validLoss /= valid_batch

        train_loss.append(epochLoss)
        valid_loss.append(validLoss)
        epochs_used.append(i)

        print(f'Epoch = {i:-3}; Training Loss = {epochLoss:.4f}; Validation Loss = {validLoss:.4f}')

        # Test if validatio loss exceed halting threshold
        epoch_used = []
        if validLoss > t2vRatio * epochLoss:
            t2vEpochs -= 1
            if t2vEpochs < 1:
                print('Validation loss to high; halting to prevent overfitting')
                break

    return train_loss, valid_loss, epochs_used
