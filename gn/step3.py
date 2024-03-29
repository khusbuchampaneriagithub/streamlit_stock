train_dataset = datasets.CIFAR10(root='./data',\
			train=True, download=True, transform=transform)
dataloader = torch.utils.data.DataLoader(train_dataset, \
								batch_size=32, shuffle=True)
