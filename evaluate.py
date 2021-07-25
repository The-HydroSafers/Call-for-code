def confusion_matrix(model,test_batch,batch_size,xtest=xtest, ytest=ytest, nClasses=nClasses, labels=labels):

    matrix = np.zeros((nClasses, nClasses), dtype=int)
    model.eval()
    with torch.no_grad():
        # shuffle the test data
        permute = torch.randperm(len(ytest))

        xtest = xtest[permute, :, :, :]
        ytest = ytest[permute]

        for j in range(test_batch):
            xbatch = xtest[j*batch_size:(j+1)*batch_size, :, :,:].to(dev)
            ybatch = ytest[j*batch_size:(j+1)*batch_size].to(dev)

            y = model(xbatch)

            pred = y.max(1, keepdim=True)[1]

            for j in torch.cat((ybatch.view_as(pred), pred), dim=1).tolist():
                # actual and predicted
                matrix[j[0],j[1]] += 1
    correct = sum([matrix[i,i] for i in range(nClasses)])

    print("Correct predictions: ", correct, "of", ntest)
    print(":-----Consufion Matrix----:")
    print(matrix)
    print(labels)
    x = sns.heatmap(matrix, fmt='.0f', annot=True)
    x.set_title(f'{model}')
    return mp.show(x)