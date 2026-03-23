int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) 
{
    int contM = 0;
    for (int i = 0; i < accountsSize; i++)
    {
        int cont = 0;
        for (int j = 0; j < *accountsColSize; j++)
            cont += accounts[i][j];
            
        if (cont > contM)
            contM = cont;
    }

    return contM;
}