int numberOfEmployeesWhoMetTarget(int* hours, int hoursSize, int target) 
{
    int cont = 0;

    for(int i=0; i < hoursSize; i++)
        if (hours[i] >= target)
            cont++;

    return cont;
}